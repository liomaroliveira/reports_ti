# 🖥️ Fontes de Dados

Todas as entradas de uma semana ficam em `semanas/<semana>/fontes/`. O que não estiver lá (ou no repositório `autotickets-v2`) não é fonte do relatório.

| Fonte | Onde colocar | Alimenta |
| :--- | :--- | :--- |
| Voalle (exportação por colaborador) | `fontes/voalle/<pessoa>.<html\|pdf\|csv>` (**HTML, "Tipo de data: Lançamento"**) | Tópicos 1 a 7 (narrativas, protocolos, horas) |
| AutoTickets — colaborador × ticket | `fontes/autotickets/colaborador_x_ticket/` | Tópico 1 (balanço da fila) e 2 (TMA, TMR, produtividade) |
| AutoTickets — acompanhamento de protocolos | `fontes/autotickets/acompanhamento_protocolos/` | Tópico 1 (pendentes, parados 15+ dias, andamento) |
| AutoTickets — WiFeed | `fontes/autotickets/wifeed_daily_update_voucher/` | 8.1 (base de clientes adimplentes do Voalle) e 9 (sincronização de vouchers) |
| AutoTickets — Fullcam financeiro | `fontes/autotickets/fullcam_lucros_prejuizos/` | 10.1 e 10.2 (tabela completa) |
| AutoTickets — Fullcam inadimplência | `fontes/autotickets/fullcam_automacao_inadimplencia/` | 10.3 e 10.4 (só execuções com ação) |
| AutoTickets — Fullcam instalação | `fontes/autotickets/fullcam_automacao_instalacao_camera/` | 10.3 e 10.4 (só execuções com ação) |
| AutoTickets — tarefas executadas | `fontes/autotickets/tarefas_executadas/` | Tópico 2 e 2.4 (produção bruta por colaborador; preferir o **CSV**, o PDF corta relatos) |
| AutoTickets — anomalias PPPoE | `fontes/autotickets/anomalias_pppoe/` | 8.4, tópico condicional (CSV). **Retrato atual** gerado no dia da emissão: não aplicar o recorte da semana |
| AutoTickets — **pacote semanal** (proposto) | `fontes/autotickets/pacote_semanal/autotickets_semana_<inicio>_<fim>.json` | Todos os tópicos do AutoTickets: substitui os arquivos por módulo quando existir (`docs/formato_exportacao_autotickets.md`) |
| AutoTickets — problemas recorrentes | `fontes/autotickets/problemas_recorrentes/` | Reincidência da semana (retorno até 60 dias) — **MD**; alimenta 8.2 e 8.3 e o cruzamento com o 8.4 |
| AutoTickets — produtividade geral | `fontes/autotickets/produtividade_geral/` | 11.3 |
| AutoTickets — desenvolvimento | commits no repositório `autotickets_v2` (`AUTOTICKETS_REPO`) ou `fontes/autotickets/desenvolvimento/` | 11 |
| Infraestrutura — backups | `fontes/infraestrutura/backups/` | 6.3 (quadrante obrigatório: sem esta fonte, declarar ausência — nunca estimar) |
| Investigações / segurança | `fontes/investigacoes/AAAA-MM-DD_<tema>/` | 3, 6.4, 7.2, 13.1 |
| Individuais enviados pelos colegas (opcional) | `individuais/<pessoa>.<ext>` | Fonte complementar do Tópico 2 |
| Relatório consolidado da semana anterior | `semanas/<anterior>/report_ti_*.md` | Continuidade (1.1, 1.2, 13.3) e comparação |
| Feedback/observações da semana anterior | `semanas/<anterior>/feedback.md` | Resumo Executivo (acompanhamento) e tópicos citados |

> Exportações brutas: máscara **opcional** (`python3 scripts/mascarar_dados.py <arquivos>`); o repositório é de uso interno e não há verificação automática. **Formato esperado de cada fonte:** `_FORMATO_ESPERADO.md` em cada pasta de `fontes/` (gerado por `scripts/formatos_esperados.py`).
>
> **Arquivos de análise (`_ANALISE_*.md`)** dentro das pastas de fontes são feedback sobre a qualidade das exportações (para o Liomar e o AutoTickets). **Não são fonte do relatório**, mas suas ressalvas devem ser respeitadas ao usar os dados (ex.: formato preferido, campos não confiáveis).

