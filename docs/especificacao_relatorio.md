# 📐 Especificação do Relatório Semanal Consolidado

> Estrutura oficial (modelo da Coordenação — ver `docs/referencias/modelo_relatorio_setor_ti.pdf`), diagramação, índice e conteúdo obrigatório por tópico.
> Regras de cálculo das métricas: `docs/regras_metricas.md`. Fluxo de geração: `docs/fluxo_geracao.md`.
> **CSS oficial:** `templates/report.css` (não reinventar o visual a cada semana). Esqueleto HTML: `templates/report.html`.

## Estrutura hierárquica e diretrizes visuais

### 🎨 1. Moldura do Topo e Bloco Institucional

A moldura de abertura do documento deve seguir estritamente o padrão corporativo:

* **Título Principal:** Relatório Semanal Consolidado - Setor TI
* **Subtítulo:** Panorama Operacional, Gestão de Demandas, Incidentes, Infraestrutura Crítica e Outros
* **Bloco de Identificação Executiva (Grid Corporativo em Tabela):**
  - **Período Analisado:** `[Data Inicial Domingo] a [Data Final Sábado] (Semana XX / AAAA)`
  - **Período Operacional Efetivo:** `[Segunda-feira] a [Sexta-feira] (Expediente Útil do Setor)`
  - **Coordenador de TI:** `Isvi Neemias`
  - **Responsável pela Consolidação:** `Liomar Antonio de Oliveira (Analista de TI Sênior — ID #107184)`
  - **Equipe Integrada:** `Liomar Oliveira, Isac Costa Silva e David Brasil Fernandes`

### 📑 2. Paginação, Diagramação e Renderização PDF

0. **Ferramentas oficiais:** o `.md` é a fonte única; o HTML sai de `python3 scripts/md_para_html.py <arquivo.md>` (moldura do template, ids do índice, statcards pelos marcadores `<!-- KPI: … -->`, barras por `<!-- BARS: … -->`, células sem quebra para números/protocolos/CPF e tabela densa quando há CPF/CNPJ) e o PDF de `bash scripts/renderizar_pdf.sh <arquivo.html>` (embute `templates/report.css` e já aplica `--no-pdf-header-footer`).
1. **Remoção de Cabeçalho/Rodapé do Navegador no PDF:**
   - Na geração do PDF via Chromium/Playwright, utilizar obrigatoriamente o parâmetro `--no-pdf-header-footer` (ou equivalente no CSS com `@page { margin: 15mm 12mm 15mm 12mm; }`), evitando que datas automáticas e caminhos locais (`file:///...` ou numerações `1/2`) poluam o cabeçalho e rodapé.
   - O próprio design HTML/CSS deve gerenciar cabeçalhos e numeração de página de forma interna e elegante.
2. **Quebra de Página por Tópico Principal:**
   - Cada tópico principal deve iniciar em uma nova página através de quebras de página explícitas (`page-break-before: always;` / `break-before: page;`).
3. **Recursos Visuais Obrigatórios:**
   - **Statcards:** No início de cada seção quantitativa, exibir cards com métricas-chave destacadas (números totais, balanço de fila, horas economizadas).
   - **Gráficos Visuais (CSS/SVG nativos):** Gráficos de barras proporcionais e distribuição setorial (pizza/donut em SVG puro ou CSS flex/grid).
   - **Tabelas Completas e Ricas:** Listagens estruturadas contendo Protocolo/ID, Solicitante/Setor, Descrição Técnica, Responsável e Status.

---

### 🗂️ Grandes Seções (organização do relatório)

Depois do Resumo Executivo, dos 📈 Destaques e dos ⭐ Fatos Notáveis, o corpo é dividido em grandes seções, cada uma com um título `#` (nível 1), uma frase de abertura e os seus tópicos numerados em sequência:

| Grande seção | Tópicos | O que entra |
| :--- | :--- | :--- |
| **Parte I — O Setor de TI** | 1 a 7 | Operação do setor e dos colaboradores analisados: demandas, atividades por pessoa, projetos, suporte interno, suporte ao campo, infraestrutura/incidentes/backups e as **iniciativas, desafios e conquistas** detectados nas atividades (gincanas, estudos, resultados que se destacaram). |
| **Parte II — A Empresa** | 8 a 10 | Dados da empresa como um todo: indicadores do ERP Voalle e da rede (base de clientes adimplentes, reincidência, ocorrências sistêmicas, PPPoE), WiFeed e Fullcam. Abrir dizendo que os relatórios vêm do **AutoTickets**, plataforma integradora desenvolvida por Liomar que consolida dados do Voalle, da Fullcam, do WiFeed e do NOC: os números são dos sistemas de origem, consolidados por ele. |
| **Parte III — Sistemas** | 11 e 12 | Os sistemas em si: desenvolvimento do AutoTickets (regra 9 do `AGENTS.md`) e situação dos demais sistemas internos ou contratados (BI, Compras, Mundiale History, Flashman, Slack etc.). |
| **Encerramento** | 13 | Pontos de atenção, investimentos e ações planejadas. |

