# Relatório Semanal Individual de Atividades — Setor de TI

---

## 🏢 Identificação Institucional e Metadados

* **Colaborador:** Liomar Antonio de Oliveira  
* **Cargo:** Analista de TI Sênior (Responsável por Engenharia de Software, Automações e Consolidação Técnica)  
* **ID Colaborador Voalle:** #107184  
* **Período de Referência:** 01/09/2026 a 13/09/2026  
* **Empresa:** Ten Soluções e Serviços LTDA. (Ten Provedor de Internet)  
* **Coordenador de Tecnologia:** Isvi Neemias  
* **Data de Emissão:** 17/09/2026  

---

## 📑 Índice de Navegação

* [Resumo Executivo](#resumo-executivo)
* [1. Gestão de Demandas](#1-gestão-de-demandas)
  * [1.1 Demandas Pendentes](#11-demandas-pendentes)
  * [1.2 Demandas em Andamento](#12-demandas-em-andamento)
  * [1.3 Demandas Concluídas no Período](#13-demandas-concluídas-no-período)
  * [1.4 Demandas Novas e Balanço da Fila](#14-demandas-novas-e-balanço-da-fila)
* [2. Registro de Atividades e Distribuição de Tempo](#2-registro-de-atividades-e-distribuição-de-tempo)
  * [2.1 Resumo Aprofundado das Atividades](#21-resumo-aprofundado-das-atividades)
  * [2.2 Distribuição da Carga Horária por Frente](#22-distribuição-da-carga-horária-por-frente)
  * [2.3 Desenvolvimento e Necessidades de Capacitação](#23-desenvolvimento-e-necessidades-de-capacitação)
  * [2.4 Apontamentos e Produtividade no ERP Voalle](#24-apontamentos-e-produtividade-no-erp-voalle)
* [3. Projetos e Entregas Técnicas](#3-projetos-e-entregas-técnicas)
  * [3.1 Projeto AutoTickets v2 (RADIUS, React 19, Arquitetura e Cache)](#31-projeto-autotickets-v2)
  * [3.2 Avaliação de Soluções de E-mail Corporativo (MailCow)](#32-avaliação-de-soluções-de-e-mail-corporativo-mailcow)
  * [3.3 Plataforma de Documentação Interna (Outline)](#33-plataforma-de-documentação-interna-outline)
  * [3.4 Painéis de BI com Parceiros (Analítica 3M e EasyBI)](#34-painéis-de-bi-com-parceiros-analítica-3m-e-easybi)
* [4. Incidentes Tratados](#4-incidentes-tratados)
* [5. Suporte Interno e Visitas Presenciais](#5-suporte-interno-e-visitas-presenciais)
  * [5.1 Atendimentos e Parametrizações Internas](#51-atendimentos-e-parametrizações-internas)
  * [5.2 Relatório de Visitas Presenciais e Gestão de Veículos](#52-relatório-de-visitas-presenciais-e-gestão-de-veículos)
* [6. Suporte ao Técnico de Campo](#6-suporte-ao-técnico-de-campo)
* [7. Infraestrutura e Sistemas Críticos](#7-infraestrutura-e-sistemas-críticos)
  * [7.1 Servidores e Virtualização (Proxmox, Dell R550, Datacom SV01)](#71-servidores-e-virtualização)
  * [7.2 Redes e Comutação do Data Center Chácara](#72-redes-e-comutação-do-data-center-chácara)
* [8. Pontos de Atenção e Próximas Ações](#8-pontos-de-atenção-e-próximas-ações)
  * [8.1 Riscos Tecnológicos Mapeados](#81-riscos-tecnológicos-mapeados)
  * [8.2 Necessidades de Investimentos e Aquisições](#82-necessidades-de-investimentos-e-aquisições)
  * [8.3 Ações Planejadas para o Próximo Período](#83-ações-planejadas-para-o-próximo-período)

---

## <a id="resumo-executivo"></a>Resumo Executivo

No período de **01/09/2026 a 13/09/2026**, a atuação de Liomar Antonio de Oliveira (Analista de TI Sênior) concentrou-se fortemente em três pilares estratégicos da infraestrutura tecnológica da Ten Provedor de Internet:

1. **Engenharia de Software e Automação (AutoTickets v2):** Evolução contínua da Sprint 222 até a Sprint 264 (mais de 80 commits de produção). Destacam-se o desenvolvimento do módulo de **FreeRADIUS Logs em Tempo Real** integrado à API do Voalle com rastreamento direto por MAC; a modernização completa da stack frontend para **React 19 e TailwindCSS v4** com decomposição atômica de componentes monolíticos; e a criação de camadas de cache intermediário no Grafana/Voalle para erradicar travamentos e timeouts (HTTP 504).
2. **Infraestrutura Física e Servidores Críticos do Data Center Chácara:** Instalação e ativação do switch gerenciável Gigabit **TP-Link T2600G-28TS 24p** (*Protocolo Voalle #3070027*), recuperação da interface remota **iDRAC do servidor Dell PowerEdge R550** mediante substituição de conector RJ45 danificado e cabeamento CAT6 (*Protocolo Voalle #3062633*), além da validação técnica de 4x SSDs NVMe E1.S no servidor Datacom DM-SV01. Em caráter emergencial, atuou na migração de VMs e containers do storage degradado no cluster Proxmox SuperMicro (*Protocolo Voalle #3187673*).
3. **Apoio Técnico Presencial e Homologação Laboratorial:** Realização de testes de bancada no laboratório de TI e deslocamento presencial externo intermunicipal até a cidade de Mairi em conjunto com Saulo Xavier e Matheus para diagnóstico da rede Wi-Fi 6 Mesh na residência do cliente Dr. Wendson (*Protocolo Voalle #3184572*), identificando limitações no modelo Datacom AX27 e formalizando recomendação de substituição pelo modelo AX30.

```
+----------------------------------------------------------------------------------------------------+
|                                    MÉTRICAS-CHAVE DO ANALISTA SÊNIOR                              |
+------------------------------------+----------------------------------+----------------------------+
| Carga Horária Voalle: 30h 09min     | Commits AutoTickets: 80+ commits | Protocolos Concluídos: 10  |
| Horas em Software: 25h 00min (70%)  | Horas em Infra: 05h 00min (15%)  | Taxa de Resolução: 83.3%   |
+------------------------------------+----------------------------------+----------------------------+
```

---

## <a id="1-gestão-de-demandas"></a>1. Gestão de Demandas

### <a id="11-demandas-pendentes"></a>1.1 Demandas Pendentes

| Protocolo / ID | Solicitante | Prioridade | Descrição Resumida | Bloqueio / Dependência | Previsão de Início |
| :---: | :--- | :---: | :--- | :--- | :---: |
| **#3184572** | Liomar Oliveira (Setor TI) | **Alta** | Substituição da ONT Datacom AX27 por ONT Datacom DM986-416 AX30 para o cliente Dr. Wendson Santana de Almeida (Mairi, login PPPoE `wendsonalmeida`). | Aguardando liberação e remessa do equipamento físico pelo Almoxarifado/Logística para envio à equipe de campo. | 18/09/2026 |
| **#3187496** | Isvi Neemias (Coordenação TI) | **Média** | Definição de arquitetura definitiva e homologação de caixas postais MailCow vs iRedMail para migração de e-mails institucionais. | Aguardando validação pela diretoria/coordenação dos custos de armazenamento e dimensionamento de backups. | 22/09/2026 |

---

### <a id="12-demandas-em-andamento"></a>1.2 Demandas em Andamento

| Protocolo / ID | Responsável | % Avanço | Descrição Detalhada da Atividade | Bloqueios / Dependências | Previsão de Conclusão |
| :---: | :---: | :---: | :--- | :--- | :---: |
| **AutoTickets Sprints** | Liomar Oliveira | **75%** | **Drivers de Telemetria de ONTs (Parks Fiberlink 611 e Datacom AX30):** Desenvolvimento de coletores de telemetria para sinal óptico (dBm), topologia EasyMesh e clientes conectados via CGNAT. | Finalização de testes de carga em topologias com mais de 3 roteadores mesh. | 18/09/2026 |
| **#3187490** | Liomar Oliveira | **30%** | **Validação da Plataforma Outline (Documentação Colaborativa):** Avaliação com Tiago Silva (Fiscal/DP) da aderência da ferramenta para substituição do Microsoft SharePoint descartado pela empresa. | Tiago Silva testando a plataforma na condição de Administrador (`https://docs.teninternet.com.br/`); aguardando retorno formal do DP/Fiscal. | 23/09/2026 |

---

### <a id="13-demandas-concluídas-no-período"></a>1.3 Demandas Concluídas no Período

1. **AutoTickets — Módulo de Logs RADIUS em Tempo Real e Monitoramento PPPoE**
   - *Origem:* Atividade Interna (DT 11/09/2026 09:30 às 23:00 — 13h30 apontadas).
   - *Entrega Realizada:* Engenharia e homologação da integração com o serviço de logs de autenticação RADIUS do ERP Voalle. Permite visualização imediata de sucessos e falhas de login PPPoE, identificando senhas incorretas, usuário inexistente e bloqueio de porta.
   - *Diferencial Técnico:* Criação de ferramenta exclusiva de busca de histórico RADIUS diretamente pelo endereço MAC da CPE, suprindo uma limitação crítica nativa do ERP Voalle, que apenas exibe logs quando o PPPoE está digitado perfeitamente no equipamento do cliente.
   - *Resultado:* Redução imediata no tempo de diagnóstico pelo NOC e suporte ao técnico de campo.
2. **AutoTickets — Otimização de Performance, Queries SQL e Cache do Grafana**
   - *Origem:* Atividade Interna (DT 12/09/2026 15:00 às 22:30 — 07h30 apontadas).
   - *Entrega Realizada:* Condução de testes rigorosos de carga e oneração de banco de dados. Implementação de camada de cache em memória intermediário para dados de telemetria óptica extraídos do Grafana e Voalle, acompanhado de reestruturação de queries SQL.
   - *Resultado:* Eliminação de riscos de deadlocks, redução de carga no servidor de produção e erradicação de erros de timeout (HTTP 504) em rotinas agendadas de sincronismo.
3. **AutoTickets — Matriz Modular de Permissões e Governança de Usuários (Spatie)**
   - *Origem:* Commits `eabcd168`, `643b04f9`, `d684729d`, `e76a3d41` (02/09/2026 — 04h00).
   - *Entrega Realizada:* Reformulação completa da segurança de rotas da aplicação, vinculando cargos funcionais aos perfis de permissão Spatie com controle granular por widget.
   - *Resultado:* Proteção de rotas sensíveis (`can:dashboard.access`), eliminação de bypass indevido e criação de tela personalizada com temática retro terminal CRT TV para resposta ao erro HTTP 403.
4. **Infraestrutura Datacenter Chácara — Switch Gerenciável TP-Link 24p Gigabit**
   - *Origem:* Protocolo Voalle #3070027 (08/09/2026 12:53 às 14:50 — 01h56 apontadas).
   - *Entrega Realizada:* Comissionamento, montagem em rack e configuração do switch gerenciável **TP-Link T2600G-28TS** (MAC `18:D6:C7:56:E7:BC`, S/N `216A521000197`, IP `172.16.30.27`, VLAN 1).
   - *Resultado:* Substituição definitiva de switch comum não gerenciável de 8 portas saturado; padronização de todo o cabeamento dos servidores em patch cords CAT6 de alta performance. O servidor Datacom SV01 permaneceu conectado diretamente ao firewall CCR1009, enquanto os demais servidores foram interligados ao novo switch.
5. **Infraestrutura Servidores — Manutenção Dell R550 e Upgrade DM-SV01**
   - *Origem:* Protocolo Voalle #3062633 (08/09/2026 12:37 às 12:50 — 00h13 apontadas).
   - *Entrega Realizada:* Identificação física de conector RJ45 quebrado na interface dedicada de gerência remota out-of-band iDRAC do servidor Dell PowerEdge R550. Confeccionado novo conector e substituído o cabeamento por CAT6, restabelecendo o acesso total à controladora.
   - *Resultado:* Validação operacional dos 4x SSDs corporativos NVMe E1.S KXD6CRJJ1T92 instalados no Datacom DM-SV01 e 2x SSDs Kingston SATA 480GB (SEDC600M480G) no servidor Proxmox SuperMicro.
6. **Virtualização Proxmox — Contenção e Migração Emergencial de Storage**
   - *Origem:* Protocolo Voalle #3187673 (09/09/2026) e Ticket Made4It #2026090910000089.
   - *Entrega Realizada:* Atuação conjunta com Isac Costa Silva no diagnóstico de falha física em discos do pool de armazenamento do servidor SuperMicro/Proxmox. Migração emergencial a quente/frio de máquinas virtuais e contêineres para storage saudável.
   - *Resultado:* Prevenção de corrupção de dados e abertura formal de chamado junto à consultoria Made4It para implantação de monitoramento preditivo de desgaste via telemetria S.M.A.R.T.
7. **Homologação Operacional do Módulo de Chamados do AutoTickets**
   - *Origem:* Protocolos Voalle #2854202, #2860473, #2854204, #2854205, #2866115 e #2873161 (08/09/2026).
   - *Entrega Realizada:* Bateria exaustiva de testes ponta a ponta simulando abertura, tramitação e fechamento automático de chamados de cancelamento de IP público e concessão de descontos por instabilidade técnica.
   - *Resultado:* Validação dos disparos de webhooks e regras de negócio no banco de dados do Voalle.

---

### <a id="14-demandas-novas-e-balanço-da-fila"></a>1.4 Demandas Novas e Balanço da Fila

No período de 01/09 a 13/09/2026, foram registradas **12 demandas formais de responsabilidade direta ou envolvimento técnico de Liomar Oliveira** no ERP Voalle:

* **Novas Demandas / Entradas:** 12 protocolos / tarefas internas
* **Demandas Concluídas / Saídas:** 10 entregas finalizadas
* **Demandas Remanescentes / Em Andamento:** 2 demandas (#3184572 e #3187490)
* **Taxa de Eficiência de Resolução:** **83,3%**
* **Balanço Líquido:** +2 demandas ativas na fila (todas com plano de ação definido e sob controle operacional).

---

## <a id="2-registro-de-atividades-e-distribuição-de-tempo"></a>2. Registro de Atividades e Distribuição de Tempo

### <a id="21-resumo-aprofundado-das-atividades"></a>2.1 Resumo Aprofundado das Atividades

A atuação de Liomar Oliveira caracterizou-se pelo foco em engenharia profunda, garantindo resiliência sistêmica tanto no ecossistema de software quanto no hardware físico da empresa:

* **Desenvolvimento e Refatoração de Software:** Entre 01/09 e 13/09, Liomar liderou a evolução técnica do **AutoTickets v2**. Além do novo motor de busca RADIUS por MAC, realizou a migração integral da base de código para **React 19** e **TailwindCSS v4**, fragmentando arquivos gigantescos que dificultavam manutenção (como `Tickets.tsx` e `SharedVoalleTicketModal.tsx`) em submódulos atômicos. Configurou suítes de teste de ponta a ponta com **Playwright**, eliminou gargalos de latência e implementou o design system corporativo moderno baseado no conceito Apple Bento Grid.
* **Manutenção Crítica de Data Center e Virtualização:** Atuou diretamente no rack da Chácara para restabelecer a conectividade do Dell R550 via iDRAC e comissionar o novo switch gerenciável TP-Link, organizando o fluxo de dados em cabos CAT6. No cluster de virtualização Proxmox, identificou a degradação de discos no servidor SuperMicro e conduziu a migração preventiva das cargas de trabalho para storage íntegro, evitando downtime de serviços essenciais.
* **Alinhamentos Tecnológicos Estratégicos com a Coordenação:** Conduziu reuniões e análises técnicas sobre plataformas corporativas demandadas por Isvi Neemias: estruturou a homologação do Outline com Tiago Silva (DP/Fiscal) e mapeou a arquitetura do MailCow para apoiar a implantação iminente do Slack corporativo na Ten Internet.

---

### <a id="22-distribuição-da-carga-horária-por-frente"></a>2.2 Distribuição da Carga Horária por Frente

Com base nas atividades apontadas no Voalle (30h09) e no esforço contínuo de gestão e monitoramento, a distribuição da carga horária de Liomar estruturou-se da seguinte forma:

```
+----------------------------------------------------------------------------------------------------+
|                             DISTRIBUIÇÃO DE CARGA HORÁRIA DO ANALISTA SÊNIOR                      |
+-----------------------------------------+---------------+------------+-----------------------------+
| Frente de Trabalho                      | Carga Horária | Percentual | Foco Técnico Principal      |
+-----------------------------------------+---------------+------------+-----------------------------+
| Projetos e Automação (AutoTickets v2)   |    25h 00min  |   70,0%    | RADIUS, React 19, SQL Cache |
| Infraestrutura e Servidores Críticos    |    05h 00min  |   15,0%    | TP-Link 24p, Dell R550, SSDs|
| Suporte Técnico e Campo Especializado   |    03h 00min  |   10,0%    | Bancada Lab e Visita Mairi  |
| Suporte Interno e Homologação           |    01h 30min  |    5,0%    | Outline, MailCow, Testes    |
+-----------------------------------------+---------------+------------+-----------------------------+
| TOTAL ESTIMADO                         |    34h 30min  |  100,0%    |                             |
+-----------------------------------------+---------------+------------+-----------------------------+
```

---

### <a id="23-desenvolvimento-e-necessidades-de-capacitação"></a>2.3 Desenvolvimento e Necessidades de Capacitação

* **Pontos Fortes Demonstrados:**
  - Capacidade analítica avançada em engenharia reversa de APIs e protocolos de rede (RADIUS, TR-069, EasyMesh).
  - Domínio completo de arquitetura frontend reativa (React 19, Tailwind v4, decomposição atômica) e backend Laravel/PostgreSQL.
  - Agilidade na identificação e contenção física de incidentes em data center (cabeamento estruturado, controladoras iDRAC, comutação L2).
* **Necessidades de Capacitação e Treinamento Identificadas:**
  - Aprofundamento em pipelines assíncronos de alta performance com **Redis** e mensageria distribuída para processamento de logs RADIUS massivos.
  - Especialização em orquestração conteinerizada (**Docker Compose e Kubernetes**) para implantação rápida e padronizada de serviços auxiliares (MailCow, Outline, Vaultwarden).

---

### <a id="24-apontamentos-e-produtividade-no-erp-voalle"></a>2.4 Apontamentos e Produtividade no ERP Voalle

Durante a quinzena, Liomar totalizou **30 horas e 09 minutos de tarefas técnicas estritamente documentadas no ERP Voalle**:

* **11/09/2026 (09:30 às 23:00):** 13h 30min — *Desenvolvimento AutoTickets: Módulo RADIUS em Tempo Real e Monitoramento PPPoE*
* **12/09/2026 (15:00 às 22:30):** 07h 30min — *Desenvolvimento AutoTickets: Otimização de consultas SQL e cache de sinal óptico do Grafana*
* **04/09/2026 (09:00 às 12:00):** 03h 00min — *Testes laboratoriais de bancada e avaliação de roteadores Wi-Fi 6 (Datacom AX27 vs AX30)*
* **08/09/2026 (12:53 às 14:50):** 01h 56min — *Protocolo #3070027: Instalação e comissionamento de switch gerenciável TP-Link 24p DC Chácara*
* **08/09/2026 (12:37 às 12:50):** 00h 13min — *Protocolo #3062633: Manutenção Dell R550 (iDRAC) e validação de upgrades no Datacom SV01*
* **08/09/2026 (12:15 às 12:29):** Tarefas de homologação de chamados de cancelamento de IP público e solicitações de desconto (#2854202, #2854204, #2854205, #2860473, #2866115, #2873161).
* **Demais períodos:** Atividades contínuas de gestão técnica, orientação aos membros da equipe, revisões de código e monitoramento.

---

## <a id="3-projetos-e-entregas-técnicas"></a>3. Projetos e Entregas Técnicas

### <a id="31-projeto-autotickets-v2"></a>3.1 Projeto AutoTickets v2 (RADIUS, React 19, Arquitetura e Cache)

O AutoTickets v2 representa a espinha dorsal de automação e integração técnica da empresa, desenvolvido e mantido por Liomar Oliveira:

* **Sprints 222 a 235 (01/09 a 03/09):**
  - Implementação da governança de permissões modulares via Spatie (`eabcd168`, `643b04f9`).
  - Criação da página 403 animada em estilo retro CRT terminal com fonte VT323 (`b18efa26`, `fb19c9d3`).
  - Módulo de auditoria do Voalle e filtros avançados com detecção de OUIs reais no NOC (`ee43ad22`).
  - Integração de script automatizado Playwright Headless Chromium para scraping de métricas do WiFeed (`47f3bb80`, `1fd1650b`).
* **Sprints 237 a 248 (11/09):**
  - Engenharia reversa e integração do serviço de logs de autenticação RADIUS do ERP Voalle (`77e346e5`, `894d00f3`).
  - Criação de ferramenta exclusiva para localizar logs RADIUS diretamente pelo endereço MAC da CPE.
  - Sincronização de IPs CGNAT com gráficos ópticos do Grafana em tempo real (`9164a66d`).
  - Migração de base tecnológica completa para **React 19** e **TailwindCSS v4**, atomizando componentes gigantescos (`690c7d2e`, `275d8006`, `aa921d97`).
* **Sprints 249 a 264 (12/09 e 13/09):**
  - Implantação do Design System Apple Bento Grid com calibrated OKLCH e KPI cards dinâmicos (`608b6bbb`, `6406ab40`).
  - Camada de cache intermediário contra deadlocks e timeouts 504 no Grafana/Voalle (`b2b8149b`).
  - Widget flutuante de chat e conectividade NOC dockable (`43e857b5`, `e5bdb5a9`).

---

### <a id="32-avaliação-de-soluções-de-e-mail-corporativo-mailcow"></a>3.2 Avaliação de Soluções de E-mail Corporativo (MailCow)

* **Contexto e Solicitação:** Protocolo Voalle #3187496 aberto por Isvi Neemias em 08/09/2026, demandando levantamento de soluções de e-mail institucional (MailCow, iRedMail e Modoboa) para suprir a necessidade de provisionamento rápido de caixas postais corporativas exigidas para a implantação do Slack.
* **Atuação de Liomar:**
  - Estudo comparativo e validação técnica da máquina virtual configurada no Proxmox por Isvi em 09/09/2026.
  - Análise dos requisitos de armazenamento, certificados SSL e registros DNS (DKIM, SPF, DMARC) necessários para garantir entregabilidade.
  - Alinhamento de que a solução baseada em MailCow atende plenamente ao caráter de urgência do Slack, mantendo interoperabilidade caso a empresa venha a migrar futuramente para o Microsoft 365 Business.

---

### <a id="33-plataforma-de-documentação-interna-outline"></a>3.3 Plataforma de Documentação Interna (Outline)

* **Contexto e Solicitação:** Protocolo Voalle #3187490 aberto por Isvi Neemias em 08/09/2026 para validação com Tiago Silva (Fiscal/DP) de uma plataforma de documentação interna em substituição ao SharePoint (descartado formalmente pela gestão).
* **Atuação de Liomar:**
  - Implantação e disponibilização do Outline no endereço `https://docs.teninternet.com.br/`.
  - Reunião técnica com Tiago Silva em 09/09/2026 às 15:57, concedendo-lhe perfil de Administrador da plataforma para avaliação de usabilidade, categorização de procedimentos e testes práticos com as equipes de DP e Fiscal.
  - Status atual: Aguardando parecer formal de Tiago Silva para fechamento do protocolo.

---

### <a id="34-painéis-de-bi-com-parceiros-analítica-3m-e-easybi"></a>3.4 Painéis de BI com Parceiros (Analítica 3M e EasyBI)

Em estrita conformidade com as regras de fidedignidade e diretrizes institucionais, esclarece-se o status fático dos ambientes de Business Intelligence:

* **Analítica 3M:** O analista Liomar Oliveira dispõe de acesso com permissões restritas apenas para visualização de telas pré-existentes. O Setor de TI não administra o ambiente e não realiza acompanhamento técnico direto da integração. Ficou pendente de o coordenador Isvi Neemias solicitar a inclusão de contato da equipe no grupo de WhatsApp com o fornecedor. Houve atendimento pontual no período para liberação de IPs no banco do Voalle solicitados por Ezequiel (IPs: `82.112.249.232/32`, `95.217.222.162/32`, `65.108.208.255/32`).
* **EasyBI (MW Solutions):** O analista nunca recebeu credenciais funcionais de acesso; o link direto da plataforma (`https://easybi.teninternet.com.br`) permanece indisponível por falha de resolução DNS pública/interna; inexiste participação da equipe técnica em grupos de suporte do parceiro, estando o sistema fora do escopo de atuação do analista.
* **Diretriz Estratégica da Coordenação:** A gestão de TI planeja construir uma tela única e dedicada para o setor dentro da ferramenta Analítica 3M, com escopo detalhado que permita benchmarking comparativo entre as plataformas e viabilize, futuramente, o uso do BI como fonte primária automatizada de relatórios.

---

## <a id="4-incidentes-tratados"></a>4. Incidentes Tratados

| Data / Hora | Ativo / Sistema | Severidade | Causa Raiz Técnica | Ação Corretiva Aplicada | Tipo / Status |
| :---: | :--- | :---: | :--- | :--- | :---: |
| **04/09 08:30** | Conectividade Wi-Fi 6 Mesh Dr. Wendson (Mairi) | **Alta** | Falha de sincronismo e instabilidade na rede 2.4/5GHz da ONT Datacom DM986 AX27 em cenário mesh com múltiplos roteadores. | Testes laboratoriais na bancada de TI e visita presencial in loco (*Prot. #3184572*). Solicitação formal de substituição para modelo AX30. | Recorrente / Mitigado (Aguardando remessa) |
| **08/09 12:35** | Interface Remota iDRAC (Dell PowerEdge R550) | **Média** | Conector físico RJ45 da porta dedicada iDRAC quebrado após manutenções no rack da Chácara, bloqueando acesso out-of-band. | Substituição física do conector RJ45, recabeamento com patch cord CAT6 e restabelecimento total da gerência remota (*Prot. #3062633*). | Novo / **Resolvido Definitivamente** |
| **09/09 11:25** | Storage Proxmox (Servidor SuperMicro) | **Crítica** | Falha física em discos rígidos/SSDs no pool de armazenamento do Proxmox, com risco iminente de corrupção de VMs corporativas. | Atuação emergencial com Isac Costa (*Prot. #3187673*), migrando VMs/CTs para storage íntegro. Abertura de chamado Made4It (#2026090910000089) para monitoramento S.M.A.R.T. | Novo / **Mitigado em Operação** |
| **12/09 16:00** | Telemetria Óptica Voalle / Grafana | **Média** | Consultas massivas síncronas ao banco de dados sem cache intermediário causando sobrecarga e risco de HTTP 504 no AutoTickets. | Refinamento de queries SQL, otimização de índices e implantação de cache em memória intermediário (DT 12/09). | Recorrente / **Resolvido Definitivamente** |

---

## <a id="5-suporte-interno-e-visitas-presenciais"></a>5. Suporte Interno e Visitas Presenciais

### <a id="51-atendimentos-e-parametrizações-internas"></a>5.1 Atendimentos e Parametrizações Internas

* Atendimento de solicitações de infraestrutura corporativa demandadas pela coordenação e parceiros (pesquisa e viabilização técnica de MailCow e Outline).
* Execução e auditoria de baterias de testes no ERP Voalle para novos módulos de cancelamento de serviços e estornos.
* Manutenção e parametrização física de portas de rede no Data Center da Chácara para atender novas demandas dos servidores de aplicação.

### <a id="52-relatório-de-visitas-presenciais-e-gestão-de-veículos"></a>5.2 Relatório de Visitas Presenciais e Gestão de Veículos

* **Auditoria do Documento Formal de Visitas:** O documento institucional [1.voalle/Relatório de Visita Técnica Presencial - Setor TI.md](file:///home/liomarti/dev/reports_ti/1.voalle/Relat%C3%B3rio%20de%20Visita%20T%C3%A9cnica%20Presencial%20-%20Setor%20TI.md) cataloga os registros manuais da equipe até agosto/2026.
* **Deslocamento Presencial Realizado no Período:**
  - *Data:* 04/09/2026 (vinculado ao Protocolo Voalle #3184572).
  - *Destino:* Residência do cliente Dr. Wendson Santana de Almeida, município de Mairi.
  - *Equipe Envolvida:* Liomar Antonio de Oliveira (Analista de TI), Saulo Xavier e Matheus.
  - *Objetivo:* Diagnóstico presencial e validação in loco da rede interna, níveis de atenuação de sinal óptico e sincronismo de roteadores Wi-Fi 6 em topologia mesh após queixas recorrentes de oscilação de link.
  - *Conclusão Técnica:* A rede interna foi homologada funcionalmente, constatando-se a necessidade de substituição da ONT Datacom AX27 por uma AX30 para estabilidade definitiva sob cargas de alta densidade.

---

## <a id="6-suporte-ao-técnico-de-campo"></a>6. Suporte ao Técnico de Campo

* **Diagnóstico Laboratorial Prévio:** Liomar realizou testes detalhados na bancada de TI avaliando roteadores Wi-Fi 6 Datacom DM986 AX27, Datacom DM956-4GT e modelos homologados, repassando instruções práticas para as equipes externas sobre limitações de firmware e métodos de pareamento mesh.
* **Ferramental de Diagnóstico Remoto no AutoTickets:** Criação e disponibilização de rotina que permite ao suporte e ao técnico localizar em poucos segundos logs de falha RADIUS apenas pelo MAC da ONT em campo, eliminando a dependência de abertura manual de chamados no Voalle para checar se o login PPPoE foi rejeitado.

---

## <a id="7-infraestrutura-e-sistemas-críticos"></a>7. Infraestrutura e Sistemas Críticos

### <a id="71-servidores-e-virtualização"></a>7.1 Servidores e Virtualização

* **Dell PowerEdge R550:** Interface de gerenciamento dedicada iDRAC restabelecida com novo conector RJ45 e cabeamento CAT6 (*Prot. #3062633*). Servidor 100% operacional.
* **Datacom DM-SV01:** Validação da instalação física e lógica de 4x SSDs NVMe corporativos modelo E1.S KXD6CRJJ1T92 (capacidade nominal de 1.92TB cada), garantindo alta vazão de I/O para as instâncias de bancos de dados.
* **Proxmox SuperMicro:** Servidor com instâncias críticas estabilizadas após migração preventiva de volumes para storages sadios (*Prot. #3187673*).

### <a id="72-redes-e-comutação-do-data-center-chácara"></a>7.2 Redes e Comutação do Data Center Chácara

* **Switch TP-Link T2600G-28TS:** Equipamento gerenciável L2 com 24 portas Gigabit e uplinks SFP comissionado com sucesso no rack de servidores (IP `172.16.30.27`, VLAN 1).
* **Organização Física do Cabeamento:** Substituição de cabos obsoletos por patch cords padronizados CAT6, mantendo conexão direta do servidor Datacom SV01 na porta dedicada do firewall CCR1009 da Chácara e concentrando os demais servidores corporativos no novo switch.

---

## <a id="8-pontos-de-atenção-e-próximas-ações"></a>8. Pontos de Atenção e Próximas Ações

### <a id="81-riscos-tecnológicos-mapeados"></a>8.1 Riscos Tecnológicos Mapeados

* **Comportamento Instável das ONTs Datacom AX27:** Equipamento apresenta inconsistências de sincronismo e instabilidade Wi-Fi sob tráfego intenso em malhas mesh, necessitando de substituição preventiva para clientes de alto valor (como o caso do cliente Dr. Wendson em Mairi).
* **Necessidade de Definição de E-mail Corporativo:** Risco de bloqueio no onboarding do Slack corporativo caso a definição entre MailCow e serviços em nuvem sofra postergações.

### <a id="82-necessidades-de-investimentos-e-aquisições"></a>8.2 Necessidades de Investimentos e Aquisições

* **Remessa de Roteadores Datacom AX30:** Envio prioritário de lote para substituição definitiva em clientes críticos e reposição de estoque de testes do laboratório de TI.
* **Storage de Alta Confiabilidade para Proxmox:** Aquisição de novas unidades SSD/NVMe corporativas para substituição dos discos degradados no pool do Proxmox SuperMicro.

### <a id="83-ações-planejadas-para-o-próximo-período"></a>8.3 Ações Planejadas para o Próximo Período

1. Concluir os testes e homologar os drivers de telemetria das ONTs Parks 611 e Datacom AX30 no AutoTickets v2.
2. Acompanhar os testes de homologação do Outline com Tiago Silva (DP/Fiscal) e formalizar o encerramento do Protocolo #3187490.
3. Monitorar a liberação e envio da ONT AX30 para o cliente Dr. Wendson em Mairi junto ao Almoxarifado (*Prot. #3184572*).
4. Acompanhar a implementação de monitoramento S.M.A.R.T. no Proxmox SuperMicro junto à consultoria Made4It.
