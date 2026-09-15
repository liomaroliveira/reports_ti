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
   - **Cargo:** Analista de TI Sênior (Supervisor de TI — responsável pela gestão técnica, supervisão do Assistente e Auxiliar, desenvolvimento de automações e consolidação dos relatórios semanais do setor)
   - **WhatsApp:** [telefone removido]

2. **Isac Costa Silva**
   - **CPF:** ***.404.875-**
   - **Cargo:** Assistente de TI Pleno
   - **WhatsApp:** [telefone removido]

3. **David Brasil Fernandes**
   - **CPF:** ***.899.744-**
   - **Cargo:** Auxiliar de TI Junior
   - **WhatsApp:** [telefone removido]

---

## 🖥️ Sistemas e Fontes de Dados em Escopo
1. **ERP Voalle:** ERP principal da empresa (Módulos de Atendimento, Service Desk, O.S., Projetos, Infraestrutura e Apontamentos).
2. **AutoTickets:** Plataforma de automação e integração de sistemas desenvolvida e mantida por Liomar Oliveira.
   - **Repositório e Commits Locais:** `/home/liomarti/dev/autotickets-v2`
3. **Históricos de WhatsApp:** Comunicações operacionais com fornecedores, equipe interna, NOC e coordenação armazenadas em `3.whatsapp_histories/`.
4. **Infraestrutura e Plataformas Integradas:** Flashman, Native PBX (telefonia), Made4NOC / Grafana, FullCam, MailCow, Servidores Datacom (SV01), Dell PowerEdge (R550) e SuperMicro, Mikrotik e Switches Gerenciáveis.

---

## 🎯 Finalidade e Objetivos
- **Alimentação da Dashboard Executiva:** Fornecer à Coordenação de TI (Isvi Neemias) um panorama fidedigno, métricas de desempenho e status das demandas do setor para apresentação semanal à Direção toda terça-feira pela manhã.
- **Transparência e Rastreabilidade Operacional:** Mapear entregas, projetos em andamento, suporte a usuários internos, suporte a técnicos de campo e saúde da infraestrutura de telecom/TI.
- **Padrão de Saída Multi-formato:** Todos os relatórios (semanais consolidados e individuais) devem ser gerados em **Markdown (.md)**, **HTML estilizado (.html)** e **PDF executivo (.pdf)** com diagramação profissional em formato A4.

---

## 📁 Estrutura de Diretórios e Harness do Projeto

```text
reports_ti/
├── GEMINI.md                                  # Contexto principal, diretrizes e regras para a IA
├── modelo_coordenador/                        # Documento oficial de padronização do Coordenador de TI
│   ├── modelo_relatorio_setor_ti.pdf          # PDF de referência emitido por Isvi Neemias
│   └── README.md                              # Resumo dos tópicos e critérios de avaliação
├── 0.individual_report/                       # Relatórios individuais dos membros da equipe
│   ├── README.md                              # Diretrizes para relatórios individuais e regras de fallback
│   ├── liomar/                                # Relatórios individuais de Liomar Oliveira (YYYY-MM-DD-YYYY-MM-DD.pdf/.md/.html)
│   ├── isac/                                  # Relatórios individuais de Isac Costa Silva
│   └── david/                                 # Relatórios individuais de David Brasil Fernandes
├── 1.voalle/                                  # Exportações e dados brutos do ERP Voalle
│   ├── README.md                              # Guia de interpretação de chamados, OS e apontamentos
│   └── [Nome]-[DataInicio]-[DataFim].pdf/.csv # Relatórios de tarefas e atendimentos do Voalle
├── 2.autotickets/                             # Dados de desenvolvimento e automações
│   ├── README.md                              # Guia para leitura de relatórios e inspeção de commits do repositório
│   └── [arquivos_exportados]                  # Exportações de métricas do AutoTickets
├── 3.whatsapp_histories/                      # Registros de conversas operacionais de TI
│   ├── README.md                              # Mapeamento dos grupos e contatos estratégicos
│   ├── Conversa do WhatsApp com Isvi TI Ten.txt
│   ├── Conversa do WhatsApp com Tecnologia TEN.txt
│   ├── Conversa do WhatsApp com Tudo Incluso - TEN.txt
│   └── Conversa do WhatsApp com [Made4NOC] TEN INTERNET LTDA PREMIUM.txt
└── 4.weekly_reports/                          # Relatórios semanais consolidados do setor de TI
    ├── README.md                              # Padrão de saída consolidado
    ├── report_ti-[YYYY-MM-DD]-[YYYY-MM-DD].md
    ├── report_ti-[YYYY-MM-DD]-[YYYY-MM-DD].html
    └── report_ti-[YYYY-MM-DD]-[YYYY-MM-DD].pdf
```

