# Análise da fonte: reincidência de problemas (semana 42, versão final de 19/10 23:44)

> Avaliação da qualidade da exportação, para ajustes no AutoTickets. **Este arquivo não é fonte do relatório.**
> O formato a usar está em [`_FORMATO_ESPERADO.md`](_FORMATO_ESPERADO.md).
> A partir da próxima rodada, esta fonte ganha um **tópico dedicado** no relatório semanal.

## Versão a considerar

| Arquivo | Uso |
| :--- | :--- |
| `reincidencia_20261019_234621.md` (258 KB) | **Fonte do relatório.** Único formato com indicadores, todas as seções e o detalhe por caso |
| `reincidencia_20261019_234615.csv` (1.249 linhas, 1.130 protocolos) | Opcional: uma linha por protocolo, sem indicadores |
| `reincidencia_20261019_234619.html` / `…_234559.pdf` | Dispensáveis. O PDF quebra as tabelas na extração |
| `todas_equipes/` | Versão anterior (20/09 a 19/10, janela de 30 dias, operação inteira): só referência |

O MD e o CSV conferem entre si: 1.130 protocolos.

## O que mudou na versão final

- **Período da semana:** **11/10 a 17/10/2026**. Um retorno conta até **60 dias** após a conclusão do atendimento anterior.
- **Exclusões:** ficam de fora as rotinas, os cancelados e os alarmes falsos.
- **Leitura:** a versão traz um texto explicando como ler o relatório.

**Indicadores:**
- 2.277 protocolos analisados.
- **202 retornos**, ou **8,9%** de reincidência.
- Mediana de 16 dias até voltar.
- 35,1% voltam em até 7 dias.
- 196 clientes reincidentes.

**Seções do MD:**
- Clientes que voltaram com o mesmo problema (206).
- Pedidos internos repetidos entre equipes (11).
- Mesmo cliente reencaminhado à mesma equipe (47).
- Problemas sistêmicos.
- Taxa de reincidência por tipo.
- Detalhe por caso, com os protocolos.

## O que interessa ao TI (insumo para o tópico dedicado)

- **Casos ligados ao TI:**
  - **Configuração de Equipamentos:** DEIVIDE LEONEL DE ARAUJO FEITOSA (Comercial Geral → Setor TI), com 1 retorno em 6 d 4 h, e DIEGO SOUZA DOS SANTOS, com 1 retorno em 21 d e 1 em aberto.
  - **Suporte ao Técnico de Campo:** JOSIENE AGUIAR PESSOA, com 1 retorno em 4 d 18 h.
- **Pedidos internos repetidos:** nenhum envolve o Setor TI nesta versão. Os 11 casos são de Patrimônio, Estoque, Contas a Pagar e Infraestrutura.
- **Problemas sistêmicos da semana** (contexto para 5 e 8.1, sem atribuir ao TI): "Problema na Rede de Distribuição/CTO/Ramal Parado" teve **32 clientes em 16/10** e 15 em 17/10.
- **Taxas por tipo:** Conexão Lenta, 27,3% (66 de 242), e Usuário Não Conecta, 15,5% (44 de 283).
- **Cruzamento com as Anomalias PPPoE (8.4):** o casamento foi feito por nome, então é preciso confirmar pelo contrato.
  - **mariafb** (razão 16x) aparece com reincidência em **Conexão Lenta**.
  - **thiagonascimento_1** (RX −40 dBm, 10 quedas) aparece com reincidência em **Usuário Não Conecta**. Isso reforça a necessidade de OS de campo.

## Pontos de melhoria no AutoTickets (não bloqueiam o uso)

1. **Temas como radicais de palavras** ("remot · recent · atend"). Mostrar o assunto ou a categoria do Voalle e deixar os radicais só para o agrupamento.
2. **Retornos com intervalo de minutos.** Exemplo: TALKD/Inventário com 13 min. Parecem lançamentos em lote, então vale um intervalo mínimo para contar como retorno.
3. **Equipe que tratou o caso.** Incluir uma coluna `equipe_tratou` (ou um filtro Setor TI / N2-TI / NOC) para isolar a parte do TI.
4. **Indicadores no CSV.** O CSV não tem indicadores. No pacote semanal, criar o módulo `reincidencia` (`docs/formato_exportacao_autotickets.md`).
