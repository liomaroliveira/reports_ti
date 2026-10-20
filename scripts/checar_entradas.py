#!/usr/bin/env python3
"""
Fase 0 do fluxo (docs/fluxo_geracao.md): checklist das entradas de uma semana.

Uso:
    python3 scripts/checar_entradas.py                      # semana a gerar (última semana encerrada em semanas/)
    python3 scripts/checar_entradas.py semanas/2026-10-11_2026-10-17

Imprime uma tabela Markdown com o status de cada fonte. Sai com código 1 se faltar fonte essencial.
"""

import json
import os
import re
import subprocess
import sys
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
from mascarar_dados import pendencias  # noqa: E402  (mesma detecção do pre-commit)
from validar_relatorio import itens_feedback  # noqa: E402

# Repositório do AutoTickets: variável de ambiente AUTOTICKETS_REPO ou o primeiro caminho conhecido que existir.
AUTOTICKETS_REPO = os.environ.get("AUTOTICKETS_REPO") or next(
    (c for c in (
        os.path.expanduser("~/dev/autotickets_v2"),
        os.path.expanduser("~/dev/autotickets-v2"),
        "/home/liomarti/dev/autotickets-v2",
    ) if os.path.isdir(c)),
    "/home/liomarti/dev/autotickets-v2",
)
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
    ("tarefas_executadas", False),
    ("anomalias_pppoe", False),
]
# Nome do módulo no pacote_semanal quando difere do nome da pasta.
PACOTE_ALIAS = {
    "wifeed_daily_update_voucher": "wifeed",
    "fullcam_lucros_prejuizos": "fullcam_financeiro",
    "fullcam_automacao_inadimplencia": "fullcam_inadimplencia",
    "fullcam_automacao_instalacao_camera": "fullcam_instalacao",
}
PERIODO = re.compile(r"^(\d{4}-\d{2}-\d{2})_(\d{4}-\d{2}-\d{2})$")


def arquivos(pasta, prefixo=""):
    if not os.path.isdir(pasta):
        return []
    # Arquivos iniciados por "." ou "_" (ex.: _ANALISE_FONTE.md) não são fontes do relatório.
    return sorted(f for f in os.listdir(pasta) if not f.startswith((".", "_")) and f.startswith(prefixo))


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

    # Pacote semanal (docs/formato_exportacao_autotickets.md): um JSON que cobre todos os módulos.
    pacote_dir = os.path.join(pasta, "fontes", "autotickets", "pacote_semanal")
    pacote = [f for f in arquivos(pacote_dir) if f.endswith(".json")]
    modulos_pacote = set()
    if pacote:
        try:
            with open(os.path.join(pacote_dir, pacote[-1]), encoding="utf-8") as h:
                dados = json.load(h)
            per = dados.get("meta", {}).get("periodo", {})
            ok_periodo = (per.get("inicio"), per.get("fim")) == (inicio, fim)
            modulos_pacote = set(dados.get("modulos", {}))
            invalidas = [v.get("regra") for v in dados.get("validacoes", []) if not v.get("ok")]
            add("AutoTickets — pacote_semanal", ok_periodo,
                f"{pacote[-1]}: {len(modulos_pacote)} módulo(s)"
                + ("" if ok_periodo else f"; período {per} ≠ {inicio}..{fim}")
                + (f"; validações com falha: {', '.join(map(str, invalidas))}" if invalidas else ""))
        except (OSError, ValueError) as e:
            add("AutoTickets — pacote_semanal", False, f"{pacote[-1]}: JSON inválido ({e})")
    else:
        add("AutoTickets — pacote_semanal", False, "ausente (formato proposto em docs/formato_exportacao_autotickets.md)",
            essencial=False)

    for mod, essencial in MODULOS:
        fs = arquivos(os.path.join(pasta, "fontes", "autotickets", mod))
        no_pacote = PACOTE_ALIAS.get(mod, mod) in modulos_pacote
        add(f"AutoTickets — {mod}", bool(fs) or no_pacote,
            ", ".join(fs) or ("coberto pelo pacote_semanal" if no_pacote else "ausente"), essencial)

    bkp = arquivos(os.path.join(pasta, "fontes", "infraestrutura", "backups"))
    add("Infraestrutura — backups (8.2)", bool(bkp),
        ", ".join(bkp) or "ausente: o quadrante de backups deve declarar ausência de fonte (nunca estimar)", essencial=False)

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
        itens = itens_feedback(fb)
        add("Feedback/observações da semana anterior", preenchido,
            f"semanas/{anteriores[-1]}/feedback.md"
            + (f" — {len(itens)} observação(ões) a tratar no Resumo Executivo" if preenchido else " (vazio ou inexistente)"),
            essencial=False)

    sem_mascara = []
    for raiz, _, fs in os.walk(os.path.join(pasta, "fontes")):
        for f in fs:
            if f.lower().endswith((".md", ".html", ".htm", ".csv", ".txt", ".json")):
                caminho = os.path.join(raiz, f)
                with open(caminho, encoding="utf-8", errors="ignore") as h:
                    if pendencias(h.read(), csv_mode=f.lower().endswith(".csv")):
                        sem_mascara.append(os.path.relpath(caminho, pasta))
    add("Dados sensíveis mascarados (CPF/CNPJ, e-mail, RTMP, senha)", not sem_mascara,
        "ok" if not sem_mascara else "rodar scripts/mascarar_dados.py em: " + ", ".join(sem_mascara),
        essencial=False)

    print(f"## Fase 0 — Checklist de entradas: {nome}\n")
    print("| Fonte | Status | Detalhe |")
    print("| :--- | :---: | :--- |")
    print("\n".join(linhas))
    print("\nLegenda: ✅ ok · ❌ essencial ausente · ⚪ opcional ausente")
    return 1 if falta_essencial else 0


if __name__ == "__main__":
    sys.exit(main())
