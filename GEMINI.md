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
   - Exportações brutas e relatórios de tarefas e atendimentos em PDF/CSV.
2. **AutoTickets (`2.autotickets/` e Repositório Local):**

   - Plataforma de automação e integração de sistemas desenvolvida e mantida por Liomar Oliveira.
   - **Repositório e Commits Locais:** `/home/liomarti/dev/autotickets-v2` (inspecionar commits no período para mapear entregas técnicas, novas features, correções e manutenções).
   - **Exportações Tratadas em CSV (`2.autotickets/*.csv`):** Arquivos contendo dados tratados, filtrados e estruturados pelo AutoTickets integrando a base de dados do Voalle (chamados ativos, chamados concluídos, tarefas ativas e protocolos de acompanhamento). Os dados têm mérito do próprio sistema AutoTickets em tratá-los e prepará-los para auditoria.
3. **Históricos e Comunicações de WhatsApp (`3.whatsapp_histories/`):**

   - **Banco SQLite Mestre (`database/msgstore.db`):** Base de dados relacional com o histórico completo de mensagens (mais de 340 conversas e quase 40.000 mensagens), atualizada semanalmente a partir do backup com chave de 64 dígitos (`input/msgstore.db.crypt15`).
   - **Exportações Manuais (`manual_exports/`):** Conversas estratégicas exportadas separadamente e de forma manual pelo WhatsApp Business (*Isvi TI Ten.txt*, *Tecnologia TEN.txt*, *Tudo Incluso - TEN.txt*, *[Made4NOC] TEN INTERNET LTDA PREMIUM.txt*).
   - **Conversas Exportadas em Lote (`conversas_exportadas/`):** Histórico completo de chats individuais extraídos em formato `.txt` puro e catálogo geral indexado em `indice_conversas.json`.
   - **Harness de Scripts (`scripts/`):**
     - `sync_backup.py`: Descriptografa o novo backup em `input/` e atualiza `database/msgstore.db`.
     - `query_history.py`: Utilitário de consulta relacional por período (`--start`, `--end`) e categoria (`campo`, `interno`, `coordenacao`, `incidentes`).
     - `export_all_chats.py`: Utilitário para re-exportar todas as conversas para `.txt`.
   - **Extratos Temporais (`exports/`):** Relatórios filtrados por período em Markdown (`extrato-campo.md`, etc.).
4. **Infraestrutura e Plataformas Integradas:**

   - Flashman, Native PBX (telefonia), Made4NOC / Grafana, FullCam, MailCow, Servidores Datacom (SV01), Dell PowerEdge (R550) e SuperMicro, Mikrotik e Switches Gerenciáveis.
5. **Painéis de BI com Parceiros (Analítica 3M e EasyBI / MW Solutions) - Contexto Real:**

   - **Analítica 3M:** Acesso limitado de Liomar Oliveira. O setor de TI não gerencia, não costuma utilizar e não realiza acompanhamento direto da integração.
   - **EasyBI (MW Solutions):** Acesso nunca recebido, link direto (`https://easybi.teninternet.com.br`) inacessível (DNS), sem participação em grupos e fora do escopo direto de atuação da equipe.
   - *Diretriz:* Caso citado no relatório, justificar formalmente o status real acima, sem simular atividades inexistentes.

---

## 🎯 Finalidade e Objetivos

