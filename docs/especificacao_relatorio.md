# 📐 Especificação do Relatório Semanal Consolidado

> Estrutura oficial (conteúdo exigido pelo modelo da Coordenação — ver `docs/referencias/modelo_relatorio_setor_ti.pdf`), diagramação, índice e conteúdo obrigatório por tópico.
> Regras de cálculo das métricas: `docs/regras_metricas.md`. Fluxo de geração: `docs/fluxo_geracao.md`.
> **CSS oficial:** `templates/report.css` (não reinventar o visual a cada semana). Esqueleto HTML: `templates/report.html`.
> **Estrutura em vigor desde a semana 43 (18 a 24/10/2026).** Relatórios até a semana 42 seguem a estrutura antiga e não são editados.

## Visão geral

| Bloco | Conteúdo | Leitor principal |
| :--- | :--- | :--- |
| **Capa-painel** (página 1) | Identificação, 📊 Painel da Semana (8 cards com farol e tendência + as 3 perguntas) e índice | Isvi → Dashboard Executiva |
| **Abertura** | Resumo Executivo (evolução e decisões solicitadas), 📈 Destaques Analíticos, ⭐ Fatos Notáveis | Coordenação |
| **Parte I — O Setor de TI** (1 a 6) | Somente os dados do setor: demandas, equipe, suporte interno, suporte ao campo, infraestrutura e projetos | Coordenação |
| **Parte II — Sistemas e Desenvolvimento** (7 a 10) | Sistemas que o TI desenvolve (AutoTickets e suas automações) e que sustenta (Voalle, Flashman, telefonia, Compras etc.), e a segurança da informação | Coordenação |
| **Parte III — A Empresa** (11 a 13) | Dados de interesse da empresa toda, consolidados pelo AutoTickets: base de clientes, qualidade do atendimento e da rede, PPPoE e o resultado da Fullcam | Coordenação, Direção e setores |
| **Encerramento** (14) | Riscos, investimentos, ações planejadas e o cumprimento das ações da semana anterior | Coordenação |
| **Anexos** (A a E) | Tabelas completas e notas metodológicas, para consulta | Quem precisa localizar o caso |

**Princípios:**

1. **Lugar canônico único.** Cada fato é detalhado em **um** lugar (tabela abaixo). Nos demais, aparece no máximo em uma linha com a remissão "(ver 5.1)". Nunca reescrever a mesma narrativa em vários tópicos.
2. **Corpo para decisão, anexo para consulta.** No corpo ficam a síntese, o top N e o que pede ação. Tabelas completas (Fullcam, PPPoE, logs das automações) vão para os Anexos.
3. **Recorte do TI na Parte I, dado geral na Parte III.** Exemplo: a reincidência geral fica no 12.1, e os casos que passaram pelo TI ficam no 4.3.
4. **Automação: a execução é do TI e o dado é da empresa.** Como a automação rodou (cargas, bloqueios, instalações) fica no 8. O que o dado diz sobre o negócio (base adimplente, saldo Fullcam) fica na Parte III.
5. **Metodologia fora do corpo.** Ressalvas das fontes, recálculos e divergências entre formatos do AutoTickets vão para o Anexo E. No corpo fica só o número oficial e, se mudar a leitura, uma frase com "(ver Anexo E)".
6. **Contexto estático não se repete.** Textos institucionais que não mudam (o que é o WiFeed, a arquitetura da automação, a situação dos BI sem atividade) ficam em `docs/referencias/` ou no glossário. O relatório traz uma linha.

### Lugar canônico de cada fato

| Fato | Detalhe completo em | Nos demais lugares |
| :--- | :--- | :--- |
| Ocorrência incomum (incidente, falha, desvio) | ⭐ Fatos Notáveis | Uma linha nas tabelas 5.1 ou 10.1 com "(ver ⭐ N)"; ação no 14.3 |
| Incidente de infraestrutura rotineiro | 5.1 | Ação no 14.3, se houver |
| Incidente ou alerta de segurança | 10.1 (ou ⭐, se incomum) | Risco em uma linha no 14.1 |
| Horas, apontamentos longos, Voalle × Pontomais | 2.4 | Destaque em 📈 só com evidência e recomendação, remetendo ao 2.4 |
| Atendimento de suporte interno | 3.1 | 1.3 agrupa: "Suporte interno (N atendimentos) — ver 3.1" |
| Apoio ao técnico de campo | 4.1/4.2 | 1.3 agrupa: "Apoio ao campo (N) — ver 4" |
| Projeto do setor (redes, monitoramento, telefonia) | 6 | 1.2 lista o protocolo com uma linha de situação |
| Entrega do AutoTickets | 7 | Uma linha no 2.3 (frente de trabalho de Liomar) |
| Execução de automação (WiFeed, Fullcam) | 8 | Parte III usa o dado, sem repetir a execução |
| Situação de sistema sustentado ou contratado | 9.1 | — |
| Compras, aquisições e requisições | 14.2 | 1.1 lista o protocolo pendente |
| Conquista de destaque | Painel/Resumo ou 📈 Destaques | Nada de seção própria de conquistas |

