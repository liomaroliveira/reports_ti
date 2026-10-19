# 📋 Prompt de Execução Semanal — Setor de TI

> Cole ou referencie este arquivo para pedir a geração do relatório. Não edite por semana: datas e focos ficam em `semanas/<semana>/PARAMETROS.md`.

---

Gere o **relatório semanal consolidado** da semana a gerar (pasta mais recente em `semanas/` cujo sábado já passou). Relatórios individuais **somente** se eu pedir abaixo ou em `PARAMETROS.md`. Siga:

1. `AGENTS.md` — regras invioláveis, estrutura e convenções.
2. `semanas/<semana>/PARAMETROS.md` — datas, período operacional efetivo e focos da semana.
3. `docs/fluxo_geracao.md` — execute as fases na ordem:
   - **Fase 0:** rode `python3 scripts/checar_entradas.py` e mostre a tabela. Se faltar fonte essencial, **pare e pergunte**.
   - **Fase 1:** leia o relatório consolidado e o `feedback.md` da semana anterior: dê desfecho a pendências e ações planejadas e trate cada observação.
   - **Etapa principal:** relatório consolidado `report_ti_<Domingo>_<Sábado>.{md,html,pdf}`.
   - **Etapa opcional:** individuais, apenas se pedidos.
4. `docs/especificacao_relatorio.md` — moldura, índice, tópicos e visual (`templates/report.html` + `templates/report.css`).
5. `docs/regras_metricas.md`, `docs/fontes_de_dados.md`, `docs/classificacao_protocolos.md`, `docs/glossario.md`.
6. `docs/licoes_aprendidas.md`.

Antes de concluir: `python3 scripts/validar_indice.py` nos relatórios gerados, `bash scripts/renderizar_pdf.sh` para os PDFs e commit no Git.

**Lembretes críticos:** nunca inventar dados nem usar números de semanas anteriores como dado atual (só como comparação rotulada) · toda afirmação com protocolo, commit ou caminho da fonte · CPFs mascarados · WhatsApp (`miscelaneous/`) não é fonte.

---

## Como pedir

| O que você quer | Prompt |
| :--- | :--- |
| Relatório da semana (padrão: só o consolidado) | `Execute o PROMPT.md` |
| Consolidado + individuais | `Execute o PROMPT.md e gere também os relatórios individuais de Liomar e Isac` |
| Uma semana específica | `Execute o PROMPT.md para a semana 2026-10-11_2026-10-17` |
| Só conferir as entradas | `Rode a Fase 0 do PROMPT.md e me mostre o que falta` |
| Ajustar um relatório já gerado | `Revise o relatório da semana 2026-10-11_2026-10-17: <o que mudar>` |
