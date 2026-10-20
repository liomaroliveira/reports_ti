# Diretrizes do Projeto: Relatório Semanal do Setor de TI

> [!IMPORTANT]
> **Fonte única de regras** para todas as IAs. `GEMINI.md` (Antigravity) é um link simbólico para este arquivo e `CLAUDE.md` (Claude Code) o importa. Edite **somente** este arquivo.
>
> **Ao iniciar uma sessão:** leia o `PARAMETROS.md` da semana a gerar (status e pendências da semana) e `docs/pontos_a_melhorar.md` (backlog do harness e problemas conhecidos).

## 🏢 Contexto

- **Empresa:** Ten Soluções e Serviços LTDA. (Ten Provedor de Internet) — https://teninternet.com.br/
- **Coordenador de Tecnologia:** Isvi Neemias — recebe o relatório e o apresenta à Direção na Dashboard Executiva (terça-feira pela manhã).
- **Prazo de entrega:** toda segunda-feira até as 14h.

| Colaborador | Cargo | ID Voalle | Pasta/arquivo |
| :--- | :--- | :--- | :--- |
| Liomar Antonio de Oliveira | Analista de TI Sênior (automações, AutoTickets, consolidação dos relatórios) | #107184 | `liomar` |
| Isac Costa Silva | Assistente de TI Pleno (N2, infraestrutura, telefonia ZEUS) | #94562 | `isac` |
| David Brasil Fernandes | Auxiliar de TI Junior (suporte interno, presencial, hardware, Wazuh) | #116367 | `david` |

**Propósito do relatório (8 regras da Coordenação):** registrar fatos · apresentar resultados · analisar causas · dar visibilidade · apoiar decisões · acompanhar evolução · criar histórico · recomendar ações.

---

## 📁 Estrutura do Repositório

```text
reports_ti/
├── AGENTS.md                 # Este arquivo: regras permanentes (fonte única)
├── GEMINI.md -> AGENTS.md    # Antigravity
├── CLAUDE.md                 # Claude Code (importa AGENTS.md)
├── PROMPT.md                 # Comando curto de execução semanal
├── README.md                 # Guia para humanos
├── docs/
│   ├── fluxo_geracao.md          # Gatekeeper e etapas de geração (Fase 0 → Etapa 2)
│   ├── especificacao_relatorio.md# Tópicos, índice, moldura e diagramação do relatório
│   ├── regras_metricas.md        # Como calcular/declarar cada métrica (correções da Coordenação)
│   ├── fontes_de_dados.md        # O que cada fonte contém e quais tópicos alimenta
│   ├── classificacao_protocolos.md # Tarefa avulsa × Solicitação interna × externa
│   ├── glossario.md              # Termos e jargões da empresa
│   ├── licoes_aprendidas.md      # Consolidado dos feedbacks da Coordenação
│   ├── pontos_a_melhorar.md      # Backlog de melhorias do próprio harness
│   ├── formato_exportacao_autotickets.md # Pacote semanal único (JSON) proposto para o AutoTickets
│   └── referencias/              # Modelo oficial da Coordenação e documentos de contexto
├── semanas/
│   └── AAAA-MM-DD_AAAA-MM-DD/    # Uma pasta por semana (Domingo a Sábado)
│       ├── PARAMETROS.md         # Datas e focos da semana (único arquivo editado à mão)
│       ├── fontes/               # ENTRADAS da semana
│       │   ├── voalle/               # liomar.html | isac.pdf | david.csv ...
│       │   ├── autotickets/<modulo>/ # relatórios gerados pelo AutoTickets
│       │   ├── investigacoes/        # AAAA-MM-DD_<tema>/ (segurança, perícias)
│       │   └── **/_ANALISE_*.md      # feedback sobre a qualidade das exportações (NÃO é fonte; respeitar as ressalvas)
│       ├── individuais/          # liomar.* | isac.* | david.* — só quando pedido, ou enviados pelos colegas
│       ├── report_ti_AAAA-MM-DD_AAAA-MM-DD.{md,html,pdf}   # SAÍDA consolidada
│       ├── feedback.md           # Parecer do Isvi + observações do Liomar sobre o relatório desta semana (templates/feedback.md)
│       ├── _VERIFICAR_EQUIPE_TI.md    # O que a equipe precisa verificar durante a semana (não é fonte)
│       └── _PENDENCIAS_AUTOTICKETS.md # Problemas das exportações do AutoTickets a corrigir (não é fonte)
├── templates/                # report.css (visual oficial), report.html (esqueleto) e feedback.md (observações)
├── scripts/                  # nova_semana.sh, checar_entradas.py, md_para_html.py, renderizar_pdf.sh, validar_indice.py, validar_relatorio.py, mascarar_dados.py
├── .githooks/pre-commit      # Bloqueia CPF sem máscara, chaves e dados do WhatsApp
└── miscelaneous/             # FORA DO ESCOPO — não ler (conhecimento de extração do WhatsApp)
```

**Semana a gerar** = a pasta mais recente em `semanas/` cujo sábado já passou (pastas de semanas futuras são ignoradas), salvo se o usuário indicar outra. Leia sempre o `PARAMETROS.md` dela antes de qualquer geração.

> As duas primeiras semanas (`2026-09-01_2026-09-13` e `2026-09-28_2026-10-04`) são legadas e não seguem o padrão Domingo a Sábado; arquivos com período diferente do da pasta carregam o período original no nome (ex.: `isac_2026-09-28_2026-10-02.pdf`). Relatórios já entregues não são editados (exceto para mascarar dados pessoais).