> A organização em grandes seções foi adotada na semana 42 e ainda será refinada ao longo das próximas semanas.

### ✍️ Estilo de escrita

- **Pessoas sem artigo:** "David atribui as falhas…", "Liomar registrou…", "Raimara confirmou no equipamento", "Isac apurou 995 quedas…"; nunca "o David", "a Raimara", "do Liomar" (usar "de Liomar", "por Isvi").
- **Base de clientes:** a base diária vem do **ERP Voalle** (clientes adimplentes em qualquer produto, de toda a empresa). O AutoTickets a apura na automação que atualiza os vouchers do WiFeed; não chamar de "base WiFeed".
- **Automações Fullcam:** o relatório registra só as execuções em que a automação agiu (bloqueio, desbloqueio, instalação). Execução sem pendência não gera registro; ausência de registro **não** significa que a automação parou.
- **Contexto antes de cobrar:** antes de apontar falta de registro ou desvio, conferir o último relato do protocolo (ex.: projeto aguardando equipamento) e o histórico do caso (ex.: configuração feita por terceiros antes de existir o setor).

### 🧩 Classes de Tópicos: Fixos, Condicionais e Dinâmicos

O relatório **não é um formulário igual toda semana**: a estrutura tem uma espinha fixa (para comparação e histórico) e partes que mudam com os dados.

| Classe | Quais | Regra |
| :--- | :--- | :--- |
| **Fixos** | Resumo Executivo, as grandes seções (Parte I, II, III e Encerramento), os tópicos 1 a 13 e seus subtópicos numerados (exceto os condicionais) | Sempre presentes. Sem demanda na semana: **ausência justificada** (nunca omitir, nunca simular). |
| **Condicionais** | **8.4** Anomalias PPPoE (fonte `fontes/autotickets/anomalias_pppoe/`). Novos módulos do AutoTickets entram nesta classe ao serem criados. | Só existem no índice e no corpo **se houver fonte**. Sem fonte: não criar a seção; registrar em uma linha no fim do Resumo Executivo: *"Tópicos condicionais sem fonte nesta semana: 8.4 …"*. |
| **Dinâmicos** | **📈 Destaques Analíticos da Semana** e **⭐ Fatos Notáveis e Anomalias da Semana** | O **título de cada item é o próprio achado** (ex.: "Fila do TI cresceu 18% puxada por Patrimônio e Logística"). Quantidade e assunto dependem dos dados da semana. Os itens são `###` não numerados e **não entram no índice** (só a seção). |
| **Subtópicos livres** | Dentro de qualquer tópico fixo | Quando os dados revelarem um padrão relevante (concentração, outlier, recorrência), criar `####` **sem número** com o achado no título (ex.: "#### Concentração de chamados no setor Financeiro"). Não entram no índice. |

**Como decidir o que vira tópico dinâmico** (critérios objetivos, aplicados às fontes da semana e à semana anterior):

1. Variação de indicador-chave ≥ 20% em relação à semana anterior (fila, volume por setor, horas, base de clientes adimplentes do Voalle, saldo Fullcam).
2. Picos e outliers (ex.: apontamento > 8h ou atravessando noite/fim de semana; tempo de atendimento absurdo; um setor ou solicitante concentrando > 30% da demanda).
3. Novos tipos de demanda, setores ou sistemas que não apareciam antes.
4. Recorrências (mesmo problema, cliente, equipamento ou POP em semanas consecutivas; janela de 30 dias para reincidência).
5. Desvios de plano (prazo, escopo ou prioridade diferente do registrado no relatório anterior).
6. Inconsistências relevantes nas próprias fontes (dados do AutoTickets/Voalle que mudam a leitura de um indicador — ver `_ANALISE_*.md`).

**Onde encaixar:** padrão de dados/indicadores → **📈 Destaques Analíticos**; ocorrência/evento incomum (incidente, falha, atraso, desvio) → **⭐ Fatos Notáveis**; padrão restrito a um tema → **subtópico livre** dentro do tópico fixo correspondente. **Entregas normais** (projetos concluídos, equipamentos instalados) vão para os Tópicos 1.3, 3, 7 ou 11, nunca para Fatos Notáveis.

### 📂 3. Índice Geral de Navegação (com Links Âncoras 100% Funcionais)

