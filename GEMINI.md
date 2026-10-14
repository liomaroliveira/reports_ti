# Diretrizes e Contexto do Projeto: Relatório Semanal do Setor de TI

## 🏢 Informações Institucionais e Gestão

- **Empresa:** Ten Soluções e Serviços LTDA. (Ten Provedor de Internet)
- **Site da empresa:** https://teninternet.com.br/
- **Coordenador de Tecnologia:** Isvi Neemias
- **WhatsApp Coordenador:** [telefone removido]
- **WhatsApp Setor TI:** [telefone removido]

---

## 👤 Equipe do Setor de TI

1. **Liomar Antonio de Oliveira**

   - **CPF:** ***.848.515-**
   - **Cargo:** Analista de TI Sênior (Responsável pelo desenvolvimento de automações, gestão técnica e consolidação dos relatórios semanais do setor)
   - **WhatsApp:** [telefone removido]
   - **ID Colaborador Voalle:**#107184
2. **Isac Costa Silva**

   - **CPF:** ***.404.875-**
   - **Cargo:** Assistente de TI Pleno
   - **WhatsApp:** [telefone removido]
   - **ID Colaborador Voalle:**#94562
3. **David Brasil Fernandes**

   - **CPF:** ***.899.744-**
   - **Cargo:** Auxiliar de TI Junior
   - **WhatsApp:** [telefone removido]
   - **ID Colaborador Voalle:**#116367

---

## 🖥️ Sistemas e Fontes de Dados em Escopo

1. **ERP Voalle (`1.voalle/`):**
   - ERP principal da empresa (Módulos de Atendimento, Service Desk, O.S., Projetos, Infraestrutura e Apontamentos).
   - Exportações brutas e relatórios organizados em subpastas por colaborador (`1.voalle/liomar/`, `1.voalle/isac/`, `1.voalle/david/`), nos formatos `.html`, `.pdf` ou `.csv`.

2. **AutoTickets (`2.autotickets/` e Repositório Local):**
   - Plataforma de automação e integração de sistemas desenvolvida e mantida por Liomar Oliveira.
   - **Repositório e Commits Locais:** `/home/liomarti/dev/autotickets-v2` (inspecionar commits no período para mapear entregas técnicas, novas features, correções e manutenções).
   - **Subdiretórios Estruturados de Relatórios de Produtividade (`2.autotickets/`):**
     - `colaborador_x_ticket/`: Cruzamento analítico de produtividade individual e volumetria por colaborador. **Regra de Leitura:** Como se baseia em dados do ERP Voalle, deve ser lido de forma estritamente complementar com as exportações em `1.voalle/`.
     - `fullcam_automacao_inadimplencia/`: Relatórios de suspensão/reativação automática por inadimplência no Fullcam.
     - `fullcam_automacao_instalacao_camera/`: Automação da esteira de ativação e instalação de câmeras.
     - `fullcam_lucros_prejuizos/`: Impacto financeiro, custos de licenças/storage, equipamentos perdidos e análise pericial de lucros/prejuízos.
     - `problemas_recorrentes/`: Mineração de padrões de falhas e reincidências no parque.
     - `produtividade_geral/`: Métricas consolidadas de esforço técnico humano economizado.
     - `wifeed_daily_update_voucher/`: Automação diária de sincronização de vouchers WiFeed (clientes adimplentes, evolução diária e histórico).
   - **Regra de Arquivos Multi-Formato:** Arquivos que compartilham o mesmo nome base em formatos diferentes (ex.: `.md`, `.html`, `.csv`, `.pdf`) são o mesmo relatório consolidado sobre os mesmos dados brutos. A IA deve avaliar apenas particularidades estruturais (como gráficos interativos/SVG no HTML ou colunas adicionais no CSV) e tratá-los de forma unificada, sem duplicar cálculos ou considerá-los fontes conflitantes.

3. **Investigações Especiais e Segurança (`2.1.others/`):**
   - Diretório dedicado a estudos de infraestrutura, testes de intrusão, mapeamento de vulnerabilidades em sistemas internos e análises periciais pontuais organizadas por data (`2.1.others/[YYYY-MM-DD]/...`). Quando houver pasta correspondente à semana do relatório, integrar seus achados nos tópicos de Projetos, Segurança e Riscos Tecnológicos.

4. **Pareceres da Coordenação (`5.feedback/`):**
   - Pareceres, feedbacks semanais e alinhamentos emitidos pelo Coordenador de TI Isvi Neemias (`feedback_[YYYY-MM-DD]_[YYYY-MM-DD].md`). Devem ser lidos como referência mandatória de governança e calibração contínua das diretrizes do setor.