- **Alimentação da Dashboard Executiva:** Fornecer à Coordenação de TI (Isvi Neemias) um panorama fidedigno, métricas de desempenho e status das demandas do setor para apresentação semanal à Direção toda terça-feira pela manhã.
- **Transparência e Rastreabilidade Operacional:** Mapear entregas, projetos em andamento, suporte a usuários internos, suporte a técnicos de campo e saúde da infraestrutura de telecom/TI.
- **Padrão de Saída Multi-formato:** Todos os relatórios (semanais consolidados e individuais) devem ser gerados em **Markdown (.md)**, **HTML estilizado (.html)** e **PDF executivo (.pdf)** com diagramação profissional em formato A4.

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
├── 1.voalle/                                  # Exportações e dados brutos do ERP Voalle
│   ├── README.md                              # Guia de interpretação de chamados, OS e apontamentos
│   ├── old/                                   # Exportações brutas e relatórios de semanas anteriores arquivados
│   └── [Nome]-[DataInicio]-[DataFim].pdf/.csv # Relatórios de tarefas e atendimentos do Voalle
├── 2.autotickets/                             # Dados tratados e relatórios gerados via AutoTickets
│   ├── README.md                              # Guia para leitura de relatórios e inspeção de commits
│   ├── old/                                   # CSVs e relatórios tratados de semanas anteriores arquivados
│   └── [arquivos_exportados].csv              # CSVs tratados (chamados ativos, concluídos, tarefas, etc.)
├── 3.whatsapp_histories/                      # Harness de comunicações e históricos do WhatsApp Business
│   ├── README.md                              # Manual completo do harness, rotina semanal e queries
│   ├── key_64digits.txt                       # Chave de 64 dígitos para descriptografia automática
│   ├── input/                                 # Onde o usuário insere o novo msgstore.db.crypt15 semanal
│   ├── database/                              # Banco SQLite mestre (msgstore.db) descriptografado
│   ├── manual_exports/                        # Conversas estratégicas exportadas manualmente no celular
│   │   ├── Conversa do WhatsApp com Isvi TI Ten.txt
│   │   ├── Conversa do WhatsApp com Tecnologia TEN.txt
│   │   ├── Conversa do WhatsApp com Tudo Incluso - TEN.txt
│   │   └── Conversa do WhatsApp com [Made4NOC] TEN INTERNET LTDA  PREMIUM.txt
│   ├── conversas_exportadas/                  # 340+ arquivos .txt individuais e indice_conversas.json
│   ├── scripts/                               # Automação de sincronização e queries da IA
│   │   ├── sync_backup.py                     # Sincroniza input/ com database/msgstore.db
│   │   ├── query_history.py                   # Utilitário CLI para filtros temporais e categorização
│   │   └── export_all_chats.py                # Utilitário de exportação sob demanda para TXT
│   └── exports/                               # Extratos semanais gerados em Markdown/JSON
└── 4.weekly_reports/                          # Relatórios semanais consolidados do setor de TI
    ├── README.md                              # Padrão de saída consolidado
    └── [YYYY-MM-DD]_[YYYY-MM-DD]/             # Subdiretório dedicado por período avaliado
        ├── report_ti-[YYYY-MM-DD]-[YYYY-MM-DD].md
        ├── report_ti-[YYYY-MM-DD]-[YYYY-MM-DD].html
        └── report_ti-[YYYY-MM-DD]-[YYYY-MM-DD].pdf
