#!/usr/bin/env bash
# Gera o PDF A4 de um relatório HTML, sem cabeçalho/rodapé do navegador.
# Antes de imprimir, embute no próprio HTML o CSS referenciado por <link ... report.css>,
# deixando o .html autocontido (pode ser enviado sozinho).
#
# Uso: bash scripts/renderizar_pdf.sh semanas/<semana>/report_ti_<...>.html [saida.pdf]
set -euo pipefail

html="$(realpath "$1")"
pdf="${2:-${html%.html}.pdf}"

python3 - "$html" <<'EOF'
import os, re, sys
path = sys.argv[1]
s = open(path, encoding="utf-8").read()
def inline(m):
    href = m.group(1)
    css_path = os.path.normpath(os.path.join(os.path.dirname(path), href))
    css = open(css_path, encoding="utf-8").read()
    return f"<style>\n{css}\n</style>"
novo, n = re.subn(r'<link[^>]+href="([^"]*report\.css)"[^>]*>', inline, s)
if n:
    open(path, "w", encoding="utf-8").write(novo)
    print(f"[OK] CSS embutido em {os.path.basename(path)}")
EOF

chrome=""
for c in google-chrome-stable google-chrome chromium chromium-browser; do
  if command -v "$c" >/dev/null 2>&1; then chrome="$c"; break; fi
done
if [ -z "$chrome" ]; then
  echo "[ERRO] Chrome/Chromium não encontrado." >&2
  exit 1
fi

"$chrome" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=10000 \
  --print-to-pdf="$pdf" "file://$html" 2>/dev/null
echo "[OK] PDF gerado: $pdf"
