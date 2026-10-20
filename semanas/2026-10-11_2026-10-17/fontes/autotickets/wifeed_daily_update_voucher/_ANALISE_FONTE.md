# Análise da fonte: WiFeed, sincronização diária de vouchers (semana 42: 11/10 a 17/10/2026)

> Feedback sobre a qualidade da exportação, para ajustes manuais e para o AutoTickets. **Não é fonte do relatório.**

**Arquivos analisados:** `relatorio_vouchers_wifeed_completo_2026-10-19_215844.pdf`, `…_215852.html`, `…_215856.md` e `…_215859.csv`.

## Período e geração

- Os quatro formatos declaram o período de 11/10/2026 a 17/10/2026, que está correto.
- Cada formato foi gerado num horário diferente: PDF 21:58:44, HTML 21:58:52, MD 21:58:56 e CSV 21:58:59.
- O rodapé do HTML e do PDF diz "Página 1 de 1", mas o PDF tem 2 páginas.

## Contagens por formato

Nos quatro formatos há 7 linhas de histórico e 7 dias de evolução. O total de 228.056 vouchers confere com a soma das 7 linhas.

| Informação | MD | CSV | HTML | PDF |
| :--- | :---: | :---: | :---: | :---: |
| Evolução diária em tabela | sim | sim | **não** (só no gráfico SVG) | **perde os valores** (só restam os rótulos dos eixos) |
| Pico/mínimo (32.611 / 32.533) | sim | sim | não | não |
| "2 com sucesso / 0 falhas" | sim | não | "2 de 7 bem-sucedidos" | "2 de 7 bem-sucedidos" |
| "Duração 7 dias" | não | não | sim | sim |
| ID do envio (43–49) | não | **sim** | não | não |

## Inconsistências de dados (iguais em todos os formatos)

- **Base de 14/10:** o histórico registra "Base 32.604" para 14/10, mas a evolução diária dá **32.611** para o mesmo dia. Como 32.604 é exatamente o valor de 11/10, parece um valor copiado ou um cache que não foi atualizado.
- **Status × taxa de sucesso:** a "Taxa Média de Sucesso 100%" e as "0 falhas" convivem com **5 de 7 envios em status "Excluído"**. O relatório não explica o que "Excluído" significa: pode ser o segmento antigo substituído, que é o comportamento esperado, ou uma falha.
- **Estilo ausente no HTML:** a classe CSS `badge-status deleted` não está definida, e o status "Excluído" aparece sem estilo.

## Dados repetidos ou desnecessários

- O MD tem barras ASCII decorativas (`███████ ▇`), e o HTML e o PDF têm emojis.
- O HTML tem cerca de 9 KB de CSS.
- O gráfico SVG repete a tabela de evolução: é útil visualmente, mas não traz dado novo.

## Dados sensíveis

Nenhum. "CPF-CNPJ" aparece apenas como nome do segmento.

## Formato recomendado

Use o **CSV** ou o **MD**, que têm cerca de 3 KB cada, são completos e trazem a evolução diária e o pico e o mínimo em texto. O gráfico SVG do tópico 4.2.4 pode ser redesenhado a partir da tabela. **Não é preciso exportar o HTML só por causa do gráfico.**

## Correções sugeridas ao AutoTickets (por prioridade)

1. Investigar a base de 14/10 (32.604 no histórico × 32.611 na evolução diária).
2. Definir o status "Excluído" e calcular a taxa de sucesso de forma coerente com ele. Por exemplo, "Substituído" para o segmento antigo, que não conta como falha.
3. Padronizar os números do CSV. Hoje o resumo usa "32.604" e "228.056" e o detalhe usa "32604"; a variação aparece como "-0.02%". Sugestão: números crus, sem separador de milhar, e decimal com ponto em todo o CSV.
4. Incluir a evolução diária e o pico/mínimo em tabela no HTML.
5. Corrigir a paginação do rodapé.