5. **Infraestrutura e Plataformas Integradas:**
   - Flashman (TR-069), Native PBX (telefonia), Made4NOC / Grafana, FullCam, MailCow, Servidores Datacom (SV01), Dell PowerEdge (R550, R910) e SuperMicro, MikroTik e Switches Gerenciáveis.

6. **Painéis de BI com Parceiros (Analítica 3M e EasyBI / MW Solutions) - Contexto Real:**
   - **Analítica 3M:** Perfil Master concedido a Liomar Oliveira para gestão de usuários. Acesso focado em telas estratégicas, sem administração técnica do backend pela equipe do TI.
   - **EasyBI (MW Solutions):** Acesso limitado com pouco valor agregado para a operação, fora do escopo direto de manutenção do TI e em processo de descontinuação contratual.
   - *Diretriz:* Informar formalmente o status real acima, sem simular atividades inexistentes.

7. **Repositório Frio e Dados Legados (`miscelaneous/`):**
   - Armazena históricos legados de mensagens de WhatsApp (`miscelaneous/whatsapp_histories/`), configurações do LiteLLM (`miscelaneous/litellm_gateway/`) e arquivos de apoio arquivados.
   - **REGRA MANDATÓRIA:** Este diretório **NÃO DEVE SER LIDO AUTOMATICAMENTE** durante a geração do relatório semanal pelo `PROMPT.md`. É um repositório frio de consulta sob demanda, devendo ser acessado **apenas se expressamente solicitado** pelo usuário.

---

## 🎯 Finalidade e Objetivos

- **Alimentação da Dashboard Executiva:** Fornecer à Coordenação de TI (Isvi Neemias) um panorama fidedigno, métricas de desempenho e status das demandas do setor para apresentação semanal à Direção toda terça-feira pela manhã.
- **Transparência e Rastreabilidade Operacional:** Mapear entregas, projetos em andamento, suporte a usuários internos, suporte a técnicos de campo e saúde da infraestrutura de telecom/TI.
- **Padrão de Saída Multi-formato:** Todos os relatórios (semanais consolidados e individuais) devem ser gerados em **Markdown (.md)**, **HTML estilizado (.html)** e **PDF executivo (.pdf)** com diagramação profissional em formato A4.
- **Propósito Institucional do Relatório (As 8 Regras da Coordenação):**
  1. Registrar fatos com precisão (o que, quando, onde e envolvidos).
  2. Apresentar resultados e métricas reais.
  3. Analisar situações e causas raízes.
  4. Dar visibilidade para a tomada de decisão da gestão.
  5. Apoiar decisões estratégicas e alocação de recursos.
  6. Acompanhar evolução comparativa entre períodos.
  7. Criar histórico fidedigno para auditoria.
  8. Recomendar ações concretas de melhoria contínua.

---

## 📁 Estrutura de Diretórios e Harness do Projeto