---

## 🎨 1. Capa-painel e bloco institucional

A página 1 é a **capa-painel**. Ela é pensada para Isvi levar direto à Dashboard Executiva de terça-feira.

* **Título principal:** Relatório Semanal Consolidado - Setor TI
* **Subtítulo:** O Setor de TI · Sistemas e Desenvolvimento · A Empresa
* **Bloco de Identificação Executiva** (tabela no `.md`, grade na capa):
  - **Período Analisado:** `[Domingo] a [Sábado] (Semana XX / AAAA)`
  - **Período Operacional Efetivo:** `[Segunda] a [Sexta] (Segunda a Sexta; feriados descontados)`
  - **Coordenador de TI:** `Isvi Neemias`
  - **Responsável pela Consolidação:** `Liomar Antonio de Oliveira (Analista de TI Sênior — ID #107184)`
  - **Equipe Integrada:** `Liomar Oliveira, Isac Costa Silva e David Brasil Fernandes`
* **`## 📊 Painel da Semana`**, antes do índice:
  - marcador `<!-- PAINEL: área | farol | valor | rótulo | detalhe | histórico ; … -->` com **8 cards**, um por área, nesta ordem:

    | Área | Indicador sugerido |
    | :--- | :--- |
    | Demandas | Balanço da fila (saídas ÷ entradas) |
    | Equipe | Horas no Voalle (critério Lançamento) e apontamentos longos |
    | Suporte | Atendimentos internos + apoios ao campo |
    | Infraestrutura | Incidentes da semana e situação dos backups |
    | Sistemas | Entregas do AutoTickets e ocorrências de sistemas |
    | Segurança | Alertas e incidentes de segurança abertos |
    | Empresa | Clientes adimplentes no ERP Voalle (fim do período) |
    | Fullcam | Saldo líquido |

  - **Farol** (verde, amarelo, vermelho ou neutro) sempre justificado pelo dado da semana. Critérios de referência:
    - Demandas: ≥ 100% verde, 90–99% amarelo, < 90% vermelho;
    - Segurança: alerta de criticidade alta sem tratativa = vermelho;
    - Infraestrutura: incidente sem causa ou backups sem fonte = amarelo;
    - na dúvida, **neutro**.
  - **Histórico:** os valores das semanas anteriores, **até 6**, seguidos do atual, separados por ` · `. Saem dos relatórios consolidados anteriores e só entram quando o método for o mesmo. Sem histórico comparável, deixar vazio.
  - **As 3 perguntas da Coordenação** em lista, uma ou duas linhas cada: **Foi boa?** · **Para onde estamos apontando?** · **O que precisa mudar?**
* **Índice** logo abaixo, em 2 níveis (seção 3).

## 📑 2. Paginação, diagramação e renderização PDF

0. **Ferramentas oficiais:**
   - o `.md` é a fonte única;
   - o HTML sai de `python3 scripts/md_para_html.py <arquivo.md>` (capa-painel, ids do índice, marcadores, chips de status, células sem quebra e tabela densa quando há CPF/CNPJ);
   - o PDF sai de `bash scripts/renderizar_pdf.sh <arquivo.html>` (embute `templates/report.css` e aplica `--no-pdf-header-footer`).
1. **Sem cabeçalho/rodapé do navegador** no PDF (`--no-pdf-header-footer`).
2. **Quebra de página só por grande seção.**
   - Página 1 = capa-painel; o Resumo Executivo abre a página 2; Destaques e Fatos Notáveis seguem corridos.
   - Cada `#` (Parte I, II, III, Encerramento, Anexos) começa em nova página. Os tópicos `##` seguem corridos, sem página meio vazia.
   - Títulos não ficam órfãos no pé da página, e linhas de tabela, cards e statcards não se partem.
   - **Meta: cerca de 15 a 18 páginas de corpo** mais os anexos.
3. **Recursos visuais:**
   - **Abertura de Parte:** frase de abertura e, quando houver dado, uma linha de 3 a 4 statcards da Parte.
   - **Statcards com cor semântica:** `verde` = bom, `amarelo` = atenção, `vermelho` = ruim, vazio = informativo. Não usar cor para identificar sistema ou pessoa.
   - **Gráficos** (marcadores ou SVG nativo):

     | Tópico | Gráfico | Como |
     | :--- | :--- | :--- |
     | 2 | Distribuição do tempo por pessoa e frente | `<!-- STACK -->` |
     | 3.2 | Setores que mais demandaram | `<!-- BARS -->` |
     | 11.1 | Evolução diária da base | SVG de área/linha |
     | 12.1 | Reincidência por tipo | `<!-- BARS -->` com a taxa |
     | 12.3 | Anomalias por POP | `<!-- BARS -->` |
     | 13.1 | Clientes com saldo positivo × negativo | `<!-- BARS -->` |

   - **Chips de status:** colunas `Status`, `Severidade`, `Criticidade` e `Prioridade` viram chips coloridos automaticamente. Escrever o status em texto, **sem emoji** (ex.: "Concluído", "Pendente — aguardando RH").
   - **Tabelas:** no máximo 6 ou 7 colunas no corpo. Tabelas mais largas vão para os Anexos.
   - **Emojis só nos títulos fixos** 📊, 📈 e ⭐. Nos demais títulos e no texto, não usar.

