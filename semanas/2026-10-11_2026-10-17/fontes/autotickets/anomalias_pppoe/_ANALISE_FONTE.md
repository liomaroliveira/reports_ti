# Análise da fonte: Anomalias PPPoE (AutoTickets NOC), semana 42 (11/10 a 17/10/2026)

> Feedback sobre a qualidade da exportação, para ajustes manuais e para o AutoTickets. **Não é fonte do relatório.** No relatório consolidado, esta fonte alimenta o tópico **8.4 Anomalias de Tráfego PPPoE e Ações Proativas para o Service Desk** (`docs/especificacao_relatorio.md`).

**Arquivos:**
- `relatorio_anomalias_pppoe_2026-10-20.csv` (CPF/CNPJ mascarado).
- `Relatório de Anomalias PPPoE - AutoTickets NOC.pdf` (traz nome e IP; uso interno, versionado).

## Natureza da fonte: retrato atual

- **É de propósito que fique fora da semana.** Decisão de 19/10: este relatório é um **retrato atual**, gerado no dia da emissão do consolidado, com problemas para serem vistos **agora**. Não se aplica o recorte da semana. No relatório basta informar a hora do retrato: **19/10/2026 22:07:06 (-03)**.
- O nome do CSV diz **2026-10-20**. Provavelmente é a data em UTC; deveria ser a data local.
- **O rótulo "24h" não descreve os números.** Os totais de upload/download são **acumulados na sessão inteira**, e há sessões de até 12 dias. O filtro de 24h só seleciona as sessões que estavam ativas. Exemplo: `idealltda` tem 552 GB de upload, o que exigiria cerca de 51 Mbps contínuos em 24h, mas o throughput informado é 8,94 Mbps, com sessão média de 6d 3h.

## Estrutura e contagens

- **Volume:** 27 registros e 27 colunas.
- **Severidade:** 15 HIGH, 8 CRITICAL e 4 MODERATE. O score varia de 15 a 80.
- **Cidades:**
  - Jacobina: 14.
  - Serrolândia e Caldeirão Grande: 3 cada.
  - Várzea do Poço: 2.
  - Quixabeira, Capim Grosso, Ourolândia e Pindobaçu: 1 cada.
  - Sem cidade: 1 (`reinasl`, POP SL-C2).
- **POPs:** 17 diferentes. Os mais frequentes são SR-C2 (4), JA-V1 (3) e JA-C3 (3).
- **CPE e tecnologia:**
  - Fabricante: Teracom 20, TP-Link 5, Routerboard 2.
  - Tecnologia: FTTH 26, Rádio 1.
- **Situação:** todos estão Online. 26 contratos estão Normal e 1 é Cortesia.
- **Última causa de desconexão:** Lost-Carrier 24, User-Request 2, NAS-Request 1.
- **Diagnóstico:**
  - "Inversão de Tráfego" em 23 registros, a partir de cerca de 1,5x.
  - "Tráfego assimétrico de upload" em 3 registros, com razão de 1,04x a 1,16x.
  - "Rajadas de Alta Taxa" em 1 registro.
  - O PDF tem o título "Telemetria Óptica", mas **nenhum diagnóstico de sinal óptico** foi gerado.

## Ranking por razão Upload/Download (top 15)

Este é o insumo do tópico 8.4. No relatório, a tabela deve trazer também **cliente, contrato, CPF/CNPJ mascarado, bairro, IP, MAC e CPE**, para que o Service Desk localize cada caso. Aqui aparece só o resumo. A razão confere com Upload ÷ Download nos 27 registros.

