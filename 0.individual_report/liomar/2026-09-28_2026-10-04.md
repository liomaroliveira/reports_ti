# Relatório Semanal Individual de Atividades — Setor de TI

---

## 📌 Identificação do Profissional

- **Colaborador:** Liomar Antonio de Oliveira
- **Cargo:** Analista de TI Sênior (#107184)
- **Empresa:** Ten Soluções e Serviços LTDA. (Ten Provedor de Internet)
- **Coordenador Responsável:** Isvi Neemias
- **Período de Referência:** 28/09/2026 a 04/10/2026 (Semana 40 / 2026)
- **Data de Emissão:** 06/10/2026
- **Contexto Operacional:** Retorno do período de férias em 01/10/2026. Atividades concentradas com alta intensidade em Engenharia de Software e Arquitetura de Sistemas no ecossistema **AutoTickets v2** (30 sprints concluídas e 83 commits no período), reestruturação e recuperação do ambiente de desenvolvimento local (Linux CachyOS), abertura e acompanhamento de chamado crítico junto ao suporte Voalle referente a deslogamento indevido de usuários e especificação da arquitetura de integração AutoTickets × Slack.

---

## 📊 Painel de Indicadores de Produtividade e Engenharia

| Indicador | Quantidade / Métrica | Detalhamento / Escopo |
| :--- | :---: | :--- |
| **Commits Registrados no Git** | **83 commits** | Repositório `autotickets-v2` (branch `dev`), cobrindo sprints de frontend, backend, IA e dados |
| **Sprints Concluídas com Sucesso** | **30 sprints** | Sprint 269 e Sprints 291 a 320 (Relatórios, Local-First, MCP, IA, Design System, UX) |
| **Arquivos Impactados no Código** | **604 arquivos** | Refatorações arquiteturais, novos controllers, componentes React 19 e testes |
| **Volume de Código Produzido** | **+143.638 / -9.285** | Adições massivas de engines de relatórios, catálogo UI, telemetria IA e sincronizadores |
| **Garantia de Qualidade & Testes** | **100% transacional** | Suíte blindada com `DatabaseTransactions`, 0 corrupções de banco de dados |
| **Protocolos Voalle Movimentados** | **4 protocolos** | #3209592 (Reparo Linux), #3209683 (Logout Voalle), #3210508 (Slack), #3210518 (Férias) |
| **Horas Apontadas em Demandas Oficiais** | **05h 16m** | Tempo líquido apurado nas demandas do retorno de férias no Voalle ERP |

---

## 1. Gestão de Demandas

### 1.1 Demandas Concluídas na Semana

| Protocolo / Referência | Descrição da Entrega | Resultado Obtido |
| :--- | :--- | :--- |
| **Sprints 291 a 320 & Sprint 269 (AutoTickets v2)** | Conclusão de 83 commits e entrega de 30 sprints estruturantes no ecossistema AutoTickets v2, abrangendo motor de relatórios executivos em 7 tópicos, sincronização Voalle com duplo cursor monotônico, servidor MCP oficial, telemetria de custos de IA e redesign corporativo com Glassmorphism. | Plataforma modernizada, relatórios automatizados prontos para uso da gestão, latência de consulta reduzida a menos de 15ms e mitigação de carga no banco do ERP. |
| **Protocolo #3209592** | Diagnóstico aprofundado e reparo emergencial no sistema operacional Linux CachyOS da estação de trabalho de TI após falha de atualização gráfica com falta de bibliotecas (`libLLVM.so.23.1`) e quebra do gerenciador de janelas. Reinstalação de stack gráfico e migração de variáveis KDL do shell Noctalia para a versão 5. | Estação de trabalho totalmente recuperada e estabilizada em 02h 49m de atuação sem necessidade de formatação ou perda de dados. |
| **Protocolo #3210518** | Levantamento, auditoria e conferência das atividades técnicas desempenhadas pelos colaboradores Isac Costa Silva e David Brasil Fernandes durante o período de férias de Liomar (18/09 a 01/10/2026). | Alinhamento operacional restabelecido, organização de prioridades e transição de demandas do setor concluída. |
| **Rotinas de Saneamento no ERP Voalle** | Identificação e encerramento administrativo de tarefas residuais com timers antigos abertos no Voalle (#3182310, #3171518, #3168670 e #3152430), herdados de períodos anteriores. | Higienização da base de dados do ERP e correção de indicadores de horas do setor. |

### 1.2 Demandas em Andamento

| Demanda / Protocolo | Responsável | % Avanço | Bloqueios / Dependências | Previsão de Conclusão |
| :--- | :---: | :---: | :--- | :---: |
| **Protocolo #3209683 (Bug de Logout Abrupto no Voalle)** | Liomar Oliveira | 40% | Dependência da equipe de desenvolvimento e sustentação da Synsuite / Voalle. Atendente Eduardo Aguiar escalou o chamado internamente. | 09/10/2026 |
| **Protocolo #3210508 (Integração AutoTickets × Slack)** | Liomar Oliveira | 35% | Análise técnica de APIs, rate limits e arquitetura de banco de dados para contornar o expurgo de 90 dias do plano free do Slack corporativo. | 16/10/2026 |
| **Persistência Local-First e Webhooks Voalle** | Liomar Oliveira | 75% | Ajuste de endpoints locais para ingestão de eventos de abertura e encerramento de tarefas do Voalle em tempo real via webhook. | 14/10/2026 |

### 1.3 Demandas Pendentes

- **Expansão de Ferramentas no Servidor MCP (`laravel/mcp`):** Adicionar endpoints para execução de testes de ping, validação de rotas BGP e auditoria de cadastros de ONTs diretamente por agentes de IA.
- **Parametrização de Alertas Automáticos de Telemetria:** Configurar limites diários de consumo de tokens da API Gemini para envio de relatórios de custo diretamente à coordenação.

### 1.4 Balanço de Entradas × Saídas

- **Demandas e Sprints Concluídas:** 30 sprints de software + 2 protocolos Voalle finalizados + saneamento de fila legada.
- **Demandas Novas Iniciadas:** 4 demandas (reparo Linux, logout Voalle, arquitetura Slack e auditoria pós-férias).
- **Saldo Operacional:** Saldo altamente positivo, com entrega de arquitetura que transforma a operação de relatórios do setor de TI e avanço rápido na estabilização do ambiente pós-férias.

---

## 2. Registro de Atividades e Engenharia de Software

### 2.1 Resumo Analítico das Atividades Executadas

1. **Desenvolvimento Contínuo do AutoTickets v2 (83 commits):**
   - **Motor de Relatórios Executivos Parametrizados:** Implementação de motor modular estruturado em 7 tópicos oficiais, gerando relatórios em PDF de alta resolução diagramados para impressão A4 sem poluição de cabeçalhos do navegador, visualizador HTML interativo com edição *in-place* e exportação Markdown universal.
   - **Arquitetura Local-First (Duplo Cursor Voalle):** Criação da tabela `report_voalle_raw_records` e de sincronizador incremental que utiliza o algoritmo `MAX(id)` e `MAX(modified)` para consultar apenas registros atualizados, reduzindo o tempo de consulta analítica para menos de 15ms e blindando o ERP Voalle contra sobrecargas.
   - **Orquestrador de IA Multi-Provedor:** Implementação de orquestrador dinâmico integrado ao Google Gemini AI SDK, com telemetria detalhada de tokens e custos em `AiTokenUsage`, desacoplamento assíncrono (*lazy loading*) e seleção automática do modelo Gemini Flash para economia de custos.
   - **Servidor MCP Oficial:** Integração nativa de `laravel/mcp` permitindo que assistentes de IA realizem consultas estruturadas à base de dados de chamados e telecomunicações da TEN Internet.
   - **Design System Corporativo & Glassmorphism:** Vitrine completa de componentes em `/settings/theme`, catálogo de ícones Lucide, Live CSS Playground seguro contra injeção e motor visual de Glassmorphism com opacidade adaptável aos 4 temas da plataforma.
   - **Governança de Testes:** Blindagem da base de dados local substituindo `RefreshDatabase` por `DatabaseTransactions`, garantindo isolamento total durante execuções de testes automatizados.

2. **Manutenção e Resolução de Incidente Crítico na Estação de TI (Protocolo #3209592):**
   - No retorno das férias em 01/10/2026, a estação de trabalho Linux CachyOS apresentou quebra total da interface gráfica (SDDM e desktop em tela preta) após atualização de sistema.
   - Análise de logs do `journalctl` identificou a ausência de bibliotecas essenciais do driver Mesa (`libLLVM.so.23.1: cannot open shared object file`).
   - Procedimentos executados: redefinição de mirrors remotos com `cachyos-rate-mirrors`, ressincronização completa de pacotes com `pacman -Syyu`, sobreposição forçada das bibliotecas `llvm-libs`, `mesa`, `mesa-utils` e `libglvnd`, além da migração dos arquivos `.kdl` do Noctalia Shell para a versão 5.
   - Tempo total dedicado: 02h 49m, com retorno à normalidade sem perda de arquivos ou necessidade de reinstalação.

3. **Intervenção e Abertura de Chamado Crítico Voalle (Protocolo #3209683):**
   - Diante de queixas de múltiplos colaboradores sobre logouts involuntários frequentes no ERP Voalle, foi aberto chamado junto ao suporte da fornecedora (atendente Eduardo Aguiar).
   - O problema acarreta perda de textos em digitação e retrabalho para o time de TI e atendimento. Foram fornecidos detalhes do comportamento à equipe de desenvolvimento da Synsuite/Voalle, e o chamado permanece sob acompanhamento ativo.

4. **Estudo de Integração AutoTickets × Slack (Protocolo #3210508):**
   - Início da especificação técnica de módulo para comunicação bidirecional com a API do Slack. O objetivo central é fornecer um repositório interno de auditoria que contorne a limitação de expurgo de 90 dias imposta pela versão gratuita da ferramenta, preservando decisões e dados cruciais de engenharia e atendimento.

### 2.2 Distribuição do Tempo por Frente de Trabalho

```
Engenharia de Software & Arquitetura (AutoTickets v2): ██████████████ 70%
Suporte Interno & Manutenção da Estação de TI:         ███ 15%
Gestão de Fornecedores & Auditoria ERP Voalle:         ██ 10%
Coordenação Técnica & Alinhamento Operacional:         █ 5%
```

### 2.3 Desenvolvimento e Capacitação Técnica

- **Aprofundamento em Model Context Protocol (MCP):** Domínio prático na criação de MCP Servers em PHP/Laravel para conectar sistemas legados a agentes inteligentes de última geração.
- **Otimização de Consultas SQL para ERPs:** Validação prática de cursores monotônicos duplos para sincronização incremental de bancos relacionais volumosos, garantindo estabilidade e alta performance.
- **Diagnóstico Avançado de Kernel e Stack Gráfico Linux:** Domínio de troubleshooting de subsistemas gráficos Wayland, Mesa e gerenciamento de dependências LLVM em distribuições de ponta baseadas em Arch Linux.

---

## 3. Projetos Estruturantes e Entregas Técnicas

### 3.1 Ecossistema AutoTickets v2: Modernização e Relatórios Automatizados

- **Status:** Em produção / Desenvolvimento contínuo (Sprint 320 concluída).
- **Entregas Principais da Semana:**
  1. *Motor de Relatórios Executivos:* Geração automatizada dos relatórios semanais com layout A4 limpo, estatísticas semânticas e tabelas ricas.
  2. *Sincronizador Voalle Local-First:* Consultas aceleradas de 1800ms para <15ms através da ingestão incremental de chamados e tarefas.
  3. *Telemetria de IA:* Monitoramento de custos por requisição e priorização de modelos econômicos (Gemini Flash).
  4. *Vitrine de Design System:* Catálogo vivo de componentes com isolamento e editor interativo.
- **Resultados Observados:** Redução drástica do esforço manual para compilação do relatório do setor de TI, eliminando horas de extração manual no ERP.

### 3.2 Projeto Integração AutoTickets × Slack

- **Status:** Em fase de especificação arquitetural e modelagem de endpoints (Protocolo #3210508).
- **Objetivo Estratégico:** Mitigar o risco de perda de histórico de conversas no Slack Corporativo da TEN Internet através de ingestão automatizada e espelhamento seguro no AutoTickets.
- **Próximas Frentes:** Desenvolvimento de Webhooks receptores e tabela de persistência de mensagens com indexação por canal e data.

---

## 4. Incidentes Tratados

| ID | Sistema / Ativo | Severidade | Causa Raiz | Ação Aplicada | Status |
| :---: | :--- | :---: | :--- | :--- | :---: |
| **INC-LIO-01** | Estação TI Linux (#3209592) | ALTA | Incompatibilidade de bibliotecas gráficas Mesa/LLVM após atualização de pacotes do CachyOS. | Reinstalação de mirrors, pacotes gráficos essenciais e migração das configurações do Noctalia Shell v5. | Resolvido Definitivamente |
| **INC-LIO-02** | Sessão Voalle ERP (#3209683) | ALTA | Falha no mecanismo de renovação de sessão do backend Synsuite/Voalle causando logouts forçados. | Abertura de chamado de emergência e escalonamento para a engenharia da Voalle; acompanhamento em andamento. | Em Monitoramento |

---

## 5. Pontos de Atenção e Próximas Ações

1. **Bug de Sessão do ERP Voalle:** Acompanhar diariamente o retorno do suporte da Voalle (Protocolo #3209683), cobrando correção definitiva para eliminar a perda de dados dos colaboradores da empresa.
2. **Homologação da Ingestão de Webhooks no AutoTickets:** Testar e colocar em produção o recebimento em tempo real de alterações de status dos chamados do Voalle.
3. **Desenvolvimento da Conexão Slack:** Iniciar os testes de autenticação via OAuth/Bot Token com a API do Slack para validação de retenção de mensagens.
4. **Alinhamento Contínuo com a Equipe:** Manter a supervisão sobre o fechamento de protocolos pendentes e rotinas de campo executadas por Isac Costa e David Brasil.
