# Análise da fonte: Reincidência de Problemas (semana 42, adicionada em 19/10 23:20)

> Feedback sobre a qualidade da exportação, para ajustes no AutoTickets. **Não é fonte do relatório.**

**Arquivos (duas versões, cada uma em 4 formatos):**

| Versão | HTML | PDF | CSV | MD |
| :--- | :--- | :--- | :--- | :--- |
| **Resumida** | `reincidencia_20261019_232008.html` (370 KB) | `…_232046.pdf` | `…_232051.csv` (995 linhas: 815 Cliente, 164 Reencaminhamento, 16 Interna) | `…_232054.md` (**99 KB**, com todas as seções) |
| **Completa** (um protocolo por linha, com descrição) | `reincidencia_completo_…_232123.html` (1,9 MB) | `…_232100.pdf` (2,1 MB) | `…_232119.csv` (2.921 linhas, 1,3 MB) | `…_232131.md` (683 KB) |

## O que é

Relatório de reincidência de **toda a operação**: "mesmo problema voltando para o mesmo cliente ou entre as mesmas equipes". Não se limita ao TI.

- **Período e janela:** período de 20/09/2026 a 19/10/2026, com **janela de retorno de 30 dias**. Os dados são de 19/10 22:43, e o arquivo foi gerado às 23:08.
- **Período diferente da semana, de propósito:** a regra de reincidência da Coordenação exige uma janela móvel de 30 dias (`docs/regras_metricas.md` §5).
- **KPIs:**
  - 11.269 protocolos analisados;
  - **957 retornos** após conclusão, ou **8,5%** de reincidência;
  - mediana de 8 dias até o problema voltar;
  - 46,1% dos retornos em até 7 dias;
  - 753 clientes reincidentes, distribuídos em 815 temas;
  - 16.816 registros de "rotina" ficaram fora da análise.
- **Seções do MD:**
  - Indicadores.
  - Clientes que voltaram com o mesmo problema (815).
  - **Pedidos internos repetidos entre equipes (16).**
  - Mesmo cliente reencaminhado à mesma equipe (164).
  - **Problemas sistêmicos** (picos de clientes por tipo e dia).
  - Taxa de reincidência por tipo.

## Uso no relatório do TI (seletivo)

O relatório é da operação inteira, então **só os tipos ligados ao TI** entram no consolidado:

| Tipo | Protocolos | Retornos | Taxa | Tópico do relatório |
| :--- | ---: | ---: | ---: | :--- |
| Suporte ao Técnico de Campo | 132 | 5 | 3,8% | 7 (qualidade do apoio do TI ao campo) |
| Pc/Note/Impressora/Rede – Manutenção/Reparo | 66 | 0 | 0,0% | 6 (suporte interno: nenhum retorno em 30 dias) |
| Inventário | 50 | 16 | **32,0%** | Verificar. Os casos do topo (TALKD e STEIN TELECOM, ONU/ONT) têm mediana de 9 a 15 **minutos**, o que indica lançamento em lote, não problema que voltou |
| Compartilhar Acesso Interno | 61 | 0 | 0,0% | 6/8, se tratado pelo TI |

- **Pedidos internos repetidos que envolvem o TI** (seção "Pedidos internos repetidos entre equipes"):
  - **Setor TI → Agendamento Geral**, tipo "Pc/Note/Impressora/Rede – Manutenção/Reparo": 9 ocorrências, **4 retornos** (2 em até 7 dias), mediana de 7 dias, **4 em aberto**. Encaminhamentos do TI para o agendamento que voltam. Vale analisar no tópico 6 (o que volta e por quê).
  - **Comercial Geral → Setor TI**, tipo "Configuração de Equipamentos": 2 ocorrências, **2 retornos**.
  - No CSV completo há 22 linhas com a equipe "Setor TI".
