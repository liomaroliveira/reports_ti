# Análise da fonte — Colaborador × Ticket (semana 42: 11/10 a 17/10/2026)

> Feedback sobre a qualidade da exportação, para ajustes manuais e para o AutoTickets. **Não é fonte do relatório.**

**Arquivos:**

- `relatorio_colaboradores_tickets_20261019_213740.pdf`
- `…_213759.html`
- `…_213803.md`
- `…_213807.csv`

## Período e geração

- **Período declarado:** MD, HTML e PDF declaram 11/10/2026 a 17/10/2026, o que está correto.
- **CSV sem cabeçalho:** o CSV não informa período nem data de geração. Ele começa direto nas colunas.
- **Horários de geração diferentes:** cada formato foi gerado num horário (PDF 21:37:40, HTML 21:37:59, MD 21:38:03). Não há um snapshot único, então os formatos podem divergir se o banco mudar entre as gerações.
- **Linhas fora do período:**
  - 25 das 76 linhas têm abertura anterior a 11/10.
  - 3 linhas foram encerradas em 19/10 (3222238, 3202572 e 3223486) e aparecem como "Concluído" na semana.

## Contagens por formato

| Item | MD | HTML | PDF | CSV |
| :--- | :---: | :---: | :---: | :---: |
| Linhas de detalhe | 76 | 76 | 76 | 76 |
| Rótulo "chamados detalhados" | — | **68** | **68** | — |
| Colunas do detalhe | 11 | 11 | 11 | **20** |
| Blocos de resumo (KPIs, por colaborador, por tipo) | sim | sim | sim | **não** |
| TMA médio (2h20m) e TMR médio (4d3h) globais | **não** | sim | sim | não |

- **Linhas por colaborador:** ISAC 18, DAVID 47, LIOMAR 11.
- **O número "68" não confere com nenhuma contagem:** são 76 linhas, 66 protocolos únicos e 73 pares protocolo + colaborador.

## Inconsistências de dados (iguais em todos os formatos)

| Indicador | Valor exibido | Valor recalculado | Observação |
| :--- | :--- | :--- | :--- |
| Total de Ações | 102 | 103 na tabela de distribuição; **115** somando a coluna Ações do CSV (DAVID 63, ISAC 31, LIOMAR 21) | Três totais diferentes para o mesmo indicador |
| Encaminhamentos | 27 | 29 (soma do CSV) | |
| LIOMAR "Sol. Concl." | 5 | 2 linhas "Concluído" no detalhe | |
| Tempo de Atendimento de 3217119 | **20670d 17h** (cerca de 56 anos) | — | Data nula convertida em epoch (1970). Esse valor contamina TMA e TMR. |
| "Equipe do Colaborador" (CSV) | Mostra a equipe do ticket | — | 17 linhas com "ADM Operacional", "COTAÇÕES", "Patrimônio e Logística" etc. |

## Duplicidades

São 66 protocolos únicos distribuídos em 76 linhas. Nenhuma linha é 100% idêntica a outra, mas há repetições sem explicação:

- **3221254:** aparece 4 vezes (2 com ISAC e 2 com DAVID), com Ações 5 e 1 e tempos diferentes.
- **3223577:** aparece como Tarefa e também como Solicitação.
- **3069558:** aparece 3 vezes, uma por colaborador.
- **3078726, 3221925, 3215368 e 3181397:** aparecem 2 vezes cada.

## Dados desnecessários e ruído

- **Bug no MD:** a linha "Gerado em" contém um `\n` literal (`21:38:03  \n**Colaboradores Avaliados:** 3`). O bug já existia na semana 41.
- **HTML pesado:** o HTML tem 153 KB, dos quais cerca de 11 KB são CSS e cerca de 3 KB são JS.
- **Ícones e emojis:** os ícones "⇅" e "ⓘ" vazam para o texto do PDF, e os títulos têm emojis.
- **PDF difícil de extrair:** as páginas são muito largas, e a extração quebra datas e títulos.

## Dados sensíveis

- **CPF, CNPJ, telefone e e-mail:** nenhum.
- **Nomes de clientes:** aparecem nos títulos e na coluna Cliente do CSV (15 linhas).

## Formato recomendado para o relatório consolidado

**MD**, que tem resumo e detalhe em cerca de 20 KB. Use o **CSV** como complemento quando precisar de Encerrado Por, Cliente, Encaminhamentos ou Prioridade. O HTML só acrescenta o TMA e o TMR globais. O PDF não acrescenta nada.

## Correções sugeridas ao AutoTickets (por prioridade)

1. **Corrigir durações nulas e absurdas** (3217119 = 20670 dias): validar intervalos acima de 365 dias e excluí-los do TMA e do TMR.
2. **Fazer os totais baterem com o detalhe:** "68 chamados", "102 ações", "103 total" e "27 encaminhamentos" precisam sair das mesmas linhas exportadas.
3. **Recortar pelo período** ou incluir a coluna `fora_do_periodo`. Chamados encerrados depois do fim do período não podem entrar como "Concluído".
4. **Deduplicar** por (protocolo, colaborador, tipo) ou explicar a repetição numa coluna (ex.: "papel" = abertura, encaminhamento, execução).
5. **Corrigir o rótulo** "Equipe do Colaborador" e separar `equipe_colaborador` de `equipe_ticket`.
6. **Incluir no CSV** uma linha de metadados (período e `generated_at`) e os KPIs, ou gerar um `.json` de resumo.
7. **Incluir TMA e TMR globais no MD** e corrigir o `\n` literal.
8. **Gerar todos os formatos a partir de um único snapshot**, com o mesmo `generated_at`.
