#!/usr/bin/env python3
"""
Fase 0 do fluxo (docs/fluxo_geracao.md): checklist das entradas de uma semana.

Uso:
    python3 scripts/checar_entradas.py                      # semana a gerar (última semana encerrada em semanas/)
    python3 scripts/checar_entradas.py semanas/2026-10-11_2026-10-17

Imprime uma tabela Markdown com o status de cada fonte. Sai com código 1 se faltar fonte essencial.
"""

import os
import re
import subprocess
import sys
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTOTICKETS_REPO = "/home/liomarti/dev/autotickets-v2"
PESSOAS = ["liomar", "isac", "david"]
MODULOS = [
    ("colaborador_x_ticket", True),
    ("wifeed_daily_update_voucher", True),
    ("fullcam_lucros_prejuizos", True),
    ("fullcam_automacao_inadimplencia", True),
    ("fullcam_automacao_instalacao_camera", True),
    ("acompanhamento_protocolos", False),
    ("problemas_recorrentes", False),
    ("produtividade_geral", False),
]
CPF = re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b")
PERIODO = re.compile(r"^(\d{4}-\d{2}-\d{2})_(\d{4}-\d{2}-\d{2})$")


def arquivos(pasta, prefixo=""):
    if not os.path.isdir(pasta):
        return []
    return sorted(f for f in os.listdir(pasta) if not f.startswith(".") and f.startswith(prefixo))


def individuais_pedidos(parametros):
    """Lê o campo 'Relatórios individuais a gerar' do PARAMETROS.md."""
    if not os.path.isfile(parametros):
        return set()
    with open(parametros, encoding="utf-8") as f:
        for linha in f:
            if "Relatórios individuais a gerar" in linha:
                valor = re.sub(r"<!--.*?-->", "", linha.split(":", 1)[-1]).lower()
                return {p for p in PESSOAS if p in valor}
    return set()


def feedback_preenchido(path):
    """True se o feedback.md tem algum conteúdo além de títulos, comentários e itens vazios."""
    if not os.path.isfile(path):
        return False
    with open(path, encoding="utf-8") as f:
        texto = re.sub(r"<!--.*?-->", "", f.read(), flags=re.S)
    for linha in texto.splitlines():
        linha = linha.strip()
        if linha and not linha.startswith("#") and linha not in ("-", "*"):
            return True
    return False


def semana_corrente():
    """Semana a gerar: a mais recente cujo sábado já passou (ignora pastas de semanas futuras)."""
    base = os.path.join(RAIZ, "semanas")
    semanas = sorted(d for d in os.listdir(base) if PERIODO.match(d))
    hoje = date.today().isoformat()
    encerradas = [d for d in semanas if PERIODO.match(d).group(2) < hoje]
    escolhida = encerradas[-1] if encerradas else semanas[-1]
    return os.path.join(base, escolhida), semanas


def commits_autotickets(inicio, fim):
    if not os.path.isdir(AUTOTICKETS_REPO):
        return None
    r = subprocess.run(
        ["git", "-C", AUTOTICKETS_REPO, "log", "--all", f"--since={inicio} 00:00:00",
         f"--until={fim} 23:59:59", "--oneline"],
        capture_output=True, text=True,
    )
    return len(r.stdout.splitlines()) if r.returncode == 0 else None


def main():
    if len(sys.argv) > 1:
        pasta = os.path.abspath(sys.argv[1])
        _, semanas = semana_corrente()
    else:
        pasta, semanas = semana_corrente()
    nome = os.path.basename(pasta.rstrip("/"))
    m = PERIODO.match(nome)
    if not m or not os.path.isdir(pasta):
        print(f"[ERRO] Pasta de semana inválida: {pasta}")
        return 2
    inicio, fim = m.groups()
    linhas = []
    falta_essencial = False

    def add(fonte, ok, detalhe, essencial=True):
        nonlocal falta_essencial
        if not ok and essencial:
            falta_essencial = True
        status = "✅" if ok else ("❌" if essencial else "⚪")
        linhas.append(f"| {fonte} | {status} | {detalhe} |")

    add("PARAMETROS.md", os.path.isfile(os.path.join(pasta, "PARAMETROS.md")), "datas e focos da semana")

    for p in PESSOAS:
        fs = arquivos(os.path.join(pasta, "fontes", "voalle"), p)
        add(f"Voalle — {p}", bool(fs), ", ".join(fs) or "ausente")

    n = commits_autotickets(inicio, fim)
    dev = arquivos(os.path.join(pasta, "fontes", "autotickets", "desenvolvimento"))
    add("AutoTickets — commits", bool(n) or bool(dev),
        (f"{n} commits em {inicio}..{fim}" if n is not None else "repositório indisponível")
        + (f"; relatório: {', '.join(dev)}" if dev else ""))

    for mod, essencial in MODULOS:
        fs = arquivos(os.path.join(pasta, "fontes", "autotickets", mod))
        add(f"AutoTickets — {mod}", bool(fs), ", ".join(fs) or "ausente", essencial)

    inv = arquivos(os.path.join(pasta, "fontes", "investigacoes"))
    add("Investigações", bool(inv), ", ".join(inv) or "nenhuma na semana", essencial=False)

    pedidos = individuais_pedidos(os.path.join(pasta, "PARAMETROS.md"))
    for p in PESSOAS:
        fs = arquivos(os.path.join(pasta, "individuais"), p)
        detalhe = ", ".join(fs) if fs else "não existe (usado só como fonte complementar)"
        if p in pedidos:
            detalhe += " — GERAR (pedido em PARAMETROS.md)"
        add(f"Individual — {p}", bool(fs), detalhe, essencial=False)

    anteriores = [s for s in semanas if s < nome]
    if anteriores:
        ant = os.path.join(RAIZ, "semanas", anteriores[-1])
        rel = arquivos(ant, "report_ti_")
        rel_md = [f for f in rel if f.endswith(".md")]
        add("Relatório da semana anterior", bool(rel_md),
            f"semanas/{anteriores[-1]}/{rel_md[0]}" if rel_md else f"sem report_ti_*.md em semanas/{anteriores[-1]}/",
            essencial=False)
        fb = os.path.join(ant, "feedback.md")
        preenchido = feedback_preenchido(fb)
        add("Feedback/observações da semana anterior", preenchido,
            f"semanas/{anteriores[-1]}/feedback.md" + ("" if preenchido else " (vazio ou inexistente)"),
            essencial=False)

    sem_mascara = []
    for raiz, _, fs in os.walk(os.path.join(pasta, "fontes")):
        for f in fs:
            if f.lower().endswith((".md", ".html", ".htm", ".csv", ".txt", ".json")):
                caminho = os.path.join(raiz, f)
                with open(caminho, encoding="utf-8", errors="ignore") as h:
                    if CPF.search(h.read()):
                        sem_mascara.append(os.path.relpath(caminho, pasta))
    add("CPFs mascarados", not sem_mascara,
        "ok" if not sem_mascara else "rodar scripts/mascarar_dados.py em: " + ", ".join(sem_mascara))

    print(f"## Fase 0 — Checklist de entradas: {nome}\n")
    print("| Fonte | Status | Detalhe |")
    print("| :--- | :---: | :--- |")
    print("\n".join(linhas))
    print("\nLegenda: ✅ ok · ❌ essencial ausente · ⚪ opcional ausente")
    return 1 if falta_essencial else 0


if __name__ == "__main__":
    sys.exit(main())
