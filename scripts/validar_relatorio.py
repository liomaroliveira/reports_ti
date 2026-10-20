#!/usr/bin/env python3
"""
Validação de conteúdo do relatório consolidado (complementa scripts/validar_indice.py).

Uso:
    python3 scripts/validar_relatorio.py semanas/<semana>/report_ti_<Domingo>_<Sábado>.md

Confere:
  1. Termos proibidos ("resolutividade", "resolubilidade").
  2. Seções obrigatórias: Resumo Executivo, 📈 Destaques Analíticos, ⭐ Fatos Notáveis e tópicos 1 a 9.
  3. Destaques Analíticos com 3 a 5 itens (ou a declaração "Semana sem desvios relevantes").
  4. Feedback da semana anterior: tabela "Acompanhamento das observações" com ao menos uma linha por observação.
  5. Tópico condicional 8.4: presente se houver fonte em fontes/autotickets/anomalias_pppoe/; ausente (e citado no
     Resumo Executivo) se não houver.
  6. CPF/CNPJ sem máscara, senhas e stream keys RTMP no relatório.
Sai com código 1 se houver erro.
"""

import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
from mascarar_dados import CNPJ_FMT, CPF_FMT, DIGITOS, RTMP, SENHA, cnpj_valido, cpf_valido  # noqa: E402

PERIODO = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{4}-\d{2}-\d{2}$")
PROIBIDOS = re.compile(r"\b(resolutividade|resolubilidade)\b", re.I)


def itens_feedback(path):
    """Observações de um feedback.md: itens de lista de primeiro nível com conteúdo (fora de comentários)."""
    if not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8") as f:
        texto = re.sub(r"<!--.*?-->", "", f.read(), flags=re.S)
    itens = []
    for linha in texto.splitlines():
        m = re.match(r"^[-*]\s+(.*\S)", linha)
        if m and not re.match(r"(?i)^(sem perguntas|nenhuma manifesta)", m.group(1)):
            itens.append(m.group(1))
    return itens


def secao(texto, titulo_regex):
    """Texto de uma seção ## até a próxima ## (ou None)."""
    m = re.search(r"^##\s+" + titulo_regex + r".*$", texto, re.M)
    if not m:
        return None
    fim = re.search(r"^##\s", texto[m.end():], re.M)
    return texto[m.end(): m.end() + fim.start()] if fim else texto[m.end():]


def validar(path):
    erros, avisos = [], []
    texto = open(path, encoding="utf-8").read()
    semana = os.path.dirname(os.path.abspath(path))
    if os.path.basename(semana) == "individuais":
        semana = os.path.dirname(semana)

    # 1. Termos proibidos
    for t in sorted({m.group(0).lower() for m in PROIBIDOS.finditer(texto)}):
        erros.append(f'termo proibido "{t}" (usar "balanço da fila (saídas ÷ entradas)")')

    # 2. Seções obrigatórias
    obrigatorias = [("Resumo Executivo", r"Resumo Executivo"),
                    ("📈 Destaques Analíticos da Semana", r"\W*Destaques Analíticos"),
                    ("⭐ Fatos Notáveis e Anomalias da Semana", r"\W*Fatos Notáveis")]
    obrigatorias += [(f"Tópico {n}", rf"{n}\.\s") for n in range(1, 10)]
    for nome, rx in obrigatorias:
        if secao(texto, rx) is None:
            erros.append(f"seção obrigatória ausente: {nome}")

    # 3. Destaques Analíticos
    dest = secao(texto, r"\W*Destaques Analíticos")
    if dest is not None:
        n = len(re.findall(r"^###\s", dest, re.M))
        if not (3 <= n <= 5) and "sem desvios relevantes" not in dest.lower():
            erros.append(f"Destaques Analíticos com {n} item(ns) (esperado 3 a 5, ou declarar semana sem desvios)")

    # 4. Feedback da semana anterior
    pai = os.path.dirname(semana)
    semanas = sorted(d for d in os.listdir(pai) if PERIODO.match(d)) if os.path.isdir(pai) else []
    nome = os.path.basename(semana)
    anteriores = [s for s in semanas if s < nome]
    if anteriores:
        fb = os.path.join(pai, anteriores[-1], "feedback.md")
        itens = itens_feedback(fb)
        if itens:
            resumo = secao(texto, r"Resumo Executivo") or ""
            m = re.search(r"Acompanhamento das observações", resumo, re.I)
            if not m:
                erros.append(f"feedback anterior tem {len(itens)} observação(ões), mas falta a tabela "
                             '"Acompanhamento das observações da semana anterior" no Resumo Executivo')
            else:
                linhas = [l for l in resumo[m.end():].splitlines() if l.strip().startswith("|")]
                linhas = [l for l in linhas if not re.match(r"^\|\s*:?-", l.strip())][1:]  # sem cabeçalho e separador
                if len(linhas) < len(itens):
                    erros.append(f"tabela de acompanhamento com {len(linhas)} linha(s) para {len(itens)} observação(ões) "
                                 f"em {os.path.relpath(fb, RAIZ)}")

    # 5. Tópico condicional 8.4
    pppoe = os.path.join(semana, "fontes", "autotickets", "anomalias_pppoe")
    tem_fonte = os.path.isdir(pppoe) and any(not f.startswith((".", "_")) for f in os.listdir(pppoe))
    tem_secao = re.search(r"^#{2,4}\s+8\.4\s", texto, re.M) is not None
    if tem_fonte and not tem_secao:
        erros.append("há fonte em fontes/autotickets/anomalias_pppoe/, mas falta o tópico 8.4")
    if not tem_fonte and tem_secao:
        erros.append("tópico condicional 8.4 presente sem fonte na semana")
    if not tem_fonte and "Tópicos condicionais sem fonte" not in texto:
        avisos.append('sem fonte PPPoE: citar "Tópicos condicionais sem fonte nesta semana: 8.4" no Resumo Executivo')

    # 6. Dados que nunca podem aparecer no relatório
    docs = [m.group(0) for m in CPF_FMT.finditer(texto)] + [m.group(0) for m in CNPJ_FMT.finditer(texto)]
    docs += [m.group(1) for m in DIGITOS.finditer(texto) if cpf_valido(m.group(1)) or cnpj_valido(m.group(1))]
    if docs:
        avisos.append(f"{len(docs)} CPF/CNPJ sem máscara no relatório (usar ***.456.789-**)")
    if SENHA.search(texto) or RTMP.search(texto):
        avisos.append("senha ou stream key RTMP transcrita no relatório")
    return erros, avisos


def main(paths):
    if not paths:
        print(__doc__)
        return 2
    falhou = False
    for path in paths:
        erros, avisos = validar(path)
        for a in avisos:
            print(f"[AVISO] {path}: {a}")
        if erros:
            falhou = True
            print(f"[ERRO] {path}:")
            for e in erros:
                print(f"  - {e}")
        else:
            print(f"[OK] {path}: conteúdo conforme a especificação")
    return 1 if falhou else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
