# 📦 Formato Proposto: Pacote Semanal do AutoTickets (fonte única)

> Especificação para o AutoTickets gerar **um único arquivo consolidado por semana**, no lugar dos vários anexos por módulo e por formato (`.md`, `.html`, `.csv`, `.pdf`). O objetivo é ter uma fonte **completa, corrigida, determinística e verificável** para o relatório semanal.
> Motivação: análise da semana 42 (`semanas/2026-10-11_2026-10-17/fontes/autotickets/_ANALISE_GERAL.md`). Os formatos atuais não são equivalentes entre si, os KPIs não batem com as linhas exportadas e cada módulo usa um período diferente.

## Decisão de formato: um JSON por semana

**Arquivo:** `semanas/<semana>/fontes/autotickets/pacote_semanal/autotickets_semana_<inicio>_<fim>.json`
(ex.: `autotickets_semana_2026-10-18_2026-10-24.json`), em UTF-8 sem BOM.

**Por que JSON e não MD, CSV, HTML ou PDF**

| Critério | JSON único | MD | CSV | HTML/PDF |
| :--- | :---: | :---: | :---: | :---: |
| Todos os módulos num só arquivo | ✅ | ✅ | ❌ (um por tabela) | ✅ |
| Números, datas e durações sem ambiguidade (tipados) | ✅ | ❌ | parcial | ❌ |
| Textos longos com quebras de linha preservadas (relatos) | ✅ | parcial | frágil | trunca |
| Metadados, KPIs com fórmula e linhas no mesmo snapshot | ✅ | parcial | ❌ | parcial |
| Conferência automática por script (somas × KPIs, período) | ✅ | ❌ | parcial | ❌ |
| Leitura pela IA que gera o relatório | ✅ | ✅ | ✅ | ruim |

- **Versão para leitura humana** (MD/PDF): pode continuar existindo, mas deve ser **gerada a partir do mesmo JSON**. Para o relatório consolidado, ela é dispensável.
- **Exportação do Voalle:** continua necessária até o pacote ser validado contra ela por 2 semanas seguidas (ver "Critério de aceite").

## Regras gerais (valem para todos os módulos)

1. **Um snapshot só.** Todos os módulos saem da mesma execução, com o mesmo `gerado_em` e `snapshot_id`.
2. **Período padrão:** domingo a sábado da semana pedida, em **horário local** (`America/Bahia`). Os timestamps vêm em ISO 8601 com fuso, por exemplo `2026-10-16T12:17:52-03:00`. Exceções declaradas no próprio módulo:
   - `anomalias_pppoe` é um **retrato atual**, do momento da geração;
   - `fullcam_financeiro` tem uma **data-base**, sem período.
3. **Valores crus:**
   - números sem separador de milhar e com ponto decimal;
   - durações em **segundos inteiros**;
   - moeda em número, como `1287.33`, com `"moeda": "BRL"` no meta.
   - Nada de "20670d 17h", "R$ 1.287,33" ou "7h".
4. **KPIs calculados a partir das linhas do próprio arquivo.** Cada KPI traz `valor` e `formula` em texto curto. O bloco `validacoes` registra as conferências que o próprio AutoTickets fez.
5. **Sem logs repetitivos.** Execuções rotineiras sem efeito (NOTIFY, "nenhuma pendência", avisos idênticos) viram **um resumo por rotina**:
   - `execucoes`, `primeira`, `ultima`, `intervalo_esperado_min`;
   - `lacunas`: períodos sem execução acima do intervalo esperado;
   - `pendencias_presas`: o mesmo item repetido por mais de 24h.
6. **Máscara na origem:**
   - CPF como `***.456.789-**` e CNPJ como `**.345.678/****-**`;
   - **senhas e stream keys RTMP removidas** dos textos (`Senha: ********`, `rtmp://host/***`).
   - Nome, login, contrato, IP, MAC e endereço **permanecem**, porque o relatório é interno e os setores precisam localizar os casos.
7. **Textos completos:** sem truncamento, com `\n` preservado e imagens substituídas por `[imagem: N]`.
8. **Alertas de qualidade por registro** (`alertas: [...]`): duração acima de 8h, apontamento que atravessa noite ou fim de semana, intervalo negativo ou acima de 365 dias, data nula, protocolo vazio, status incoerente com o progresso, registro fora do período.