| # | Login | Cidade / POP | Plano | Upload / Download | Razão | Quedas | Sev./Score |
| :-: | :--- | :--- | :--- | :--- | :-: | :-: | :--- |
| 1 | nelmasantos_3 | Capim Grosso / CG-C3 | 300 Mb res. | 222,42 / 4,72 GB | **47,17x** | 3 | CRITICAL 80 |
| 2 | inailderocha | Jacobina / JA-V1 | 90 Mb res. | 614,47 / 14,59 GB | **42,13x** | 1 | HIGH 65 |
| 3 | carlossouza_6 | Serrolândia / SR-C2 | 300 Mb res. | 447,47 / 13,88 GB | **32,23x** | 5 | CRITICAL 80 |
| 4 | reinasl | (sem cidade) / SL-C2 | 200 Mb res. | 114,55 / 5,85 GB | 19,59x | 3 | CRITICAL 80 |
| 5 | jadersantos_1 | Jacobina / OLT JUNCO | 500 Mb res. | 135,17 / 7,43 GB | 18,20x | 3 | CRITICAL 80 |
| 6 | josefilho_34 | Quixabeira / OLT VARZEA DO CANTO | 300 Mb res. | 276,18 / 16,30 GB | 16,94x | 1 | HIGH 65 |
| 7 | mariafb | Jacobina / JA-V1 | 300 Mb res. | 164,90 / 10,21 GB | 16,15x | 1 | HIGH 55 |
| 8 | idealltda | Jacobina / JA-C4 | 500 Mb corp. | 552,41 / 45,53 GB | 12,13x | 1 | HIGH 50 |
| 9 | thiagonascimento_1 | Várzea do Poço / OLT VÁRZEA DO POÇO | 1000 Mb res. | 144,75 / 15,08 GB | 9,60x | 10 | CRITICAL 70 |
| 10 | nathaliavieira_1 | Serrolândia / SR-C2 | 500 Mb res. | 117,38 / 12,43 GB | 9,44x | 8 | CRITICAL 70 |
| 11 | mariaoliveira_60 | Jacobina / JA-MV1 | 500 Mb res. | 204,53 / 24,44 GB | 8,37x | 1 | HIGH 40 |
| 12 | elieneribeiro | Jacobina / JA-JII1 | 90 Mb res. | 147,48 / 18,19 GB | 8,11x | 1 | HIGH 45 |
| 13 | 1068.megapix | Pindobaçu / Pindobaçu | Corp 100 Mb (Rádio) | 112,16 / 14,04 GB | 7,99x | 1 | HIGH 40 |
| 14 | escritoriocaldeirao | Caldeirão Grande / SR-C2 | Corp 100 Mb (**Cortesia**) | 262,05 / 43,88 GB | 5,97x | 1 | HIGH 40 |
| 15 | mailsoncruz | Ourolândia / OLT OUROLANDIA-DATACOM | 600 Mb res. | 218,78 / 42,42 GB | 5,16x | **28** | CRITICAL 70 |

### Leitura para o Service Desk (hipóteses a confirmar, não fatos)

- **Razão acima de 15x com download baixo** (nelmasantos_3, inailderocha, carlossouza_6, reinasl, jadersantos_1, josefilho_34, mariafb): pode ser CPE comprometida (botnet ou proxy residencial). Ação: verificar a CPE, atualizar o firmware, trocar a senha e checar portas expostas. O caso `inailderocha` subiu 614 GB num plano de 90 Mb.
- **Upload alto e constante, com throughput baixo e sessão longa** (idealltda, mariaoliveira_60, elieneribeiro): pode ser DVR ou câmeras, backup em nuvem ou servidor. Ação: confirmar o uso com o cliente e oferecer plano corporativo ou IP fixo.
- **Provedor como cliente** (`1068.megapix`, empresa provedora de internet): pode ser revenda. Ação: verificar o contrato com o Comercial.
- **Contrato interno/cortesia** (`escritoriocaldeirao`): rotular como interno e excluir do ranking.
- **Muitas quedas ou sinal ruim** (mailsoncruz com 28 quedas, wilsonjunior_2 com 20 quedas e rajadas, thiagonascimento_1 com 10 quedas e RX de −40 dBm): provável problema físico ou óptico. Ação: abrir OS de campo.
- **Concentração por POP:** SR-C2 tem 4 casos (Serrolândia e Caldeirão Grande).

## Comparação CSV × PDF

| Informação | CSV | PDF |
| :--- | :---: | :---: |
| Os mesmos 27 registros, na mesma ordem (Upload Total desc.) | sim | sim |
| CPF/CNPJ (23 CPF + 4 CNPJ, só dígitos) | sim; **mascarados em 19/10** | não |
| IP do cliente (22 CGNAT 100.70.x, 5 públicos 177.93.x) | **não** | **sim** |
| Nome do cliente | sim | sim |
| KPIs (27 anomalias, 8 críticas, 11 instáveis, 23 inversões, 5,66 TB up / 1,52 TB down) | não | sim |
| Filtros aplicados (Upload mínimo ≥ 100000 MB, últimas 24h) e data de geração | não | sim |
| Bairro, Cidade, POP, Tecnologia, Potência TX, Tempo Bloqueio, Duração Média Sessão em colunas | sim | parcial |

