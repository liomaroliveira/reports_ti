# ⚙️ Parâmetros da Semana 42 / 2026

> [!NOTE]
> Único arquivo editado à mão a cada semana. Fluxo: `docs/fluxo_geracao.md` · Estrutura: `docs/especificacao_relatorio.md`.

- **Data Inicial (Domingo Oficial):** `2026-10-11`
- **Data Final (Sábado Oficial):** `2026-10-17`
- **Período Operacional Efetivo do TI (Segunda a Sexta):** `2026-10-13` a `2026-10-16` <!-- ajustar: 12/10 é feriado -->
- **Semana do Ano:** Semana 42 / 2026
- **Colaborador Principal (Responsável pela Consolidação):** Liomar Antonio de Oliveira
- **Prazo de Entrega:** `2026-10-19` (segunda-feira) até as 14h — **entrega adiada** (dados ainda não gerados)
- **Relatórios individuais a gerar:** nenhum <!-- padrão: só o consolidado. Para gerar, liste: liomar, isac, david -->

## 📝 Instruções e Focos Específicos Desta Semana

<!-- Escreva aqui apenas o que é ESPECÍFICO desta semana: destaques, eventos, feriados, pontos de atenção. -->
<!-- Não escreva números esperados: todos os valores devem ser extraídos das fontes do período. -->

1. **Feriado:** 2026-10-12 (segunda) é feriado nacional (Nossa Senhora Aparecida). Não houve expediente do Setor de TI neste dia.
2. **AutoTickets (4.1):** minerar os commits do `autotickets_v2` (`AUTOTICKETS_REPO`, padrão `~/dev/autotickets_v2`) entre 2026-10-11 e 2026-10-17.
3. **Pendências do feedback anterior:** cobrir os itens listados em `docs/licoes_aprendidas.md` (Wazuh/filiais, telefonia fixa, backups, veículos, Windows 10 × 11).

## 📥 Entradas esperadas

- [ ] `fontes/voalle/`: `liomar.*`, `isac.*`, `david.*`
- [ ] `fontes/autotickets/colaborador_x_ticket/`
- [ ] `fontes/autotickets/wifeed_daily_update_voucher/` (`.md` + `.html` com o SVG)
- [ ] `fontes/autotickets/fullcam_lucros_prejuizos/`
- [ ] `fontes/autotickets/fullcam_automacao_inadimplencia/`
- [ ] `fontes/autotickets/fullcam_automacao_instalacao_camera/`
- [ ] `fontes/autotickets/acompanhamento_protocolos/` (os CSVs de 2026-10-16 foram removidos no commit `0de3892`: gerar de novo cobrindo a semana inteira)
- [ ] `fontes/autotickets/tarefas_executadas/` (CSV por colaborador; o PDF corta relatos — ver `_ANALISE_FONTE.md`)
- [ ] `fontes/autotickets/anomalias_pppoe/` (CSV mascarado → tópico 8.4; retrato de 18–19/10, fora da semana: rotular)
- [ ] `fontes/investigacoes/`: estudos datados da semana (se houver)
- [ ] `individuais/`: relatórios que Isac e David enviarem (opcional; usados como fonte complementar)
- [ ] *(Opcional)* Observações suas e do Isvi sobre o relatório da semana 41 em `semanas/2026-10-04_2026-10-10/feedback.md` (arquivo já criado a partir do template)
- [ ] Decidir o feriado de 12/10 (acima)

Depois de copiar: `python3 scripts/mascarar_dados.py <arquivos>` e `python3 scripts/checar_entradas.py`.

> **Qualidade das fontes desta semana:** cada pasta de `fontes/` tem um `_ANALISE_FONTE.md` (e `fontes/autotickets/_ANALISE_GERAL.md`) com divergências entre formatos e campos não confiáveis. Respeitar as ressalvas ao gerar o relatório. PDFs com dados sensíveis estão no `.gitignore` (não versionados).
