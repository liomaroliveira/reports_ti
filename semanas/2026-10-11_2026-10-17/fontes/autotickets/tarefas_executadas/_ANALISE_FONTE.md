# Comparativo: Tarefas Executadas AutoTickets × Voalle ERP (semana 42: 11/10 a 17/10/2026)

> Feedback sobre a qualidade da exportação, para ajustes manuais e para o AutoTickets. **Não é fonte do relatório.**
> Pergunta: o relatório de Tarefas Executadas do AutoTickets (`/modules/tickets` > Tarefas Executadas) é confiável e suficiente para **dispensar** o do Voalle? Ele serve como fonte primária de dados brutos da produção de cada colaborador.

**Arquivos comparados:**
- **AutoTickets:** `{liomar,isac,david}_tarefas_executadas_*.csv` e `.pdf`, nesta pasta.
- **Voalle:** `../../voalle/{liomar,isac,david}_tarefas_executadas_20261019_221147.html` e `.pdf`.

**Método:** os registros foram casados por protocolo e por data e hora de início. Antes de comparar o texto dos relatos, normalizamos os espaços e a formatação.

## Veredito

- **CSV do AutoTickets:** o **conteúdo está correto** e é **mais estruturado que o do Voalle**. Nos 98 pares casados, título, descrição, relato e progresso batem 100%. **Ainda não dispensa o Voalle**: antes é preciso corrigir os 4 bloqueios abaixo. Depois disso, pode substituí-lo como fonte primária.
- **PDF do AutoTickets:** **não deve ser usado como fonte**. Ele corta relatos, perde registros e perde colunas.
- **Melhor exportação do Voalle:** **HTML**. Ver `../../voalle/_ANALISE_FONTE.md`.

### Bloqueios para dispensar o Voalle

1. **Filtro de período diferente.** O Voalle filtra por data de **lançamento**; o AutoTickets, pela data de **início**. Por isso o AutoTickets **omite 2 apontamentos do Liomar** que somam **209h46m**: 3217119 (início em 08/10 08:29, 120:09) e 3218766 (início em 09/10 15:03, 89:37). Os dois foram iniciados antes da semana e ficaram abertos por dias. Nenhum lugar do relatório avisa a diferença.
2. **Arredondamento de minutos.** O CSV arredonda os minutos linha a linha, enquanto o Voalle trunca. A soma do CSV fica de 5 a 14 min acima da do Voalle. Exemplos: 3221689 em 15/10 dá 420 × 421 min, e 3219157 dá 228 × 229. O próprio PDF do AutoTickets usa segundos e bate com o Voalle, então **o CSV e o PDF do AutoTickets divergem entre si**.
3. **Linhas espúrias.** Há 4 linhas espúrias no Isac: protocolo 3221254, chamado 3455962, de 14/10 entre 09:20 e 09:23. São do tipo "Sol. Interna", com relato "Solicitação inicial", 0 min e sem data fim.
4. **Protocolo vazio** nas "Tarefa de Solicitação" do David: 3201861 (2 linhas), 3200974 e 3203059. O número só aparece no título, e duas dessas linhas vêm com Tipo/Ação "Relato".

## Comparativo por colaborador

| | Liomar | Isac | David |
| :--- | :---: | :---: | :---: |
| Voalle: tarefas / HT no cabeçalho | 6 / **306:11** | 17 / **22:43** | 41 / **31:05** |
| Voalle HTML: registros / soma das linhas | 17 / 306:05 | 26 / 22:36 | 57 / 30:52 |
| AutoTickets CSV: linhas / soma | 15 / **96:24** | 30 / **22:44** | 57 / **31:06** |
| AutoTickets PDF: registros no corpo / HT | 15 / 96h23m | 30 / 22h43m (**sem coluna Data**) | **50 de 57** / 31h05m |
| Registros casados (HT Voalle × CSV) | 15 (96:19 × 96:24) | 26 (22:36 × 22:44) | 57 (30:52 × 31:06) |
| No Voalle e ausentes no AutoTickets | **2** (3217119, 3218766 = 209h46m) | — | — |
| No AutoTickets e ausentes no Voalle | — | **4** linhas espúrias (3221254) | — |

> A diferença de 306h × 96h no Liomar é efeito do item 1. Os dois apontamentos longos, de 120h e 90h, também merecem revisão no próprio Voalle: são cronômetros que ficaram abertos por dias e distorcem o confronto com o Pontomais (tópico 2.4).

## Fidelidade do conteúdo (CSV × Voalle)

- **Texto:** título, descrição, relato e progresso batem nos 98 pares. Há duas exceções, e nenhuma é perda de texto:
  - **Isac 3078726:** o relato no Voalle é uma tabela HTML aninhada, que o AutoTickets converteu em texto com o link.
  - **David 3216735:** o relato tem uma imagem embutida, que o AutoTickets **removeu sem deixar marcador**.
- **Quebras de linha perdidas.** Parágrafos e listas viram texto colado, como "Setor de TI:Oscilações" e "técnica.Aguar". Isso ocorre em 3 relatos do Liomar, 9 do Isac e 9 do David.
- **Imagens descartadas sem marcador:** 4 no David (3215368 com 2, 3216735 e 3202572).