- **Unidades:** os valores em "GB" são binários (GiB). 5.800,71 GB ÷ 1024 dá 5,66 "TB", que é o KPI do PDF. O filtro, porém, está em MB.

## Erros e incoerências de cálculo

1. **O throughput é inflado pelo número de quedas.** Ele é calculado como Upload × 8 ÷ *duração média* da sessão, quando deveria usar a duração total online. Exemplos:
   - `mailsoncruz` aparece com 545,68 Mbps num plano de 600 Mb; o valor real, considerando as 28 sessões, é de cerca de 19 Mbps.
   - `carlossouza_6`: 237 Mbps viram cerca de 47.
   - `thiagonascimento_1`: 175 Mbps viram cerca de 17.
2. **A severidade não segue uma regra única de score.** O PDF diz "ALERTA CRÍTICO = Score ≥ 70", mas:
   - `rodrigopinho_2` é **CRITICAL com 60**, enquanto `pedrooliveira_4` é **HIGH com 60**;
   - `wilsonjunior_2`, com 20 quedas e rajadas, fica em HIGH 30.
3. **A razão quase não pesa no score.** `inailderocha` (42x) fica em HIGH 65 porque teve só 1 queda, enquanto `rodrigopinho_2` (3,35x) é CRITICAL. Como o throughput já é inflado pelas quedas, o score **pune o flapping duas vezes**.
4. **Falsos positivos:** 4 registros têm razão entre 1,04x e 1,16x e entram só pelo filtro de upload ≥ 100 GB. Simetria não é anomalia.
5. **Dados de cadastro e sinal:**
   - `reinasl` está sem cidade.
   - Os bairros têm grafia inconsistente ("CENTRO" e "Centro", "CAEIRA " com espaço).
   - `thiagonascimento_1` tem RX de −40 dBm (valor de LOS ou sentinela) e nenhum diagnóstico o menciona.
   - Há 3 FTTH com sinal N/D.

## Colunas inúteis ou redundantes

- **Potência TX:** N/D ou N/A em todos os 27.
- **Tempo Bloqueio:** vazio em todos os 27.
- **Status Conexão:** "Online" em todos os 27.
- **Status Contrato:** quase constante.
- **Diagnóstico:** repete o contrato e o uptime, que já têm coluna própria.

## Formato recomendado

**Hoje:** use o CSV mais o PDF. O CSV traz as colunas; o PDF traz o **IP**, que não está no CSV, além dos KPIs e dos filtros. **Correção ideal:** incluir o IP e os KPIs no CSV (ou no pacote semanal). Assim o PDF deixa de ser necessário.

## Correções sugeridas ao AutoTickets NOC (por prioridade)

1. **Exportar no CSV tudo o que for preciso para localizar o caso:** incluir **IP**, KPIs e filtros, que hoje só estão no PDF. Mascarar CPF/CNPJ na origem.
2. **Janela de tráfego explícita (início e fim)**, com bytes **calculados dentro da janela**, e não acumulados por sessão. Assim o rótulo "últimas 24h" passa a corresponder ao dado.
3. **Throughput médio real** = bytes da janela ÷ tempo online na janela, mais o pico separado.
4. **Regra de severidade publicada e coerente com o score.** Dar à razão Upload/Download um peso próprio, sem penalizar as quedas duas vezes.
5. **Limiar mínimo de razão** (ex.: ≥ 1,5x) para classificar como "inversão" e eliminar os falsos positivos.
6. **Colunas de gestão:**
   - **primeira detecção**;
   - **semanas consecutivas** em anomalia (recorrência);
   - **ticket/OS aberto** e seu status.
   Isso permite medir se o Service Desk está agindo.
7. **Rótulos de contexto:**
   - **cliente interno/cortesia**;
   - **provedor/revenda**;
   - **diagnóstico óptico** (RX abaixo de −27 dBm, LOS).
8. Remover as colunas constantes ou vazias e normalizar cidade e bairro.
9. Usar no nome do arquivo a data local e o período coberto.
