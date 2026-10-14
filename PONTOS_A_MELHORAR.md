# Pontos a melhorar

Criar dicionário de termos e jargões utilizados na empresa. Irei incluir informações adicionais para que não gere dúvidas, abaixo, em cada categoria, para ser consultada quando preciso para melhor entendimento.

- Criar um diretório com arquivos e informações distintas, para melhor consulta no harness.

# A empresa

# Correções / aprimoramentos

- Contagem de demandas (concluídas, em andamento...): Olhando a tabela, alguns itens agrupam várias solicitações numa única linha (como os descontos analisados e as atribuições de IP público). Sugiro criar um item específico agrupando esse tipo de demanda, por exemplo, "Análise de Desconto" e "Atribuição/Remoção de IP Público Fixo", só com a quantidade tratada em cada, sem precisar listar cada protocolo individualmente. Isso deixa a contagem mais fiel sem inchar a tabela, não é necessário detalhes a mais que contagem (citar protocolos nessas "categorias"), fica mais enxuto. Porém, para protocolos que não são recorrentes como estes, pode ser mais analítico.

# Análise de protocolo



DEMANDAS ADMINISTRATIVAS - ABRIR TAREFA AVULSA. EXEMPLOS:

- IMPRESSORA
- COMPUTADOR
- RAMAL
- PROBLEMAS ENTRE O COLABORADOR E O SISTEMA



DEMANDAS MAIS COMPLEXAS, QUE EXIGEM VÁRIAS ETAPAS, PROCESSOS, DEPENDÊNCIA DE TERCEIROS OU QUE PODEM EXIGIR A ATUAÇÃO DE MAIS DE UM COLABORADOR - ABRIR SOLICITAÇÃO INTERNA. EXEMPLOS:

- PROBLEMAS NOS SISTEMAS (ABRIR SUPORTE NATIVE, VOALLE, FULLCAM...)
- ESTUDOS INTERNOS, HOMOLOGAÇÕES E TESTES
- DEMAIS SITUAÇÕES QUE POSSAM PASSAR PARA OUTROS COLABORADORES (DO MESMO SETOR OU OUTROS).
- SOLICITAÇÕES DE MATERIAL (ESTOQUE)
- REEMBOLSOS

QUANDO HOUVER NECESSIDADE DE MAIS DE UM COLABORADOR ATUAR NO MESMO PROBLEMA, ABRIR TAREFAS DENTRO DA SOLICITAÇÃO INTERNA EM "Tarefas / Processos > Adicionar nova tarefa" > Tarefa Comum ou Aprovação.

![1789746598106](image/PONTOS_A_MELHORAR/1789746598106.png)

![1789746631734](image/PONTOS_A_MELHORAR/1789746631734.png)

DEMANDAS QUE ENVOLVAM DIRETAMENTE UM CLIENTE - OBRIGATORIAMENTE SOLICITAÇÃO EXTERNA

- SUPORTE A TÉCNICO DE CAMPO
- VIABILIDADE TÉCNICA
- VISITA TÉCNICA FEITA PELO PRÓPRIO TI - NESTE CASO, SE MAIS DE UM COLABORADOR FOR ENVOLVIDO, ABRIR TAREFA DENTRO DA MESMA SOLICITAÇÃO PARA CADA UM REGISTRAR SUA ATIVIDADE.

---

# 🎓 Lições Aprendidas e Diretrizes da Coordenação (Feedback 2026-09-28 a 2026-10-04)

Registros extraídos do feedback e alinhamento com o Coordenador de TI Isvi Neemias para calibração contínua dos relatórios:

## 1. O Propósito Real do Relatório (As 8 Regras da Coordenação)
O relatório deve deixar de ser apenas um registro do "que fizemos" e responder: "foi bom?", "para onde estamos apontando?", "o que precisa mudar?", "que tipo de profissionais somos?":
1. **Registrar fatos:** documentar o que aconteceu, quando, onde e com quais envolvidos.
2. **Apresentar resultados:** mostrar indicadores, metas, entregas e desempenho.
3. **Analisar uma situação:** identificar causas raízes, tendências, problemas e impactos.
4. **Dar visibilidade:** permitir que gestores e outras áreas entendam a operação sem precisar acompanhar os detalhes diários.
5. **Apoiar decisões:** fornecer evidências sólidas para decidir próximos passos e alocação de recursos.
6. **Acompanhar evolução:** comparar períodos, metas e resultados históricos.
7. **Criar histórico:** manter referência para consultas futuras e prestação de contas.
8. **Recomendar ações:** indicar melhorias e próximos passos técnicos fundamentados.

## 2. Correções Conceituais de Métricas Obrigatórias
- **Balanço da Fila vs Resolutividade:** No Service Desk, "resolutividade" é outra métrica (FCR/resolução no primeiro contato). Para a relação de saídas ÷ entradas no setor de TI, utilizar estritamente **"Balanço da fila (saídas ÷ entradas)"** ou **"Variação do Backlog"**.
- **Disponibilidade / Uptime sem Achismo:** Se não houver monitoramento externo medindo tempo no ar, não inventar percentuais como 99,8% ou 100%. Utilizar **"Sem indisponibilidade de rede registrada"**. Falhas em telas ou sessões (como o bug Voalle) entram como **"Ocorrências Operacionais de Sistemas"**, não como queda de infraestrutura.
- **Auditoria de Backups (4 Pilares):** Dizer que backups estão "100% OK" não garante restauração. Trazer sempre:
  1. Quantas VMs e CTs estão na rotina diária;
  2. Total de jobs executados vs falhas na semana;
  3. Quais foram refeitos manualmente e a causa da falha;
  4. Data e resultado do último teste prático de Disaster Recovery (restauração).
- **Acurácia Pericial e Reincidência:** Nunca declarar "100% sem reincidência" com base em apenas uma semana. Adotar janela móvel mínima de **30 dias de observação**.
- **Confronto Voalle x Pontomais:** Sempre comparar o total de horas de tickets apontados com o espelho do ponto. Havendo divergência, explicar detalhadamente as causas (tickets deixados abertos, sobreposição de demandas em paralelo, deslocamentos ou intervalos).

## 3. Aprofundamento em Fatos Incomuns e Anomalias
- Desvios em relação a planos da semana anterior (ex.: VPN Wazuh priorizando certas RBs em vez das filiais previstas) devem ser explicitamente explicados, justificando o motivo da mudança de prioridade e fixando novo prazo.
- Dificuldades de frota/veículos (atrasos na entrega do carro, tempo perdido e impacto em visitas) devem ser registradas de forma fidedigna.
- Novas instalações de Windows 10 devem ser justificadas tecnicamente, considerando o fim do suporte da Microsoft, políticas de licenciamento e limitações de hardware.

