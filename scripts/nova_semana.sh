#!/usr/bin/env bash
# Cria a pasta de uma semana (Domingo a Sábado) em semanas/ com PARAMETROS.md e subpastas.
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
if [ -e "$pasta" ]; then
  echo "[ERRO] $pasta já existe." >&2
  exit 1
fi

mkdir -p "$pasta"/fontes/{voalle,autotickets,investigacoes} "$pasta"/individuais
touch "$pasta"/fontes/voalle/.gitkeep "$pasta"/fontes/autotickets/.gitkeep "$pasta"/fontes/investigacoes/.gitkeep "$pasta"/individuais/.gitkeep

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

## 📝 Instruções e Focos Específicos Desta Semana

<!-- Escreva aqui apenas o que é ESPECÍFICO desta semana: destaques, eventos, feriados, pontos de atenção. -->
<!-- Não escreva números esperados: todos os valores devem ser extraídos das fontes do período. -->

1.

## 📥 Entradas esperadas

- \`fontes/voalle/\`: liomar.*, isac.*, david.*
- \`fontes/autotickets/<modulo>/\`: relatórios do AutoTickets cobrindo ${domingo} a ${sabado}
- \`fontes/investigacoes/\`: estudos datados da semana (se houver)
- \`individuais/\`: relatórios dos colegas (se enviados)

Depois de copiar: \`python3 scripts/mascarar_dados.py <arquivos>\` e \`python3 scripts/checar_entradas.py\`.
EOF

echo "[OK] Criado $pasta (Semana ${semana}/${ano}: ${domingo} a ${sabado})"