## Estrutura

```json
{
  "meta": {
    "gerador": "AutoTickets", "versao": "x.y.z", "snapshot_id": "2026-10-25T08:00:00-03:00#a1b2c3",
    "gerado_em": "2026-10-25T08:00:00-03:00", "fuso": "America/Bahia", "moeda": "BRL",
    "periodo": { "inicio": "2026-10-18", "fim": "2026-10-24" },
    "colaboradores": [ { "nome": "LIOMAR ANTONIO DE OLIVEIRA", "id_voalle": 107184, "pasta": "liomar" } ],
    "modulos_incluidos": ["tarefas_executadas", "colaborador_x_ticket", "wifeed", "fullcam_financeiro",
                          "fullcam_inadimplencia", "fullcam_instalacao", "acompanhamento_protocolos", "anomalias_pppoe"],
    "avisos": ["texto livre: falhas de coleta, módulos indisponíveis etc."]
  },
  "modulos": { "...": "ver abaixo" },
  "validacoes": [ { "regra": "horas_tarefas_bate_voalle", "ok": true, "detalhe": "..." } ]
}
```

## Dados esperados por módulo

### `tarefas_executadas` (substitui as exportações do Voalle e os CSV/PDF por colaborador)

- **`meta`:**
  - `filtro_periodo`: `"lancamento"`, `"inclusao"` ou `"sobreposicao"`. O padrão proposto é **`sobreposicao`**: entra todo apontamento cujo intervalo toca a semana, com `segundos_no_periodo` recortado (ver `tarefas_executadas/_ANALISE_FONTE.md`).
  - definição de cada indicador.
- **`totais.por_colaborador`:**
  - `apontamentos`, `protocolos_distintos`;
  - `segundos_total`, `segundos_no_periodo`;
  - **equivalente Voalle**: `segundos_por_lancamento` e `segundos_por_inclusao`, para conferência com o ERP;
  - `alertas` (contagem por tipo).
- **`apontamentos[]`, um por apontamento:**
  - identificação: `id_apontamento`, `colaborador`, `protocolo` (sempre preenchido), `id_chamado`, `origem` (Solicitação / Atividade Interna / Tarefa de Solicitação), `tipo_evento` (apontamento / abertura / encaminhamento / relato), `titulo` (sem o prefixo "Protocolo N –"), `cliente {nome, contrato}`, `setor_colaborador`, `setor_destino`;
  - tempo: `inicio`, `fim` (data completa) ou `null` se o play estiver aberto, `em_execucao` (bool), `segundos`, `segundos_no_periodo`;
  - situação: `progresso`, `status_real`;
  - texto: `relato` (completo, com `\n` e `[imagem: N]`) e `relato_data_hora` (data em campo próprio);
  - `encaminhamento {origem, destino, destinatario, motivo}`, `alertas[]`.
- **`demandas[]`, um por protocolo, sem repetir a cada apontamento:** `protocolo`, `descricao`, `solicitante`, `setor_solicitante`, `abertura`, `encerramento`, `status_real`.

### `colaborador_x_ticket`

- **`kpis`** com fórmula: entradas, saídas, balanço da fila (saídas ÷ entradas), TMA, TMR, ações e encaminhamentos. Os KPIs são **globais e por colaborador**, e **excluem** registros com alerta de duração inválida.
- **`chamados[]`:**
  - identificação: `protocolo`, `tipo`, `titulo`, `colaborador`, `papel` (abriu / atuou / encaminhou / encerrou, para explicar a repetição do mesmo protocolo);
  - pessoas e equipes: `criado_por`, `encerrado_por`, `responsavel`, `cliente`, `equipe_colaborador`, `equipe_solicitante`, `equipe_atual`;
  - datas: `abertura`, `encerramento`;
  - contagens e tempos: `acoes`, `segundos_trabalhados`, `tempo_atendimento_seg`, `tempo_resolucao_seg`, `encaminhamentos`;
  - situação: `status`, `prioridade`, `fora_do_periodo` (bool), `alertas[]`.

### `wifeed`

