# ⚙️ Parâmetros da Semana 42 / 2026

> [!NOTE]
> Único arquivo editado à mão a cada semana. Fluxo: `docs/fluxo_geracao.md` · Estrutura: `docs/especificacao_relatorio.md`.

- **Data Inicial (Domingo Oficial):** `2026-10-11`
- **Data Final (Sábado Oficial):** `2026-10-17`
- **Período Operacional Efetivo do TI (Segunda a Sexta):** `2026-10-12` a `2026-10-16` <!-- ajustar: 12/10 é feriado -->
- **Semana do Ano:** Semana 42 / 2026
- **Colaborador Principal (Responsável pela Consolidação):** Liomar Antonio de Oliveira
- **Prazo de Entrega:** `2026-10-19` (segunda-feira) até as 14h — **entrega adiada** (dados ainda não gerados)

## 📝 Instruções e Focos Específicos Desta Semana

<!-- Escreva aqui apenas o que é ESPECÍFICO desta semana: destaques, eventos, feriados, pontos de atenção. -->
<!-- Não escreva números esperados: todos os valores devem ser extraídos das fontes do período. -->

1. **Feriado:** 2026-10-12 (segunda) é feriado nacional (Nossa Senhora Aparecida). Confirmar se houve expediente e ajustar o período operacional efetivo e o confronto Voalle × Pontomais.
2. **AutoTickets (4.1):** minerar os commits de `/home/liomarti/dev/autotickets-v2` entre 2026-10-11 e 2026-10-17.
3. **Pendências do feedback anterior:** cobrir os itens listados em `docs/licoes_aprendidas.md` (Wazuh/filiais, telefonia fixa, backups, veículos, Windows 10 × 11).

## 📥 Entradas esperadas

- `fontes/voalle/`: liomar.*, isac.*, david.* — **pendente**
- `fontes/autotickets/<modulo>/`: relatórios cobrindo 2026-10-11 a 2026-10-17 — **pendente** (já existe `acompanhamento_protocolos/`, gerado em 2026-10-16: conferir se cobre a semana inteira ou gerar de novo)
- `fontes/investigacoes/`: estudos datados da semana (se houver)
- `individuais/`: relatórios dos colegas (se enviados)

Depois de copiar: `python3 scripts/mascarar_dados.py <arquivos>` e `python3 scripts/checar_entradas.py`.