---

## 1. ERP Voalle

ERP principal (Atendimento, Service Desk, O.S., Projetos, Infraestrutura e Apontamentos). Extrair de cada exportação:

- **Protocolo e título** da tarefa;
- **Tipo de solicitação:** (TI) Sol. Interna, (NOC), (N2-TI), Manutenção Programada, Infraestrutura etc. — ver `docs/classificacao_protocolos.md`;
- **Datas e horários** (lançamento, início, fim) e **horas trabalhadas (HT)**;
- **Progresso (%)**;
- **Relato técnico:** solução aplicada, peças substituídas (SSDs, fontes, switches, ONTs Datacom), configurações de rede (IPs, VLANs, interfaces);
- **Confronto com o Pontomais:** somatório de HT × ponto real, justificando divergências (`docs/regras_metricas.md` §3).

## 2. AutoTickets

Plataforma de automação desenvolvida e mantida por Liomar Oliveira. Repositório local: variável `AUTOTICKETS_REPO` ou, por padrão, `~/dev/autotickets_v2` (antigo: `/home/liomarti/dev/autotickets-v2`).

**Mineração de commits** (quando não houver relatório em `fontes/autotickets/desenvolvimento/`):

```bash
git -C "${AUTOTICKETS_REPO:-$HOME/dev/autotickets_v2}" log --since="AAAA-MM-DD 00:00:00" --until="AAAA-MM-DD 23:59:59" \
  --pretty=format:"%h - %an, %ad : %s" --date=iso --shortstat
```

- **Arquivos multi-formato:** mesmo nome base em `.md`, `.html`, `.csv`, `.pdf` = mesmo relatório. Os nomes trazem a **data de geração**, não o período: confirmar dentro do arquivo que o período coberto é a semana corrente.
- **Formatos não são equivalentes** (análise da semana 42, `fontes/autotickets/_ANALISE_GERAL.md`): usar o formato preferido de cada módulo. Resumo: colaborador × ticket → MD (+ CSV para colunas extras); WiFeed → CSV ou MD (o SVG do HTML é opcional); Fullcam inadimplência e instalação → CSV/MD filtrando NOTIFY e a semana; Fullcam lucros → CSV (KPIs do PDF não fecham); tarefas executadas → CSV; anomalias PPPoE → CSV; Voalle → **HTML**. Formato-alvo único: `docs/formato_exportacao_autotickets.md`.
- **colaborador_x_ticket** é gerado a partir do banco do Voalle: é a fonte métrica primária; `fontes/voalle/` complementa com o qualitativo.
- **WiFeed:** contexto institucional do Captive Portal em `docs/referencias/wifeed_contexto.md`.
- **Uso no relatório (`AGENTS.md`, regras 1 e 9):** os commits são minerados para entender o que foi entregue, mas o texto descreve as entregas de forma genérica, pelo valor para a operação (segurança da plataforma, painel executivo, relatórios, automações, desempenho), sem detalhes de implementação, e a segurança do AutoTickets como reforço. Fontes são citadas pelo nome descritivo, nunca pelo caminho do arquivo.

## 3. Investigações especiais e segurança

Estudos pontuais, testes de intrusão, mapeamento de vulnerabilidades e perícias, em `fontes/investigacoes/AAAA-MM-DD_<tema>/` (data de conclusão). Quando houver na semana:

1. **Tópico 3:** registrar o estudo como entrega técnica;
2. **Tópico 6.4:** resumir testes executados e superfície avaliada (e 7.2, quando for desafio/gincana);
3. **Tópico 13.1:** riscos, falhas de controle e plano de mitigação.

## 4. Infraestrutura e plataformas (contexto)

Flashman (TR-069), Native PBX / ZEUS (telefonia), Made4NOC / Grafana, FullCam, MailCow, servidores Datacom (SV01), Dell PowerEdge (R550, R910), SuperMicro, MikroTik e switches gerenciáveis.

## 5. Fora do escopo

- **WhatsApp** (`miscelaneous/whatsapp_histories/`): apenas conhecimento técnico guardado; não é fonte.
