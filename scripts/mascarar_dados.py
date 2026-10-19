#!/usr/bin/env python3
"""
Mascara CPFs (LGPD) em arquivos de texto antes de versionar exportações brutas.

Formato aplicado: AAA.BBB.CCC-DD -> ***.BBB.CCC-**

Uso:
    python3 scripts/mascarar_dados.py semanas/2026-10-11_2026-10-17/fontes/voalle/* semanas/2026-10-11_2026-10-17/fontes/autotickets/*/*

PDFs não são alterados: para PDFs, gere a partir do HTML/CSV já mascarado.
"""

import re
import sys

CPF = re.compile(r"\b\d{3}\.(\d{3})\.(\d{3})-\d{2}\b")
TEXT_EXT = (".md", ".html", ".htm", ".csv", ".txt", ".json")


def mascarar(texto):
    return CPF.subn(r"***.\1.\2-**", texto)


def main(paths):
    if not paths:
        print(__doc__)
        return 1
    total = 0
    for path in paths:
        if not path.lower().endswith(TEXT_EXT):
            print(f"[IGNORADO] {path} (não é texto; gere o PDF a partir da versão mascarada)")
            continue
        with open(path, "r", encoding="utf-8", errors="surrogateescape", newline="") as f:
            original = f.read()
        novo, n = mascarar(original)
        if n:
            with open(path, "w", encoding="utf-8", errors="surrogateescape", newline="") as f:
                f.write(novo)
        total += n
        print(f"[OK] {path}: {n} CPF(s) mascarado(s)")
    print(f"Total: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