```text
reports_ti/
├── GEMINI.md                                  # Contexto principal, diretrizes e regras obrigatórias para a IA
├── PROMPT.md                                  # Especificação das tarefas, direcionamento e regras do usuário
├── PONTOS_A_MELHORAR.md                       # Registro de oportunidades de melhoria e ajustes identificados
├── .gitignore                                 # Controle de exclusão de arquivos binários pesados e venv
├── modelo_coordenador/                        # Documento oficial de padronização do Coordenador de TI
│   ├── modelo_relatorio_setor_ti.pdf          # PDF de referência emitido por Isvi Neemias
│   └── README.md                              # Resumo dos tópicos e critérios de avaliação
├── 0.individual_report/                       # Relatórios individuais dos membros da equipe
│   ├── README.md                              # Diretrizes para relatórios individuais e regras de fallback
│   ├── liomar/                                # Relatórios individuais de Liomar Oliveira
│   │   ├── old/                               # Versões legadas e relatórios de semanas anteriores arquivados
│   │   └── [YYYY-MM-DD]_[YYYY-MM-DD].[ext]    # Novo relatório individual gerado
│   ├── isac/                                  # Relatórios individuais de Isac Costa Silva
│   │   ├── old/                               # Relatórios e documentos de semanas anteriores arquivados
│   │   └── [YYYY-MM-DD]_[YYYY-MM-DD].[ext]    # Relatório individual gerado no período
│   └── david/                                 # Relatórios individuais de David Brasil Fernandes
│       ├── old/                               # Relatórios e documentos de semanas anteriores arquivados
│       └── [YYYY-MM-DD]_[YYYY-MM-DD].[ext]    # Relatório individual gerado no período
├── 1.voalle/                                  # Exportações do ERP Voalle organizadas por colaborador
│   ├── README.md                              # Guia de interpretação de chamados, OS e apontamentos
│   ├── liomar/                                # Arquivos de Liomar ([Nome]-[DataInicio]-[DataFim].html/.pdf/.csv)
│   ├── isac/                                  # Arquivos de Isac ([Nome]-[DataInicio]-[DataFim].html/.pdf/.csv)
│   └── david/                                 # Arquivos de David ([Nome]-[DataInicio]-[DataFim].html/.pdf/.csv)
├── 2.autotickets/                             # Dados tratados e relatórios gerados via AutoTickets
│   ├── README.md                              # Guia para leitura de relatórios e inspeção de commits
│   ├── colaborador_x_ticket/                  # Produtividade cruzada colaborador x tickets
│   ├── fullcam_automacao_inadimplencia/       # Relatórios de automação de inadimplência Fullcam
│   ├── fullcam_automacao_instalacao_camera/   # Automação de esteira de instalação de câmeras
│   ├── fullcam_lucros_prejuizos/              # Análise financeira e perdas evitadas por automação
│   ├── problemas_recorrentes/                 # Padrões e recorrências de falhas no parque
│   ├── produtividade_geral/                   # Horas técnicas economizadas e eficiência operacional
│   ├── wifeed_daily_update_voucher/           # Atualizações diárias de vouchers e base WiFeed
│   └── old/                                   # Arquivos legados arquivados
├── 2.1.others/                                # Estudos de segurança, perícias e investigações pontuais
│   ├── README.md                              # Guia de investigações especiais e vulnerabilidades
│   └── [YYYY-MM-DD]/...                       # Relatórios técnicos datados de segurança/infraestrutura
├── 4.weekly_reports/                          # Relatórios semanais consolidados do setor de TI
│   ├── README.md                              # Padrão de saída consolidado
│   └── [YYYY-MM-DD]_[YYYY-MM-DD]/             # Subdiretório dedicado por período avaliado (Dom a Sáb)
│       ├── report_ti-[YYYY-MM-DD]-[YYYY-MM-DD].md
│       ├── report_ti-[YYYY-MM-DD]-[YYYY-MM-DD].html
│       └── report_ti-[YYYY-MM-DD]-[YYYY-MM-DD].pdf
├── 5.feedback/                                # Feedbacks e pareceres da Coordenação de TI
│   ├── README.md                              # Descrição do diretório de feedback
│   └── feedback_[YYYY-MM-DD]_[YYYY-MM-DD].md  # Considerações semanais de Isvi Neemias
└── miscelaneous/                              # REPOSITÓRIO FRIO / BACKUP (NÃO LER NO PROMPT SEMANAL)
    ├── README.md                              # Manual de arquivos legados e sob demanda
    ├── litellm_gateway/                       # Configurações e documentação do gateway LiteLLM
    └── whatsapp_histories/                    # Histórico e scripts de WhatsApp (acessar só sob demanda)
```

---

## 🔍 Regra de Mapeamento Ativo e Fallback de Atividades

Quando for gerar o relatório individual ou consolidado de um período (`YYYY-MM-DD` a `YYYY-MM-DD`):

1. **Aproveitamento de Relatórios Individuais Existentes:**
   - A IA deve verificar previamente se já existe arquivo de relatório referente ao período em `0.individual_report/[colaborador]/` (em formato `.pdf`, `.md` ou `.html`).
   - **Caso já houver arquivo dentro do período:** **NÃO é necessário gerar um novo relatório individual**. O relatório existente é a fonte oficial do colaborador e deve ser lido e considerado integralmente na confecção do relatório semanal consolidado em `4.weekly_reports/`.
   - **Caso NÃO haja arquivo para o colaborador:** Proceder com a mineração multi-fonte (fallback) para compilar e gerar o relatório individual pendente antes da consolidação.