---

## ✍️ Estilo de escrita

- **Pessoas sem artigo:** "David atribui as falhas…", "Liomar registrou…", "Raimara confirmou no equipamento", "Isac apurou 995 quedas…". Nunca "o David", "a Raimara", "do Liomar" (usar "de Liomar", "por Isvi").
- **Base de clientes:** a base diária vem do **ERP Voalle** (clientes adimplentes em qualquer produto, de toda a empresa). O AutoTickets a apura na automação que atualiza os vouchers do WiFeed. Não chamar de "base WiFeed".
- **Automações Fullcam:** o relatório registra só as execuções em que a automação agiu (bloqueio, desbloqueio, instalação). Execução sem pendência não gera registro, e ausência de registro **não** significa que a automação parou.
- **Contexto antes de cobrar:** antes de apontar falta de registro ou desvio, conferir o último relato do protocolo (ex.: projeto aguardando equipamento) e o histórico do caso (ex.: configuração feita por terceiros antes de existir o setor).
- **Parte III:** abrir dizendo que os dados vêm do **AutoTickets**, plataforma integradora desenvolvida por Liomar, que consolida dados do Voalle, da Fullcam, do WiFeed e do NOC. Os números são dos sistemas de origem, consolidados por ele.

---

## 🧩 Classes de tópicos: fixos, condicionais e dinâmicos

O relatório **não é um formulário igual toda semana**: a estrutura tem uma espinha fixa (para comparação e histórico) e partes que mudam com os dados.

| Classe | Quais | Regra |
| :--- | :--- | :--- |
| **Fixos** | Painel da Semana, Resumo Executivo, as grandes seções, os tópicos 1 a 14 e seus subtópicos numerados (exceto os condicionais) e os Anexos A, B, D e E | Sempre presentes. Sem demanda na semana: **ausência justificada** em uma linha (nunca omitir, nunca simular). Anexo sem conteúdo: uma linha "Sem registros nesta semana". |
| **Condicionais** | **12.3** Anomalias PPPoE e **Anexo C** (fonte `fontes/autotickets/anomalias_pppoe/`); **11.2** Vendas e Cancelamentos (fonte do painel executivo do AutoTickets, quando exportada). Novos módulos do AutoTickets entram nesta classe ao serem criados. | Só existem no índice e no corpo **se houver fonte**. Sem fonte: não criar a seção e registrar em uma linha no fim do Resumo Executivo: *"Tópicos condicionais sem fonte nesta semana: 12.3 …"*. |
| **Dinâmicos** | **📈 Destaques Analíticos da Semana** e **⭐ Fatos Notáveis e Anomalias da Semana** | O **título de cada item é o próprio achado** (ex.: "Fila do TI cresceu 18% puxada por Patrimônio e Logística"). Quantidade e assunto dependem dos dados da semana. Os itens são `###` não numerados e **não entram no índice** (só a seção). |
| **Subtópicos livres** | Dentro de qualquer tópico fixo | Quando os dados revelarem um padrão relevante (concentração, outlier, recorrência), criar `####` **sem número** com o achado no título. Não entram no índice. |

**Como decidir o que vira tópico dinâmico** (critérios objetivos, aplicados às fontes da semana e à semana anterior):

1. Variação de indicador-chave ≥ 20% em relação à semana anterior (fila, volume por setor, horas, base de clientes adimplentes do Voalle, saldo Fullcam).
2. Picos e outliers: apontamento > 8h ou atravessando noite/fim de semana; tempo de atendimento absurdo; um setor ou solicitante concentrando > 30% da demanda.
3. Novos tipos de demanda, setores ou sistemas que não apareciam antes.
4. Recorrências: mesmo problema, cliente, equipamento ou POP em semanas consecutivas (janela de 30 dias para reincidência).
5. Desvios de plano: prazo, escopo ou prioridade diferente do registrado no relatório anterior.
6. Inconsistências relevantes nas próprias fontes que mudem a leitura de um indicador. Vira destaque só se mudar a decisão; o detalhe vai para o Anexo E.

**Onde encaixar:**
- padrão de dados ou indicadores → **📈 Destaques Analíticos**;
- ocorrência ou evento incomum (incidente, falha, atraso, desvio) → **⭐ Fatos Notáveis**;
- padrão restrito a um tema → **subtópico livre** dentro do tópico fixo correspondente.