```

---

## 🔍 Regra de Mapeamento Ativo e Fallback de Atividades

Quando for gerar o relatório individual ou consolidado de um período (`YYYY-MM-DD` a `YYYY-MM-DD`):

1. **Mineração Multi-Fonte:** A IA deve analisar ativamente todas as fontes de dados disponíveis no período:
   - **AutoTickets Commits (`/home/liomarti/dev/autotickets-v2`):** Histórico de commits no git no período da semana (sprints entregues, refatorações, novas features, correções).
   - **AutoTickets CSVs (`2.autotickets/`):** Tarefas, chamados ativos e concluídos tratados e consolidados.
   - **Voalle (`1.voalle/`):** Atendimentos, OS, relatos avulsos e horas apontadas.
   - **WhatsApp (`3.whatsapp_histories/`):** Executar (apenas se os arquivos forem criados/modificados dentro do período solicitado) `query_history.py --start YYYY-MM-DD --end YYYY-MM-DD` para extrair mensagens de suporte ao campo, suporte interno, coordenação e Made4NOC, cruzando também com `manual_exports/` quando aplicável. Caso não hajam modificações, o diretório deve ser ignorado na análise.
2. **Geração do Relatório Individual:** Compilar e salvar o relatório individual nas extensões `.md`, `.html` e `.pdf` em `0.individual_report/[nome_colaborador]/[data-inicio]_[data-fim].[ext]`.
3. **Consolidação do Setor:** Integrar as entregas de Liomar, Isac e David no relatório semanal consolidado, criando e salvando no subdiretório dedicado em `4.weekly_reports/[data_inicio]_[data_fim]/report_ti-[data_inicio]-[data_fim].[ext]`.

---

## 📋 Tópicos Obrigatórios do Relatório (Conforme Modelo da Coordenação)

Cada relatório (individual ou consolidado) deve respeitar a estrutura oficial:

1. **Gestão de Demandas:**

   - Demandas pendentes (descrição resumida, solicitante, prioridade e previsão de início).
   - Demandas em andamento (responsável, % de avanço, bloqueios/dependências e previsão de conclusão).
   - Demandas concluídas na semana (entrega realizada e resultado obtido).
   - Demandas novas abertas e comparativo entradas × saídas (fila crescendo ou reduzindo).
2. **Registro de Atividades por Membro da Equipe:**

   - Resumo das atividades executadas por integrante no período.
   - Distribuição do tempo por frentes de trabalho (Projetos, Suporte Interno, Suporte ao Campo, Infraestrutura).
   - Pontos de desenvolvimento e necessidades de treinamento identificadas.
   - **Colaborador do TI mais ativo no Voalle:** Gráfico/estatística comparativa de apontamentos.
3. **Projetos e Entregas:**

   - Status dos projetos em andamento (AutoTickets, integrações Voalle x Flashman, telefonia Native PBX, WiFeed, etc.).
   - Painéis de BI com parceiros: Esclarecer o status real de Analítica 3M e EasyBI (MW Solutions).
   - Entregas colocadas em produção na semana e resultados observados.
   - Dependências de terceiros ou outros setores que estejam travando entregas.
4. **Incidentes Tratados:**

   - Relação dos incidentes da semana (sistema/serviço afetado, severidade, data/hora, duração e impacto).
   - Causa raiz identificada e correção aplicada (definitiva ou paliativa).
   - Incidentes recorrentes e planos de mitigação (com base nas tratativas da Made4NOC e monitoramento).
5. **Suporte Interno (Informática):**

   - Quantidade de solicitações recebidas e atendidas (computadores, acessos, e-mails, impressoras).
   - Tempo médio de atendimento e pendências em aberto.
   - **Setores que mais demandaram suporte do TI:** Lista e estatísticas de interações.
   - **Colaboradores que mais abriram chamados:** Informando equipe e setor.
   - **Relatório de Visitas Presenciais:** Deslocamentos operacionais com veículos da empresa.
6. **Suporte ao Técnico de Campo:**

   - Quantidade de apoios prestados a equipes de campo (provisionamento de ONTs, liberações, consultas, troca de estrutura).
   - Tipos de apoio mais frequentes e tempo médio de resposta (extraídos de *ServiceDesk Suporte ao técnico* e Voalle).
   - Oportunidades de automação ou capacitação para redução de dependência do TI.
7. **Infraestrutura e Sistemas Críticos:**

   - Disponibilidade dos sistemas críticos (Voalle, Flashman, servidores, telefonia, links).
   - Execução e validação de backups (sucessos × falhas).
   - Capacidade de armazenamento, memória e processamento dos servidores (alertas de esgotamento).
   - Ações de modernização (cluster, SSDs, migração de VMs, cabeamento estruturado).
   - Atualizações de segurança e vulnerabilidades identificadas.
8. **Pontos de Atenção e Próximas Ações:**

   - Riscos tecnológicos para a operação.
   - Necessidades de investimento ou aquisição de equipamentos/licenças.
   - Ações planejadas para a semana seguinte.

---

## ⚖️ Regras Explícitas de Fidedignidade e Auditoria

1. **Nunca inventar dados:** O relatório deve ser 100% baseado em fatos, números e evidências comprovadas.
2. **Fontes Auditáveis:** Toda afirmação ou número citado deve ter sua origem rastreável (ex.: número do protocolo Voalle, ID de tarefa, hash de commit no repositório `autotickets-v2`, data e hora da mensagem no WhatsApp).
3. **Ausência Justificada:** É permitido não preencher conteúdo em um tópico obrigatório caso não tenham ocorrido demandas compatíveis na semana, desde que acompanhado de justificativa formal clara.
4. **Sem Distorções:** Não alterar o sentido original das informações, manutenções ou incidentes relatados pelas equipes.

---

## ⏰ Prazos e Convenção de Nomes

- **Período de Referência:** Segunda-feira a Domingo.
- **Padrão de Datas em Arquivos:** `YYYY-MM-DD_YYYY-MM-DD` (ex.: `2026-09-07_2026-09-13`).
- **Prazo Limite de Entrega:** Toda segunda-feira até as 14h.

---

## 🔄 Controle de Versão e Commits Obrigatórios (Git)

- **Regra Fundamental:** **TODA E QUALQUER ALTERAÇÃO** realizada no repositório (atualização de dados, novos relatórios em `0.individual_report/` ou `4.weekly_reports/`, inclusão de READMEs de harness ou alterações no `GEMINI.md`) **DEVE SER OBRIGATORIAMENTE COMMITADA NO GIT**.
- **Padrão de Mensagens de Commit:** Devem ser descritivas e claras, utilizando boas práticas (ex.: `docs: atualiza GEMINI.md com novas fontes e harness`, `feat: gera relatorio individual liomar 2026-09-07 a 2026-09-13`).
- **Automação:** A IA deve executar os commits no repositório imediatamente após concluir as modificações.