- **`kpis`:** base no início e no fim, variação (absoluta e %), pico, mínimo, sincronizações, sucesso e vouchers.
- **`diario[]`:** `{data, base_ativa}`.
- **`envios[]`:** `{id, data_hora, operador, segmento, base_erp, vouchers, status, status_significado}`, com "Substituído" para o segmento antigo, que **não conta como falha**.

### `fullcam_financeiro`

- `data_base` e `kpis` com fórmula. A soma das linhas deve ser **idêntica** à do KPI.
- **`clientes[]`:** `cliente`, `documento` (mascarado), `contratos[]`, `situacao`, `faturas_pagas`, `gb`, `faturado`, `custo_licencas`, `custo_storage`, `equip_perdido`, `saldo`, `flags[]`. Exemplos de flag: `sem_etiqueta_videomonitoramento`, `fatura_incompativel_com_camera`, `colaborador_interno` (caso do contrato de David Brasil Fernandes apontado pelo Isvi).
- **`variacao_vs_anterior`:** clientes que entraram ou saíram e maiores mudanças de saldo. Isso permite trocar a tabela integral do relatório por "top N + variação".

### `fullcam_inadimplencia` e `fullcam_instalacao`

- **`acoes[]`:** só eventos com efeito (BLOCK, UNBLOCK, INSTALL), com `id`, `id_original` (se reprocessado), `data_hora`, `cliente`, `contrato`, `protocolo`, `cameras[]` (lista real), `status` e `mensagem` completa (sem stream key).
- **`kpis_periodo`:** contratos e câmeras **únicos**, separando sucesso, aviso e erro.
- **`rotina`:** resumo das checagens automáticas (execuções, primeira, última, `lacunas[]`). Exemplo: os NOTIFY de inadimplência pararam em 06/10.
- **`pendencias_presas[]`:** `{protocolo, contrato, desde, tentativas, ultimo_aviso, motivo}`. Exemplo: 3198228 em instalação.

### `acompanhamento_protocolos`

- **`protocolos[]` (determinístico, direto do Voalle):** `protocolo`, `titulo`, `setor_destino`, `status_real`, `abertura`, `ultimo_relato`, `dias_parado`, `responsavel`.
- **`analise_ia`** (opcional e separada): `{modelo, texto, protocolos_citados[], protocolos_citados_inexistentes[]}`.

### `anomalias_pppoe` (retrato atual)

- **Janela e critérios:** `retrato_em`, `janela_trafego {inicio, fim}` (bytes **dentro** da janela) e `filtros` aplicados.
- **Regra de severidade:** `regra_severidade` (faixas de score) e peso de cada critério.
- **`kpis`.**
- **`casos[]`:**
  - identificação: `cliente`, `login`, `documento` (mascarado), `contrato`, `status_contrato`, `cidade`, `bairro`, `pop`, `ip`, `mac`, `fabricante_cpe`, `tecnologia`, `plano`;
  - medições: `rx_dbm`, `upload_bytes`, `download_bytes`, `razao`, `throughput_medio_mbps` (bytes da janela ÷ tempo online), `throughput_pico_mbps`, `quedas`, `ultima_causa`;
  - classificação: `severidade`, `score`, `diagnosticos[]` (incluindo o óptico), `rotulos[]` (interno/cortesia, provedor/revenda);
  - acompanhamento: `primeira_deteccao`, `semanas_consecutivas`, `ticket {protocolo, status}`.

## Critério de aceite (para dispensar as exportações atuais)

1. `scripts/checar_entradas.py` reconhece o pacote: o JSON é válido, o período confere e os módulos essenciais estão presentes.
2. Em **2 semanas seguidas**, `totais.por_colaborador.segundos_por_lancamento` e `segundos_por_inclusao` batem com os cabeçalhos do Voalle, com tolerância de 0 minutos, e a lista de protocolos é a mesma.
3. Nenhum KPI diverge da soma das linhas (`validacoes` todas `ok: true`).
4. Nenhum registro com intervalo negativo, acima de 365 dias ou data nula sem `alertas`.

Cumprido isso, `fontes/voalle/` e os arquivos por módulo deixam de ser exigidos. O pacote vira a fonte primária, e o Voalle fica apenas para auditoria por amostragem.
