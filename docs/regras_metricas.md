# 📏 Regras de Métricas e Declarações

Correções conceituais exigidas pela Coordenação (feedback de 2026-09-28 a 2026-10-04). Aplicam-se a todo relatório individual e consolidado.

## 1. Balanço da fila (Tópico 1)

- Indicador: **"Balanço da fila (saídas ÷ entradas)"** ou **"Variação do Backlog"**.
- É **proibido** usar o termo "resolutividade": no Service Desk ele significa outra métrica (resolução no primeiro contato).
- Fonte primária: `fontes/autotickets/colaborador_x_ticket/` (entradas, saídas, TMA, TMR por colaborador). `fontes/voalle/` dá a narrativa de cada protocolo.

## 2. Contagem de demandas (Tópicos 1 e 7)

- Demandas **recorrentes de mesma natureza** (ex.: "Análise de Desconto", "Atribuição/Remoção de IP Público Fixo") viram **uma linha agrupada com a quantidade tratada**, sem listar cada protocolo.
- Demandas **não recorrentes** são descritas de forma analítica, protocolo a protocolo.
- Totais citados no texto devem **somar exatamente** os totais das tabelas categorizadas.
- Um mesmo número não pode aparecer como total do setor e total de uma pessoa sem conferência.

## 3. Horas: Voalle × Pontomais (Tópico 2.4)

- Tabela por colaborador: horas apontadas no Voalle × horas trabalhadas no Pontomais.
- Divergência é **obrigatoriamente explicada**: tickets deixados em execução, sobreposição de demandas, deslocamento intermunicipal, cronômetro ativo em almoço/interjornada — ou corrigida.
- **Critério de data do Voalle:** exportar e citar por **"Lançamento"** (cada apontamento conta uma vez, na semana em que foi finalizado). Se a fonte for o AutoTickets, declarar o critério usado (hoje ele reproduz "Inclusão").
- **Apontamentos longos:** todo apontamento > 8h ou que atravessa noite/fim de semana deve ser listado no 2.4 com o protocolo e a justificativa (ex.: 3217119 com 120:09 e 3218766 com 89:37 na semana 42). Orientação da Coordenação (feedback da semana 41): fechar os relatos no fim do expediente e pausar o play ao mudar de foco.

## 4. Apoio ao técnico de campo (Tópico 7)

- Todo apoio com atuação técnica (abrir tela, verificar sistema, executar algo) exige **protocolo formal**. Conversas rápidas e dúvidas são a exceção.
- Volumetria com e sem protocolo deve fechar com a tabela de tipos.

## 5. Incidentes e reincidência (Tópico 5)

- Proibido afirmar "100% de precisão" ou "sem reincidência" com base em uma semana. Usar **janela móvel mínima de 30 dias**.

## 6. Disponibilidade (Tópico 8.1)

- Percentual de disponibilidade **só com ferramenta de monitoramento** que meça tempo no ar — informar a fonte e o tempo fora do ar.
- Sem monitoramento: declarar **"Sem indisponibilidade de rede registrada"**.
- Falhas de aplicação/sessão (ex.: sessão do Voalle, #3209683) **não viram percentual**: entram como **"Ocorrências Operacionais de Sistemas"**, com severidade e impacto.
- "100% por ausência de erros" não é medição de tempo no ar.

## 7. Backups (Tópico 8.2) — quadrante obrigatório

1. Quantidade de VMs e CTs na rotina diária;
2. Jobs executados na semana × falhas;
3. Quais foram refeitos manualmente e a causa da falha;
4. Data e resultado do último teste prático de restauração (Disaster Recovery).

"Backup OK" confirma que rodou, não que restaura.

## 8. Mudanças de plano e fatos incomuns

- Mudança de escopo ou prioridade em relação à semana anterior entra no relatório **com o motivo e o novo prazo** (ex.: VPN/Wazuh priorizando a RB com mais acessos indevidos em vez das filiais previstas).
- Dificuldades com frota: data, protocolo da requisição, horário combinado × horário de recebimento do carro e o que foi afetado.
- Nova instalação de Windows 10: justificar (fim do suporte em outubro/2025, licenças, hardware).

## 9. Painéis de BI (Tópico 3.3)

- **Analítica 3M:** perfil Master de Liomar para gestão de usuários; acesso restrito a ele por orientação da Coordenação; telas úteis podem virar grupo com usuários para Isac e David.
- **EasyBI (MW Solutions):** acesso limitado, pouco valor, provável descontinuação. Informar o status real, sem simular atividades.

## 10. Dados pessoais em tabelas

- CPF/CNPJ de clientes sempre mascarado (`***.456.789-**`), inclusive na tabela de auditoria Fullcam (4.3.2).
- Relatório de uso interno: nome, contrato, login, IP, MAC e endereço **aparecem** quando o setor precisar localizar o caso (ex.: 8.4 PPPoE). Senhas e stream keys nunca.

## 11. Fullcam — registros excluídos

- **Contrato 96660 (DAVID BRASIL FERNANDES):** ignorar na auditoria financeira (4.3) até a correção da regra do módulo (não é contrato de câmera; feedback da semana 41).
