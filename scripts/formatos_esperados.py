#!/usr/bin/env python3
"""
Escreve `_FORMATO_ESPERADO.md` em cada pasta de fontes de uma semana: qual formato exportar, período e observações.
Fonte única das regras de formato (decididas na análise da semana 42 — fontes/**/_ANALISE_*.md).

Uso:
    python3 scripts/formatos_esperados.py semanas/2026-10-18_2026-10-24     # (chamado também por nova_semana.sh)
"""

import os
import sys

DOM_SAB = "domingo a sábado da semana (pasta)"

# pasta (relativa à semana) -> (formato esperado, período, observações)
FORMATOS = {
    "fontes/voalle": (
        "**HTML** do relatório *Tarefas Executadas*, um arquivo por colaborador, com **\"Tipo de data: Lançamento\"**.",
        DOM_SAB,
        "Nome: `<pessoa>_tarefas_executadas_<AAAAMMDD_HHMMSS>.html` (ou `<pessoa>.html`). PDF não é necessário "
        "(o do David perde horas). A pasta `*_files/` (jQuery/CSS) não é necessária. Será dispensado quando "
        "`autotickets/tarefas_executadas` (ou o pacote semanal) cumprir o critério de aceite.",
    ),
    "fontes/autotickets/pacote_semanal": (
        "**Um JSON** `autotickets_semana_<inicio>_<fim>.json` com todos os módulos (formato-alvo).",
        DOM_SAB + " (PPPoE: retrato atual; Fullcam financeiro: data-base)",
        "Especificação: `docs/formato_exportacao_autotickets.md`. Quando existir, substitui as pastas por módulo.",
    ),
    "fontes/autotickets/tarefas_executadas": (
        "**CSV** por colaborador (`<pessoa>_tarefas_executadas_<...>.csv`).",
        DOM_SAB,
        "PDF não é necessário (corta relatos e perde registros). Hoje o AutoTickets reproduz o critério "
        "\"Inclusão\" do Voalle; declarar o critério no nome quando houver o parâmetro.",
    ),
    "fontes/autotickets/colaborador_x_ticket": (
        "**MD** (resumo + detalhe). CSV opcional, para colunas extras (Encerrado por, Cliente, Encaminhamentos).",
        DOM_SAB,
        "HTML e PDF não são necessários. Atenção aos KPIs que não fecham com o detalhe (ver `_ANALISE_FONTE.md` da semana 42).",
    ),
    "fontes/autotickets/wifeed_daily_update_voucher": (
        "**MD** (ou CSV — um dos dois basta).",
        DOM_SAB,
        "O gráfico do 11.1 (base de clientes adimplentes do Voalle) é redesenhado a partir da tabela diária; HTML e PDF não são necessários.",
    ),
    "fontes/autotickets/fullcam_lucros_prejuizos": (
        "**CSV**.",
        "data-base atual (foto acumulada)",
        "PDF não é necessário (os KPIs do PDF não fecham com o CSV). Ignorar o contrato 96660 (DAVID BRASIL "
        "FERNANDES) até a correção do módulo.",
    ),
    "fontes/autotickets/fullcam_automacao_inadimplencia": (
        "**CSV** (único com a mensagem completa).",
        DOM_SAB + " — hoje o AutoTickets exporta 30 dias móveis: filtrar a semana e desconsiderar os NOTIFY",
        "MD, HTML e PDF não são necessários.",
    ),
    "fontes/autotickets/fullcam_automacao_instalacao_camera": (
        "**MD** (ou CSV).",
        DOM_SAB + " — hoje exporta 30 dias móveis: filtrar a semana e desconsiderar os avisos repetidos",
        "HTML e PDF não são necessários.",
    ),
    "fontes/autotickets/acompanhamento_protocolos": (
        "**MD**.",
        "lista acumulada de protocolos abertos (usar só os eventos da semana)",
        "Texto gerado por IA: confirmar status e datas no Voalle antes de citar.",
    ),
    "fontes/autotickets/anomalias_pppoe": (
        "**CSV + PDF** (o IP, os KPIs e os filtros só existem no PDF).",
        "**retrato atual**, gerado no dia da emissão do relatório consolidado (sem recorte da semana)",
        "Alimenta o tópico condicional 12.3 e o Anexo C.",
    ),
    "fontes/autotickets/problemas_recorrentes": (
        "**MD** (`reincidencia_<...>.md`): único formato com indicadores, todas as seções (clientes, pedidos "
        "internos, reencaminhamentos, problemas sistêmicos, taxa por tipo) e o detalhe por caso.",
        DOM_SAB + " (retorno contado até 60 dias após a conclusão anterior)",
        "CSV opcional (uma linha por protocolo, sem indicadores). HTML e PDF não são necessários. "
        "Subpasta `todas_equipes/` (se existir): versão anterior de 30 dias, só referência.",
    ),
    "fontes/autotickets/produtividade_geral": (
        "A definir (alimenta o 7.3).",
        DOM_SAB,
        "Sem exportação definida ainda; o 7.3 declara a ausência e mostra o volume executado.",
    ),
    "fontes/autotickets/desenvolvimento": (
        "Nenhum arquivo é necessário: os commits são minerados do repositório `autotickets_v2` (`AUTOTICKETS_REPO`).",
        DOM_SAB,
        "Opcional: MD com resumo das sprints.",
    ),
    "fontes/investigacoes": (
        "Uma subpasta por estudo: `AAAA-MM-DD_<tema>/` com relatório **MD** e anexos.",
        "data de conclusão do estudo dentro da semana",
        "Ex.: relatórios da gincana de pentest.",
    ),
    "fontes/infraestrutura/backups": (
        "**MD ou CSV** (exportação/print do Proxmox/PBS) com: VMs/CTs na rotina, jobs executados × falhas, "
        "refeitos manualmente (causa) e data do último teste de restauração.",
        DOM_SAB,
        "Sem este arquivo, o 5.4 declara ausência de fonte (nunca estimar).",
    ),
    "individuais": (
        "Qualquer formato (MD, HTML ou PDF) enviado pelos colegas.",
        DOM_SAB,
        "Fonte complementar do Tópico 2. Gerados só quando pedidos.",
    ),
}


def escrever(semana):
    escritos = []
    for pasta, (formato, periodo, obs) in FORMATOS.items():
        destino = os.path.join(semana, pasta)
        if not os.path.isdir(destino):
            if pasta in ("fontes/autotickets/produtividade_geral", "fontes/autotickets/desenvolvimento"):
                continue
            os.makedirs(destino, exist_ok=True)
        with open(os.path.join(destino, "_FORMATO_ESPERADO.md"), "w", encoding="utf-8") as f:
            f.write(f"# Formato esperado — `{pasta}`\n\n"
                    "> Gerado por `scripts/formatos_esperados.py` (não editar aqui). Não é fonte do relatório.\n\n"
                    f"- **Formato:** {formato}\n- **Período:** {periodo}\n- **Observações:** {obs}\n")
        escritos.append(pasta)
    return escritos


if __name__ == "__main__":
    if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
        print(__doc__)
        sys.exit(2)
    for p in escrever(sys.argv[1]):
        print(f"[OK] {p}/_FORMATO_ESPERADO.md")
