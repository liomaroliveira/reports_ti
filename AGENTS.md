# Diretrizes do Projeto: Relatório Semanal do Setor de TI

> [!IMPORTANT]
> **Fonte única de regras** para todas as IAs. `GEMINI.md` (Antigravity) é um link simbólico para este arquivo e `CLAUDE.md` (Claude Code) o importa. Edite **somente** este arquivo.

> [!WARNING]
> **Trabalho em andamento:** leia [`CONTINUIDADE.md`](CONTINUIDADE.md) no início da sessão — lista o que já foi feito, as decisões tomadas e as pendências. Quando estiver tudo concluído, apague o arquivo e este aviso.

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
│   └── referencias/              # Modelo oficial da Coordenação e documentos de contexto
├── semanas/
│   └── AAAA-MM-DD_AAAA-MM-DD/    # Uma pasta por semana (Domingo a Sábado)
│       ├── PARAMETROS.md         # Datas e focos da semana (único arquivo editado à mão)
│       ├── fontes/               # ENTRADAS da semana
│       │   ├── voalle/               # liomar.html | isac.pdf | david.csv ...
│       │   ├── autotickets/<modulo>/ # relatórios gerados pelo AutoTickets
│       │   └── investigacoes/        # AAAA-MM-DD_<tema>/ (segurança, perícias)
│       ├── individuais/          # liomar.* | isac.* | david.*  (md/html/pdf)
│       ├── report_ti_AAAA-MM-DD_AAAA-MM-DD.{md,html,pdf}   # SAÍDA consolidada
│       └── feedback.md           # Parecer da Coordenação sobre o relatório desta semana
├── templates/                # report.css (visual oficial) e report.html (esqueleto)
├── scripts/                  # nova_semana.sh, checar_entradas.py, renderizar_pdf.sh, validar_indice.py, mascarar_dados.py
├── .githooks/pre-commit      # Bloqueia CPF sem máscara, chaves e dados do WhatsApp
└── miscelaneous/             # FORA DO ESCOPO — não ler (conhecimento de extração do WhatsApp)
```

**Semana corrente** = a pasta mais recente em `semanas/` (ordem alfabética). Leia sempre o `PARAMETROS.md` dela antes de qualquer geração.

> As duas primeiras semanas (`2026-09-01_2026-09-13` e `2026-09-28_2026-10-04`) são legadas e não seguem o padrão Domingo a Sábado; arquivos com período diferente do da pasta carregam o período original no nome (ex.: `isac_2026-09-28_2026-10-02.pdf`).

---

## 🧭 Como gerar o relatório

Siga `docs/fluxo_geracao.md` (Fase 0 com `scripts/checar_entradas.py`, Etapa 1 individual, Fase 1.5 colegas, Etapa 2 consolidado). Estrutura e visual em `docs/especificacao_relatorio.md`; métricas em `docs/regras_metricas.md`; fontes em `docs/fontes_de_dados.md`. Leia também `docs/licoes_aprendidas.md` e o `feedback.md` da semana anterior.

---

## ⚖️ Regras Invioláveis

1. **Nunca inventar dados.** Todo número e afirmação vem de evidência rastreável: protocolo Voalle (`#3183637`), hash de commit do `autotickets-v2`, ou caminho do relatório em `fontes/`.
2. **Somente dados da semana corrente.** Nenhum valor de semanas anteriores pode ser reaproveitado. Se a fonte da semana não existir, registrar a ausência justificada.
3. **Ausência justificada:** subtópico sem demanda compatível recebe justificativa formal — nunca é omitido nem preenchido com atividade simulada.
4. **Sem distorções:** não alterar o sentido do que as equipes relataram.
5. **Consistência do índice:** toda entrada do índice existe no corpo com o mesmo título e âncora funcional (`scripts/validar_indice.py`).
6. **Multi-formato:** arquivos com o mesmo nome base em extensões diferentes (`.md`, `.html`, `.csv`, `.pdf`) são o mesmo relatório; tratar de forma unificada, observando só particularidades (SVG no HTML, colunas extras no CSV).
7. **Proteção de dados (LGPD):** CPF, telefones, senhas e chaves de API nunca em arquivos versionados. CPFs de clientes sempre mascarados (`***.456.789-**`) — rodar `python3 scripts/mascarar_dados.py <arquivos>` nas exportações brutas antes do commit. O repositório tem remote no GitHub.
8. **WhatsApp não é fonte de dados.** `miscelaneous/` não deve ser lido em nenhuma fase.

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
- O histórico foi reescrito em 2026-10-19 para remover dados sensíveis: clones anteriores a essa data devem ser descartados (não fazer merge/pull deles).
