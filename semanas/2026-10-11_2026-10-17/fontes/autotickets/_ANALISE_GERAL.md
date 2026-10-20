# Análise geral: exportações do AutoTickets (semana 42: 11/10 a 17/10/2026)

> Este arquivo resume os `_ANALISE_FONTE.md` de cada pasta. Serve de feedback para o AutoTickets e para ajustes manuais. **Não é fonte do relatório.**

## Visão geral

- **Codificação:** nenhum formato tem problema de codificação. Os CSVs são UTF-8 com BOM.
- **Divergência entre formatos:** a exportação de um mesmo relatório **não é equivalente entre formatos**:
  - o MD costuma omitir a coluna de mensagem;
  - o HTML e o PDF truncam textos;
  - o CSV não traz período nem KPIs;
  - o PDF perde colunas e registros (tarefas executadas do David).
- **KPIs incoerentes:** em vários módulos, os KPIs do cabeçalho **não são calculados a partir das mesmas linhas exportadas**. Exemplos:
  - colaborador × ticket: 68 × 76 linhas e 102 × 103 × 115 ações;
  - Fullcam lucros: os KPIs do PDF não fecham com o CSV;
  - instalação: 7 × 9 câmeras.
- **Período:** cada módulo usa um. Inadimplência e instalação usam **30 dias móveis** (20/09 a 20/10). Lucros não tem período. PPPoE é um retrato de 18 a 19/10. Apenas colaborador × ticket, WiFeed e tarefas executadas cobrem a semana.
- **Ruído:** 96% a 97% das linhas de inadimplência e de instalação são NOTIFY ou avisos repetidos.
  - Na inadimplência, os NOTIFY **pararam em 06/10**: verificar o agendador.
  - Na instalação, o protocolo 3198228 está preso na fila desde 20/09.
- **Dados sensíveis:** CPF/CNPJ (lucros e PPPoE), stream keys RTMP e e-mails (instalação) e senhas em relatos (tarefas executadas) estavam sem máscara. **Os arquivos de texto foram mascarados em 19/10.** Por decisão da mesma data, os PDFs também são versionados, porque o uso é interno, e o pre-commit apenas avisa.

## Formato recomendado por módulo

| Módulo | Formato | Motivo |
| :--- | :--- | :--- |
| colaborador_x_ticket | **MD** (+ CSV para colunas extras) | Tem resumo e detalhe em 20 KB. O CSV tem 20 colunas, mas não tem período nem KPIs. O HTML só acrescenta TMA e TMR globais. |
| wifeed_daily_update_voucher | **CSV** ou **MD** | São os únicos com evolução diária e pico/mínimo em texto. O SVG do HTML é redundante, e o PDF perde os valores. |
| fullcam_automacao_inadimplencia | **CSV filtrado** (sem NOTIFY, só a semana) | É o único com a mensagem completa. O HTML e o PDF truncam, e o MD omite a mensagem. |
| fullcam_automacao_instalacao_camera | **MD** (ou CSV mascarado) | Os avisos repetidos devem ser descartados. |
| fullcam_lucros_prejuizos | **CSV mascarado** | Permite recalcular os KPIs. Os do PDF não são confiáveis. |
| acompanhamento_protocolos | **MD** | É idêntico ao PDF, mas o texto é gerado por IA e precisa ser confirmado no Voalle. |
| tarefas_executadas | **CSV** | Reproduz exatamente o Voalle por **Inclusão**, e o conteúdo bate 100%. O PDF corta relatos e perde registros. |
| anomalias_pppoe | **CSV + PDF** (retrato atual) | O IP, os KPIs e os filtros só existem no PDF. |
| Voalle (ERP) | **HTML, por Lançamento** | Está completo. O PDF do David não tem as horas. Lançamento conta cada apontamento uma única vez. |

**Formatos que podem deixar de ser exportados para o relatório semanal:** os PDFs do AutoTickets e o HTML de quase todos os módulos.

## Prioridades para o exportador do AutoTickets

1. **Máscara na origem:** CPF/CNPJ, e-mails de clientes, stream keys RTMP, senhas em relatos e, no PDF, nome + IP juntos.
2. **Período solicitado** (domingo a sábado) em **todos** os módulos, com o filtro declarado no cabeçalho e no nome do arquivo (`<modulo>_<inicio>_<fim>_gerado-<AAAAMMDDTHHMM>`, em **data local**, não UTC).
3. **Um snapshot por exportação:** todos os formatos gerados a partir dos mesmos dados, com o mesmo `generated_at`.
4. **KPIs calculados das linhas exportadas**, com a fórmula documentada e uma linha de totais ou um bloco de metadados no CSV.
5. **Agregar logs repetitivos** (NOTIFY, avisos) em uma linha de resumo e **alertar** quando uma rotina parar.
6. **Não truncar texto** em nenhum formato. Preservar quebras de linha e marcar imagens.
7. **Valores crus no CSV:** número sem separador de milhar, decimal com ponto, datas em ISO 8601 e duração em segundos. A formatação brasileira fica só no PDF e no HTML.
8. **Validações automáticas:**
   - durações acima de 365 dias (3217119 = 20670 dias);
   - protocolos citados que não existem;
   - linhas duplicadas;
   - status incoerente com o progresso.
9. **Formato-alvo:** um único **pacote semanal em JSON**, especificado em [`docs/formato_exportacao_autotickets.md`](../../../../docs/formato_exportacao_autotickets.md). Ele substitui todos os arquivos acima. Pendências consolidadas: [`../../_PENDENCIAS_AUTOTICKETS.md`](../../_PENDENCIAS_AUTOTICKETS.md).
10. *(Detalhe do item 9)* Uma exportação **"pacote da semana"** com todos os módulos em CSV + um `manifest.json` (período, contagens, somas, checksums). O `scripts/checar_entradas.py` poderia conferir esse pacote automaticamente.
