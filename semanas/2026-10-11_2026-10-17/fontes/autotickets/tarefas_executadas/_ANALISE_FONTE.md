# Comparativo: Tarefas Executadas AutoTickets × Voalle ERP (semana 42: 11/10 a 17/10/2026)

> Feedback sobre a qualidade da exportação, para ajustes no AutoTickets. **Este arquivo não é fonte do relatório.**
> **Pergunta:** o relatório de Tarefas Executadas do AutoTickets (`/modules/tickets` > Tarefas Executadas) é confiável e suficiente para **dispensar** o do Voalle, como fonte primária da produção bruta de cada colaborador?
> **Revisão de 19/10, após a reexportação do Voalle por "Data de Inclusão":** a conclusão anterior mudou (ver seção 1).

**Arquivos comparados:**
- **AutoTickets:** `{liomar,isac,david}_tarefas_executadas_*.csv` e `.pdf`, nesta pasta.
- **Voalle por Lançamento:** `../../voalle/{pessoa}_tarefas_executadas_20261019_221147.html`.
- **Voalle por Inclusão:** `../../voalle/{pessoa}_tarefas_executadas_20261019_221147_por_data_inclusao.html`.

**Método:** os registros foram casados por protocolo e por data e hora de início.

## 1. Lançamento × Inclusão no Voalle, e qual delas o AutoTickets reproduz

| Colaborador | Voalle **Lançamento**: registros / HT | Voalle **Inclusão**: registros / HT | AutoTickets CSV: linhas / HT |
| :--- | :---: | :---: | :---: |
| Liomar | 17 / **306:11** | 15 / **96:23** | 15 / 96:24 |
| Isac | 26 / 22:43 | 30 / 22:43 | 30 / 22:44 |
| David | 57 / 31:05 | 57 / 31:05 | 57 / 31:06 |

**O AutoTickets reproduz exatamente o filtro "Inclusão" do Voalle.** Os mesmos registros aparecem nos dois, inclusive as 4 linhas de 3221254 do Isac. O que a análise anterior chamou de "omissão" e de "linhas espúrias" é, na verdade, **diferença de critério**, e não erro do AutoTickets.

**O que muda entre os dois filtros (casos reais da semana):**

- **Somente em Lançamento:** os apontamentos do Liomar **3217119** (início 08/10 08:29, **120:09**) e **3218766** (início 09/10 15:03, **89:37**).
  - Os dois começaram **antes** da semana e foram fechados **dentro** dela.
  - "Lançamento" atribui o apontamento à semana em que ele é finalizado; "Inclusão", à semana em que foi criado.
- **Somente em Inclusão:** 4 apontamentos do Isac em 3221254, em 14/10 às 09:20, 09:21, 09:22 e 09:23.
  - Têm 00:00 de HT e **nenhuma data de fim**: foram criados, mas nunca lançados.
  - "Lançamento" os ignora porque não foram finalizados. **Vale verificar com o Isac** se são cliques repetidos no play ou apontamentos que ficaram abertos.

**Qual é o mais adequado, se o ERP continuar sendo usado:**
- **Padronizar "Lançamento".** Cada apontamento é contado **uma única vez**, na semana em que é finalizado. Nenhuma hora se perde.
- **Problema do "Inclusão":** um apontamento aberto no momento da exportação, como o 3217119, que estava em execução, cai numa semana que já foi relatada. Depois de fechado, ele **não aparece em relatório nenhum**.
- **Limitação dos dois critérios:** nenhum distribui as horas entre as semanas. Os 120h do 3217119 vão inteiros para uma única semana, embora cerca de 56h tenham ocorrido em 11–13/10 e o restante na semana 41.
- **O que só o AutoTickets pode fazer:** recortar as horas por semana. É o principal ganho possível sobre o ERP (ver seção 4).

## 2. Veredito

- **Conteúdo:** o **CSV** do AutoTickets está **correto e é mais completo que o Voalle**. Nos 98 pares casados, título, descrição, relato e progresso batem 100%. Ele também traz a data e hora de fim completas (o Voalle mostra "13/10/2026 16:57 até 07:43" sem o dia), encaminhamentos com hora, cliente, tipo da demanda e ID do chamado.
- **Ainda não dispensa o ERP:** os itens da seção 3 precisam ser corrigidos primeiro.
- **Critério para dispensar:** os mesmos totais do Voalle nos dois critérios, em 2 semanas seguidas (ver `docs/formato_exportacao_autotickets.md`, "Critério de aceite").
- **PDF do AutoTickets:** não deve ser usado como fonte. Ele corta relatos, perde registros e perde colunas.

## 3. Correções necessárias para dispensar o Voalle

