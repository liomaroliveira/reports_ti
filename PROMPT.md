# 📋 Prompt de Execução Semanal — Setor de TI

> Cole ou referencie este arquivo para pedir a geração do relatório. Não edite por semana: datas e focos ficam em `semanas/<semana>/PARAMETROS.md`.

---

Gere os relatórios da **semana corrente** (pasta mais recente em `semanas/`), seguindo:

1. `AGENTS.md` — regras invioláveis, estrutura e convenções.
2. `semanas/<semana>/PARAMETROS.md` — datas, período operacional efetivo e focos da semana.
3. `docs/fluxo_geracao.md` — execute as fases na ordem:
   - **Fase 0:** rode `python3 scripts/checar_entradas.py` e mostre a tabela. Se faltar fonte essencial, **pare e pergunte**.
   - **Etapa 1:** relatório individual de Liomar (se `individuais/liomar.*` não existir).
   - **Fase 1.5:** individuais de Isac e David — se faltarem, **pare e pergunte** (aguardar ou fallback).
   - **Etapa 2:** relatório consolidado `report_ti_<Domingo>_<Sábado>.{md,html,pdf}`.
4. `docs/especificacao_relatorio.md` — moldura, índice, tópicos e visual (`templates/report.html` + `templates/report.css`).
5. `docs/regras_metricas.md`, `docs/fontes_de_dados.md`, `docs/classificacao_protocolos.md`, `docs/glossario.md`.
6. `docs/licoes_aprendidas.md` e o `feedback.md` da semana anterior.

Antes de concluir: `python3 scripts/validar_indice.py` nos relatórios gerados, `bash scripts/renderizar_pdf.sh` para os PDFs e commit no Git.

**Lembretes críticos:** nunca inventar ou reaproveitar números de semanas anteriores · toda afirmação com protocolo, commit ou caminho da fonte · CPFs mascarados · WhatsApp (`miscelaneous/`) não é fonte.