- **Problemas sistêmicos (picos por dia):** servem de contexto para o 8.1 e o 5. No resto do relatório da operação, não são atribuídos ao TI.
  - "Problema na Rede de Distribuição/CTO/Ramal Parado": **32 clientes em 16/10** e 15 em 17/10, dentro da semana.
  - "Usuário Não Conecta": **139 clientes em 19/10** (mediana diária de 42). É um evento fora da semana, mas grande; verificar se houve incidente.
- **Cruzamento com Anomalias PPPoE (8.4):** 4 clientes do retrato PPPoE aparecem com reincidência. **Confirmar pelo contrato**, porque o casamento foi feito por nome e pode haver homônimos.
  - **nelmasantos_3** (razão de 47x) com reincidência em **Alteração de Senha do Wi-Fi**. Isso **reforça a hipótese de CPE comprometida**.
  - **mariafb** (16x) com **Conexão Lenta** e "Resolução de tickets" reincidentes.
  - **antoniogoncalves_2** com **Conexão Lenta** reincidente.
  - **idealltda** com reincidência em Atendimento Fiscal, que não tem relação com o tráfego.

  Esse cruzamento é um bom insumo para o Service Desk e pode virar um destaque.
- **Visão geral da operação:** "Conexão Lenta" (1.539 protocolos, 23,5%) e "Usuário Não Conecta" (1.294, 12,0%) concentram o volume. Só cabem no relatório do TI como contexto do 8.4 ou de automações (7.3), sem atribuir o resultado ao TI.

## Problemas de qualidade

1. **Temas pouco legíveis:** os temas são **radicais de palavras** ("tentei, pendent, consegui, assinatur"; "lent, conex"). Ajudam a agrupar, mas não informam o problema. Sugestão: mostrar o assunto do protocolo ou a categoria do Voalle, e deixar os radicais só para o agrupamento.
2. **Falsos positivos de "retorno":** casos com mediana de minutos (Inventário de TALKD e STEIN) parecem lançamentos repetidos no mesmo atendimento. Sugestão: definir um intervalo mínimo entre a conclusão e a nova abertura (ex.: mais de 1h) para contar como retorno.
3. **Arquivo grande demais:** a tabela de 815 temas, um cliente por linha, é longa para o relatório semanal. Sugestão: top N por retornos e por "em aberto", mais o resumo por tipo e por equipe.
4. **Formatos e versões:** a versão completa tem de 0,7 a 2,1 MB e repete a descrição de cada protocolo. Para o relatório semanal, a **versão resumida em MD** basta. A completa serve para aprofundar casos específicos. Sugestão: incluir no pacote semanal (`docs/formato_exportacao_autotickets.md`) como módulo `reincidencia`, com `{tipo, protocolos, retornos, taxa}` e `casos[] {cliente, contrato, tema, ocorrencias, retornos, retornos_7d, mediana_seg, em_aberto, confianca, protocolos[]}`. Os protocolos permitem conferir no Voalle.
5. **Falta a relação com a equipe do TI:** o relatório não separa o que passou pelo TI. Sugestão: um filtro ou coluna `equipe_tratou` (Setor TI, N2-TI, NOC).

## Dados sensíveis

- **Nomes de clientes:** aparecem, o que é aceitável para uso interno.
- **Versão resumida:** nenhum CPF, CNPJ, senha ou RTMP.
- **Versão completa (CSV e HTML):** as descrições tinham **572 e-mails de clientes, 40 senhas, 2 CPFs e 1 CNPJ**. Os dados foram mascarados em 19/10 (615 itens por arquivo). O **PDF completo** contém os mesmos dados sem máscara e foi versionado por ser de uso interno.

## Formato recomendado

**MD resumido** (`reincidencia_20261019_232054.md`, 99 KB). Ele tem todas as seções em tabelas legíveis. Use o **CSV completo** só para aprofundar casos do TI (filtro `Equipe = Setor TI`).

O HTML e o PDF não acrescentam nada, e a versão completa em HTML, PDF e MD é dispensável para o relatório semanal.