2. **Mineração Multi-Fonte (para colaboradores sem relatório pré-existente):**
   - **AutoTickets Commits (`/home/liomarti/dev/autotickets-v2`):** Histórico de commits no git no período da semana (sprints entregues, refatorações, novas features, correções).
   - **AutoTickets Relatórios (`2.autotickets/`):** Relatórios de produtividade de automações, tickets por colaborador, WiFeed e Fullcam.
   - **Voalle (`1.voalle/[colaborador]/`):** Atendimentos, OS, relatos avulsos e horas apontadas em `.html`, `.pdf` ou `.csv`.
   - **Investigações Pontuais (`2.1.others/`):** Relatórios e estudos de vulnerabilidades datados no período da semana.
   - **Nota sobre WhatsApp:** O diretório `miscelaneous/whatsapp_histories/` é frio e **não deve ser lido no fallback padrão**, a menos que expressamente determinado pelo usuário.
3. **Geração do Relatório Individual (se necessário):** Compilar e salvar o relatório individual nas extensões `.md`, `.html` e `.pdf` em `0.individual_report/[nome_colaborador]/[data-inicio]_[data-fim].[ext]`.
4. **Consolidação do Setor:** Integrar as entregas de Liomar, Isac e David no relatório semanal consolidado, criando e salvando no subdiretório dedicado em `4.weekly_reports/[data_inicio]_[data_fim]/report_ti-[data_inicio]-[data_fim].[ext]`.

---

## 📋 Tópicos Obrigatórios do Relatório (Conforme Modelo da Coordenação)

Cada relatório semanal consolidado deve respeitar a estrutura oficial:

### ⭐ Seção de Abertura: Fatos Notáveis e Anomalias da Semana
*(Localizada logo após o Resumo Executivo e antes do Tópico 1)*
- **Objetivo:** Dar visibilidade imediata a eventos atípicos, desvios de planejamento, incidentes incomuns, anomalias de hardware/redes ou bloqueios operacionais críticos.
- **Estrutura Obrigatória por Ocorrência:**
  - **Identificação do Fato:** O que ocorreu e ativos envolvidos.
  - **Contexto e Causa Raiz:** Por que aconteceu e quais fatores desencadearam a situação.
  - **Impacto Operacional:** Consequências para a equipe, usuários ou clientes.
  - **Ação Imediata e Mitigação:** Solução paliativa ou definitiva aplicada.
  - **Lição Aprendida e Próximo Passo:** Ajuste de processo, aquisição ou mudança de rota.

### 1. Gestão de Demandas
- Demandas pendentes (descrição resumida, solicitante, prioridade e previsão de início).
- Demandas em andamento (responsável, % de avanço, bloqueios/dependências e previsão de conclusão).
- Demandas concluídas na semana (entrega realizada e resultado obtido).
- Demandas novas abertas e comparativo entradas × saídas.
- **MÉTRICA OBRIGATÓRIA:** Utilizar **"Balanço da fila (saídas ÷ entradas)"** ou **"Variação do Backlog"**. É **TERMINANTEMENTE PROIBIDO** utilizar o termo "resolutividade" para este indicador.

### 2. Registro de Atividades por Membro da Equipe
- Resumo das atividades executadas por integrante no período.
- Distribuição do tempo por frentes de trabalho (Projetos, Suporte Interno, Suporte ao Campo, Infraestrutura).
- Pontos de desenvolvimento e necessidades de treinamento identificadas.
- **Desempenho no Voalle e Confronto com Jornada de Ponto (Pontomais):**
  - Tabela comparativa com total de horas apontadas no Voalle vs. total de horas da jornada real no Pontomais.
  - **Regra de Auditoria:** Havendo divergência de horas (ex.: horas apontadas maiores que o ponto), é **obrigatório explicar a causa** (tickets sobrepostos deixados em execução, cronômetros abertos fora do expediente, tempo de deslocamento intermunicipal ou atendimento em almoço/interjornada).

### 3. Projetos e Entregas
- Status dos projetos de conectividade, infraestrutura de rede e parcerias estratégicas.
- **Projetos de Redes e Conectividade:** Túneis WireGuard, MikroTik, hardening de portas e SIEM Wazuh. Justificar qualquer desvio de prioridade ou replanejamento de cronograma (ex.: foco em RBs locais da sede e chácara em vez das filiais), fixando novo prazo.
- **Telefonia Fixa e Comunicação Corporativa (Native PBX / ZEUS):** Diagnóstico operacional, ramais corporativos e chamadas.
- **Painéis de BI com Parceiros:** Esclarecer formalmente a situação real de **Analítica 3M** (Perfil Master para gestão de acessos, foco em dashboards estratégicos) e **EasyBI / MW Solutions** (fora do escopo direto de manutenção do TI, processo de descontinuação).

