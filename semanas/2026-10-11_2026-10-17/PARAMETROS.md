# ⚙️ Parâmetros da Semana 42 / 2026

> [!NOTE]
> Único arquivo editado à mão a cada semana. Fluxo: `docs/fluxo_geracao.md` · Estrutura: `docs/especificacao_relatorio.md`.

- **Data Inicial (Domingo Oficial):** `2026-10-11`
- **Data Final (Sábado Oficial):** `2026-10-17`
- **Período Operacional Efetivo do TI (Segunda a Sexta):** `2026-10-13` a `2026-10-16` <!-- ajustar: 12/10 é feriado -->
- **Semana do Ano:** Semana 42 / 2026
- **Colaborador Principal (Responsável pela Consolidação):** Liomar Antonio de Oliveira
- **Prazo de Entrega:** `2026-10-19` (segunda-feira) até as 14h — **entrega adiada**; relatório gerado em 2026-10-20
- **Relatórios individuais a gerar:** nenhum <!-- padrão: só o consolidado. Para gerar, liste: liomar, isac, david -->

## 📝 Instruções e Focos Específicos Desta Semana

<!-- Escreva aqui apenas o que é ESPECÍFICO desta semana: destaques, eventos, feriados, pontos de atenção. -->
<!-- Não escreva números esperados: todos os valores devem ser extraídos das fontes do período. -->

1. **Feriado:** 2026-10-12 (segunda) é feriado nacional (Nossa Senhora Aparecida). Não houve expediente do Setor de TI neste dia.
2. **AutoTickets (4.1):** minerar os commits do `autotickets_v2` (`AUTOTICKETS_REPO`, padrão `~/dev/autotickets_v2`) entre 2026-10-11 e 2026-10-17.
3. **Pendências do feedback anterior:** cobrir os itens listados em `docs/licoes_aprendidas.md` (Wazuh/filiais, telefonia fixa, backups, veículos, Windows 10 × 11).
4. **Feedback da semana 41** (`semanas/2026-10-04_2026-10-10/feedback.md`, 8 observações): tratar todas na tabela de acompanhamento do Resumo Executivo. Destaques: Fullcam (ignorar o contrato 96660 de DAVID BRASIL FERNANDES), apontamentos deixados em play (fechar relatos no fim do expediente), frota escalada ao COO, Slack com MFA 3 de 6 (**pendência com marca de atenção**), descrição de cargos (3218356) e a gincana de pentest começando pelo sistema de Compras (3218766).
5. **Primeira geração com tópicos dinâmicos:** aplicar "Classes de Tópicos" (`docs/especificacao_relatorio.md`): 📈 Destaques Analíticos, tópico condicional 8.4 PPPoE (retrato atual) e subtópicos livres. Ler os `_ANALISE_*.md` das fontes antes de usar os números (há KPIs do AutoTickets que não fecham).
6. **Horas do Voalle:** usar a exportação por **Lançamento** (`fontes/voalle/<pessoa>_tarefas_executadas_20261019_221147.html`). As versões `_por_data_inclusao` servem só para a comparação. Listar no 2.4 os apontamentos longos (3217119 e 3218766).

## 📥 Entradas esperadas

- [x] `fontes/voalle/`: HTML por Lançamento (Liomar, Isac, David). As versões por Inclusão foram removidas em 2026-10-20 (a comparação está no `_ANALISE_FONTE.md`)
- [x] `fontes/autotickets/colaborador_x_ticket/`
- [x] `fontes/autotickets/wifeed_daily_update_voucher/` (`.md` + `.html` com o SVG)
- [x] `fontes/autotickets/fullcam_lucros_prejuizos/`
- [x] `fontes/autotickets/fullcam_automacao_inadimplencia/`
- [x] `fontes/autotickets/fullcam_automacao_instalacao_camera/`
- [x] `fontes/autotickets/acompanhamento_protocolos/` (análise por IA de 26 protocolos, acumulada; usada só com cautela)
- [x] `fontes/autotickets/tarefas_executadas/` (CSV por colaborador; o PDF corta relatos — ver `_ANALISE_FONTE.md`)
- [x] `fontes/autotickets/anomalias_pppoe/` (CSV + PDF → tópico condicional 8.4; **retrato atual** de 19/10 22:07, sem recorte da semana)
- [x] `fontes/autotickets/problemas_recorrentes/` (versão final `reincidencia_20261019_234621.md`: semana 11–17/10, retorno até 60 dias; `todas_equipes/` é só referência)
- [ ] `fontes/infraestrutura/backups/` (quadrante do 8.2; sem fonte nesta semana → declarar ausência, nunca estimar)
- [ ] `fontes/investigacoes/`: estudos datados da semana (se houver)
- [ ] `individuais/`: relatórios que Isac e David enviarem (opcional; usados como fonte complementar)
- [x] Observações suas e do Isvi sobre o relatório da semana 41 em `semanas/2026-10-04_2026-10-10/feedback.md`
- [x] Decidir o feriado de 12/10 (sem expediente)

Depois de copiar: `python3 scripts/checar_entradas.py`. Formato esperado de cada fonte: `_FORMATO_ESPERADO.md` em cada pasta.

> **Qualidade das fontes desta semana:** cada pasta de `fontes/` tem um `_ANALISE_FONTE.md` (e `fontes/autotickets/_ANALISE_GERAL.md`) com divergências entre formatos e campos não confiáveis. Respeitar as ressalvas ao gerar o relatório. Verificações da equipe: `_VERIFICAR_EQUIPE_TI.md` · Pendências do AutoTickets: `_PENDENCIAS_AUTOTICKETS.md` (nenhum dos dois é fonte).

## 📌 Status da geração (2026-10-20)

- **Gerado:** `report_ti_2026-10-11_2026-10-17.{md,html,pdf}` (consolidado; individuais não pedidos). `validar_indice.py` e `validar_relatorio.py` sem erros.
- **Ausências declaradas no relatório:** backups (8.2), Pontomais (2.4), `produtividade_geral` (4.5), investigações (8.3), pacote semanal.
- **Correções feitas ao relatório da semana 41 (registradas no texto):** quadrante de backups sem fonte, 45h45m de economia sem fonte, "100% DatabaseTransactions" (62 arquivos ainda com RefreshDatabase), automação WiFeed diária (não semanal).
- **Pendências para a semana 43:** ver 9.3 do relatório (perfctl/Flashman #3219879, apontamentos longos do Liomar, ZEUS #3137037, gincana de pentest, segredo do webhook Fullcam, quadrante de backups).