**Entregas normais** (projetos concluídos, equipamentos instalados) vão para os tópicos 1.3, 6 ou 7, nunca para Fatos Notáveis.

---

## 📑 3. Índice geral de navegação (2 níveis, âncoras 100% funcionais)

O índice lista **só as grandes seções e os tópicos** (e os Anexos). Os subtópicos ficam só no corpo. **O título no corpo deve ser idêntico ao do índice** (sem parênteses ou complementos a mais, que mudam a âncora). Conferir com `python3 scripts/validar_indice.py`:

* [Resumo Executivo](#resumo-executivo)
* [📈 Destaques Analíticos da Semana](#-destaques-analíticos-da-semana)
* [⭐ Fatos Notáveis e Anomalias da Semana](#-fatos-notáveis-e-anomalias-da-semana)
* [Parte I — O Setor de TI](#parte-i--o-setor-de-ti)
  * [1. Gestão de Demandas](#1-gestão-de-demandas)
  * [2. Registro de Atividades por Membro da Equipe](#2-registro-de-atividades-por-membro-da-equipe)
  * [3. Suporte Interno (Informática)](#3-suporte-interno-informática)
  * [4. Suporte ao Técnico de Campo](#4-suporte-ao-técnico-de-campo)
  * [5. Infraestrutura, Incidentes e Backups](#5-infraestrutura-incidentes-e-backups)
  * [6. Projetos e Iniciativas do Setor](#6-projetos-e-iniciativas-do-setor)
* [Parte II — Sistemas e Desenvolvimento](#parte-ii--sistemas-e-desenvolvimento)
  * [7. AutoTickets – Desenvolvimento da Plataforma](#7-autotickets--desenvolvimento-da-plataforma)
  * [8. Automações Operadas pelo TI](#8-automações-operadas-pelo-ti)
  * [9. Sistemas Sustentados e Contratados](#9-sistemas-sustentados-e-contratados)
  * [10. Segurança da Informação](#10-segurança-da-informação)
* [Parte III — A Empresa](#parte-iii--a-empresa)
  * [11. Base de Clientes no ERP Voalle](#11-base-de-clientes-no-erp-voalle)
  * [12. Qualidade do Atendimento e da Rede](#12-qualidade-do-atendimento-e-da-rede)
  * [13. Fullcam – Resultado do Negócio](#13-fullcam--resultado-do-negócio)
* [Encerramento](#encerramento)
  * [14. Pontos de Atenção e Próximas Ações](#14-pontos-de-atenção-e-próximas-ações)
* [Anexos](#anexos)
  * [Anexo A — Acompanhamento das Observações da Semana Anterior](#anexo-a--acompanhamento-das-observações-da-semana-anterior)
  * [Anexo B — Auditoria Financeira Fullcam Completa](#anexo-b--auditoria-financeira-fullcam-completa)
  * [Anexo C — Anomalias PPPoE: Lista Completa](#anexo-c--anomalias-pppoe-lista-completa) *(condicional)*
  * [Anexo D — Registros das Automações](#anexo-d--registros-das-automações)
  * [Anexo E — Notas Metodológicas e Qualidade das Fontes](#anexo-e--notas-metodológicas-e-qualidade-das-fontes)

---

## 📝 4. Conteúdo detalhado por tópico

### 📊 Painel da Semana
Ver seção 1. Nada de texto corrido além das 3 perguntas.

### Resumo Executivo
No máximo uma página. Não repete as 3 perguntas do painel.
- **Evolução em relação à semana anterior:** tabela curta com os indicadores-chave da semana ao lado dos valores da semana anterior (citar como "relatório da semana NN"), sempre rotulados "semana anterior".
- **Decisões solicitadas à Coordenação:** tabela *Decisão · Contexto · Opções / valor · Prazo · Onde*. Exemplos: aprovar uma compra, escolher entre alternativas, definir um plano, autorizar um acesso. Sem decisão pendente: "Nenhuma decisão pendente nesta semana". É o que atende à função "apoiar decisões".
- **Tópicos condicionais ausentes:** uma linha no fim (ver "Classes de Tópicos").

### 📈 Destaques Analíticos da Semana
Seção dinâmica obrigatória. Responde "foi bom?", "para onde estamos apontando?" e "o que precisa mudar?" a partir dos **dados** (critérios em "Classes de Tópicos"). De **3 a 5 destaques**, cada um como `###` sem número cujo título é o próprio achado:
- **Evidência:** número(s) da semana com a fonte (nome descritivo do relatório, protocolo ou commit, nunca nome ou caminho de arquivo) e, quando houver, o valor da semana anterior rotulado.
- **Leitura:** o que o dado significa para a operação (bom, ruim, neutro, e por quê).
- **Recomendação:** ação concreta, responsável sugerido e onde será acompanhada.
Se nenhum critério for atingido, declarar "Semana sem desvios relevantes nos indicadores" e citar os indicadores verificados.

### ⭐ Fatos Notáveis e Anomalias da Semana
Lugar canônico das ocorrências incomuns: incidentes, falhas físicas atípicas, atrasos, desvios, contestação indevida de cliente e incidentes de segurança. Entregas normais não entram aqui. Para cada fato:
- **Ocorrência e Ativos Envolvidos:** o que aconteceu, a data e os equipamentos ou sistemas impactados.
- **Causa Raiz Técnica e Contexto:** por que ocorreu e os fatores determinantes.
- **Impacto Operacional:** horas perdidas, retrabalho ou risco gerado.
- **Tratativa Aplicada:** medida de contenção imediata ou definitiva.
- **Recomendação e Próximo Passo:** ação estruturante para evitar repetição.

---

### Parte I — O Setor de TI
Título `#` com uma frase de abertura e, se houver dado, statcards da Parte. Somente dados do setor. Agrupa os tópicos 1 a 6.

#### 1. Gestão de Demandas
- **1.1 Demandas Pendentes:** paradas ou aguardando início: protocolo, solicitante/setor, responsável, prioridade, motivo da espera e previsão. Fechar com o **desfecho** das pendências do relatório anterior.
- **1.2 Demandas em Andamento:** responsável, avanço, bloqueios e previsão. Para projetos, só uma linha de situação com a remissão ao 6.
- **1.3 Demandas Concluídas:** entregas finalizadas e o resultado prático.
  - Rotinas repetitivas (perícias de desconto, IP público) ficam numa linha agrupada com a quantidade.
  - Suporte interno e apoio ao campo também ficam agrupados, com a remissão ao 3 e ao 4.
- **1.4 Demandas Novas e Balanço da Fila:**
  - entradas (por tipo), saídas e variação do backlog;
  - statcards e balanço líquido (**saídas ÷ entradas**, por protocolo único, a partir de `fontes/autotickets/colaborador_x_ticket/`);
  - **PROIBIDO usar o termo "resolutividade".**

  Divergência entre o recálculo e o indicador do AutoTickets: uma frase no corpo e o detalhe no Anexo E.
- **1.5 Dependências de Terceiros e de Outros Setores:** tabela única *Protocolo · Depende de · O quê · Desde · Impacto*. Exemplos: Compras, RH, manutenção, fornecedor, outro setor. Atende ao modelo da Coordenação: "dependências que estejam travando entregas".

#### 2. Registro de Atividades por Membro da Equipe
Abrir com:
- a tabela-síntese por colaborador: tarefas e apontamentos (Voalle), HT (Lançamento), atuadas, ações, TMA, TMR e % concluídas (AutoTickets);
- o gráfico `<!-- STACK -->` da distribuição do tempo por frente: Projetos, Suporte Interno, Suporte ao Campo, Infraestrutura e Rotinas Administrativas.

Para cada colaborador (**2.1 David Brasil Fernandes**, **2.2 Isac Costa Silva** e **2.3 Liomar Antonio de Oliveira**), em parágrafos com rótulo em negrito (sem subtópicos numerados):
- **Atividades por frente:** horas e protocolos de cada frente, em uma ou duas linhas por frente. Não reescrever o detalhe que já está em 1.3, 3, 4, 6 ou 7.
- **Desenvolvimento e capacitação:** pontos fortes, pontos de atenção e necessidade de treinamento.

**2.4 Desempenho no Voalle e Confronto com Jornada Real (Pontomais):**
- tabela Horas no Voalle × Pontomais;
- lista dos apontamentos longos (> 8h ou atravessando noite, fim de semana ou feriado), com a justificativa ou o encaminhamento;
- é o lugar canônico do tema.

#### 3. Suporte Interno (Informática)
- **3.1 Atendimentos da Semana:** tabela *Protocolo/registro · Solicitante · Setor · Atendimento · Responsável · Status*.
- **3.2 Setores e Solicitantes que mais Demandaram:**
  - ranking por setor com `<!-- BARS -->`;
  - solicitantes só quando alguém concentrar ≥ 3 atendimentos ou > 30%. Se não, declarar "sem concentração por solicitante".
- **3.3 Tempo de Atendimento e Pendências:** tempo médio de atendimento do suporte interno (modelo da Coordenação 2.5) e os atendimentos em aberto com previsão. Sem fonte de tempo: declarar.
- **3.4 Visitas Presenciais, Frota e Estações:**
  - deslocamentos (data, quem, destino, motivo, veículo);
  - **avaliação da frota**: horário combinado × liberado e o impacto;
  - padrão **Windows 10 × 11** nas formatações, com a justificativa de cada Windows 10 e a situação das licenças.

#### 4. Suporte ao Técnico de Campo
- **4.1 Volumetria de Solicitações (Com e Sem Protocolo):**
  - total de apoios, com e sem protocolo;
  - reforçar a diretriz de protocolo formal para todo suporte com atuação em sistema ou análise;
  - perícias e IP público não entram aqui (estão no 1.3).
- **4.2 Tipos de Apoio e Tempo de Resposta:**
  - exemplos: provisionamento de ONTs, configuração de equipamentos de cliente, manobras de CTO, consultas cadastrais, liberações;
  - a soma da tabela deve bater exatamente com o total do 4.1;
  - tempo de resposta quando a fonte trouxer; se não trouxer, o tempo de resolução declarado como tal.
- **4.3 Reincidências com Envolvimento do TI:** recorte do relatório de Reincidência de Problemas: os protocolos que voltaram e passaram pelo TI (cliente, protocolo de origem → retorno, intervalo, situação). A reincidência geral fica no 12.1.
- **4.4 Oportunidades de Automação e Redução de Dependência:** propostas de melhoria no AutoTickets ou de capacitação para os técnicos dependerem menos do TI.

#### 5. Infraestrutura, Incidentes e Backups
- **5.1 Incidentes Tratados e Recorrentes:**
  - tabela *ID · Ativo · Severidade · Data/hora · Impacto · Causa raiz · Solução (definitiva/paliativa) · Reincidência (janela de 30 dias)*;
  - incidente detalhado em ⭐ entra com uma linha e a remissão;
  - incidentes de **sistemas e de segurança** ficam no 9.1 e no 10.1;
  - fechar com os **incidentes recorrentes e o plano para eliminar a recorrência** (modelo da Coordenação 2.4).
- **5.2 Disponibilidade da Rede, Links e Servidores:**
  - sem ferramenta que meça o tempo fora do ar, declarar expressamente **"Sem indisponibilidade de rede registrada"**;
  - com Zabbix/Grafana ou outra fonte de medição, informar a disponibilidade e a duração das quedas por link e por servidor, com a fonte.
- **5.3 Capacidade dos Servidores:** armazenamento, memória e processamento dos servidores e hosts de virtualização, com os alertas de esgotamento (modelo da Coordenação 2.7). Sem fonte, ausência justificada. Fonte prevista: Zabbix/Grafana ou exportação do Proxmox.
- **5.4 Execução e Validação de Backups:** o quadrante de governança:
  - total de VMs/CTs na rotina;
  - jobs executados × falhas;
  - falhas refeitas manualmente, com a causa;
  - data do último teste de restauração.

  Sem fonte: os 4 pilares "sem fonte", nunca estimados.
- **5.5 Manutenção e Modernização:** patches, manutenção física preventiva (climatização, nobreaks, Dell R910) e ações de modernização (cluster, SSDs, balanceamento, migração de VMs).

#### 6. Projetos e Iniciativas do Setor
- **6.1 Conectividade, Redes e Monitoramento:** WireGuard/VPN, Wazuh, padronização MikroTik, TACACS+, Zabbix/Grafana e energia de reserva. Justificar qualquer mudança de cronograma ou prioridade e registrar o novo prazo.
- **6.2 Telefonia Fixa e Comunicação Corporativa:** Native PBX e ZEUS (prioridade da Coordenação), Slack (operação e contas) e ChatSeguro. Diagnóstico, migrações de ramais e suporte telefônico.
- **6.3 Iniciativas, Estudos e Desafios da Equipe:** gincanas e desafios da Coordenação, estudos e provas de conceito, e iniciativas extras, com a situação e o próximo passo. O resultado de testes de segurança vai para o 10.2.

---

### Parte II — Sistemas e Desenvolvimento
Título `#` com uma frase de abertura. Trata dos sistemas que o TI **desenvolve** (AutoTickets e suas automações) e que **sustenta ou contrata**, e da segurança da informação. Agrupa os tópicos 7 a 10.

#### 7. AutoTickets – Desenvolvimento da Plataforma
**Confidencialidade (`AGENTS.md`, regra 9):**
- o AutoTickets é desenvolvimento interno;
- texto genérico, humanizado e profissional, pelo valor para a operação;
- sem rotas, bibliotecas, frameworks, modelos de IA, comandos, linhas de código ou tipos de commit;
- segurança sempre como **reforço**, nunca como exposição ou falha.

Subtópicos:
- **7.1 Entregas da Semana:** statcards (atualizações publicadas, ciclos de entrega concluídos, novos testes) e a tabela por **frente de evolução**: o que foi entregue, o valor para a operação e os hashes de commit só como referência.
- **7.2 Evolução da Plataforma, IA e Governança:** síntese em poucos itens do que muda para a empresa.
- **7.3 Impacto Operacional das Automações:**
  - horas de esforço humano economizadas **só com fonte** (relatório Produtividade Geral e tempos manuais de referência validados pela Coordenação);
  - sem fonte: ausência justificada e o volume executado (remissão ao 8).

#### 8. Automações Operadas pelo TI
Lugar canônico da **execução** das automações. O que os dados dizem sobre o negócio fica na Parte III.
- **8.1 Sincronização Diária de Vouchers WiFeed:**
  - uma linha de contexto (o detalhe fica em `docs/referencias/wifeed_contexto.md`);
  - statcards: cargas na semana, vouchers transmitidos e taxa de validação;
  - falhas ou divergências, se houver;
  - o log completo vai para o Anexo D.
- **8.2 Automações Fullcam: Inadimplência e Instalação:**
  - statcards de bloqueios, desbloqueios, instalações, câmeras afetadas e ações com sucesso;
  - os casos que pedem atenção (ex.: ciclo repetido de bloqueio e desbloqueio);
  - a tabela completa vai para o Anexo D;
  - execuções sem pendência não geram registro e não são falha.
- **8.3 Ocorrências das Automações:** avisos repetidos, itens travados ou divergências que pedem correção de cadastro ou do sistema, com severidade e situação.

#### 9. Sistemas Sustentados e Contratados
- **9.1 Situação dos Sistemas na Semana:**
  - tabela *Sistema · Tipo (interno/contratado) · Situação na semana · Disponibilidade/ocorrências · Onde*;
  - exemplos: Voalle, Flashman, Native PBX/ZEUS, Slack, Compras, Mundiale History, integrações bancárias e Bemobi, MailCow;
  - falhas funcionais (ex.: sessão do Voalle) entram como **Ocorrências Operacionais de Sistemas**, sem distorcer o uptime de rede;
  - incluir o andamento de integrações citadas no modelo da Coordenação (ex.: Voalle × Flashman) quando houver registro.
- **9.2 Painéis de BI com Parceiros:** Analítica 3M e EasyBI (MW Solutions). Sem atividade, uma linha: "Sem atividade; situação inalterada (ver `docs/regras_metricas.md` §9)". Citar no relatório a situação, não o arquivo.

#### 10. Segurança da Informação
Lugar canônico de segurança. Os riscos vão em uma linha para o 14.1.
- **10.1 Incidentes e Alertas de Segurança:** tabela *Protocolo · Sistema · Criticidade · Data · Situação · Próximo passo*. Inclui incidentes em sistemas internos, alertas externos sobre fornecedores e tentativas bloqueadas relevantes. Incidente detalhado em ⭐ entra com uma linha e a remissão.
- **10.2 Testes, Estudos e Reforços:**
  - gincanas de pentest: o resumo no semanal e o relatório completo à parte;
  - investigações (`fontes/investigacoes/`);
  - reforços aplicados nos sistemas, inclusive o AutoTickets, narrado como reforço (regra 9).
- **10.3 Conformidade e Dados Pessoais (LGPD):** retenção e armazenamento (ex.: histórico do Slack), credenciais registradas em relatos, acessos e MFA. Pendências com a marca ⚠️ até serem concluídas.

---

### Parte III — A Empresa
Título `#` com a frase de abertura sobre o AutoTickets como integrador (ver "Estilo de escrita") e os statcards da Parte. Dados de interesse da empresa toda, que o TI consolida. Agrupa os tópicos 11 a 13.

#### 11. Base de Clientes no ERP Voalle
- **11.1 Clientes Adimplentes no ERP Voalle:**
  - quantidade diária de clientes adimplentes em qualquer produto, apurada pelo AutoTickets na automação de vouchers do WiFeed;
  - statcards: início, fim, variação líquida (absoluta e %), pico e mínimo;
  - SVG de área/linha com a evolução diária e a tabela diária.
- **11.2 Vendas e Cancelamentos** *(condicional)*: novas adesões, cancelamentos e adições líquidas por categoria, do painel executivo do AutoTickets, quando exportado.

#### 12. Qualidade do Atendimento e da Rede
- **12.1 Reincidência de Problemas no Atendimento:**
  - statcards: protocolos analisados, retornos, taxa, mediana até voltar e clientes reincidentes;
  - taxa por tipo de protocolo (`<!-- BARS -->` ou tabela) e por cidade/POP quando a fonte trouxer;
  - janela de retorno de até 60 dias;
  - os casos do TI ficam no 4.3.
- **12.2 Ocorrências Sistêmicas na Rede de Distribuição:** dias em que um tipo de protocolo atingiu muitos clientes acima da mediana diária. É informação para o NOC e o Campo, não indisponibilidade do TI.
- **12.3 Anomalias de Tráfego PPPoE para o Service Desk** *(condicional; fonte `fontes/autotickets/anomalias_pppoe/`)*. Entrega ao Service Desk a lista priorizada de clientes com comportamento anômalo, **para ação proativa imediata**.
  - **Natureza da fonte:** **retrato atual**, gerado no dia da emissão. **Não se aplica o recorte da semana**: informar só a data e hora do retrato.
  - **Statcards:** total de anomalias, críticas, inversões de tráfego, volume de upload × download e casos com ticket/OS aberto (quando a fonte informar).
  - **No corpo:** os casos **agrupados por ação sugerida**, com cliente, login, POP e o indicador que justifica, e a concentração por POP (`<!-- BARS -->`). As hipóteses abaixo são a confirmar pelo Service Desk, nunca afirmadas como fato:

    | Perfil | Hipótese | Ação |
    | :--- | :--- | :--- |
    | Razão > 15x com download baixo | CPE possivelmente comprometida | Verificar a CPE, atualizar o firmware, trocar a senha e checar portas |
    | Upload alto e constante | DVR, câmeras, backup ou servidor | Confirmar o uso e oferecer plano corporativo/IP fixo |
    | Provedor ou empresa de telecom | Possível revenda | Encaminhar ao Comercial |
    | Contrato interno ou cortesia | — | Rotular como interno, fora do ranking |
    | Muitas quedas ou RX ruim (< −27 dBm ou −40 dBm/LOS) | Problema físico | Abrir OS de campo |

  - **Recorrência:** marcar os casos que já constavam no retrato anterior.
  - **Desfecho:** no relatório seguinte, os casos encaminhados voltam com o ticket/OS e o resultado.
  - **Tabela completa** com os dados de identificação no **Anexo C**. Ressalvas de cálculo no Anexo E.

#### 13. Fullcam – Resultado do Negócio
- **13.1 Diagnóstico Financeiro e Indicadores-Chave:**
  - statcards: total faturado, licenças, storage, equipamentos perdidos e saldo líquido;
  - clientes com saldo positivo × negativo (`<!-- BARS -->`) e clientes sem fatura paga;
  - quando houver dado: **ROI e payback** (custo do equipamento e da instalação × receita);
  - análise de risco e recomendação ao Comercial e ao Financeiro;
  - recalculado a partir do CSV, com os registros excluídos por regra (`docs/regras_metricas.md` §11).
- **13.2 Clientes de Maior e Menor Saldo:** os 5 maiores e os 5 menores saldos e os casos que pedem ação (equipamento perdido, contrato sem fatura com consumo). A tabela completa fica no **Anexo B**.

---

### Encerramento
Título `#` que antecede o tópico 14.

#### 14. Pontos de Atenção e Próximas Ações
- **14.1 Riscos Tecnológicos e Vulnerabilidades:** tabela *Risco · Evidência · Criticidade · Mitigação · Responsável*, uma linha por risco, com remissão ao tópico canônico.
- **14.2 Necessidades de Investimentos e Aquisições:** equipamentos, licenças e peças, com quantidade, destino e protocolo. Itens que dependem de aprovação também entram em "Decisões solicitadas" no Resumo.
- **14.3 Ações Planejadas para as Próximas Semanas:** *Ação · Responsável · Prazo · Origem*.
- **14.4 Cumprimento das Ações da Semana Anterior:**
  - linha-resumo "X de Y ações concluídas no prazo";
  - tabela das ações do 14.3 anterior (ou do 13.3, até a semana 42) que **não** foram concluídas, com a situação e o novo prazo.

---

### Anexos
Título `#` (renderizado em tom neutro e fonte menor). Material de consulta; o corpo não depende dele para ser entendido.
- **Anexo A — Acompanhamento das Observações da Semana Anterior:** quando existir `semanas/<anterior>/feedback.md`, a tabela com **todas** as observações (de Isvi, Liomar e equipe): *Observação · Autor · Como foi tratada · Onde (tópico) · Status*. Sem feedback: "Sem observações registradas sobre o relatório anterior".
- **Anexo B — Auditoria Financeira Fullcam Completa:**
  - transcrição completa de todos os registros auditados: Cliente, CPF/CNPJ **mascarado** (`***.456.789-**`), Contratos, Faturas Pagas, GB, Faturado, Licenças, Storage, Equip. Perdido e Saldo;
  - cores semânticas (verde para positivo, vermelho para negativo).
- **Anexo C — Anomalias PPPoE: Lista Completa** *(condicional, com o 12.3)*:
  - tabela ordenada pela razão Upload/Download (decrescente);
  - colunas: cliente, login PPPoE, contrato, CPF/CNPJ mascarado, cidade/bairro, POP, IP, MAC, CPE, plano, RX, upload/download, razão, throughput, quedas, severidade e hipótese → ação;
  - até 30 casos na íntegra; acima disso, os 30 primeiros e a contagem do restante.
- **Anexo D — Registros das Automações:**
  - log das cargas do WiFeed: data/hora, operador, segmento, base ERP, vouchers, taxa e status;
  - ações Fullcam: ID, data/hora, cliente, contrato, protocolo/OS, ação, câmeras e status.
- **Anexo E — Notas Metodológicas e Qualidade das Fontes:**
  - convenções da semana (critério Lançamento do Voalle, recálculos por protocolo único, registros excluídos);
  - ressalvas de cada fonte que afetaram números (divergências entre formatos, totais que não fecham, campos não confiáveis);
  - fontes ausentes na semana;
  - correções de relatórios anteriores.

  Sempre pelo nome descritivo da fonte, nunca pelo caminho do arquivo.
