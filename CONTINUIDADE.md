# 🔁 Continuidade — o que falta concluir

> Arquivo de passagem de contexto (criado em 2026-10-19) para continuar o trabalho em outro PC ou em outra sessão de IA.
> **IA:** leia este arquivo no início da sessão, junto com `AGENTS.md`. **Quando todos os itens estiverem concluídos, apague este arquivo e a referência a ele no `AGENTS.md`.**

---

## 1. O que já foi feito (não refazer)

| Etapa | Resultado | Commit |
| :--- | :--- | :--- |
| Diagnóstico do harness | Regras duplicadas e divergentes, números da semana 41 fixos nas regras, períodos fora do padrão, dados sensíveis no Git | — |
| Passo 1 — harness | Parâmetros semanais separados, números fixos removidos, CPF/telefones da equipe removidos, `CLAUDE.md`, hook `pre-commit`, `scripts/mascarar_dados.py`, WhatsApp reclassificado como conhecimento | `03b1284`, `6b487d4` |
| Limpeza do histórico | `git-filter-repo` em todos os commits: removidos dados do WhatsApp (conversas, backups, chave), gateway LiteLLM e `LITELLM_OPERATIONS.md`; mascarados os CPFs de clientes e da equipe (inclusive dentro dos PDFs), os telefones da equipe e a master key do LiteLLM | (reescrita) |
| Push forçado | Feito pelo usuário. `origin/main` = `ebbe67f` | — |
| Reorganização | `semanas/`, `docs/`, `templates/`, `scripts/`, `AGENTS.md` (fonte única), `GEMINI.md` → link, `PROMPT.md` curto | `ebbe67f` |

**Decisões tomadas (não rediscutir sem motivo novo):**
- Organização **por semana** (`semanas/<Domingo>_<Sábado>/`), com entradas em `fontes/` e saídas na raiz da pasta da semana.
- `AGENTS.md` é a única fonte de regras; `GEMINI.md` é link simbólico; `CLAUDE.md` importa.
- **WhatsApp não é fonte de dados.** `miscelaneous/whatsapp_histories/` guarda só o tutorial e os scripts de extração, como conhecimento.
- Máscara de CPF: `***.456.789-**`.
- Proibido reaproveitar números de semanas anteriores.
- As semanas legadas `2026-09-01_2026-09-13` e `2026-09-28_2026-10-04` mantêm os nomes originais (não seguem Domingo a Sábado).
- Relatórios já entregues **não** foram alterados, exceto pela máscara de CPF.

---

## 2. Segurança — pendências do usuário

- [ ] **Trocar a master key do LiteLLM** (`sk-titen-…`). Ela ficou exposta no GitHub (repositório privado) até a limpeza de 19/10.
- [ ] **Gerar uma nova chave de 64 dígitos do backup do WhatsApp** no celular (opcional; a antiga também ficou no GitHub privado).
- [ ] **Remover do GitHub os commits antigos que ainda estão em cache** (ver seção 7). Opções: chamado ao GitHub Support **ou** excluir e recriar o repositório.
- [ ] **Apagar o backup local** `~/dev/reports_ti-backup-antes-limpeza-2026-10-19.bundle` no PC original. Ele contém todos os segredos.
- [ ] **Descartar qualquer clone feito antes de 2026-10-19** (outro PC, Antigravity). Clonar de novo, sem `pull`/`merge` do histórico antigo.

## 3. Preparar o novo PC

- [ ] `git clone https://github.com/liomaroliveira/reports_ti.git`
- [ ] `git config core.hooksPath .githooks` (ativa o bloqueio de CPF, chaves e dados do WhatsApp)
- [ ] Clonar o AutoTickets em **`/home/liomarti/dev/autotickets-v2`**. O caminho está fixo em `scripts/checar_entradas.py` e em `docs/fontes_de_dados.md`: se for diferente, ajustar os dois (ou pedir à IA para tornar configurável por variável de ambiente).
- [ ] Instalar Python 3, Google Chrome/Chromium (usado pelo `scripts/renderizar_pdf.sh`) e `poppler`/`pdftotext` (opcional, checagem de CPF em PDFs).
- [ ] **Validar no Antigravity** se ele lê o `GEMINI.md` (link simbólico para `AGENTS.md`). Se não ler, trocar o link por uma cópia, ou por um `GEMINI.md` curto que mande ler o `AGENTS.md`.
- [ ] Teste rápido: `python3 scripts/checar_entradas.py` deve mostrar a tabela da semana 42.

## 4. Relatório da semana 42 (2026-10-11 a 2026-10-17) — pendente

Pasta: `semanas/2026-10-11_2026-10-17/` (já criada, com `PARAMETROS.md`).

