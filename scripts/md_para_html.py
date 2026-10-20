#!/usr/bin/env python3
r"""
Converte o relatório consolidado em Markdown no HTML oficial (moldura de templates/report.html + templates/report.css).

Uso:
    python3 scripts/md_para_html.py semanas/<semana>/report_ti_<Domingo>_<Sábado>.md [saida.html]

Depois: bash scripts/renderizar_pdf.sh <saida.html>  (embute o CSS e gera o PDF A4).

O Markdown é a fonte única; o HTML sai dele. O script:
  - monta a moldura (cabeçalho, bloco de identificação, convenções e índice) a partir do próprio .md
    (linhas "**Período Analisado**" e "**Período Operacional Efetivo**" do bloco de identificação);
  - página 1 = capa-painel: cabeçalho, bloco de identificação, "## 📊 Painel da Semana" (marcador PAINEL + as 3
    perguntas) e o índice (2 níveis: Partes e tópicos);
  - o Resumo Executivo abre a página 2; 📈 Destaques e ⭐ Fatos Notáveis seguem corridos (os "### " viram cards);
  - cada "# " (Parte I, II, III, Encerramento, Anexos) vira faixa de grande seção e começa em nova página; os "## "
    dentro de uma Parte seguem corridos, sem quebra de página;
  - colunas Status, Severidade, Criticidade e Prioridade viram chips coloridos (emoji inicial descartado);
  - ids iguais às âncoras do índice (mesmo algoritmo de scripts/validar_indice.py);
  - tabelas com td.nowrap em números, protocolos, datas, valores e CPF mascarado; tabela-densa quando houver
    coluna CPF/CNPJ; CPF mascarado deve vir escapado no .md (\*\*\*.456.789-\*\*);
  - blocos <svg>…</svg> passam direto.

Marcadores (comentários HTML, invisíveis no .md renderizado):
  <!-- KPI: valor | rótulo | descrição | cor ; valor | rótulo | descrição | cor ; ... -->
       statcards; cor semântica = verde (bom) | amarelo (atenção) | vermelho (ruim) | vazio (informativo);
       aceita também os nomes antigos emerald | amber | rose | purple; a grade se ajusta à quantidade (3, 4, 5 ou 6)
  <!-- PAINEL: área | farol | valor | rótulo | detalhe | histórico ; ... -->
       cards da capa-painel; farol = verde | amarelo | vermelho | neutro; histórico opcional = valores das semanas
       anteriores até a atual separados por " · " (ex.: 32.600 · 32.596), desenhados como minigráfico
  <!-- BARS: Rótulo|12 ; Rótulo|3 ; ... -->
       barras horizontais proporcionais (ranking)
  <!-- STACK: Pessoa | Frente=19:11, Frente=9:09 ; Pessoa | ... -->
       barras empilhadas (ex.: distribuição do tempo por frente); valores em h:mm ou decimais; mesma cor por frente
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


CORES = {"verde": "emerald", "amarelo": "amber", "vermelho": "rose", "neutro": ""}
SERIE = ["#0284c7", "#10b981", "#f59e0b", "#8b5cf6", "#f43f5e", "#64748b", "#14b8a6", "#a16207"]


def numero(txt):
    """Valor numérico de um texto em formato brasileiro (32.604 · R$ 6.725,27 · 100% · 19:11); None se não houver."""
    t = txt.strip()
    m = re.fullmatch(r"(\d+):(\d\d)", t)
    if m:
        return int(m.group(1)) + int(m.group(2)) / 60
    t = re.sub(r"[^\d,.−-]", "", t).replace("−", "-")
    if not re.search(r"\d", t):
        return None
    t = t.replace(".", "").replace(",", ".") if "," in t or re.fullmatch(r"-?\d{1,3}(\.\d{3})+", t) else t
    try:
        return float(t)
    except ValueError:
        return None


def sparkline(valores):
    nums = [numero(v) for v in valores]
    nums = [n for n in nums if n is not None]
    if len(nums) < 2:
        return ""
    lo, hi = min(nums), max(nums)
    w, h, pad = 90, 22, 3
    pts = [(pad + i * (w - 2 * pad) / (len(nums) - 1), h - pad - (0 if hi == lo else (n - lo) / (hi - lo)) * (h - 2 * pad))
           for i, n in enumerate(nums)]
    linha = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    x, y = pts[-1]
    return (f'<svg class="spark" viewBox="0 0 {w} {h}" width="{w}" height="{h}" aria-hidden="true">'
            f'<polyline points="{linha}" fill="none" stroke="#64748b" stroke-width="1.5" stroke-linejoin="round"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.2" fill="#0f172a"/></svg>')


def painel(spec):
    cards = []
    for item in spec.split(" ; "):
        p = [x.strip() for x in item.split("|")] + [""] * 6
        area, farol, val, lab, det, hist = p[:6]
        farol = farol.lower() if farol.lower() in ("verde", "amarelo", "vermelho") else "neutro"
        serie = [v for v in re.split(r"\s+·\s+", hist) if v] if hist else []
        rot_hist = f'<div class="painel-hist">{" → ".join(html.escape(v) for v in serie)}</div>' if serie else ""
        cards.append(f'<div class="painel-card {farol}"><div class="painel-area"><span class="farol"></span>{inline(area)}</div>'
                     f'<div class="kpi-value">{inline(val)}</div><div class="kpi-label">{inline(lab)}</div>'
                     f'<div class="kpi-desc">{inline(det)}</div>{sparkline(serie)}{rot_hist}</div>')
    return '<div class="painel-grid">' + "".join(cards) + "</div>"


def empilhado(spec):
    pessoas, frentes = [], []
    for item in spec.split(" ; "):
        nome, resto = item.split("|", 1)
        partes = []
        for par in resto.split(","):
            f, v = par.rsplit("=", 1)
            f, v = f.strip(), v.strip()
            if f not in frentes:
                frentes.append(f)
            partes.append((f, v, numero(v) or 0))
        pessoas.append((nome.strip(), partes))
    cor = {f: SERIE[i % len(SERIE)] for i, f in enumerate(frentes)}
    out = ['<div class="stack-chart">']
    for nome, partes in pessoas:
        tot = sum(n for _, _, n in partes) or 1
        segs = "".join(f'<div class="stack-seg" style="width:{100 * n / tot:.1f}%;background:{cor[f]}" title="{html.escape(f)}: {html.escape(v)}">'
                       f'{html.escape(v) if n / tot >= 0.08 else ""}</div>' for f, v, n in partes if n)
        out.append(f'<div class="stack-row"><span class="stack-name">{html.escape(nome)}</span><div class="stack-bar">{segs}</div></div>')
    out.append('<div class="stack-legend">' + "".join(f'<span><i style="background:{cor[f]}"></i>{html.escape(f)}</span>' for f in frentes) + "</div></div>")
    return "".join(out)


CHIP_COLS = ("status", "severidade", "criticidade", "prioridade")
CHIP = [("danger", r"não atendid|falh|crític|critical|\balta\b|vencid|atrasad"),
        ("warning", r"pendent|aguard|paliativ|atenção|média|parcial|observação|\bhigh\b|não informad"),
        ("success", r"conclu|encerrad|sucesso|aplicad|resolvid|atendid|normal|\bbaixa\b|\bok\b")]
EMOJI = re.compile(r"^[\u2190-\u2BFF\u2600-\u27BF\U0001F000-\U0001FAFF\uFE0F\s]+")


def chip(c):
    texto = EMOJI.sub("", c.strip())
    if not texto or len(texto) > 40:
        return inline(c)
    puro = re.sub(r"\*|<[^>]+>", "", texto).lower()
    tipo = next((t for t, rx in CHIP if re.search(rx, puro)), "info")
    return f'<span class="badge badge-{tipo}">{inline(texto)}</span>'


def kpis(spec):
    cards = []
    for item in spec.split(" ; "):
        partes = [x.strip() for x in item.split("|")]
        val, lab, desc = partes[:3]
        cor = partes[3] if len(partes) > 3 and partes[3] else ""
        cor = CORES.get(cor, cor)
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
    chips = {k for k, c in enumerate(cab) if re.sub(r"\*|<[^>]+>", "", c).strip().lower().startswith(CHIP_COLS)}
    for l in linhas[2:]:
        out.append("<tr>" + "".join(f'<td{nowrap(c)} style="text-align:{a}">{chip(c) if k in chips else inline(c)}</td>'
                                    for k, (c, a) in enumerate(zip(cel(l), alin))) + "</tr>")
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
    global corpo, vistos, secao_atual, card_aberto, em_parte
    corpo, vistos, secao_atual, card_aberto, em_parte = [], {}, "", None, False
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
    ms = re.search(r"^\*\*(.+?)\*\*\s*$", md[:inicio], re.M)
    subtitulo = ms.group(1) if ms else "O Setor de TI · Sistemas e Desenvolvimento · A Empresa"
    periodo_curto = f"{p_datas.group(1)} a {p_datas.group(3)}"
    conv = re.search(r"^> (Convenções:.*)$", md[:inicio], re.M)
    conv_html = f'<div class="card-narrative note"><p>{inline(conv.group(1))}</p></div>' if conv else ""

    # Capa-painel: "## 📊 Painel da Semana" (antes do índice) com o marcador PAINEL e as 3 perguntas em lista
    painel_html = ""
    mp = re.search(r"^##\s+\W*Painel da Semana\s*$(.*?)(?=^##\s)", md[:inicio], re.M | re.S)
    if mp:
        blocos = []
        for bl in re.split(r"\n\s*\n", mp.group(1).strip()):
            mk = re.match(r"^<!-- PAINEL: (.*) -->$", bl.strip())
            if mk:
                blocos.append(painel(mk.group(1)))
            elif re.match(r"^\s*[-*]\s", bl):
                blocos.append('<div class="painel-leitura">' + lista(bl.splitlines()) + "</div>")
            elif bl.strip():
                blocos.append("<p>" + inline(" ".join(bl.split())) + "</p>")
        painel_html = '<div class="section-title" id="-painel-da-semana"><span>Painel da Semana</span></div>' + "".join(blocos)

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
        m = re.match(r"^<!-- STACK: (.*) -->$", l)
        if m:
            corpo.append(empilhado(m.group(1)))
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
                # Grande seção (Parte I, II, III, Encerramento, Anexos): nova página com faixa; os "## " seguem corridos
                fechar_card()
                if corpo:
                    corpo.append("</div>")
                anexos = " anexos" if titulo.startswith("Anexos") else ""
                corpo.append(f'<div class="page-section page-break{anexos}"><div class="part-banner" id="{aid}">{inline(titulo)}</div>')
                em_parte = True
            elif nivel == 2:
                fechar_card()
                secao_atual = titulo
                resto = linhas[i + 1:]
                fim = next((k for k, x in enumerate(resto) if re.match(r"^#{1,2} ", x)), len(resto))
                n3 = sum(1 for x in resto[:fim] if x.startswith("### "))
                selo = {"Destaques": f"{n3} destaques", "Fatos": f"{n3} ocorrências"}
                selo = next((v for k, v in selo.items() if k in titulo), "")
                selo = f'<span class="badge-count">{selo}</span>' if selo else ""
                if not corpo:
                    # Resumo Executivo abre a página 2 (a página 1 é a capa-painel)
                    corpo.append('<div class="page-section page-break">')
                corpo.append(f'<div class="section-title" id="{aid}"><span>{inline(titulo)}</span>{selo}</div>')
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
      <p class="subtitle">{html.escape(subtitulo)}</p>
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
    {painel_html}
    {conv_html}
    <div class="section-title" id="indice-geral"><span>Índice Geral de Navegação</span></div>
    {"".join(toc)}
  </div>
"""
    corpo_html = "".join(corpo)
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
