# Análise da fonte — Fullcam: automação de inadimplência (semana 42: 11/10 a 17/10/2026)

> Feedback sobre a qualidade da exportação, para ajustes manuais e para o AutoTickets. **Não é fonte do relatório.**

**Arquivos analisados:**

- `relatorio_fullcam_inadimplentes_2026_10_19_220112.md`
- `…_220116.csv`
- `…_220119.html`
- `Tratamento de Inadimplência - AutoTickets.pdf` (o nome não tem data)

## Período (principal problema)

- **A janela não corresponde à semana.** Todos os formatos declaram **20/09/2026 a 20/10/2026**, uma janela móvel de cerca de 30 dias que termina no futuro. Os dados reais vão de 20/09 00:31 a 15/10 12:01.
- **A janela mudou em relação à semana 41**, que usava 14/09 a 14/10. As duas se sobrepõem, então **existe risco de contar duas vezes** se o relatório usar os totais do cabeçalho.

## Contagens por formato

- **410 registros em todos os formatos.** O PDF tem 410 IDs únicos em **42 páginas**.
- **Distribuição por tipo:** NOTIFY 394 (96%), BLOCK 12 e UNBLOCK 4, todos com status `success`.
- **Dentro da semana há apenas 4 ações:** #763 (BLOCK, 13/10), #783 e #784 (BLOCK, 15/10) e #787 (UNBLOCK, 15/10).

| Formato | Coluna Mensagem | Hora |
| :--- | :--- | :--- |
| MD | **ausente** | sem segundos |
| HTML | **truncada com "…"** (400 ocorrências) | — |
| PDF | truncada | — |
| CSV | **completa** | com segundos |

**Outras diferenças entre formatos:**

- O status aparece como "success" no MD e no CSV, e como "SUCCESS" no HTML e no PDF.
- Protocolo vazio aparece como "—" no MD e no HTML, e como "N/D" no CSV. Nos NOTIFY aparece "N/A".

## Anomalias de dados

- **Os NOTIFY param em 06/10 20:45.** Não há nenhum NOTIFY na semana. **Verificar se o agendador da checagem horária parou.** Pode ser o fato operacional mais relevante desta fonte.
- **IDs 758–762 com data e formato diferentes.** Estão datados de 21/09 10:53:09, a mesma data do #194, mas vêm numerados depois do #743 (06/10). Parecem reprocessamento ou *backfill* e usam outro formato de mensagem ("Cliente: … Ação: BLOCK (CLIENT)" × "Bloqueio efetuado:").
- **Contrato 99755 bloqueado 3 vezes** (#761, #763 e outro).
- **"Câmeras Afetadas 28" soma ações repetidas** sobre os mesmos contratos. São 11 contratos únicos.
- A ordenação é por ID decrescente, não por data.

## Dados repetidos ou desnecessários

- **Os 394 NOTIFY são batimentos de hora em hora quase idênticos** ("Nenhuma pendência…"). Somam cerca de 111 KB de mensagens no CSV, ou 96% das linhas.
- O emoji 🤖 aparece 394 vezes no CSV, no HTML e no PDF.

## Dados sensíveis

- **Nome e contrato de clientes inadimplentes** aparecem em todos os formatos.
- **Documento junto do nome:** no #300, a raiz de CNPJ de MEI (8 dígitos) aparece junto ao nome do cliente.
- **Nenhum CPF completo.**

## Formato recomendado

**CSV filtrado:** sem NOTIFY e só com as datas da semana. É o único formato com a mensagem completa. O HTML e o PDF não trazem nada exclusivo.

## Correções sugeridas ao AutoTickets (por prioridade)

1. **Exportar pelo período solicitado** (domingo a sábado) em vez de 30 dias móveis.
2. **Agregar os NOTIFY** em uma linha de resumo ("N checagens sem pendência entre X e Y; última em DD/MM HH:MM") e **alertar quando a checagem horária parar**.
3. **Separar os KPIs da semana dos KPIs acumulados**, contando contratos e câmeras **únicos**.
4. **Não truncar a mensagem** no HTML e no PDF, ou extrair o alvo (câmeras/contrato) para uma coluna própria.
5. Sinalizar reprocessamentos com a coluna `id_original` e manter a mensagem num formato único.
6. Mascarar documentos dentro do nome do cliente.
7. Nome de arquivo com o período e com data local, também no PDF.