### 4. Plataforma e Automações AutoTickets
Macro-tópico de governança de software e automações do TI, detalhado em subtópicos específicos:
- **4.1 Desenvolvimento e Engenharia de Software AutoTickets v2:**
  - Histórico de commits no período (`autotickets-v2`), relação de sprints entregues (Sprints 315 a 332), volume de adições/exclusões e governança com `DatabaseTransactions`.
  - Evolução da arquitetura Local-First (Duplo Cursor), orquestrador de IA multi-provedor (LiteLLM, Ollama GPU e cotas Gemini) e Servidor MCP Oficial (`laravel/mcp`).
- **4.2 Automação WiFeed – Hotspots e Sincronização Diária de Vouchers:**
  - Contextualização do Captive Portal (TEN_Wi-Fi), fluxo de clientes (CPF/voucher) e não clientes (cadastro por celular).
  - Problema anterior (upload manual de CSV, risco de erro e tempo perdido) e arquitetura da automação diária às 11h conectando ao Voalle.
  - Resumo executivo da base (32.512 a 32.600 clientes ativos, +88 no período, 100% sucesso, 227.483 vouchers transmitidos).
  - **Gráfico SVG de evolução diária de clientes ativos** e histórico detalhado de envios e validações na íntegra.
- **4.3 Módulo Fullcam – Auditoria Financeira de Lucros e Prejuízos:**
  - Resumo executivo financeiro inicial com statcards: Total Faturado (R$ 10.612,36), Custo de Licenças (R$ 1.875,00), Custo de Storage (R$ 334,00), Prejuízo com Equipamentos Perdidos (R$ 1.350,00) e Saldo Líquido (+R$ 7.053,36). Análise dos 51 contratos deficitários vs 34 superavitários.
  - **Tabela Completa de Auditoria de todos os 85 clientes na íntegra**, estilizada em formato compacto com quebras de página otimizadas para PDF e cores semânticas no saldo líquido.
- **4.4 Módulo Fullcam – Produção Operacional das Automações:**
  - Painel consolidado com statcards da esteira horária (553 rotinas processadas, 32 câmeras tratadas, 99,2% sucesso) + tabela destacando as ações operacionais efetivas (BLOCK, UNBLOCK e INSTALL).
- **4.5 Impacto Operacional e Métricas de Produtividade das Automações:**
  - Quantificação de horas técnicas de esforço humano economizadas pelas automações ativas.

### 5. Incidentes Tratados
- Relação dos incidentes da semana (sistema/serviço afetado, severidade, data/hora, duração e impacto).
- Causa raiz identificada e correção aplicada (definitiva ou paliativa).
- **Regra de Reincidência Pericial:** É **proibido** afirmar "100% de precisão" ou "sem reincidência" com base em apenas uma semana. A métrica de reincidência deve adotar **janela móvel mínima de observação de 30 dias**.

### 6. Suporte Interno (Informática)
- Quantidade de solicitações recebidas e atendidas (computadores, acessos, e-mails, impressoras).
- Tempo médio de atendimento e pendências em aberto.
- **Setores que mais demandaram suporte do TI:** Ranking e estatísticas.
- **Colaboradores que mais abriram chamados:** Informando equipe e departamento.
- **Relatório de Visitas Técnicas Presenciais e Gestão de Veículos:** Detalhamento de deslocamentos operacionais, quilometragem, veículos utilizados e **dificuldades/atrasos gerados pela frota** (horário combinado vs. horário de entrega do carro e impacto na agenda de visitas).
- **Política de Sistemas Operacionais (Windows 10 x Windows 11):** Justificativa técnica para novas instalações de Windows 10 considerando o fim do suporte oficial da Microsoft, situação das licenças e limitações de hardware.

### 7. Suporte ao Técnico de Campo
- Quantidade de apoios prestados a equipes de campo (provisionamento de ONTs, liberações, consultas, troca de estrutura).
- **Rigor Matemático e Formalização:** Todo apoio precisa de protocolo formal sempre que envolver atuação técnica, abertura de telas ou sistemas. A volumetria descrita no texto deve somar exatamente o total das tabelas categorizadas.
- Tipos de apoio mais frequentes e tempo médio de resposta.
- Oportunidades de automação ou capacitação para redução de dependência do TI.

