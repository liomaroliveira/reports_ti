#!/usr/bin/env python3
"""
Confere se todos os links do índice (#âncora) apontam para seções existentes.

Uso:
    python3 scripts/validar_indice.py semanas/<semana>/report_ti_<...>.md semanas/<semana>/report_ti_<...>.html

- .md: âncoras geradas a partir dos títulos (#, ##, ...) no padrão do GitHub/VS Code.
- .html: atributos id="..." presentes no documento.
Sai com código 1 se houver âncora quebrada.
"""

import re
import sys
from urllib.parse import unquote


def slug(titulo):
    t = re.sub(r"<[^>]+>", "", titulo).strip().lower()
    t = re.sub(r"[^\w\- ]", "", t)
    return t.replace(" ", "-")


def ancoras_md(texto):
    vistos = {}
    ancoras = set()
    em_codigo = False
    for linha in texto.splitlines():
        if linha.lstrip().startswith("```"):
            em_codigo = not em_codigo
            continue
        m = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", linha)
        if m and not em_codigo:
            base = slug(m.group(1))
            n = vistos.get(base, 0)
            ancoras.add(base if n == 0 else f"{base}-{n}")
            vistos[base] = n + 1
    ancoras.update(re.findall(r'id="([^"]+)"', texto))
    return ancoras


def main(paths):
    if not paths:
        print(__doc__)
        return 2
    erro = False
    for path in paths:
        texto = open(path, encoding="utf-8").read()
        if path.endswith((".html", ".htm")):
            ancoras = set(re.findall(r'id="([^"]+)"', texto))
            links = re.findall(r'href="#([^"]+)"', texto)
        else:
            ancoras = ancoras_md(texto)
            links = re.findall(r"\]\(#([^)]+)\)", texto)
        quebrados = sorted({unquote(l) for l in links if unquote(l) not in ancoras})
        if quebrados:
            erro = True
            print(f"[ERRO] {path}: {len(quebrados)} âncora(s) sem seção correspondente:")
            for q in quebrados:
                print(f"  - #{q}")
        else:
            print(f"[OK] {path}: {len(set(links))} links do índice válidos")
    return 1 if erro else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