---

## 🔍 Regra de Mapeamento Ativo e Fallback de Atividades

Quando um colaborador **NÃO possuir** um relatório semanal individual prévio dentro de `0.individual_report/[nome_colaborador]/`:

1. **Mineração Multi-Fonte:** A IA deve analisar ativamente todas as fontes de dados disponíveis no período (`YYYY-MM-DD` a `YYYY-MM-DD`):
   - **Voalle (`1.voalle/`):** Tarefas executadas, chamados, O.S., relatos de atendimento e tempos trabalhados.
   - **AutoTickets Commits (`/home/liomarti/dev/autotickets-v2`):** Histórico de commits no git do repositório local dentro do período especificado (sprints entregues, refatorações, novas features, correções).
   - **WhatsApp (`3.whatsapp_histories/`):** Alinhamentos com o Coordenador, orientações dadas ao time, tratativas de incidentes com fornecedores (Made4NOC, TIP Brasil, Bemobi, etc.).
2. **Geração do Relatório Individual:** A IA deve primeiro compilar e salvar o relatório individual nas extensões `.md`, `.html` e `.pdf` em `0.individual_report/[nome_colaborador]/[data_inicio]-[data_fim].[ext]`.
3. **Consolidação:** Em seguida, integrar os dados individuais no relatório semanal consolidado do setor em `4.weekly_reports/`.

---

## 📋 Tópicos Obrigatórios do Relatório (Conforme Modelo da Coordenação)

Cada relatório (individual ou consolidado) deve respeitar rigorosamente a seguinte estrutura:

1. **Gestão de Demandas:**
   - Demandas pendentes (descrição resumida, solicitante, prioridade e previsão de início).
   - Demandas em andamento (responsável, % de avanço, bloqueios/dependências e previsão de conclusão).
   - Demandas concluídas na semana (entrega realizada e resultado obtido).
   - Demandas novas abertas e comparativo entradas × saídas (fila crescendo ou reduzindo).

2. **Registro de Atividades por Membro da Equipe:**
   - Resumo das atividades executadas por integrante no período.
   - Distribuição do tempo por frentes de trabalho (Projetos, Suporte Interno, Suporte ao Campo, Infraestrutura).
   - Pontos de desenvolvimento e necessidades de treinamento identificadas.

3. **Projetos e Entregas:**
   - Status dos projetos em andamento (AutoTickets, integrações Voalle x Flashman, telefonia Native PBX, WiFeed, etc.).
   - Painéis de BI com parceiros (Analítica 3M, MW Solutions EasyBI ou AutoTickets).
   - Entregas colocadas em produção na semana e resultados observados.
   - Dependências de terceiros ou outros setores que estejam travando entregas.

4. **Incidentes Tratados:**
   - Relação dos incidentes da semana (sistema/serviço afetado, severidade, data/hora, duração e impacto).
   - Causa raiz identificada e correção aplicada (definitiva ou paliativa).
   - Incidentes recorrentes e planos de mitigação.

5. **Suporte Interno (Informática):**
   - Quantidade de solicitações recebidas e atendidas (computadores, acessos, e-mails, impressoras).
   - Tempo médio de atendimento e pendências em aberto.
   - Setores que mais demandaram suporte.

6. **Suporte ao Técnico de Campo:**
   - Quantidade de apoios prestados a equipes de campo (provisionamento de ONTs/roteadores, liberações, consultas).
   - Tipos de apoio mais frequentes e tempo médio de resposta.
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

## ⏰ Prazos e Convenção de Nomes
- **Período de Referência:** Segunda-feira a Domingo.
- **Padrão de Datas em Arquivos:** `YYYY-MM-DD-YYYY-MM-DD` (ex.: `2026-09-07-2026-09-13`).
- **Prazo Limite de Entrega:** Toda segunda-feira até as 14h.

---

## 🔄 Controle de Versão e Commits Obrigatórios (Git)
- **Regra Fundamental:** **TODA E QUALQUER ALTERAÇÃO** realizada no repositório (atualização de dados, novos relatórios em `0.individual_report/` ou `4.weekly_reports/`, inclusão de READMEs de harness ou alterações no `GEMINI.md`) **DEVE SER OBRIGATORIAMENTE COMMITADA NO GIT**.
- **Padrão de Mensagens de Commit:** Devem ser descritivas e claras, utilizando boas práticas (ex.: `docs: atualiza GEMINI.md e harness`, `feat: gera relatorio individual liomar 2026-09-07 a 2026-09-13`).
- **Automação:** A IA deve executar os commits no repositório imediatamente após concluir as modificações.
