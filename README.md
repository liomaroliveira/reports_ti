# 📊 Relatórios Semanais do Setor de TI — Ten Internet

Repositório do processo de coleta, consolidação e geração dos relatórios semanais do **Setor de TI** da **Ten Soluções e Serviços LTDA (Ten Provedor de Internet)**, entregues toda segunda-feira até as 14h ao Coordenador de TI (**Isvi Neemias**) para a Dashboard Executiva da Direção.

**Equipe:** Liomar Antonio de Oliveira (Analista Sr — consolidação e AutoTickets) · Isac Costa Silva (Assistente Pl) · David Brasil Fernandes (Auxiliar Jr).

---

## 🗓️ Rotina semanal

```bash
# 1. Criar a pasta da semana (por padrão, a última semana Dom–Sáb completa)
bash scripts/nova_semana.sh

# 2. Editar semanas/<semana>/PARAMETROS.md (focos, feriados)

# 3. Copiar as entradas
#    semanas/<semana>/fontes/voalle/liomar.html | isac.pdf | david.csv
#    semanas/<semana>/fontes/autotickets/<modulo>/...
#    semanas/<semana>/individuais/<pessoa>.*   (se os colegas enviarem)

# 4. Mascarar CPFs das exportações brutas
python3 scripts/mascarar_dados.py semanas/<semana>/fontes/voalle/* semanas/<semana>/fontes/autotickets/*/*

# 5. Conferir as entradas
python3 scripts/checar_entradas.py

# 6. Pedir à IA (Antigravity ou Claude Code): "Execute o PROMPT.md"

# 7. Conferir índice e gerar PDFs (a IA também faz isso no fim do fluxo)
python3 scripts/validar_indice.py semanas/<semana>/report_ti_*.{md,html}
bash scripts/renderizar_pdf.sh semanas/<semana>/report_ti_<semana>.html

# 8. Quando chegar o parecer: salvar em semanas/<semana>/feedback.md
```

---

## 📁 Estrutura

```text
reports_ti/
├── AGENTS.md            # Regras permanentes para as IAs (fonte única)
├── GEMINI.md            # → link para AGENTS.md (Antigravity)
├── CLAUDE.md            # Importa AGENTS.md (Claude Code)
├── PROMPT.md            # Comando de execução semanal
├── docs/                # Fluxo, especificação, métricas, fontes, glossário, lições, referências
├── semanas/             # Uma pasta por semana: PARAMETROS.md, fontes/, individuais/, report_ti_*, feedback.md
├── templates/           # report.css (visual oficial) e report.html (esqueleto)
├── scripts/             # nova_semana, checar_entradas, mascarar_dados, validar_indice, renderizar_pdf
├── .githooks/           # pre-commit contra CPF sem máscara, chaves e dados do WhatsApp
└── miscelaneous/        # Fora do escopo: conhecimento de extração do WhatsApp
```

Detalhes de cada pasta e regra: [AGENTS.md](AGENTS.md).

---

## ⚙️ Configuração de um novo PC

```bash
git clone https://github.com/liomaroliveira/reports_ti.git ~/dev/reports_ti
cd ~/dev/reports_ti
git config core.hooksPath .githooks          # ativa o bloqueio de dados sensíveis

# AutoTickets no caminho esperado por scripts/checar_entradas.py e docs/fontes_de_dados.md
git clone <url-do-autotickets-v2> /home/liomarti/dev/autotickets-v2

python3 scripts/checar_entradas.py           # teste: deve exibir a tabela da semana corrente
```

- **Requisitos:** Python 3, Google Chrome/Chromium (`scripts/renderizar_pdf.sh`) e `pdftotext`/poppler (opcional: checagem de CPF em PDFs pelo hook).
- **Antigravity:** `GEMINI.md` é um link simbólico para `AGENTS.md`. Se o Antigravity não carregar as regras, substitua o link por um `GEMINI.md` com a linha `Leia e siga integralmente o AGENTS.md.`
- **Caminho diferente para o AutoTickets:** ajuste `AUTOTICKETS_REPO` em `scripts/checar_entradas.py` e o caminho em `docs/fontes_de_dados.md`.

> ⚠️ O histórico foi reescrito e o repositório do GitHub recriado em 2026-10-19 para remover dados sensíveis. Clones anteriores a essa data devem ser apagados; nunca faça push, pull ou merge a partir deles.
