# Análise da fonte: Fullcam, auditoria financeira de lucros e prejuízos (semana 42: 11/10 a 17/10/2026)

> Feedback sobre a qualidade da exportação, para ajustes manuais e para o AutoTickets. **Não é fonte do relatório.**

**Arquivos analisados:**
- `auditoria_financeira_fullcam_2026-10-20.csv`
- `Auditoria Financeira - FullCam.pdf` (contém CPF/CNPJ sem máscara; uso interno, versionado)

## Período e geração

- **Nenhum dos dois arquivos declara período.** O conteúdo é uma foto acumulada da base.
- **Data de geração:**
  - O PDF diz "Gerado em: 19/10/2026, 21:59:25".
  - O CSV não tem data interna, e o nome traz **2026-10-20**. Provavelmente é a data em UTC, que já virou o dia.
- **Mudança de nome:** na semana 41 o PDF se chamava `…csv.pdf`; agora não tem data no nome.

## Contagens por formato

- **Clientes:** 92 nos dois arquivos, com 103 contratos. Na semana 41 eram 84.
- **Colunas:** o CSV tem 10 colunas, com GB consumido, custo de licenças, custo de storage e equipamento perdido separados. O PDF junta tudo em "Custos/Perdas" e não traz o GB.

## Principal problema: os KPIs do PDF não fecham com o CSV

| KPI | PDF | Recalculado a partir do CSV |
| :--- | ---: | ---: |
| Lucro Total (Adimplentes) | R$ 7.511,02 | saldo positivo 9.433,09 / faturado 10.867,13 |
| Custo por Câmera | R$ 1.863,71 | licenças + storage = 2.351,25 |
| Perdas em Equipamentos | R$ 450,00 | **1.350,00** (900 + 450) |
| Saldo Líquido | R$ 5.197,31 | **7.165,88** |

- **Nenhum filtro reproduz os números do PDF.** Testamos filtros por situação do contrato (Normal, Bloqueio, não-Normal).
- **Consequência para o relatório:** até a fórmula ser documentada, **os statcards do tópico 4.3.1 devem ser calculados a partir do CSV**, e a divergência com o PDF deve ser registrada.
- **Distribuição no CSV:** 56 clientes com saldo negativo e 36 com saldo positivo.

## Outros pontos

- **Formatação de valores:**
  - O PDF usa o formato "R$ 1287.33", com ponto decimal, e "-R$" quebra de linha na extração de texto.
  - O CSV usa ponto decimal, com todos os valores entre aspas.
- **Contrato de colaborador classificado como videomonitoramento (apontado pelo Isvi, feedback da semana 41):** o registro **DAVID BRASIL FERNANDES** (contrato nº 96660, Normal) aparece com 15 faturas pagas, R$ 455,61 faturados, **0,00 GB consumidos** e R$ 15,00 de licença. As faturas não parecem de câmera e o contrato não tem etiqueta do serviço. **Decisão (Liomar):** ignorar este registro nos relatórios até a correção. **Hipótese para o AutoTickets:** a regra do módulo está selecionando contratos sem o serviço de videomonitoramento, provavelmente por um item de fatura ou de plano genérico. Sinal útil para detectar outros casos: contratos com **0 GB consumido** e sem etiqueta de câmera.
- **Possível homônimo:** o mesmo nome de cliente aparece 2 vezes com documentos diferentes. Não é duplicata.
- **Tabela integral no relatório:** a tabela completa (4.3.2) ocupa cerca de 19% do relatório consolidado da semana 41 e se repete quase igual toda semana. Ver recomendação em `docs/pontos_a_melhorar.md`.

## Dados sensíveis

- **CSV:** tinha 87 CPFs e 5 CNPJs sem máscara (só dígitos). Foram mascarados em 19/10.
- **PDF:** contém os mesmos documentos sem máscara. Como é de uso interno, foi versionado. O ideal é regerá-lo no AutoTickets já com máscara.

## Formato recomendado

**CSV mascarado.** Ele tem o detalhamento de custos e permite recalcular os KPIs. O PDF não é confiável para os indicadores.

## Correções sugeridas ao AutoTickets (por prioridade)

1. **Corrigir a regra de seleção de contratos** (caso DAVID BRASIL FERNANDES): exigir a etiqueta ou o serviço de videomonitoramento e sinalizar os contratos com 0 GB.
2. **Mascarar CPF/CNPJ na origem** (`***.456.789-**`) ou substituir pelo ID do cliente no Voalle.
3. **Documentar a fórmula de cada KPI** e fazer o PDF somar exatamente as mesmas linhas do CSV.
4. **Declarar a data-base e o período** e incluir uma linha de totais no CSV.
5. **Usar a data local no nome do arquivo**, também no PDF.
6. **Formatar a moeda no padrão brasileiro só no PDF** e manter valores numéricos crus, sem aspas, no CSV.
7. *(Opcional)* Exportar a variação em relação à auditoria anterior (clientes que entraram ou saíram, mudança de saldo). Isso permitiria trocar a tabela integral do relatório por um "top N + variação".
