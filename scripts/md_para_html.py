#!/usr/bin/env python3
r"""
Converte o relatório consolidado em Markdown no HTML oficial (moldura de templates/report.html + templates/report.css).

Uso:
    python3 scripts/md_para_html.py semanas/<semana>/report_ti_<Domingo>_<Sábado>.md [saida.html]

Depois: bash scripts/renderizar_pdf.sh <saida.html>  (embute o CSS e gera o PDF A4).

O Markdown é a fonte única; o HTML sai dele. O script:
  - monta a moldura (cabeçalho, bloco de identificação, convenções e índice) a partir do próprio .md
    (linhas "**Período Analisado**" e "**Período Operacional Efetivo**" do bloco de identificação);
  - cada "# " (Parte I, II, III…) vira faixa de grande seção com quebra de página; cada "## " vira tópico com quebra
    de página (o primeiro tópico de uma parte fica na mesma página da faixa); os "### " de 📈 Destaques e ⭐ Fatos Notáveis viram cards;
  - ids iguais às âncoras do índice (mesmo algoritmo de scripts/validar_indice.py);
  - tabelas com td.nowrap em números, protocolos, datas, valores e CPF mascarado; tabela-densa quando houver
    coluna CPF/CNPJ; CPF mascarado deve vir escapado no .md (\*\*\*.456.789-\*\*);
  - blocos <svg>…</svg> passam direto.

Marcadores (comentários HTML, invisíveis no .md renderizado):
  <!-- KPI: valor | rótulo | descrição | cor ; valor | rótulo | descrição | cor ; ... -->
       statcards; cor = emerald | purple | amber | rose ou vazio; a grade se ajusta à quantidade (3, 4, 5 ou 6)
  <!-- BARS: Rótulo|12 ; Rótulo|3 ; ... -->
       barras horizontais proporcionais (ranking)
"""
import html
import os
import re
import sys

def slug(titulo):
    t = re.sub(r"<[^>]+>", "", titulo).strip().lower()
    t = re.sub(r"[^\w\- ]", "", t)
    return t.replace(" ", "-")


def inline(s):
    s = s.replace("\\*", "\x00")
    s = html.escape(s, quote=False)
    s = s.replace("&lt;br&gt;", "<br>")
    s = re.sub(r"&lt;span style='([^']*)'&gt;(.*?)&lt;/span&gt;", r"<span style='\1'>\2</span>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\((#[^)]+)\)", r'<a href="\2">\1</a>', s)
    return s.replace("\x00", "*")


def kpis(spec):
    cards = []
    for item in spec.split(" ; "):
        partes = [x.strip() for x in item.split("|")]
        val, lab, desc = partes[:3]
        cor = partes[3] if len(partes) > 3 and partes[3] else ""
        cards.append(f'<div class="kpi-card {cor}"><div class="kpi-value">{inline(val)}</div>'
                     f'<div class="kpi-label">{inline(lab)}</div><div class="kpi-desc">{inline(desc)}</div></div>')
    cols = {3: " cols-3", 5: " cols-5", 6: " cols-3"}.get(len(cards), "")
    return f'<div class="kpi-grid{cols}">' + "".join(cards) + "</div>"


def barras(spec):
    itens = [(a.strip(), int(b)) for a, b in (x.split("|") for x in spec.split(" ; "))]
    tot = sum(v for _, v in itens)
    out = ['<div class="time-dist-grid">']
    for nome, v in itens:
        pct = round(100 * v / tot)
        out.append(f'<div class="time-item"><div class="time-item-top"><span>{html.escape(nome)} ({v})</span><span class="pct">{pct}%</span></div>'
                   f'<div class="progress-bar-container"><div class="progress-bar" style="width:{pct}%;"></div></div></div>')
    out.append("</div>")
    return "".join(out)


