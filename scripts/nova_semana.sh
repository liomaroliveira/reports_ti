#!/usr/bin/env bash
# Cria (ou completa) a pasta de uma semana (Domingo a Sábado) em semanas/ com PARAMETROS.md e subpastas.
# Pode ser executado de novo sobre uma pasta existente: só cria o que falta e nunca sobrescreve o PARAMETROS.md.
#
# Uso:
#   bash scripts/nova_semana.sh               # última semana completa (Dom–Sáb anterior a hoje)
#   bash scripts/nova_semana.sh 2026-10-14    # semana que contém a data informada
set -euo pipefail

cd "$(dirname "$0")/.."

if [ $# -ge 1 ]; then
  ref="$1"
  dow=$(date -d "$ref" +%w)                       # 0 = domingo
  domingo=$(date -d "$ref -$dow days" +%F)
else
  sabado_ref=$(date -d "last saturday" +%F)
  domingo=$(date -d "$sabado_ref -6 days" +%F)
fi
sabado=$(date -d "$domingo +6 days" +%F)
segunda=$(date -d "$domingo +1 day" +%F)
sexta=$(date -d "$domingo +5 days" +%F)
prazo=$(date -d "$domingo +8 days" +%F)            # segunda-feira seguinte
semana=$(date -d "$segunda" +%V)
ano=$(date -d "$segunda" +%G)

pasta="semanas/${domingo}_${sabado}"
modulos="colaborador_x_ticket wifeed_daily_update_voucher fullcam_lucros_prejuizos fullcam_automacao_inadimplencia fullcam_automacao_instalacao_camera acompanhamento_protocolos"

for d in fontes/voalle fontes/investigacoes individuais; do
  mkdir -p "$pasta/$d" && touch "$pasta/$d/.gitkeep"
done
for m in $modulos; do
  mkdir -p "$pasta/fontes/autotickets/$m" && touch "$pasta/fontes/autotickets/$m/.gitkeep"
done

if [ -f "$pasta/PARAMETROS.md" ]; then
  echo "[OK] $pasta já existia: subpastas conferidas, PARAMETROS.md mantido."
  exit 0
fi

cat > "$pasta/PARAMETROS.md" <<EOF
# ⚙️ Parâmetros da Semana ${semana} / ${ano}

> [!NOTE]
> Único arquivo editado à mão a cada semana. Fluxo: \`docs/fluxo_geracao.md\` · Estrutura: \`docs/especificacao_relatorio.md\`.

- **Data Inicial (Domingo Oficial):** \`${domingo}\`
- **Data Final (Sábado Oficial):** \`${sabado}\`
- **Período Operacional Efetivo do TI (Segunda a Sexta):** \`${segunda}\` a \`${sexta}\` <!-- ajustar se houver feriado -->
- **Semana do Ano:** Semana ${semana} / ${ano}
- **Colaborador Principal (Responsável pela Consolidação):** Liomar Antonio de Oliveira
- **Prazo de Entrega:** \`${prazo}\` (segunda-feira) até as 14h
- **Relatórios individuais a gerar:** nenhum <!-- padrão: só o consolidado. Para gerar, liste: liomar, isac, david -->

## 📝 Instruções e Focos Específicos Desta Semana

<!-- Escreva aqui apenas o que é ESPECÍFICO desta semana: destaques, eventos, feriados, pontos de atenção. -->
<!-- Não escreva números esperados: todos os valores devem ser extraídos das fontes do período. -->

1.

## 📥 Entradas esperadas

- \`fontes/voalle/\`: liomar.*, isac.*, david.*
- \`fontes/autotickets/<modulo>/\`: relatórios do AutoTickets cobrindo ${domingo} a ${sabado}
- \`fontes/investigacoes/\`: estudos datados da semana (se houver)
- \`individuais/\`: relatórios dos colegas (se enviados; usados como fonte complementar)
- Observações sobre o relatório anterior (opcional): \`semanas/<anterior>/feedback.md\` a partir de \`templates/feedback.md\`

Depois de copiar: \`python3 scripts/mascarar_dados.py <arquivos>\` e \`python3 scripts/checar_entradas.py\`.
EOF

echo "[OK] Criado $pasta (Semana ${semana}/${ano}: ${domingo} a ${sabado})"