- [ ] Decidir o **feriado de 12/10** (segunda): houve expediente? Ajustar o período operacional efetivo em `PARAMETROS.md`.
- [ ] Gerar e copiar as **exportações do Voalle**: `fontes/voalle/liomar.*`, `isac.*`, `david.*`.
- [ ] Gerar e copiar os **relatórios do AutoTickets** cobrindo 11/10 a 17/10:
  - [ ] `fontes/autotickets/colaborador_x_ticket/`
  - [ ] `fontes/autotickets/wifeed_daily_update_voucher/` (`.md` + `.html` com o SVG)
  - [ ] `fontes/autotickets/fullcam_lucros_prejuizos/`
  - [ ] `fontes/autotickets/fullcam_automacao_inadimplencia/`
  - [ ] `fontes/autotickets/fullcam_automacao_instalacao_camera/`
  - [ ] Conferir se os CSVs em `fontes/autotickets/acompanhamento_protocolos/` (gerados em 16/10) cobrem a semana inteira; se não, gerar de novo.
- [ ] Copiar para `individuais/` os relatórios que Isac e David enviarem (se não enviarem, o fluxo oferece fallback).
- [ ] `python3 scripts/mascarar_dados.py semanas/2026-10-11_2026-10-17/fontes/voalle/* semanas/2026-10-11_2026-10-17/fontes/autotickets/*/*`
- [ ] `python3 scripts/checar_entradas.py` (Fase 0). Já detecta 163 commits do AutoTickets no período.
- [ ] Pedir à IA: **"Execute o PROMPT.md"**. Ela gera o individual de Liomar, verifica os colegas e gera o consolidado, valida o índice, gera os PDFs e commita.
- [ ] Enviar o PDF ao Isvi e, quando vier o parecer, salvar em `semanas/2026-10-11_2026-10-17/feedback.md` e atualizar `docs/licoes_aprendidas.md`.

**Pendências da Coordenação que o relatório da semana 42 precisa responder** (detalhes em `docs/licoes_aprendidas.md`): status das filiais no Wazuh/VPN, com percentual e novo prazo · evolução da telefonia fixa (prioridade principal) · quadrante de backups e rotina de teste de restauração · relatório de veículos (David) · padrão Windows 10 × 11 e licenças · alinhamento LGPD Slack × AutoTickets.

## 5. Melhorias do harness (backlog)

Detalhes em `docs/pontos_a_melhorar.md`:

- [ ] Completar `docs/glossario.md` com termos internos (setores, siglas, grupos).
- [ ] Criar `docs/empresa.md` (setores, filiais, estrutura).
- [ ] AutoTickets: incluir o **período coberto** no nome dos arquivos exportados (hoje só trazem a data de geração).
- [ ] AutoTickets: gerar a auditoria Fullcam já com **CPF mascarado na origem**.
- [ ] Reinserir em `docs/referencias/` as imagens de exemplo da abertura de tarefas no Voalle (citadas em `docs/classificacao_protocolos.md`; os originais não estavam no repositório).
- [ ] (Opcional) Tornar o caminho do `autotickets-v2` configurável (`AUTOTICKETS_REPO`) em `scripts/checar_entradas.py`.
- [ ] (Opcional) Avaliar o mascaramento de **telefones de clientes** nas exportações brutas do Voalle (hoje só os CPFs são mascarados; o repositório é privado).

## 6. Pontos conhecidos (não são erros novos)

- Os relatórios já entregues têm âncoras quebradas no índice (`python3 scripts/validar_indice.py semanas/*/report_ti_*`): semana 41 (3.1–3.3), semana 2026-09-28 (3.x, 1.4, 5.1, 6.1) e semana 2026-09-01 (4.1–4.6). A causa (títulos com parênteses na especificação) já foi corrigida em `docs/especificacao_relatorio.md`. Os arquivos entregues foram mantidos como estavam.
- As exportações HTML do Voalle referenciam pastas `*_files/` que nunca foram versionadas (CSS/JS do Voalle). O conteúdo textual está completo.
- O lint de Markdown do VS Code mostra avisos de espaçamento e estilo de lista. São cosméticos e não afetam as IAs.

## 7. GitHub após o push forçado

O `git push --force` fez a `main` apontar para o histórico limpo, e quem clonar agora recebe só ele. Mas o GitHub **não apaga na hora** os commits antigos: eles ficam inacessíveis pela navegação normal, porém ainda podem ser abertos por quem souber o hash (ex.: `github.com/<repo>/commit/94f7f1e`) e podem continuar em cache até uma limpeza interna do GitHub. Como o repositório é privado, só quem tem acesso a ele conseguiria vê-los.

Para eliminar de vez:
- **Opção A — chamado ao GitHub Support:** pedir a remoção das "cached views" e das referências a dados sensíveis do repositório, informando os hashes antigos (o último foi `94f7f1e`).
- **Opção B — excluir e recriar o repositório** (Settings ▸ Delete this repository; criar de novo, privado e vazio; `git push -u origin main`). Apaga tudo do lado do GitHub. Perde-se apenas o que existe só no GitHub (issues, PRs, configurações); neste repositório, nada relevante.

Em qualquer caso, a medida que realmente neutraliza o vazamento é **trocar as chaves** (seção 2).