CURTO = re.compile(r"^(\*\*)?(#?\d[\d.,:/ ×÷=%~≈+−-]*|[−-]?R\$ ?[\d.,]+|(\\\*)+[.\d]+[./-][\d]+-?(\\\*)*|#\d+ / #\d+|\d+ de \d+|[\w/]{1,9})(\*\*)?$")


def nowrap(c):
    c = re.sub(r"<span[^>]*>|</span>", "", c.strip())
    return ' class="nowrap"' if c and len(c) <= 18 and CURTO.match(c) else ""


def tabela(linhas):
    cel = lambda l: [c.strip() for c in l.strip().strip("|").split("|")]
    cab = cel(linhas[0])
    alin = []
    for c in cel(linhas[1]):
        alin.append("center" if c.startswith(":") and c.endswith(":") else ("right" if c.endswith(":") else "left"))
    densa = ' class="tabela-densa"' if any("CPF/CNPJ" in c for c in cab) else ""
    out = [f'<div class="table-container"><table{densa}><thead><tr>']
    out += [f'<th style="text-align:{a}">{inline(c)}</th>' for c, a in zip(cab, alin)]
    out.append("</tr></thead><tbody>")
    for l in linhas[2:]:
        out.append("<tr>" + "".join(f'<td{nowrap(c)} style="text-align:{a}">{inline(c)}</td>' for c, a in zip(cel(l), alin)) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def lista(linhas):
    out, pilha = [], []
    for l in linhas:
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", l)
        if not m:
            out[-1] = out[-1][:-5] + " " + inline(l.strip()) + "</li>"
            continue
        nivel = len(m.group(1)) // 2
        tag = "ol" if m.group(2)[0].isdigit() else "ul"
        while len(pilha) > nivel + 1:
            out.append(f"</{pilha.pop()}>")
        if len(pilha) < nivel + 1:
            out.append(f"<{tag}>")
            pilha.append(tag)
        out.append(f"<li>{inline(m.group(3))}</li>")
    while pilha:
        out.append(f"</{pilha.pop()}>")
    return "".join(out)




def converter(md, css_href):
    global corpo, vistos, secao_atual, card_aberto, pagina, parte_aberta
    corpo, vistos, secao_atual, card_aberto, pagina, parte_aberta = [], {}, "", None, 0, False
    indice = []

    def fechar_card():
        global card_aberto
        if card_aberto:
            corpo.append("</div>")
            card_aberto = None

    def anchor(titulo):
        base = slug(titulo)
        n = vistos.get(base, 0)
        vistos[base] = n + 1
        return base if n == 0 else f"{base}-{n}"

    inicio = md.index("## Resumo Executivo")
    for l in md[:inicio].splitlines():
        m = re.match(r"^\s*\* \[(.+?)\]\((#.+?)\)", l)
        if m:
            indice.append(((len(l) - len(l.lstrip())) // 2, m.group(1), m.group(2)))
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", l)
        if m:
            anchor(m.group(2))

    def campo(rotulo):
        m = re.search(r"^\|\s*\*\*" + rotulo + r"\*\*\s*\|\s*(.*?)\s*\|\s*$", md, re.M)
        return m.group(1) if m else ""

    periodo = campo("Período Analisado")
    operacional = campo("Período Operacional Efetivo")
    p_datas = re.search(r"(\d\d/\d\d)/(\d{4}) a (\d\d/\d\d/\d{4})", periodo)
    semana = re.search(r"Semana (\d+) / (\d{4})", periodo)
    o_datas = re.search(r"(\d\d/\d\d)/\d{4} a (\d\d/\d\d/\d{4})", operacional)
    o_obs = re.search(r"\((.*)\)", operacional)
    if not (p_datas and semana and o_datas):
        sys.exit("[ERRO] bloco de identificação sem 'Período Analisado' (com Semana XX / AAAA) ou 'Período Operacional Efetivo'")
    sem_txt = f"Semana {semana.group(1)} / {semana.group(2)}"
    periodo_curto = f"{p_datas.group(1)} a {p_datas.group(3)}"
    conv = re.search(r"^> (Convenções:.*)$", md, re.M)
    conv_html = f'<div class="card-narrative note"><p>{inline(conv.group(1))}</p></div>' if conv else ""

    linhas = md[inicio:].split("\n")
    i = 0
    while i < len(linhas):
        l = linhas[i]
        if not l.strip() or l.strip() == "---":
            i += 1
            continue
        m = re.match(r"^<!-- KPI: (.*) -->$", l)
        if m:
            corpo.append(kpis(m.group(1)))
            i += 1
            continue
        m = re.match(r"^<!-- BARS: (.*) -->$", l)
        if m:
            corpo.append(barras(m.group(1)))
            i += 1
            continue
        if l.startswith("<svg"):
            j = i
            while not linhas[j].startswith("</svg>"):
                j += 1
            corpo.append('<div class="card-narrative" style="padding:10px">' + "\n".join(linhas[i:j + 1]) + "</div>")
            i = j + 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", l)
        if m:
            nivel, titulo = len(m.group(1)), m.group(2).strip()
            aid = anchor(titulo)
            if nivel == 1:
                # Grande seção (Parte I, II, III, Encerramento): abre página com faixa; o primeiro "## " segue na mesma página
                fechar_card()
                if corpo:
                    corpo.append("</div>")
                pagina += 1
                corpo.append(f'<div class="page-section page-break"><div class="part-banner" id="{aid}">{inline(titulo)}</div>')
                parte_aberta = True
            elif nivel == 2 and parte_aberta:
                fechar_card()
                secao_atual = titulo
                parte_aberta = False
                corpo.append(f'<div class="section-title" id="{aid}"><span>{inline(titulo)}</span></div>')
            elif nivel == 2:
                fechar_card()
                if corpo:
                    corpo.append("</div>")
                secao_atual = titulo
                classe = "page-section" + (" page-break" if pagina else "")
                pagina += 1
                resto = linhas[i + 1:]
                fim = next((k for k, x in enumerate(resto) if x.startswith("## ")), len(resto))
                n3 = sum(1 for x in resto[:fim] if x.startswith("### "))
                selo = {"Destaques": f"{n3} destaques", "Fatos": f"{n3} ocorrências"}
                selo = next((v for k, v in selo.items() if k in titulo), "")
                selo = f'<span class="badge-count">{selo}</span>' if selo else ""
                corpo.append(f'<div class="{classe}"><div class="section-title" id="{aid}"><span>{inline(titulo)}</span>{selo}</div>')
            elif nivel == 3 and ("Destaques" in secao_atual or "Fatos" in secao_atual):
                fechar_card()
                classe = "card-narrative" if "Destaques" in secao_atual else "anomalia-card"
                corpo.append(f'<div class="{classe}" id="{aid}"><h4>{inline(titulo)}</h4>')
                card_aberto = classe
            elif nivel == 3:
                fechar_card()
                corpo.append(f'<div class="sub-section-title" id="{aid}">{inline(titulo)}</div>')
            else:
                fechar_card()
                corpo.append(f'<h4 class="sub-sub-title" id="{aid}">{inline(titulo)}</h4>')
            i += 1
            continue
        if l.lstrip().startswith("|"):
            j = i
            while j < len(linhas) and linhas[j].lstrip().startswith("|"):
                j += 1
            corpo.append(tabela(linhas[i:j]))
            i = j
            continue
        if re.match(r"^\s*([-*]|\d+\.)\s+", l):
            j = i
            while j < len(linhas) and (re.match(r"^\s*([-*]|\d+\.)\s+", linhas[j]) or (linhas[j].startswith("  ") and linhas[j].strip())):
                j += 1
            corpo.append(lista(linhas[i:j]))
            i = j
            continue
        if l.startswith(">"):
            j = i
            while j < len(linhas) and linhas[j].startswith(">"):
                j += 1
            texto = " ".join(x.lstrip("> ").strip() for x in linhas[i:j])
            texto = re.sub(r"^\[!\w+\]\s*", "", texto)
            corpo.append(f'<div class="card-narrative note"><p>{inline(texto)}</p></div>')
            i = j
            continue
        j = i
        while j < len(linhas) and linhas[j].strip() and not re.match(r"^(#|\||>|<|\s*([-*]|\d+\.)\s)", linhas[j]):
            j += 1
        corpo.append("<p>" + inline(" ".join(x.strip() for x in linhas[i:max(j, i + 1)])) + "</p>")
        i = max(j, i + 1)
    fechar_card()
    corpo.append("</div>")


    toc = ['<div class="toc-box"><ul>']
    for nivel, txt, href in indice:
        toc.append(f'<li class="toc-h{nivel + 2}"><a href="{href}">{html.escape(txt)}</a></li>')
    toc.append("</ul></div>")
    obs = o_obs.group(1) if o_obs else "Segunda a Sexta"
    moldura = f"""<div class="page-section">
    <div class="header-banner">
      <span class="header-badge">Uso interno · {sem_txt}</span>
      <h1>Relatório Semanal Consolidado - Setor TI</h1>
      <p class="subtitle">Panorama Operacional, Gestão de Demandas, Incidentes, Infraestrutura Crítica e Outros</p>
    </div>
    <div class="meta-grid">
      <div class="meta-item"><span class="label">Período Analisado</span><span class="val">{periodo_curto}</span><span class="val-sub">{sem_txt}</span></div>
      <div class="meta-item"><span class="label">Período Operacional Efetivo</span><span class="val">{o_datas.group(1)} a {o_datas.group(2)}</span><span class="val-sub">{html.escape(obs)}</span></div>
      <div class="meta-item"><span class="label">Coordenação de TI</span><span class="val">Isvi Neemias</span><span class="val-sub">Coordenador de TI</span></div>
      <div class="meta-item"><span class="label">Consolidação</span><span class="val">Liomar Antonio de Oliveira</span><span class="val-sub">Analista TI Sênior (#107184)</span></div>
    </div>
    <div class="meta-grid" style="grid-template-columns: 1fr; margin-top: -6px; margin-bottom: 12px; padding: 7px 14px;">
      <div class="meta-item"><span class="label">Equipe Integrada do Setor</span><span class="val" style="font-size: 7.8pt;">Liomar Antonio de Oliveira (Analista Sr), Isac Costa Silva (Assistente Pl) e David Brasil Fernandes (Auxiliar Jr)</span></div>
    </div>
    {conv_html}
    <div class="section-title" id="indice-geral"><span>Índice Geral de Navegação</span></div>
    {"".join(toc)}
  </div>
"""
    corpo_html = "".join(corpo).replace('<div class="page-section">', '<div class="page-section page-break">', 1)
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Relatório Semanal Consolidado — Setor TI ({p_datas.group(1)}/{p_datas.group(2)} a {p_datas.group(3)})</title>
  <link rel="stylesheet" href="{css_href}">
</head>
<body>
  {moldura}
  {corpo_html}
  <div class="footer"><span>Relatório Semanal Consolidado — Setor de TI</span><span>{sem_txt} — Ten Internet</span><span>{periodo_curto}</span></div>
</body>
</html>
"""


def main(args):
    if not args:
        print(__doc__)
        return 2
    md_path = args[0]
    saida = args[1] if len(args) > 1 else os.path.splitext(md_path)[0] + ".html"
    raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    css = os.path.relpath(os.path.join(raiz, "templates", "report.css"), os.path.dirname(os.path.abspath(saida)))
    md = open(md_path, encoding="utf-8").read()
    open(saida, "w", encoding="utf-8").write(converter(md, css))
    print(f"[OK] HTML gerado: {saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
