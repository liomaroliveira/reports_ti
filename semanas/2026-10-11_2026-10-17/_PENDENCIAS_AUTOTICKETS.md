# 🛠️ Pendências do AutoTickets: exportações para o relatório semanal

> Lista de correções no `autotickets_v2` levantadas na análise das fontes da semana 42 (11/10 a 17/10/2026). **Não é fonte do relatório.** O detalhe e as evidências de cada item estão no `_ANALISE_FONTE.md` de cada pasta. O formato-alvo que substitui todos os anexos está em [`docs/formato_exportacao_autotickets.md`](../../docs/formato_exportacao_autotickets.md).
>
> **Prioridade:** **P1** = dado errado que muda a leitura do relatório ou rotina parada · **P2** = inconsistência ou omissão · **P3** = formato e conforto.

## P1: corrigir antes do próximo relatório

| # | Módulo | Problema | Evidência | Ação | Detalhe |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | colaborador_x_ticket | **"Tempo Atendimento" de 20670 dias** (cerca de 56 anos) no protocolo 3217119 | É o único chamado "Em Execução" do relatório. `CollaboratorTicketReportService.php:493` usa `in_execution` como **data** de início, mas esse campo só serve como indicador (`IS NOT NULL`) no resto do sistema. O `abs()` na linha 499 esconde o erro. Início implícito: 10/03/1970 | Confirmar o tipo e o valor de `assignments.in_execution` (SQL no detalhe). Usar `first_report_at`, remover o `abs()`, validar intervalos acima de 365 dias e criar teste com chamado em execução | [colaborador_x_ticket](fontes/autotickets/colaborador_x_ticket/_ANALISE_FONTE.md#investigação-tempo-atendimento-de-20670-dias-3217119) |
| 2 | fullcam_automacao_inadimplencia | **Checagem horária (NOTIFY) parada desde 06/10 20:45**. Nenhuma execução na semana 42 | Mais de 390 execuções de hora em hora até 06/10, e depois nada | Verificar o agendador e a fila. Criar alerta quando a rotina ficar mais de 2 intervalos sem rodar | [inadimplência](fontes/autotickets/fullcam_automacao_inadimplencia/_ANALISE_FONTE.md) |
| 3 | fullcam_lucros_prejuizos | **Contrato sem câmera tratado como videomonitoramento** | DAVID BRASIL FERNANDES, contrato 96660: 15 faturas, R$ 455,61, **0 GB**, sem etiqueta do serviço (apontado pelo Isvi) | Exigir a etiqueta ou o serviço de videomonitoramento na regra. Sinalizar contratos com 0 GB | [Fullcam financeiro](fontes/autotickets/fullcam_lucros_prejuizos/_ANALISE_FONTE.md) |
| 4 | fullcam_lucros_prejuizos | **KPIs do PDF não fecham com o CSV** | Saldo líquido de R$ 5.197,31 no PDF × 7.165,88 no CSV; perdas de 450 × 1.350 | Calcular os KPIs a partir das mesmas linhas e documentar a fórmula | idem |
| 5 | tarefas_executadas | **Critério de data fixo e não declarado** (reproduz o "Inclusão" do Voalle) | Liomar: 96:24 no AutoTickets × 306:11 no Voalle por Lançamento | Parâmetro `filtro_periodo` (lançamento, inclusão ou sobreposição), declarado no cabeçalho e no nome do arquivo, com padrão `sobreposicao` e `segundos_no_periodo` | [tarefas executadas](fontes/autotickets/tarefas_executadas/_ANALISE_FONTE.md) |
| 6 | fullcam_automacao_instalacao_camera | **Item preso na fila** gerando 209 avisos idênticos | Protocolo 3198228, contrato interno 85854, "Nenhuma câmera localizada", a cada 2h desde 20/09 | Agrupar em "pendência presa desde DD/MM, N tentativas". Avisar a equipe para corrigir o cadastro | [instalação](fontes/autotickets/fullcam_automacao_instalacao_camera/_ANALISE_FONTE.md) |

## P2: inconsistências e omissões

