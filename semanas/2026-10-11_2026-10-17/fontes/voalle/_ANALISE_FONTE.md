# Análise da fonte: Voalle ERP, Tarefas Executadas (semana 42: 11/10 a 17/10/2026)

> Feedback sobre a qualidade da exportação, para ajustes manuais. **Não é fonte do relatório.**
> Comparativo com o AutoTickets: `../autotickets/tarefas_executadas/_ANALISE_FONTE.md`.

**Arquivos:** `{liomar,isac,david}_tarefas_executadas_20261019_221147.html` e `.pdf`. Os PDFs estão no `.gitignore` porque contêm senhas e e-mails que não podem ser mascarados.

- **Período:** todos declaram 11/10/2026 a 17/10/2026.
- **Filtro:** "Tipo de data: Lançamento".

## HTML ou PDF?

**Use o HTML.**

| Critério | HTML | PDF |
| :--- | :--- | :--- |
| Registros | 100, todos completos (Liomar 17, Isac 26, David 57) | Completos no Liomar e no Isac. **No David faltam DT, HT e Progresso**, e o texto é cortado à direita |
| Facilidade de extração | Campos rotulados com `<strong>` (Tarefa, Origem, DT, HT, Progresso, Descrição, Relato) | Cabeçalhos e rodapés repetidos e quebras de linha artificiais |
| Formatação dos relatos | Preservada (listas, tabelas, imagens) | Perdida |
| Tamanho | David com 2,49 MB, dos quais **94% são 4 imagens em base64**. Liomar e Isac têm de 60 a 72 KB | De 0,2 a 1,6 MB |

O PDF do David não serve para contar horas.

## Cuidados ao extrair dados do HTML

- **Pastas auxiliares:** as pastas `*_files/` (CSS, JS e logo do Voalle) não são necessárias. O texto está completo sem elas.
- **Tabelas dentro de relatos:** alguns relatos contêm tabelas HTML aninhadas (ex.: Isac 3078726). Um parser que corte na primeira `</td>` perde o relato.
- **Imagem escapada como texto:** uma das imagens do David foi exportada como texto escapado (`&lt;img`), não como imagem.
- **Data de fim sem dia:** o Voalle mostra "13/10/2026 16:57 até 07:43" sem informar o dia do fim (era 15/10). Para apontamentos que viram o dia, a data de fim tem de vir de outra fonte (o CSV do AutoTickets já traz).
- **Duas formas de contar:** o total no cabeçalho conta "tarefas" (Liomar 6, Isac 17, David 41), enquanto as linhas são apontamentos (17, 26, 57). O relatório deve deixar claro qual dos dois está citando.

## Pontos de atenção nos dados da semana

- **Liomar: 306:11 de HT no Voalle.** Os apontamentos 3217119 (120:09) e 3218766 (89:37) começaram em 08/10 e 09/10 e ficaram com o cronômetro aberto por dias, inclusive no fim de semana. É o mesmo padrão da "distorção de 234h" registrada na semana 41. **É preciso corrigir os apontamentos no Voalle ou justificá-los no tópico 2.4.** Caso contrário, o confronto com o Pontomais fica sem sentido.
- **Feriado de 12/10:** confirmar se houve apontamentos nesse dia antes de fechar o período operacional efetivo.

## Dados sensíveis (mascarados em 19/10 nos HTMLs)

- **Isac:** senhas em texto aberto de Wi-Fi de cliente, Unifi e Mikrotik (protocolo 3221804 e "Rede VITU").
- **David e Liomar:** e-mails pessoais de clientes e colaboradores (os e-mails `@teninternet.net` foram mantidos).
- **Telefones:** há telefones em descrições (ex.: 3218766, 3224039). Eles **não são mascarados** pelo script atual; a pendência já está registrada em `docs/pontos_a_melhorar.md`.

**Recomendação à equipe:** não registrar credenciais em relatos do Voalle. Usar o cofre de senhas e citar só a referência.