O relatório deve conter um **Índice Completo** no início, com links internos rigorosamente correspondentes aos títulos do corpo do texto. **O título no corpo deve ser idêntico ao do índice** (sem acrescentar parênteses ou complementos — eles mudam a âncora). Conferir com `python3 scripts/validar_indice.py`:

* [Resumo Executivo](#resumo-executivo)
* [📈 Destaques Analíticos da Semana](#-destaques-analíticos-da-semana)
* [⭐ Fatos Notáveis e Anomalias da Semana](#-fatos-notáveis-e-anomalias-da-semana)
* [Parte I — O Setor de TI](#parte-i--o-setor-de-ti)
  * [1. Gestão de Demandas](#1-gestão-de-demandas)
    * [1.1 Demandas Pendentes](#11-demandas-pendentes)
    * [1.2 Demandas em Andamento](#12-demandas-em-andamento)
    * [1.3 Demandas Concluídas](#13-demandas-concluídas)
    * [1.4 Demandas Novas](#14-demandas-novas)
      * [1.4.1 Comparativo Entradas × Saídas (Balanço da Fila)](#141-comparativo-entradas--saídas-balanço-da-fila)
  * [2. Registro de Atividades por Membro da Equipe](#2-registro-de-atividades-por-membro-da-equipe)
    * [2.1 David Brasil Fernandes](#21-david-brasil-fernandes)
      * [2.1.1 Resumo das Atividades](#211-resumo-das-atividades)
      * [2.1.2 Distribuição do Tempo](#212-distribuição-do-tempo)
      * [2.1.3 Desenvolvimento e Capacitação](#213-desenvolvimento-e-capacitação)
    * [2.2 Isac Costa Silva](#22-isac-costa-silva)
      * [2.2.1 Resumo das Atividades](#221-resumo-das-atividades)
      * [2.2.2 Distribuição do Tempo](#222-distribuição-do-tempo)
      * [2.2.3 Desenvolvimento e Capacitação](#223-desenvolvimento-e-capacitação)
    * [2.3 Liomar Antonio de Oliveira](#23-liomar-antonio-de-oliveira)
      * [2.3.1 Resumo das Atividades](#231-resumo-das-atividades)
      * [2.3.2 Distribuição do Tempo](#232-distribuição-do-tempo)
      * [2.3.3 Desenvolvimento e Capacitação](#233-desenvolvimento-e-capacitação)
    * [2.4 Desempenho no Voalle e Confronto com Jornada Real (Pontomais)](#24-desempenho-no-voalle-e-confronto-com-jornada-real-pontomais)
  * [3. Projetos e Entregas do Setor](#3-projetos-e-entregas-do-setor)
    * [3.1 Projetos de Conectividade e Redes](#31-projetos-de-conectividade-e-redes)
    * [3.2 Telefonia Fixa e Comunicação Corporativa](#32-telefonia-fixa-e-comunicação-corporativa)
  * [4. Suporte Interno (Informática)](#4-suporte-interno-informática)
    * [4.1 Relação de Atendimentos e Chamados da Semana](#41-relação-de-atendimentos-e-chamados-da-semana)
    * [4.2 Setores que mais Demandaram Atendimento](#42-setores-que-mais-demandaram-atendimento)
    * [4.3 Colaboradores Solicitantes Mais Frequentes](#43-colaboradores-solicitantes-mais-frequentes)
    * [4.4 Relatório de Visitas Técnicas Presenciais e Gestão de Veículos](#44-relatório-de-visitas-técnicas-presenciais-e-gestão-de-veículos)
  * [5. Suporte ao Técnico de Campo](#5-suporte-ao-técnico-de-campo)
    * [5.1 Volumetria de Solicitações (Com e Sem Protocolo)](#51-volumetria-de-solicitações-com-e-sem-protocolo)
    * [5.2 Tipos de Apoio Mais Frequentes e Tempo de Resposta](#52-tipos-de-apoio-mais-frequentes-e-tempo-de-resposta)
    * [5.3 Oportunidades de Automação e Redução de Dependência](#53-oportunidades-de-automação-e-redução-de-dependência)
  * [6. Infraestrutura, Incidentes e Backups](#6-infraestrutura-incidentes-e-backups)
    * [6.1 Incidentes Tratados](#61-incidentes-tratados)
    * [6.2 Disponibilidade de Serviços e Incidentes em Sistemas](#62-disponibilidade-de-serviços-e-incidentes-em-sistemas)
    * [6.3 Execução e Validação de Backups](#63-execução-e-validação-de-backups)
    * [6.4 Atualizações, Melhorias e Ações de Modernização](#64-atualizações-melhorias-e-ações-de-modernização)
  * [7. Iniciativas, Desafios e Conquistas da Semana](#7-iniciativas-desafios-e-conquistas-da-semana)
    * [7.1 Conquistas e Resultados de Destaque](#71-conquistas-e-resultados-de-destaque)
    * [7.2 Desafios e Iniciativas do Setor](#72-desafios-e-iniciativas-do-setor)
* [Parte II — A Empresa](#parte-ii--a-empresa)
  * [8. Indicadores da Empresa: ERP Voalle e Rede](#8-indicadores-da-empresa-erp-voalle-e-rede)
    * [8.1 Base de Clientes Adimplentes no ERP Voalle](#81-base-de-clientes-adimplentes-no-erp-voalle)
    * [8.2 Reincidência de Problemas no Atendimento](#82-reincidência-de-problemas-no-atendimento)
    * [8.3 Ocorrências Sistêmicas na Rede de Distribuição](#83-ocorrências-sistêmicas-na-rede-de-distribuição)
    * [8.4 Anomalias de Tráfego PPPoE e Ações Proativas para o Service Desk](#84-anomalias-de-tráfego-pppoe-e-ações-proativas-para-o-service-desk) *(condicional)*
  * [9. WiFeed – Captive Portal e Sincronização Diária de Vouchers](#9-wifeed--captive-portal-e-sincronização-diária-de-vouchers)
    * [9.1 Contexto Institucional e Problema Operacional do Captive Portal](#91-contexto-institucional-e-problema-operacional-do-captive-portal)
    * [9.2 Solução Automatizada Desenvolvida no AutoTickets](#92-solução-automatizada-desenvolvida-no-autotickets)
    * [9.3 Histórico Detalhado de Envios e Validações de Vouchers](#93-histórico-detalhado-de-envios-e-validações-de-vouchers)
  * [10. Fullcam – Videomonitoramento em Nuvem](#10-fullcam--videomonitoramento-em-nuvem)
    * [10.1 Diagnóstico Financeiro Executivo e Indicadores-Chave](#101-diagnóstico-financeiro-executivo-e-indicadores-chave)
    * [10.2 Tabela Completa de Auditoria de Contratos e Saldo Líquido na Íntegra](#102-tabela-completa-de-auditoria-de-contratos-e-saldo-líquido-na-íntegra)
    * [10.3 Painel Consolidado de Execução das Automações](#103-painel-consolidado-de-execução-das-automações)
    * [10.4 Ações Efetivas de Inadimplência e Instalações de Câmeras](#104-ações-efetivas-de-inadimplência-e-instalações-de-câmeras)
* [Parte III — Sistemas](#parte-iii--sistemas)
  * [11. AutoTickets – Plataforma de Automação e Integração](#11-autotickets--plataforma-de-automação-e-integração)
    * [11.1 Entregas da Semana](#111-entregas-da-semana)
    * [11.2 Evolução da Plataforma, IA e Governança](#112-evolução-da-plataforma-ia-e-governança)
    * [11.3 Impacto Operacional e Métricas de Produtividade das Automações](#113-impacto-operacional-e-métricas-de-produtividade-das-automações)
  * [12. Outros Sistemas Internos e Contratados](#12-outros-sistemas-internos-e-contratados)
    * [12.1 Painéis de BI com Parceiros](#121-painéis-de-bi-com-parceiros)
    * [12.2 Sistemas Internos e de Terceiros](#122-sistemas-internos-e-de-terceiros)
* [Encerramento](#encerramento)
  * [13. Pontos de Atenção e Próximas Ações](#13-pontos-de-atenção-e-próximas-ações)
    * [13.1 Riscos Tecnológicos e Vulnerabilidades Identificadas](#131-riscos-tecnológicos-e-vulnerabilidades-identificadas)
    * [13.2 Necessidades de Investimentos e Aquisições](#132-necessidades-de-investimentos-e-aquisições)
    * [13.3 Ações Planejadas para as Próximas Semanas](#133-ações-planejadas-para-as-próximas-semanas)

---

### 📝 4. Conteúdo Detalhado por Tópico

#### Resumo Executivo
Visão geral analítica da semana: síntese das principais entregas de engenharia de software e infraestrutura, quantitativo global de chamados e suportes a técnicos, principais conquistas e prioridades operacionais para a próxima semana.

- **Evolução em relação à semana anterior:** statcards ou tabela curta com os indicadores-chave da semana ao lado dos valores da semana anterior (citar como "relatório da semana NN"), sempre rotulados como "semana anterior".
- **Tópicos condicionais ausentes:** quando algum tópico condicional não tiver fonte, uma linha no fim do Resumo Executivo listando-os (ver "Classes de Tópicos").
- **Acompanhamento das observações da semana anterior:** quando existir `semanas/<anterior>/feedback.md`, incluir no fim do Resumo Executivo uma tabela com **todas** as observações (do Isvi e do Liomar): *Observação · Autor · Como foi tratada · Onde (tópico) · Status*. Esta tabela fica dentro do Resumo Executivo e **não** ganha entrada própria no índice.

#### 📈 Destaques Analíticos da Semana
Seção dinâmica obrigatória, logo após o Resumo Executivo. Responde "foi bom?", "para onde estamos apontando?" e "o que precisa mudar?" a partir dos **dados** (critérios em "Classes de Tópicos"). De **3 a 5 destaques**, cada um como `###` sem número cujo título é o próprio achado, contendo:
- **Evidência:** número(s) da semana com a fonte (nome descritivo do relatório, protocolo ou commit — nunca nome ou caminho de arquivo) e, quando houver, o valor da semana anterior rotulado.
- **Leitura:** o que o dado significa para a operação (bom, ruim, neutro, e por quê).
- **Recomendação:** ação concreta, responsável sugerido e onde será acompanhada (ex.: "13.3", "próximo relatório").
Se nenhum critério for atingido, declarar "Semana sem desvios relevantes nos indicadores" e citar os indicadores verificados.

#### ⭐ Fatos Notáveis e Anomalias da Semana
Seção obrigatória dedicada ao aprofundamento de ocorrências incomuns (incidentes, falhas, atrasos, desvios). Entregas normais não entram aqui (vão para os Tópicos 1.3, 3, 7 ou 11). Para cada fato notável identificado no período (desvio de planejamento, atraso de frota, falha física atípica, contestação indevida de cliente ou incidente de segurança):
- **Ocorrência e Ativos Envolvidos:** O que aconteceu, data e equipamentos/sistemas impactados.
- **Causa Raiz Técnica e Contexto:** Por que ocorreu e fatores determinantes.
- **Impacto Operacional:** Horas perdidas, retrabalho ou risco gerado.
- **Tratativa Aplicada:** Medida de contenção imediata ou definitiva.
- **Recomendação e Próximo Passo:** Ação estruturante recomendada para evitar repetição.

#### Parte I — O Setor de TI
Título `#` com uma frase de abertura; agrupa os tópicos 1 a 7.

#### 1. Gestão de Demandas
- **1.1 Demandas Pendentes:** Demandas paradas ou na fila aguardando início, informando ID/Protocolo, solicitante, prioridade técnica e data prevista.
- **1.2 Demandas em Andamento:** Atividades em execução, indicando responsável direto, percentual de avanço estimado, bloqueios técnicos ou dependências de terceiros e previsão de conclusão.
- **1.3 Demandas Concluídas:** Todas as entregas finalizadas na semana com detalhamento do resultado prático obtido. Demandas de rotina repetitiva de mesma natureza (ex.: análises periciais de desconto de fatura ou atribuições de IP público) podem ser sintetizadas com contagem total e amostragem de protocolos.
- **1.4 Demandas Novas:** Demandas abertas durante o período avaliado.
  - **1.4.1 Comparativo Entradas × Saídas (Balanço da Fila):** Análise quantitativa demonstrando se a fila de trabalho do setor está crescendo ou reduzindo (com statcards e balanço líquido). **PROIBIDO usar o termo "resolutividade".** A fonte primária de vazão deve ser respaldada por `fontes/autotickets/colaborador_x_ticket/` (saídas ÷ entradas do período, calculado sobre os dados da semana corrente).

#### 2. Registro de Atividades por Membro da Equipe
Para cada colaborador (**2.1 David Brasil Fernandes**, **2.2 Isac Costa Silva** e **2.3 Liomar Antonio de Oliveira**), detalhar:
- **Resumo das Atividades:** Narrativa aprofundada dos chamados, projetos e intervenções técnicas realizadas, integrando os dados de `fontes/voalle/[colaborador].*` enriquecidos pelos indicadores sintéticos de `fontes/autotickets/colaborador_x_ticket/` (total de ações, chamados atuados, TMA, TMR e resolubilidade).
- **Distribuição do Tempo:** Percentual de alocação entre frentes (Projetos, Suporte Interno, Suporte ao Campo, Infraestrutura e Rotinas Administrativas).
- **Desenvolvimento e Capacitação:** Dificuldades observadas, pontos fortes demonstrados e necessidades de treinamento identificadas.
- **2.4 Desempenho no Voalle e Confronto com Jornada Real (Pontomais):**
  - Tabela comparando Horas no Voalle x Horas no Pontomais.
  - Justificativa técnica obrigatória para divergências (cronômetros de tickets abertos, sobreposição de demandas em paralelo, deslocamentos ou atendimentos em intervalos).

#### 3. Projetos e Entregas do Setor
- **3.1 Projetos de Conectividade e Redes:** WireGuard, MikroTik, hardening e SIEM Wazuh. Justificar formalmente qualquer alteração de cronograma ou prioridade técnica (ex.: foco em RBs locais em vez de filiais) e registrar o novo prazo pactuado.
- **3.2 Telefonia Fixa e Comunicação Corporativa (Native PBX / ZEUS):** Diagnóstico de estabilidade, migrações de ramais e suporte telefônico corporativo.

#### 4. Suporte Interno (Informática)
- **4.1 Relação de Atendimentos e Chamados:** Análise dos atendimentos a usuários internos (estações de trabalho, acessos, e-mails, sistemas operacionais e periféricos), com tabela e detalhamento técnico.
- **4.2 Setores que mais Demandaram:** Ranking e gráfico visual dos departamentos mais demandantes.
- **4.3 Colaboradores Solicitantes Mais Frequentes:** Ranking nominal identificando setor e tipo de demanda.
- **4.4 Relatório de Visitas Técnicas Presenciais e Gestão de Veículos:** Detalhamento de deslocamentos operacionais, quilometragem, veículos utilizados e **avaliação da frota** (atrasos na liberação, impactos no cumprimento de cronogramas e tempo perdido). Justificar instalações de Windows 10 considerando o fim do suporte oficial.

#### 5. Suporte ao Técnico de Campo
- **5.1 Volumetria de Solicitações:** Quantidade total de apoios prestados via ServiceDesk e Voalle, reforçando a diretriz de abertura de protocolo formal para todo suporte com atuação em sistema ou análise.
- **5.2 Tipos de Apoio Mais Frequentes e Tempo Médio de Resposta:** Provisionamento de ONTs Datacom/Parks, manobras de CTO, consultas cadastrais, liberação de portas e trocas de estrutura. A soma da tabela de categorias deve corresponder exatamente ao total relatado.
- **5.3 Oportunidades de Automação e Capacitação:** Propostas de melhorias no AutoTickets ou capacitação para os técnicos reduzirem a dependência do TI.

#### 6. Infraestrutura, Incidentes e Backups
- **6.1 Incidentes Tratados:** Detalhamento de cada incidente ocorrido na semana:
  - Identificação, sistema afetado, severidade, data/hora e impacto.
  - Causa raiz técnica identificada e solução adotada (definitiva ou paliativa).
  - **Janela de Reincidência:** Adotar janela móvel de **30 dias de observação** antes de declarar ausência de reincidência.
- **6.2 Disponibilidade de Serviços e Incidentes em Sistemas:**
  - Sem ferramenta de monitoramento externo medindo o tempo fora do ar, declarar expressamente **"Sem indisponibilidade de rede registrada"**.
  - Registrar falhas funcionais (como bugs de sessão no Voalle) como **Ocorrências Operacionais de Sistemas**, sem distorcer o uptime de rede.
- **6.3 Execução e Validação de Backups:**
  - Apresentar o quadrante de governança: total de VMs/CTs na rotina, jobs executados x falhas na semana, falhas refeitas manualmente com justificativa e data do último teste de Disaster Recovery.
- **6.4 Atualizações, Melhorias e Ações de Modernização:** Aplicações de patches, manutenção física preventiva (ex.: Dell R910, nobreaks NHS) e estudos de segurança (integrar dados de `fontes/investigacoes/`).

#### 7. Iniciativas, Desafios e Conquistas da Semana
Tópicos detectados nas atividades da semana que merecem visibilidade além da rotina.
- **7.1 Conquistas e Resultados de Destaque:** resultados que se destacaram (problema evitado, entrega com impacto, meta atingida), com o protocolo e quem fez.
- **7.2 Desafios e Iniciativas do Setor:** gincanas e desafios propostos pela Coordenação, estudos e provas de conceito, iniciativas extras e desafios internos da equipe, com situação e próximo passo.

#### Parte II — A Empresa
Título `#` com uma frase de abertura dizendo que os dados vêm do AutoTickets, plataforma integradora desenvolvida por Liomar, consolidados a partir dos sistemas de origem (Voalle, Fullcam, WiFeed, NOC). Agrupa os tópicos 8 a 10.

#### 8. Indicadores da Empresa: ERP Voalle e Rede
- **8.1 Base de Clientes Adimplentes no ERP Voalle:** quantidade diária de clientes adimplentes em qualquer produto no Voalle, de toda a empresa, apurada pelo AutoTickets na automação de vouchers do WiFeed (fonte: Relatório de Vouchers WiFeed). Statcards com início, fim, variação líquida (absoluta e %), pico, mínimo e apurações diárias; gráfico SVG de área e linhas com a evolução diária e a tabela diária.
- **8.2 Reincidência de Problemas no Atendimento:** indicadores do relatório de Reincidência de Problemas (protocolos analisados, retornos, taxa, mediana até voltar, clientes reincidentes), taxa por tipo de protocolo e os casos que passaram pelo Setor de TI. Janela de retorno de até 60 dias.
- **8.3 Ocorrências Sistêmicas na Rede de Distribuição:** dias em que um tipo de protocolo atingiu muitos clientes acima da mediana diária (informação para NOC e Campo, não indisponibilidade do TI).
- **8.4 Anomalias de Tráfego PPPoE e Ações Proativas para o Service Desk** *(tópico condicional — ver "Classes de Tópicos"; fonte `fontes/autotickets/anomalias_pppoe/`)*. Objetivo: entregar ao Service Desk, com todos os dados necessários para localizar cada caso nos sistemas, a lista priorizada de clientes com comportamento anômalo **para investigação e ação proativa imediata**.
  - **Natureza da fonte:** é um **retrato atual**, gerado no dia da emissão do relatório consolidado, com problemas a serem tratados **agora**. **Não se aplica o recorte do período da semana**: informar apenas a data/hora do retrato (ex.: "retrato de 19/10/2026 22:07").
  - **Statcards:** total de anomalias, críticas, inversões de tráfego (upload > download), volume de upload × download e quantos casos já têm ticket/OS aberto (quando a fonte informar).
  - **Tabela completa, ordenada por razão Upload/Download (decrescente)**, com os dados de identificação: **cliente (nome), login PPPoE, contrato, CPF/CNPJ mascarado, cidade/bairro, POP/concentrador, IP, MAC, fabricante da CPE, plano**, sinal RX, upload/download, razão, throughput, quedas, severidade/score e **hipótese → ação proativa**. Até 30 casos na íntegra; acima disso, os 30 primeiros e a contagem do restante.
  - **Hipóteses e ações por perfil** (a confirmar pelo Service Desk, nunca afirmadas como fato):
    - razão muito alta (> 15x) com download baixo → CPE possivelmente comprometida (botnet/proxy residencial) → verificar a CPE, atualizar firmware, trocar senha e checar portas expostas;
    - upload alto e constante em sessão longa → DVR/câmeras, backup em nuvem ou servidor → confirmar o uso com o cliente e oferecer plano corporativo/IP fixo;
    - cliente que é provedor ou empresa de telecom → possível revenda → encaminhar ao Comercial;
    - contrato interno/cortesia → rotular como interno (manter na tabela, fora do ranking de prioridade);
    - muitas quedas (flapping), rajadas ou sinal óptico ruim (RX < −27 dBm ou −40 dBm/LOS) → problema físico → abrir OS de campo.
  - **Concentração por POP/concentrador** e **recorrência** (casos que já constavam no retrato do relatório anterior, quando houver).
  - **Encaminhamento:** fechar com a lista de ações sugeridas ao Service Desk e, no relatório seguinte, o desfecho dos casos encaminhados.
  - **Ressalvas de cálculo:** enquanto o AutoTickets não corrigir, declarar que o volume é acumulado por sessão (não "últimas 24h"), que o throughput pode estar inflado pelo número de quedas e que a severidade não segue uma regra única de score (`fontes/autotickets/anomalias_pppoe/_ANALISE_FONTE.md`).

#### 9. WiFeed – Captive Portal e Sincronização Diária de Vouchers
- **9.1 Contexto Institucional e Problema Operacional do Captive Portal:** Explicar a função do WiFeed como Captive Portal da Ten Internet para captura de leads e fidelização (rede "TEN_Wi-Fi"), diferenciando o fluxo de não-clientes (cadastro por celular) e clientes (validação via CPF do titular com base de vouchers). Detalhar o problema operacional anterior (geração e upload 100% manual de arquivos CSV de CPFs sanitizados, risco de sensação de "propaganda enganosa" para assinantes recentes e perda de tempo técnico do TI).
- **9.2 Solução Automatizada Desenvolvida no AutoTickets:** Descrever a arquitetura da automação: conexão direta ao banco Voalle, filtro exclusivo de clientes adimplentes em qualquer plano, sanitização estrita de CPFs/CNPJs, rotina agendada diária às 11h, exclusão do segmento antigo, upload do novo lote, paginação de integridade linha por linha e comutação segura para o segmento ativo.
- **9.3 Histórico Detalhado de Envios e Validações de Vouchers:** Tabela completa na íntegra registrando Data/Hora, Operador, Segmento, Base ERP, Vouchers Transmitidos, Taxa de Sucesso (100%), Status e Observações.

#### 10. Fullcam – Videomonitoramento em Nuvem
- **10.1 Diagnóstico Financeiro Executivo e Indicadores-Chave:** Síntese executiva com statcards do parque auditado: Total Faturado, Custo de Licenças Fullcam, Custo de Storage em Nuvem, Prejuízo com Equipamentos Perdidos e Saldo Líquido Consolidado. Análise crítica de risco comparando a quantidade de clientes com saldo negativo (contratos cancelados/bloqueados gerando custos residuais de licença/storage ou perda de hardware) contra os superavitários.
- **10.2 Tabela Completa de Auditoria de Contratos e Saldo Líquido na Íntegra:** Transcrição completa e sem omissões de todos os registros auditados em tabela compacta estilizada (Cliente, CPF/CNPJ **obrigatoriamente mascarado** no formato `***.456.789-**`, Contratos Voalle, Faturas Pagas, GB Consumido, Valor Faturado, Custo de Licenças, Custo de Storage, Equip. Perdido e Saldo Líquido). Aplicar cores semânticas (verde para saldos positivos, vermelho para negativos) e diagramação limpa para paginação A4.
- **10.3 Painel Consolidado de Execução das Automações:** statcards com as ações da semana (bloqueios, desbloqueios, instalações e câmeras), ações com sucesso e a forma de registro: a automação registra só as execuções em que agiu.
- **10.4 Ações Efetivas de Inadimplência e Instalações de Câmeras:** Tabela analítica estruturada destacando todos os eventos operacionais com impacto direto em clientes (ações de BLOCK, UNBLOCK e INSTALL, indicando ID, Data/Hora, Cliente, Contrato Voalle, Protocolo/OS, Quantidade de Câmeras e Status). Execuções sem pendência não geram registro e não devem ser tratadas como falha.

#### Parte III — Sistemas
Título `#` com uma frase de abertura; agrupa os tópicos 11 e 12.

#### 11. AutoTickets – Plataforma de Automação e Integração
**Confidencialidade (`AGENTS.md`, regra 9):** o AutoTickets é desenvolvimento interno. Texto genérico, humanizado e profissional, pelo valor para a operação; sem rotas, bibliotecas, frameworks, modelos de IA, comandos, linhas de código ou tipos de commit. Segurança sempre como **reforço** (firewall, análise de vulnerabilidades, proteção de integrações), nunca como exposição ou falha.
- **11.1 Entregas da Semana:** statcards (atualizações publicadas, ciclos de entrega concluídos, novos testes automatizados) e uma tabela por **frente de evolução** (ex.: segurança da plataforma, painel executivo, relatórios, módulos novos, desempenho): o que foi entregue, o valor para a operação e os hashes de commit só como referência.
- **11.2 Evolução da Plataforma, IA e Governança:** síntese em poucos itens do que muda para a empresa (segurança, IA local, confiabilidade dos dados, qualidade e publicação), sem detalhes de implementação.
- **11.3 Impacto Operacional e Métricas de Produtividade das Automações:**
  - Total consolidado de horas técnicas de esforço humano economizadas no período (rotinas diárias de vouchers WiFeed, auditorias automáticas Fullcam e esteira de provisionamento).

#### 12. Outros Sistemas Internos e Contratados
- **12.1 Painéis de BI com Parceiros:** Esclarecimento formal do status real de **Analítica 3M** (Perfil Master para gestão de usuários, escopo estratégico) e **EasyBI / MW Solutions** (fora do escopo direto, descontinuação contratual).
- **12.2 Sistemas Internos e de Terceiros:** tabela Sistema · Tipo (interno/contratado) · Situação na semana · Onde, para os sistemas citados no período (ex.: Compras, Mundiale History, Flashman, Slack, Native PBX/ZEUS, integrações bancárias), apontando para os tópicos com o detalhe.

#### Encerramento
Título `#` que antecede o tópico 13.

#### 13. Pontos de Atenção e Próximas Ações
- **13.1 Riscos Tecnológicos e Vulnerabilidades Identificadas:** Registro aprofundado de vulnerabilidades críticas, riscos de conformidade (LGPD, planos gratuitos de ferramentas) e segurança.
- **13.2 Necessidades de Investimentos e Aquisições:** Equipamentos, licenças, nobreaks senoidais e peças de reposição.
- **13.3 Ações Planejadas para as Próximas Semanas:** Roadmap de entregas e cronograma de prioridades com prazos alinhados.