### 8. Infraestrutura e Sistemas Críticos
- **Disponibilidade dos Sistemas Críticos (Acabou o "achismo" de 99,8% ou 100%):**
  - Caso não haja ferramenta de monitoramento externo medindo o tempo real de atividade/queda, declarar expressamente **"Sem indisponibilidade de rede registrada"**.
  - Falhas de aplicação, instabilidades funcionais ou quedas de sessão (ex.: bug de sessão Voalle) **não devem ser calculadas como percentual de indisponibilidade**, mas sim registradas à parte como **Ocorrências Operacionais de Sistemas**, com severidade e impacto.
- **Execução e Validação de Backups (Rigor de Governança):**
  - Apresentar o quadrante mandatório:
    1. Quantidade de VMs e Containers (CTs) cadastrados na rotina diária;
    2. Total de jobs executados na semana vs. total de falhas registradas;
    3. Relação das VMs refeitas manualmente e causa da falha pontual (ex.: instabilidade transitória de link);
    4. Data e resultado do último teste prático de restauração (Disaster Recovery).
- Ações de modernização e manutenção preventiva (servidores, nobreaks senoidais, cabeamento).
- Atualizações de segurança e vulnerabilidades identificadas (integrar dados de `2.1.others/` quando aplicável).

### 9. Pontos de Atenção e Próximas Ações
- Riscos tecnológicos para a operação e segurança da informação (LGPD, retenção de dados, senhas e portas).
- Necessidades de investimento ou aquisição de equipamentos/licenças.
- Ações planejadas para a semana seguinte com responsáveis e prazos alinhados.

---

## ⚖️ Regras Explícitas de Fidedignidade e Auditoria

1. **Nunca inventar dados:** O relatório deve ser 100% baseado em fatos, números e evidências comprovadas.
2. **Fontes Auditáveis:** Toda afirmação ou número citado deve ter sua origem rastreável (ex.: número do protocolo Voalle, ID de tarefa, hash de commit no repositório `autotickets-v2`).
3. **Consistência do Índice:** Toda seção listada no Índice Geral de Navegação DEVE existir exatamente com o mesmo título e âncora funcional no corpo do texto.
4. **Ausência Justificada:** É permitido não preencher conteúdo em um subtópico caso não tenham ocorrido demandas compatíveis na semana, desde que acompanhado de justificativa formal clara.
5. **Sem Distorções:** Não alterar o sentido original das informações, manutenções ou incidentes relatados pelas equipes.
6. **Regra de Arquivos Multi-Formato:** Arquivos com o mesmo nome base em formatos diferentes (`.md`, `.html`, `.csv`, `.pdf`) são o mesmo relatório consolidado sob os mesmos dados brutos; avaliar apenas particularidades estruturais (como SVG ou colunas extras no CSV) e tratá-los de forma unificada.
7. **Cruzamento Voalle + AutoTickets:** O relatório `colaborador_x_ticket` fornece as métricas oficiais consolidadas de vazão, produtividade, TMA e TMR, enquanto `1.voalle/` provê o detalhamento qualitativo de cada protocolo e apontamento.

---

## ⏰ Prazos e Convenção de Datas e Nomes

- **Período Oficial da Diretoria:** **Domingo a Sábado** (`YYYY-MM-DD` a `YYYY-MM-DD`).
- **Período Operacional Efetivo do TI:** **Segunda a Sexta** (expediente útil de trabalho do setor).
- **Cabeçalho Institucional do Relatório:**
  - *Período Oficial:* `DD/MM/AAAA a DD/MM/AAAA (Semana XX / AAAA)`
  - *Período Operacional Efetivo do TI:* `DD/MM/AAAA a DD/MM/AAAA (Segunda a Sexta)`
- **Padrão de Pastas e Arquivos:** `[Data_Inicio_Domingo]_[Data_Fim_Sabado]` (ex.: `2026-10-04_2026-10-10`).
- **Prazo Limite de Entrega:** Toda segunda-feira até as 14h.

---

## 🔄 Controle de Versão e Commits Obrigatórios (Git)

- **Regra Fundamental:** **TODA E QUALQUER ALTERAÇÃO** realizada no repositório (atualização de dados, novos relatórios em `0.individual_report/` ou `4.weekly_reports/`, inclusão de READMEs de harness ou alterações no `GEMINI.md`) **DEVE SER OBRIGATORIAMENTE COMMITADA NO GIT**.
- **Padrão de Mensagens de Commit:** Devem ser descritivas e claras, utilizando boas práticas (ex.: `docs: atualiza GEMINI.md com novas fontes e harness`, `feat: gera relatorio individual liomar 2026-10-04 a 2026-10-10`).
- **Automação:** A IA deve executar os commits no repositório imediatamente após concluir as modificações.