---

## 🧭 Como gerar o relatório

Siga `docs/fluxo_geracao.md`: Fase 0 (`scripts/checar_entradas.py`) → Fase 1 (contexto da semana anterior: relatório consolidado e `feedback.md`) → relatório consolidado → individuais **somente se pedidos**. Estrutura e visual em `docs/especificacao_relatorio.md`; métricas em `docs/regras_metricas.md`; fontes em `docs/fontes_de_dados.md`; lições em `docs/licoes_aprendidas.md`.

- **Padrão:** gerar **somente o relatório semanal consolidado**. Relatórios individuais apenas quando o usuário pedir no prompt ou em `PARAMETROS.md` ("Relatórios individuais a gerar").

---

## ⚖️ Regras Invioláveis

1. **Nunca inventar dados.** Todo número e afirmação vem de evidência rastreável: protocolo Voalle (`#3183637`), hash de commit do AutoTickets ou um relatório de `fontes/`. **No texto do relatório, a fonte é citada pelo nome descritivo** (ex.: "Voalle — Tarefas Executadas, critério Lançamento", "AutoTickets — Colaborador × Ticket", "Auditoria Financeira Fullcam", "relatório da semana 41", "regra da Coordenação"), **nunca pelo nome ou caminho do arquivo** (`fontes/...`, `docs/...`, `_ANALISE_*.md`, `report_ti_*.md`, nome do repositório).
2. **Somente dados da semana corrente.** Nenhum valor de semanas anteriores pode ser reaproveitado como dado atual. Valores da semana anterior só aparecem como **comparação explícita** (rotulados "semana anterior", com a fonte). Se a fonte da semana não existir, registrar a ausência justificada.
3. **Ausência justificada:** subtópico sem demanda compatível recebe justificativa formal — nunca é omitido nem preenchido com atividade simulada.
4. **Sem distorções:** não alterar o sentido do que as equipes relataram.
5. **Consistência do índice:** toda entrada do índice existe no corpo com o mesmo título e âncora funcional (`scripts/validar_indice.py`).
6. **Multi-formato:** arquivos com o mesmo nome base em extensões diferentes (`.md`, `.html`, `.csv`, `.pdf`) são o mesmo relatório; tratar de forma unificada, observando só particularidades (SVG no HTML, colunas extras no CSV).
7. **Dados pessoais — uso interno:** o relatório e o repositório são de **uso interno da empresa**. Não há verificação automática de dados pessoais (nem no pre-commit, nem na Fase 0); o pre-commit bloqueia só chaves de API e dados do WhatsApp. No **relatório**: CPF/CNPJ mascarado (`***.456.789-**`) quando aparecer e senhas nunca transcritas; os demais dados de identificação (nome, login PPPoE, contrato, protocolo, IP, MAC, POP, endereço) **devem** aparecer quando forem necessários para que os setores localizem o caso. `scripts/mascarar_dados.py` fica disponível para uso manual e opcional.
8. **WhatsApp não é fonte de dados.** `miscelaneous/` não deve ser lido em nenhuma fase.
9. **AutoTickets é desenvolvimento interno e confidencial.** No relatório, descrever as entregas do AutoTickets de forma **genérica e profissional**, pelo valor para a operação (o que mudou para quem usa), sem detalhes de implementação: nada de nomes de rotas/endpoints, bibliotecas, frameworks, modelos de IA, classes, comandos, estrutura de testes, contagem de linhas ou tipos de commit. Hashes de commit podem aparecer só como referência. **Segurança do AutoTickets** é narrada como **reforço** (barreiras do firewall aprimoradas, análise de vulnerabilidades, proteção reforçada de integrações como o servidor MCP e os webhooks), nunca como exposição, falha ou vulnerabilidade da plataforma; o mesmo vale para riscos, incidentes e ações planejadas. Detalhes técnicos ficam no repositório do AutoTickets.

---

## ⏰ Datas e Nomes

- **Período oficial:** Domingo a Sábado. **Período operacional efetivo do TI:** Segunda a Sexta (descontar feriados).
- **Cabeçalho:** *Período Oficial:* `DD/MM/AAAA a DD/MM/AAAA (Semana XX / AAAA)` · *Período Operacional Efetivo:* `DD/MM/AAAA a DD/MM/AAAA (Segunda a Sexta)`.
- **Pasta da semana:** `semanas/[Domingo]_[Sábado]/` (ex.: `semanas/2026-10-11_2026-10-17/`), criada com `scripts/nova_semana.sh`.
- **Arquivos:** `fontes/voalle/<pessoa>.<ext>` · `individuais/<pessoa>.<ext>` · `report_ti_<Domingo>_<Sábado>.<ext>`.

---

## 🔄 Git

- Toda alteração no repositório deve ser commitada, com mensagens descritivas (ex.: `feat(report): gera relatorio semana 42 (2026-10-11 a 2026-10-17)`).
- Ativar o hook uma vez por clone: `git config core.hooksPath .githooks`. Não usar `--no-verify` para contornar bloqueio de dados sensíveis.
- O histórico foi reescrito e o repositório do GitHub recriado em 2026-10-19 para remover dados sensíveis: clones anteriores a essa data devem ser descartados (nunca fazer push, pull ou merge a partir deles).
