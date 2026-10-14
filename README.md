# 📊 Repositório de Relatórios Semanais do Setor de TI

Este repositório centraliza o processo de governança, coleta de métricas, consolidação de dados e geração automatizada dos relatórios semanais de desempenho do **Setor de Tecnologia da Informação** da **Ten Soluções e Serviços LTDA (Ten Provedor de Internet)**.

Os relatórios alimentam semanalmente a Dashboard Executiva apresentada pelo Coordenador de TI (**Isvi Neemias**) à Direção da empresa.

---

## 👥 Equipe do Setor de TI

* **Liomar Antonio de Oliveira:** Analista de TI Sênior (Responsável pelo AutoTickets v2, Arquitetura e Consolidação dos Relatórios) — ID #107184
* **Isac Costa Silva:** Assistente de TI Pleno (Atendimento N2, Infraestrutura, Telefonia ZEUS) — ID #94562
* **David Brasil Fernandes:** Auxiliar de TI Junior (Suporte Interno, Operações Presenciais, Hardware, SIEM Wazuh) — ID #116367

---

## 📁 Arquitetura do Repositório

```text
reports_ti/
├── GEMINI.md                                  # Contexto mestre, diretrizes institucionais e regras de governança
├── PROMPT.md                                  # Orquestrador semanal e parâmetros executáveis pela IA
├── PONTOS_A_MELHORAR.md                       # Lições aprendidas, calibrações de métricas e alinhamentos
├── modelo_coordenador/                        # Padrão visual e modelo oficial de referência
├── 0.individual_report/                       # Relatórios individuais por membro da equipe
│   ├── liomar/                                # Relatórios semanais de Liomar Oliveira (.md, .html, .pdf)
│   ├── isac/                                  # Relatórios semanais de Isac Costa Silva
│   └── david/                                 # Relatórios semanais de David Brasil Fernandes
├── 1.voalle/                                  # Dados brutos e exportações do ERP Voalle por colaborador
│   ├── liomar/                                # Exportações de Liomar (.html, .pdf, .csv)
│   ├── isac/                                  # Exportações de Isac (.html, .pdf, .csv)
│   └── david/                                 # Exportações de David (.html, .pdf, .csv)
├── 2.autotickets/                             # Relatórios analíticos e métricas geradas pelo AutoTickets v2
│   ├── colaborador_x_ticket/                  # Análise de produtividade e tickets por colaborador
│   ├── fullcam_automacao_inadimplencia/       # Suspensões e reativações automáticas Fullcam
│   ├── fullcam_automacao_instalacao_camera/   # Ativações e instalações de câmeras automatizadas
│   ├── fullcam_lucros_prejuizos/              # Prevenção de perdas e impacto financeiro
│   ├── problemas_recorrentes/                 # Padrões de incidentes e recorrências no parque
│   ├── produtividade_geral/                   # Esforço técnico humano economizado pelas automações
│   └── wifeed_daily_update_voucher/           # Atualizações diárias de vouchers e base de clientes WiFeed
├── 2.1.others/                                # Estudos de segurança, perícias e investigações técnicas datadas
│   └── [YYYY-MM-DD]/...                       # Relatórios técnicos pontuais de segurança/redes
├── 4.weekly_reports/                          # Relatórios semanais consolidados do setor de TI
│   └── [YYYY-MM-DD]_[YYYY-MM-DD]/             # Subdiretório por semana oficial (Dom a Sáb)
│       ├── report_ti-[YYYY-MM-DD]-[YYYY-MM-DD].md
│       ├── report_ti-[YYYY-MM-DD]-[YYYY-MM-DD].html
│       └── report_ti-[YYYY-MM-DD]-[YYYY-MM-DD].pdf
├── 5.feedback/                                # Pareceres e feedbacks semanais da Coordenação
│   └── feedback_[YYYY-MM-DD]_[YYYY-MM-DD].md  # Apontamentos de Isvi Neemias
└── miscelaneous/                              # REPOSITÓRIO FRIO / BACKUP (NÃO lido na rotina padrão do PROMPT.md)
    ├── litellm_gateway/                       # Configurações e documentação do gateway LiteLLM
    └── whatsapp_histories/                    # Histórico e scripts de WhatsApp (acesso apenas sob demanda)
```

---

## 🔄 Fluxo de Geração do Relatório Semanal

A geração semanal é orquestrada através do arquivo [PROMPT.md](file:///home/liomarti/dev/reports_ti/PROMPT.md) em duas etapas com **Gatekeeper**:

1. **Parâmetros da Semana:** Definir `Data Inicial` (domingo) e `Data Final` (sábado) no topo do `PROMPT.md`.
2. **Fase 0 (Validação de Pré-requisitos):** A IA valida a existência das exportações ativas em `1.voalle/`, relatórios analíticos em `2.autotickets/` e dados locais do `/home/liomarti/dev/autotickets-v2`.
3. **Etapa 1 (Relatório Individual de Liomar):** Se ainda não existir relatório em `0.individual_report/liomar/`, a IA gera os arquivos `.md`, `.html` e `.pdf`.
4. **Fase 1.5 (Checagem dos Colegas):** Se já existirem relatórios para Isac e David em `0.individual_report/`, eles são integrados diretamente; caso contrário, a IA executa o fallback nos dados do Voalle.
5. **Etapa 2 (Consolidação Semanal):** Geração do relatório executivo denso em `4.weekly_reports/[periodo]/`, abrangendo a seção de **Fatos Notáveis e Anomalias**, Gestão de Demandas (Balanço da Fila), Produtividade do AutoTickets (Subtópico 3.1.4), Incidentes, Suporte Interno/Campo e Infraestrutura Crítica.
6. **Controle de Versão (Git):** Toda alteração realizada no repositório é obrigatoriamente commitada com mensagem descritiva.