| # | Módulo | Problema | Ação |
| :-: | :--- | :--- | :--- |
| 7 | colaborador_x_ticket | Totais incoerentes: "68 chamados" para 76 linhas; ações 102 × 103 × 115; encaminhamentos 27 × 29; "Sol. Concl." do Liomar 5 × 2 | Calcular os KPIs das linhas exportadas |
| 8 | colaborador_x_ticket | Linhas fora do período (25 abertas antes, 3 encerradas em 19/10 contadas como "Concluído") e protocolos repetidos sem explicação (3221254 ×4, 3069558 ×3) | Recortar pelo período ou usar a flag `fora_do_periodo`. Coluna `papel` |
| 9 | colaborador_x_ticket | "Equipe do Colaborador" mostra a equipe do ticket | Separar `equipe_colaborador` e `equipe_ticket` |
| 10 | tarefas_executadas | Minutos arredondados por linha (CSV × PDF × Voalle divergem) | Somar segundos |
| 11 | tarefas_executadas | Apontamentos sem fim exportados como "Concluído" com 0 min (Isac, 3221254) | Coluna `em_execucao`/`sem_fim` e alerta |
| 12 | tarefas_executadas | Protocolo vazio em "Tarefa de Solicitação" (David: 3201861, 3200974, 3203059). Falta o campo **Origem**. Status sempre "Concluído" | Preencher pelo vínculo. Exportar `origem` e o status real |
| 13 | tarefas_executadas | Quebras de linha perdidas, imagens removidas sem marcador | Preservar `\n` e usar `[imagem: N]` |
| 14 | tarefas_executadas (PDF) | Relato cortado em 140 caracteres, 7 registros a menos no David, sem coluna Data no Isac | Corrigir ou descontinuar o PDF |
| 15 | fullcam_inadimplencia / instalacao | Janela móvel de 30 dias (20/09 a 20/10) que se sobrepõe à semana anterior. Câmeras não únicas. "Câmeras afetadas 7" × 9 reais (#786). Reprocessamento 758–762 sem marca | Período pedido, contagem de únicos, `id_original` |
| 16 | wifeed | Base de 14/10: 32.604 no histórico × 32.611 na evolução. "Excluído" × "100% sucesso / 0 falhas" | Investigar o valor. Status "Substituído" para o segmento antigo, que não conta como falha |
| 17 | anomalias_pppoe | Volume acumulado por sessão (não "24h"), throughput inflado pelas quedas, severidade incoerente com o score (60 = CRITICAL e HIGH), 4 falsos positivos (1,04x–1,16x) | Bytes dentro da janela, throughput por tempo online, regra de severidade publicada, limiar de razão ≥ 1,5x |
| 18 | anomalias_pppoe | IP, KPIs e filtros só no PDF. Faltam primeira detecção, recorrência e ticket aberto. Faltam rótulos interno (o contrato 00900 é da Ten Internet) e revenda | Incluir no CSV ou no pacote |
| 18b | problemas_recorrentes | Temas mostrados como radicais de palavras; retornos com mediana de minutos (Inventário: TALKD/STEIN); sem CSV; sem filtro da equipe do TI; 815 temas, longo demais | Assunto ou categoria legível, intervalo mínimo para contar retorno, coluna `equipe_tratou`, módulo `reincidencia` no pacote |
| 19 | acompanhamento_protocolos | Texto da IA não determinístico: status "Novo" × "resolvidos", 3306821 possivelmente inexistente | Tabela determinística do Voalle mais a análise da IA separada, com validação dos protocolos citados |

## P3: formato e conforto

| # | Problema | Ação |
| :-: | :--- | :--- |
| 20 | Cada formato é gerado num horário diferente, e o nome do arquivo usa data em UTC (`2026-10-20` para geração em 19/10 22h) | Um snapshot só, nome com período, filtro e data **local** |
| 21 | O CSV não tem período nem KPIs. O MD não tem a mensagem. HTML e PDF truncam | Resolvido pelo pacote semanal |
| 22 | Números formatados no CSV ("32.604", "R$ 1287.33"), emojis e ícones vazando no texto | Valores crus no CSV. Formatação só na apresentação |
| 23 | `\n` literal no MD do colaborador × ticket. Rodapé "Página 1 de 1" num PDF de 2 páginas (WiFeed) | Correções pontuais |
| 24 | Dados sensíveis nos textos: CPF/CNPJ sem pontuação, stream keys RTMP, e-mails de clientes, senhas em relatos | Mascarar na origem: CPF/CNPJ mascarado; senha e stream key removidas. Nome, contrato e IP permanecem (uso interno) |

## Meta: pacote semanal único

Substituir todos os arquivos por **um JSON por semana**: `fontes/autotickets/pacote_semanal/autotickets_semana_<inicio>_<fim>.json`. A especificação completa está em [`docs/formato_exportacao_autotickets.md`](../../docs/formato_exportacao_autotickets.md). O `scripts/checar_entradas.py` já reconhece o pacote, confere o período e lista as validações com falha.

**Critério para dispensar o Voalle:** em 2 semanas seguidas, os totais por colaborador batem com o Voalle nos critérios Lançamento e Inclusão, e as `validacoes` do pacote ficam todas `ok`.

## Índice das análises por fonte

- [Análise geral e formato recomendado por módulo](fontes/autotickets/_ANALISE_GERAL.md)
- [Colaborador × ticket](fontes/autotickets/colaborador_x_ticket/_ANALISE_FONTE.md)
- [Tarefas executadas: AutoTickets × Voalle](fontes/autotickets/tarefas_executadas/_ANALISE_FONTE.md)
- [WiFeed](fontes/autotickets/wifeed_daily_update_voucher/_ANALISE_FONTE.md)
- [Fullcam financeiro](fontes/autotickets/fullcam_lucros_prejuizos/_ANALISE_FONTE.md)
- [Fullcam inadimplência](fontes/autotickets/fullcam_automacao_inadimplencia/_ANALISE_FONTE.md)
- [Fullcam instalação de câmeras](fontes/autotickets/fullcam_automacao_instalacao_camera/_ANALISE_FONTE.md)
- [Acompanhamento de protocolos](fontes/autotickets/acompanhamento_protocolos/_ANALISE_FONTE.md)
- [Anomalias PPPoE](fontes/autotickets/anomalias_pppoe/_ANALISE_FONTE.md)
- [Reincidência de problemas](fontes/autotickets/problemas_recorrentes/_ANALISE_FONTE.md)
- [Voalle ERP (Lançamento × Inclusão, HTML × PDF)](fontes/voalle/_ANALISE_FONTE.md)