| # | Problema | Evidência | Correção |
| :-: | :--- | :--- | :--- |
| 1 | Só existe o critério "Inclusão" (fixo e não declarado) | Liomar: 96:24 no AutoTickets × 306:11 no Voalle por Lançamento | Parâmetro `filtro_periodo` = `lancamento` \| `inclusao` \| `sobreposicao`, **declarado no cabeçalho e no nome do arquivo**. Padrão: `sobreposicao` (seção 4). Exibir sempre os totais equivalentes do Voalle nos dois critérios para conferência. |
| 2 | Minutos arredondados por linha (o CSV e o PDF divergem entre si) | Soma do CSV de 1 a 14 min acima do Voalle; 3221689 em 15/10 = 421 × 420 min | Guardar e somar **segundos**. Exibir com truncamento igual ao Voalle (HH:MM) só na apresentação. |
| 3 | Apontamentos sem fim exportados como 0 min, "Concluído" e sem alerta | 4 linhas do Isac em 3221254 | Coluna `em_execucao`/`sem_fim` e alerta "apontamento aberto sem lançamento". Não chamar de "Concluído". |
| 4 | Coluna Protocolo vazia nas "Tarefa de Solicitação" | David: 3201861 (2 linhas), 3200974 e 3203059 | Preencher o protocolo pelo vínculo da tarefa com a solicitação. Nunca deixar o número só no título. |
| 5 | Quebras de linha perdidas nos relatos | 3 relatos do Liomar, 9 do Isac e 9 do David viram texto colado ("Setor de TI:Oscilações") | Preservar `\n` entre aspas (CSV) ou converter para Markdown. |
| 6 | Imagens removidas sem marcador | David: 3215368 (2), 3216735 e 3202572 | Inserir `[imagem: N]` no ponto do relato. |
| 7 | Falta o campo **Origem** do Voalle | Solicitação / Atividade Interna / Tarefa de Solicitação | Exportar `origem`. |
| 8 | Status sempre "Concluído", mesmo com progresso 0% | Todas as linhas | Status real da tarefa/solicitação. |
| 9 | "Equipe / Setor" mostra o setor da solicitação | "Patrimônio e Logística – Sede – Triagem" em atividade do TI | Separar `setor_colaborador` de `setor_destino`. |
| 10 | "Encaminhamento – Destinatário" sempre vazio | Todas as linhas | Preencher ou remover. |
| 11 | O nome do arquivo não traz período, filtro nem horário real | `_221147`, mas o cabeçalho diz 22:14 | `tarefas_executadas_<colab>_<inicio>_<fim>_<filtro>_gerado-<AAAAMMDDTHHMM>.csv`. |
| 12 | PDF: relato cortado em 140 caracteres, 7 registros a menos no David, coluna Data ausente no Isac, indicadores "iniciadas" incoerentes | Detalhes na versão anterior deste arquivo (git) | Gerar o PDF a partir dos mesmos dados, sem corte, e conferir o total de linhas com o cabeçalho. Ou descontinuar o PDF. |

## 4. Como tornar o AutoTickets **melhor** que o ERP

1. **Filtro `sobreposicao`:** inclui todo apontamento cujo intervalo toca a semana, com duas colunas:
   - `segundos` (total do apontamento);
   - `segundos_no_periodo` (recortado ao intervalo domingo 00:00 a sábado 23:59).

   Assim cada hora é atribuída à semana em que ocorreu, sem perder nem duplicar. No caso do 3217119, cerca de 56h ficariam na semana 42 e o restante na 41.
2. **Alertas automáticos por apontamento:**
   - duração acima de 8h;
   - atravessa noite, fim de semana ou feriado;
   - play aberto no momento da exportação;
   - sem fim.

   Esses alertas alimentam direto o confronto Voalle × Pontomais (tópico 2.4) e a orientação do Isvi de **fechar os relatos no fim do expediente** (feedback da semana 41).
3. **Confronto com a jornada:** se o Pontomais for integrado (ou importado), adicionar `segundos_jornada` por dia e a divergência já calculada.
4. **Uma linha por apontamento**, com:
   - `id_apontamento` estável;
   - `inicio` e `fim` em ISO 8601;
   - `tipo_evento` (apontamento, abertura, encaminhamento, relato);
   - `relato_data_hora` separado do texto.

   A descrição da demanda vai num bloco por protocolo, sem repetir a cada linha.
5. **Exportação única com os 3 colaboradores**, além das individuais, ou já dentro do **pacote semanal** (`docs/formato_exportacao_autotickets.md`).
6. **Bloco de conferência:**
   - total de registros, protocolos distintos e segundos por colaborador nos 3 critérios;
   - divergência em relação ao Voalle, quando o AutoTickets puder consultar o mesmo dado.

   É isso que permite dispensar o ERP com segurança.

## 5. Dados sensíveis

- **Senhas nos relatos do Isac:** Wi-Fi do cliente, Unifi e Mikrotik, no 3221804 e na "Rede VITU". Foram mascaradas nos CSVs e HTMLs em 19/10.
- **Decisão de 19/10:** os arquivos são de uso interno e o commit não é bloqueado; o pre-commit só avisa.
- **Orientação à equipe:** registrar credenciais no cofre de senhas, não no relato do protocolo.