## Outras falhas

**CSV:**
- O Status é sempre "Concluído", mesmo com progresso de 0%.
- "Encaminhamento – Destinatário" está sempre vazio.
- "Equipe / Setor" traz o setor da solicitação (ex.: "Patrimônio e Logística – Sede – Triagem"), não o do colaborador. Nas atividades internas, fica vazio.

**PDF:**
- O relato é cortado em **140 caracteres sem reticências**: 8 de 15 relatos no Liomar, 14 de 30 no Isac e 26 de 57 no David. A descrição da demanda não aparece.
- O **PDF do David omite 7 registros (5h03m)**, embora o cabeçalho diga "57 relatos / 31h05m". Faltam 3455201, 3454884, 3454379, 3454798, 3454791, 3453476 e 3446098, todos de 13/10.
- O **PDF do Isac não tem a coluna Data/Período**, que foi cortada pela largura da página.
- Os indicadores do cabeçalho não batem: Liomar aparece com "15 iniciadas", mas tem 3 aberturas; David com "19 iniciadas", mas tem 10. Só "concluídas" (progresso 100%) e "trâmites" (encaminhamentos) conferem.
- O nome do arquivo não reflete a geração: o sufixo é `_221147`, mas o cabeçalho diz "Gerado em 22:14".

## Onde o AutoTickets já é melhor que o Voalle

- **Data e hora de fim completas.** O Voalle mostra "13/10/2026 16:57 até 07:43" sem dizer que o fim foi em 15/10.
- **Hora nas aberturas e encaminhamentos.** O Voalle mostra só "13/10 até 13/10".
- **Colunas próprias** para Cliente, Tipo da Demanda, Tipo/Ação, encaminhamento de origem e destino, ID do chamado e Data Registro com segundos.

## O que só o Voalle tem hoje

- Campo **Origem** (Solicitação / Atividade Interna / Tarefa de Solicitação).
- Formatação dos relatos (listas, tabelas, parágrafos) e imagens.
- Total por pessoa calculado em segundos.

## Dados sensíveis

- Os relatos do Isac continham **senhas em texto aberto**: Wi-Fi do cliente, Unifi e Mikrotik, no protocolo 3221804 e no "Rede VITU". Também havia e-mails pessoais em relatos do David e do Liomar. **Tudo foi mascarado em 19/10 nos CSVs e HTMLs.** O PDF do Isac nesta pasta e os PDFs do Voalle **não foram versionados**.
- **Recomendação à equipe:** credenciais devem ficar no cofre de senhas, não no relato do protocolo.

## Melhorias recomendadas para a exportação do AutoTickets

**Antes de dispensar o Voalle (bloqueios):**
1. **Escolha do filtro de período:** início, lançamento ou "qualquer sobreposição com o período". Por padrão, listar à parte os apontamentos que começaram antes do período e informar no cabeçalho qual filtro foi usado.
2. **Tempo em segundos inteiros mais horas decimais**, com o mesmo cálculo no CSV e no PDF.
3. **Remover as linhas "Solicitação inicial"** com 0 min, ou marcá-las com `tipo_evento=abertura`.
4. **Preencher sempre a coluna Protocolo.**

**Estrutura:**
- **Uma linha por apontamento**, com `id_apontamento` estável, `inicio` e `fim` em ISO 8601 (`2026-10-16T12:17:52-03:00`), `segundos` e `horas_decimais`.
- **Novos campos:**
  - `origem`, como no Voalle;
  - `tipo_evento` normalizado (apontamento, abertura, encaminhamento, relato);
  - `setor_colaborador` separado de `setor_destino`.
- **Alerta automático** para apontamentos acima de 8h ou que atravessam a noite ou o fim de semana. Isso alimenta direto a justificativa do Voalle × Pontomais.
- **Relatos:**
  - preservar as quebras de linha (`\n` entre aspas, ou Markdown);
  - separar num campo próprio a data e hora que abrem o relato;
  - inserir `[imagem: N]` onde houver imagem.
- **Descrição da demanda** num arquivo à parte (um registro por protocolo), em vez de repetida a cada linha.
- **Remover:** "Tempo Trabalhado (Formatado)", o prefixo "Protocolo N –" no título e o Status fixo.

**Metadados e conferência:**
- Nome do arquivo com o período: `tarefas_executadas_<colab>_2026-10-11_2026-10-17_gerado-20261019T2214.csv`.
- Bloco de resumo (JSON ou rodapé) com:
  - período e tipo de filtro;
  - total de registros e protocolos distintos;
  - soma em segundos;
  - definição de cada indicador ("iniciadas" etc.);
  - **checksum que bata com o cabeçalho do Voalle** (tarefas e HT).
- Exportação única com os 3 colaboradores e a coluna `colaborador`, além das individuais.

**PDF:** se mantido, sem corte de texto, com layout que não perca colunas e com conferência de que o número de linhas bate com o cabeçalho. Para o relatório consolidado, ele é dispensável.
