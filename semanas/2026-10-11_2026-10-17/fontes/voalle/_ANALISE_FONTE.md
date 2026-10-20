# Análise da fonte — Voalle ERP, Tarefas Executadas (semana 42: 11/10 a 17/10/2026)

> Feedback sobre a qualidade da exportação, para ajustes manuais. **Não é fonte do relatório.**
> Comparativo com o AutoTickets e escolha do critério de data: `../autotickets/tarefas_executadas/_ANALISE_FONTE.md`.

**Arquivos:**
- `{liomar,isac,david}_tarefas_executadas_20261019_221147.html` e `.pdf` — "Tipo de data: **Lançamento**".
- `{pessoa}_tarefas_executadas_20261019_221147_por_data_inclusao.html` — "Tipo de data: **Inclusão**".
- Período de todos: 11/10/2026 a 17/10/2026.

## Lançamento ou Inclusão?

| Colaborador | Lançamento (registros / HT) | Inclusão (registros / HT) | Diferença |
| :--- | :---: | :---: | :--- |
| Liomar | 17 / 306:11 | 15 / 96:23 | Só em Lançamento: 3217119 (120:09) e 3218766 (89:37), iniciados em 08/10 e 09/10 e fechados na semana |
| Isac | 26 / 22:43 | 30 / 22:43 | Só em Inclusão: 4 apontamentos de 3221254 (14/10, 09:20–09:23), 00:00 e **sem data de fim** |
| David | 57 / 31:05 | 57 / 31:05 | Nenhuma |

**Padronizar Lançamento** enquanto o Voalle for usado.

- **Lançamento:** cada apontamento entra uma única vez, na semana em que é finalizado. Nenhuma hora se perde.
- **Inclusão:** um apontamento ainda aberto no momento da exportação fica preso a uma semana já relatada e depois não aparece em relatório nenhum.
- **Os dois critérios:** atribuem o apontamento inteiro a uma única semana. Só o AutoTickets pode recortar as horas por semana.

O AutoTickets hoje reproduz o critério **Inclusão**.

## HTML ou PDF?

**HTML.** A diferença vale para os dois critérios.

| Critério | HTML | PDF |
| :--- | :--- | :--- |
| Registros | 100 completos (Lançamento) | Completos no Liomar e no Isac. **No David faltam DT, HT e Progresso**, e o texto é cortado à direita |
| Extração | Campos rotulados (Tarefa, Origem, DT, HT, Progresso, Descrição, Relato) | Cabeçalhos repetidos e quebras artificiais |
| Relatos | Formatação e imagens preservadas | Perdidas |
| Tamanho | David com 2,49 MB, dos quais 94% são 4 imagens em base64 | 0,2 a 1,6 MB |

- **Pastas `*_files/`** (jQuery, CSS e logo do Voalle, adicionadas junto com as exportações por Inclusão): **não são necessárias**, porque o texto está completo sem elas. Podem ser apagadas para não versionar bibliotecas de terceiros.
- **Basta um critério por semana:** não é preciso exportar Lançamento e Inclusão juntos. A dupla exportação desta semana serviu só para a comparação.

## Cuidados ao processar o HTML

- **Tabelas aninhadas:** alguns relatos têm tabelas HTML dentro (ex.: Isac 3078726). Um parser que corte o texto na primeira `</td>` perde o relato.
- **Imagem como texto:** uma das imagens do David vem escapada como texto (`&lt;img`).
- **Data de fim incompleta:** o campo DT mostra "13/10/2026 16:57 até 07:43" sem o dia do fim. Quando o apontamento vira o dia, use a data de fim do CSV do AutoTickets.
- **Tarefas × apontamentos:** o cabeçalho conta "tarefas" (6 / 17 / 41), e as linhas são apontamentos (17 / 26 / 57 em Lançamento). O relatório deve dizer qual dos dois está citando.

## Pontos de atenção nos dados da semana

- **Liomar, 3217119 (120:09) e 3218766 (89:37):** são cronômetros que ficaram abertos por dias, inclusive no fim de semana. É o mesmo padrão que o Isvi apontou no feedback da semana 41 (274h17 de "play" aberto). **Encaminhamento:** corrigir os apontamentos no Voalle ou justificá-los no tópico 2.4, e seguir a orientação de fechar os relatos no fim do expediente.
- **Isac, 4 apontamentos sem fim em 3221254:** verificar se são cliques repetidos ou apontamentos esquecidos abertos.
- **Feriado de 12/10:** sem expediente (PARAMETROS.md). Conferir se há apontamentos nesse dia.

## Dados sensíveis

- **Isac:** senhas de Wi-Fi de cliente, Unifi e Mikrotik (3221804 e "Rede VITU").
- **Outros:** e-mails pessoais em relatos do David e do Liomar.
- **Telefones** em descrições (ex.: 3218766, 3224039): não são mascarados.

As senhas e os e-mails foram mascarados nos HTMLs em 19/10. Os arquivos são de uso interno e o commit não é bloqueado. **Recomendação à equipe:** não registrar credenciais em relatos do Voalle.
