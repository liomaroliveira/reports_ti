# Relatório Semanal Individual de Atividades — Setor de TI

---

## 📌 Identificação do Profissional

- **Colaborador:** Liomar Antonio de Oliveira
- **Cargo:** Analista de TI Sênior (#107184)
- **Empresa:** Ten Soluções e Serviços LTDA. (Ten Provedor de Internet)
- **Coordenador Responsável:** Isvi Neemias
- **Período de Referência:** 04/10/2026 a 10/10/2026 (Semana 41 / 2026)
- **Período Operacional Efetivo do TI:** 05/10/2026 a 09/10/2026
- **Data de Emissão:** 14/10/2026
- **Contexto Operacional:** Atuação focada em frentes de alta relevância estratégica e segurança: Engenharia de Software e governança no ecossistema **AutoTickets v2** (84 commits, sprints 321 a 352 com novo IP Firewall, exportador Playwright e relatórios Fullcam/WiFeed), instalação física e lógica do novo **Servidor de Inteligência Artificial Local (GPU)** no rack do Data Center Chácara em Capim Grosso (Protocolos #3212215 e #3214172), resposta pericial a incidente de segurança com mapeamento de vulnerabilidade crítica no sistema Supabase de compras (Protocolo #3218766) e saneamento profundo da fila de chamados legados no ERP Voalle.

---

## 📊 Painel de Indicadores de Produtividade e Engenharia

| Indicador | Quantidade / Métrica | Detalhamento / Escopo |
| :--- | :---: | :--- |
| **Commits Registrados no Git** | **84 commits** | Repositório `autotickets-v2` cobrindo Sprints 321 a 352 (Frontend, Backend, IA, NOC e Segurança) |
| **Sprints Concluídas com Sucesso** | **32 sprints** | Sprints 321 a 352 (IP Firewall, Write-Only Secrets, Relatórios Fullcam/NOC, Progressive Loader) |
| **Arquivos Impactados no Código** | **587 arquivos** | Implementação de IP Firewall, exportador Playwright, sub-abas analíticas e suíte de testes |
| **Volume de Código Produzido** | **+50.026 / -179.578** | Refatorações arquiteturais, higienização de bases e componentes React 19 / Laravel 12 |
| **Garantia de Qualidade & Testes** | **100% transacional** | Suíte de testes automatizados com `DatabaseTransactions`, zero regressões em produção |
| **Protocolos Voalle Movimentados** | **40 registros (26 únicos)** | 33 solicitações abertas, 20 concluídas, 1 tarefa aberta e 1 concluída na semana |
| **Taxa de Resolubilidade Direta** | **80.8%** | 21 concluídas sobre 26 chamados com atuação direta no período (fonte: `colaborador_x_ticket`) |
| **Horas Apontadas no Voalle (Bruto)** | **274h 17m** | Inclui cronômetros abertos/sobrepostos em rotinas contínuas (explicado em auditoria de ponto) |
| **Horas da Jornada Real (Pontomais)** | **40h 00m** | Expediente contratual regular cumprido integralmente de segunda a sexta-feira |

---

## 1. Gestão de Demandas

### 1.1 Demandas Concluídas na Semana

| Protocolo / Referência | Descrição Técnica da Entrega | Resultado Obtido |
| :--- | :--- | :--- |
| **Sprints 321 a 352 (AutoTickets v2)** | Conclusão de 84 commits no período de 04/10 a 10/10/2026. Entregas estruturantes: novo módulo de IP Firewall com detecção de intrusão, blacklist e whitelist de IPs dinâmicos; padronização de credenciais *write-only secrets*; módulo completo de relatórios Fullcam com esteira de inadimplência, instalações e auditoria financeira de lucros/prejuízos; exportação multiformato em Playwright Headless sem travamentos; progressive loader com animação de etapas e persistência pós-F5. | Plataforma AutoTickets blindada contra acessos indevidos, auditoria financeira precisa do Fullcam economizando milhares de reais e automação de exportação de relatórios executivos. |
| **Protocolo #3212215 & #3214172** | Configuração completa do Servidor de IA Local com GPU (Proxmox VE, modelos LLM locais e embeddings offline) e instalação física no rack de servidores do Data Center Chácara (Capim Grosso). O equipamento foi acomodado na parte inferior traseira do rack, conectado à porta 23 do switch gerenciável via cabo CAT-6 e alimentado pela régua de tomadas do banco de baterias senoidal. BIOS configurada com *AC Power Loss: Power On* e VM Proxmox com *autostart*. | Servidor de IA 100% operacional no Data Center, permitindo processamento local e seguro de inteligência artificial sem dependência exclusiva de APIs em nuvem. |
| **Protocolo #3213644** | Diagnóstico e correção de falha no apontamento DNS da plataforma de ensino corporativo `universidade.teninternet.com.br` ("Plataforma indisponível"), solicitada por Raimara Santos. | Acesso dos colaboradores à Universidade Ten integralmente restabelecido. |
| **Protocolo #3216016** | Força-tarefa em conjunto com Isac Costa para restabelecer os acessos e credenciais dos colaboradores à plataforma Universidade Ten. | Usuários autenticados e aptos para a continuidade dos treinamentos internos. |
| **Protocolo #3209683** | Acompanhamento do chamado técnico aberto junto à fornecedora Synsuite/Voalle a respeito de deslogamentos abruptos de sessão dos usuários no ERP. Fornecidas evidências adicionais e escalonado internamente pelo suporte da Voalle. | Problema devidamente catalogado como ocorrência de sistema e sob monitoramento da engenharia do ERP. |
| **Protocolos de Saneamento Legado Voalle** | Identificação, auditoria e encerramento formal de tarefas com histórico pendente no ERP: #3187496 (Ferramentas de E-mail), #3187490 (Documentação Tiago Silva), #3182310 (Conexão Lenta e substituição por ONT AX30 Wi-Fi 6), #3168670 (Desbloqueio celular Samsung baixado após conclusão no #3191752), #3171518 (Configuração de equipamentos), #3152430 (Reparo PC Larissa Roza), #3112382 (Análise de equipamentos cliente), #3103374 (Zabbix coleta DHCP Mikrotik ROS 7 via API e suspensão de ROS 6 via SSH por hardening) e #3083979 (Parâmetros Voalle x Flashman). | Eliminação de 10 chamados antigos pendentes, saneando a fila histórica do setor no ERP Voalle. |
| **Protocolo #3218075** | Teste prático de movimentação e baixas de estoque de ativos de TI no Voalle. | Fluxo validado com sucesso para controle patrimonial. |

### 1.2 Demandas em Andamento

| Demanda / Protocolo | Responsável | % Avanço | Bloqueios / Dependências | Previsão de Conclusão |
| :--- | :---: | :---: | :--- | :---: |
| **Protocolo #3218766 (Investigação de Segurança - Supabase Compras)** | Liomar Oliveira (Apoio David Brasil) | 85% | Aplicação das regras de RLS (Row Level Security) e desativação de cadastro público no projeto Supabase pelo mantenedor da aplicação. | 16/10/2026 |
| **Protocolo #3217119 (Aprimoramento de Coleta Determinística AutoTickets)** | Liomar Oliveira | 75% | Ajustes finais nas rotinas de deduplicação e paridade entre banco Voalle e visões analíticas. | 17/10/2026 |
| **Protocolo #3210508 (Integração AutoTickets × Slack)** | Liomar Oliveira | 50% | Aguarda alinhamento com a Coordenação sobre diretrizes de retenção de dados e conformidade com LGPD. | 21/10/2026 |
| **Protocolos #3217070 e #3217077 (Auditoria e Desativação VM Gerenet)** | Liomar Oliveira | 40% | Confirmação formal da ausência de dependências operacionais para descontinuação e economia de recursos. | 20/10/2026 |
| **Protocolo #3215368 & #3214092 (Plataforma Slack Corporativo)** | Liomar Oliveira | 60% | Estruturação de grupos, canais e padronização de campos de identificação de colaboradores por filial. | 19/10/2026 |

### 1.3 Demandas Pendentes

- **Protocolo #3218356:** Requerimento de Documentos Normativos e Regulares da Empresa (aguardando liberação documental interna).
- **Protocolos #3216254 e #3216259:** Inventário físico de objetos internos e atualização formal das categorias de chamados internos/externos do setor de TI.
- **Protocolo #3181397:** Verificação de câmeras PPA integradas à plataforma Fulltime.
- **Protocolos Legados em Aberto (#3137037, #3078726, #3069558, #3048028):** Demandas estruturais de telefonia fixa (Zeus/TIP Brasil), documentação detalhada de MikroTiks e migração ChatSeguro para Native PBX aguardando agenda de prioridades.

### 1.4 Balanço de Entradas × Saídas

- **Solicitações Abertas no Período:** 33 solicitações
- **Solicitações Encerradas no Período:** 20 solicitações
- **Tarefas / OS Abertas:** 1 tarefa
- **Tarefas / OS Encerradas:** 1 tarefa
- **Total de Ações:** 40 ações registradas
- **Balanço da Fila Individual:** 21 saídas ÷ 34 entradas = **61,8%** (vazão concentrada em demandas de alta densidade técnica, como servidor GPU e resposta a incidentes).
- **Taxa de Resolubilidade nos Chamados Atuados:** **80,8%** (21 concluídos de 26 atuados diretamente).

---

## 2. Registro de Atividades e Engenharia de Software

### 2.1 Resumo Analítico das Atividades Executadas

1. **Desenvolvimento e Blindagem do AutoTickets v2 (84 commits):**
   - **Módulo de Segurança IP Firewall e Threat Intelligence (Sprints 352 a 357):** Implementação de middleware de firewall de aplicação com suporte a regras de blacklist e whitelist, tela de 403 personalizada, emissão de alertas em tempo real via toast e comando CLI de auditoria de conexões diretas ao PostgreSQL.
   - **Padrão Write-Only Secrets (Sprint 358):** Refatoração integral do gerenciamento de credenciais de integração (LiteLLM, Provedores IA, SMTP), eliminando o risco de exposição de tokens e chaves no frontend.
   - **Relatórios Analíticos Colaborador × Ticket (Sprints 336 a 347):** Criação das sub-abas de relatórios com cálculo dinâmico de TMA, TMR, resolubilidade individual, vazão da fila e classificação precisa de tarefas x solicitações.
   - **Exportador Multi-formato Resiliente via Playwright:** Substituição de chamadas síncronas bloqueantes do Chrome por script Node.js com protocolo DevTools, garantindo geração instantânea de PDFs e visualização HTML com escala compacta calibrada (0.67).
   - **Módulo Fullcam & Vouchers WiFeed (Sprints 348 a 351):** Esteira automatizada de checagem horária de inadimplência, esteira de instalações e auditoria financeira detalhada dos contratos de videomonitoramento.

2. **Instalação e Comissionamento do Servidor IA GPU no Data Center Chácara (#3212215 / #3214172):**
   - Configuração do sistema operacional base Proxmox VE com suporte a *PCIe Passthrough* para alocação direta da GPU dedicada aos contêineres e VMs.
   - Instalação e teste dos modelos de Inteligência Artificial offline com motores de *embedding* vetorial para consultas RAG seguras sem tráfego de dados confidenciais pela internet.
   - Deslocamento técnico ao Data Center Chácara em Capim Grosso: fixação física no rack principal de servidores, cabeamento CAT-6 estruturado na porta 23 de switch gerenciável e conexão redundante ao banco de baterias.
   - Parametrização da placa-mãe para reinicialização automática (*Power-On*) pós-queda de energia e auto-inicialização da VM de IA.

3. **Resposta a Incidente de Segurança Cibernética — Caso Supabase Compras (#3218766):**
   - Tratativa imediata após contato suspeito via WhatsApp do TI (`~Reis` / Discord `felipi090090`) afirmando ter obtido credenciais administrativas.
   - Perícia forense nos códigos: validação de que o sistema `mundialehistory.teninternet.com.br` está totalmente íntegro e sem brechas.
   - Identificação da vulnerabilidade na SPA `compras.teninternet.com.br`: projeto Supabase com registro público de usuários habilitado e ausência de políticas RLS restritivas nas tabelas `companies`, `users` e `purchase_orders`.
   - Desenvolvimento de script Python (`mapear_subdominios_teninternet.py`) para varredura do ecossistema de subdomínios da Ten Internet, auditoria via Postman e elaboração de relatório pericial completo de 242 linhas com orientações de saneamento e rastreamento de IP no Log Explorer do Supabase.

4. **Saneamento e Governança no ERP Voalle:**
   - Varredura e fechamento de 10 chamados com pendências históricas abertas, garantindo higienização de métricas e conformidade operacional.
   - Tratativa de ocorrências operacionais internas (DNS Universidade Ten, alinhamento de ramais e suporte a ferramentas de comunicação).

### 2.2 Distribuição do Tempo por Frente de Trabalho

```
Engenharia de Software & Arquitetura (AutoTickets v2): ████████████ 55%
Infraestrutura Crítica & Servidor IA (Data Center):     █████ 25%
Segurança da Informação & Perícia Cibernética:          ███ 15%
Gestão Operacional, Voalle & Suporte Interno:           █ 5%
```

### 2.3 Desenvolvimento e Capacitação Técnica

- **Engenharia de Infraestrutura para IA On-Premise:** Domínio prático em comissionamento de nós de inferência local com GPU, gerenciamento de memória VRAM e otimização de latência em modelos de linguagem locais via Proxmox.
- **Segurança Ofensiva e Defensiva em BaaS (Backend-as-a-Service):** Diagnóstico aprofundado de falhas em arquiteturas baseadas em Supabase/PostgREST, parametrização avançada de Row Level Security (RLS) e isolamento de APIs públicas.
- **Hardening de Aplicações Corporativas:** Implementação de camadas de controle de acesso por IP, blindagem contra ataques de injeção e sanitização estrita de dados em ecossistemas de missão crítica.

---

## 3. Projetos Estruturantes e Entregas Técnicas

### 3.1 Ecossistema AutoTickets v2: Módulos de Segurança e Relatórios

- **Status:** Em produção contínua (Sprints 321 a 352 entregues).
- **Entregas Principais:**
  1. *IP Firewall de Aplicação:* Monitoramento e bloqueio de tráfego malicioso em tempo real com whitelist corporativa e blacklist configurável.
  2. *Write-Only Secrets:* Gestão criptográfica de credenciais de APIs sem retorno visual para o navegador.
  3. *Motor Analítico Colaborador × Ticket:* Dashboard executivo com TMA, TMR, resolubilidade e vazão da fila.
  4. *Playwright Exporter:* Geração instantânea de relatórios em PDF com precisão visual milimétrica.

### 3.2 Servidor de IA Local (GPU Dedicated Node)

- **Status:** Concluído e operacional no Data Center Chácara (Protocolos #3212215 e #3214172).
- **Objetivo Estratégico:** Fornecer à empresa soberania de dados e capacidade computacional própria para inteligência artificial, processamento de documentos e automação de atendimento com custo zero de tokens externos.

### 3.3 Mitigação de Risco e Segurança no Portal de Compras (Supabase)

- **Status:** Perícia concluída e recomendações estruturais formalizadas (Protocolo #3218766).
- **Objetivo Estratégico:** Eliminação definitiva de brecha em banco de dados na nuvem, bloqueio de extração de dados e proteção da integridade cadastral das empresas do grupo.

---

## 4. Incidentes Tratados

| ID | Sistema / Ativo | Severidade | Causa Raiz Técnica | Ação Aplicada | Status |
| :---: | :--- | :---: | :--- | :--- | :---: |
| **INC-LIO-01** | Plataforma de Compras (`compras.teninternet.com.br`) | CRÍTICA | Supabase Auth com *disable_signup: false* e ausência de RLS em tabelas PostgreSQL (`companies`, `users`). | Investigação forense imediata, elaboração de relatório de resposta a incidentes, acionamento do time responsável e orientação para bloqueio de signup e aplicação de RLS restrito. | Mitigado / Em Correção pelo Mantenedor |
| **INC-LIO-02** | Universidade Ten (`universidade.teninternet.com.br`) | MÉDIA | Falha de apontamento DNS e configuração de rota gerando tela de indisponibilidade aos colaboradores. | Revalidação e ajuste nos registros DNS e restabelecimento de autenticação em conjunto com Isac Costa (#3213644 e #3216016). | Resolvido Definitivamente |
| **INC-LIO-03** | Sessão ERP Voalle (#3209683) | ALTA | Bug de expiração involuntária de sessão no backend Synsuite deslogando colaboradores com chamados em aberto. | Atualização do chamado junto à desenvolvedora Voalle, fornecimento de evidências adicionais e acompanhamento pelo suporte de nível 3. | Em Monitoramento |

---

## 5. Auditoria de Horas: Voalle × Pontomais

| Colaborador | Horas no Voalle | Horas no Pontomais | Variação | Justificativa Técnica Obrigatória |
| :--- | :---: | :---: | :---: | :--- |
| **Liomar Antonio de Oliveira** | **274h 17m** | **40h 00m** | **+234h 17m** | A divergência decorre estritamente de cronômetros deixados em execução contínua no ERP durante rotinas ininterruptas e finais de semana:<br>1. **Protocolo #3210518** (87h 25m) e **#3210508** (87h 30m): cronômetros iniciados na volta das férias (01/10) e mantidos ativos durante o fim de semana até a segunda-feira de manhã (05/10);<br>2. **Protocolo #3212215** (52h 01m): cronômetro contínuo mantido ativo durante a compilação, download de modelos e homologação do Servidor IA GPU de 05/10 a 07/10;<br>3. **Protocolo #3171518** (19h 39m) e **#3218069** (16h 15m): cronômetros deixados abertos durante a noite.<br>Descontando esses 5 timers sobrepostos (total de 262h 50m), o tempo líquido trabalhado em apontamentos pontuais é de aproximadamente **11h 27m**, compatível com a dedicação prioritária ao desenvolvimento de código fora do Voalle (84 commits no AutoTickets). |

---

## 6. Pontos de Atenção e Próximas Ações

1. **Aplicação Imediata de RLS no Supabase:** Cobrar dos desenvolvedores do sistema de compras a desativação urgente do signup aberto e o travamento de leitura anônima no PostgreSQL.
2. **Governança do Servidor IA GPU:** Integrar os agentes do AutoTickets ao endpoint local do Ollama no Data Center Chácara para absorver as rotinas de análise determinística sem consumir cotas de nuvem.
3. **Formalização Slack Corporativo:** Agendar reunião com o Coordenador Isvi Neemias para alinhar termos de privacidade e parâmetros de arquivamento da integração Slack × AutoTickets.
4. **Fechamento de Chamados Sem Timer Residual:** Adotar o hábito de pausar e encerrar os cronômetros das ordens de serviço no Voalle imediatamente após a conclusão dos testes de bancada.
