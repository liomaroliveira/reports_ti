# 🚦 Fluxo de Geração do Relatório Semanal

`<semana>` = pasta da semana corrente em `semanas/` (a mais recente). `<anterior>` = a pasta imediatamente anterior.

> [!IMPORTANT]
> **Padrão: gerar somente o relatório semanal consolidado.** Relatórios individuais só são gerados quando o usuário pedir explicitamente, no prompt ou no campo **"Relatórios individuais a gerar"** do `PARAMETROS.md`.

```mermaid
graph TD
    A[Ler semanas/&lt;semana&gt;/PARAMETROS.md] --> B[Fase 0: scripts/checar_entradas.py]
    B -->|Falta fonte essencial| C[INTERROMPER: mostrar tabela e perguntar se prossegue]
    B -->|OK| D[Fase 1: contexto da semana anterior]
    D --> E[Etapa principal: relatório consolidado]
    E --> F{Individuais pedidos?}
    F -->|Sim| G[Etapa opcional: individuais pedidos]
    F -->|Não| H[Finalização]
    G --> H[Validar índice, gerar PDF, commitar]
```

---

## Preparação (usuário)

1. `bash scripts/nova_semana.sh` — cria `semanas/<Domingo>_<Sábado>/` com `PARAMETROS.md` e as subpastas.
2. Preencher em `PARAMETROS.md` os focos da semana, os feriados e, se quiser, os relatórios individuais a gerar.
3. Copiar as entradas para `fontes/` (nomes em `docs/fontes_de_dados.md`). Relatórios que os colegas enviarem vão para `individuais/` e servem como **fonte**.
4. *(Opcional)* Escrever as observações sobre o relatório anterior (suas e do Isvi) em `semanas/<anterior>/feedback.md`, a partir de `templates/feedback.md` (**copiar** o template para a pasta da semana avaliada; não editar o próprio template).
5. *(Opcional)* Mascarar dados pessoais e credenciais: `python3 scripts/mascarar_dados.py semanas/<semana>/fontes/voalle/* semanas/<semana>/fontes/autotickets/*/*`.

---

## Fase 0: Checklist de entradas

Rodar `python3 scripts/checar_entradas.py` e mostrar a tabela ao usuário. São essenciais: Voalle dos três colaboradores, commits do AutoTickets e os cinco relatórios principais do AutoTickets. Também aparecem, como informativos: o relatório e o `feedback.md` da semana anterior, os individuais já existentes e os CPFs sem máscara.

> [!WARNING]
> **Ponto de interrupção:** se faltar fonte essencial, **interromper**, mostrar a tabela e perguntar se o usuário prossegue com dados parciais (registrando a ausência justificada no relatório) ou aguarda.

---

## Fase 1: Contexto da semana anterior (obrigatória)

Ler, antes de escrever qualquer seção:

1. **`semanas/<anterior>/report_ti_*.md`** — o relatório consolidado anterior. Usar para:
   - **Continuidade:** cada item de *1.2 Demandas em andamento*, *1.1 Pendentes* e *13.3 Ações planejadas* (*9.3* nos relatórios até a semana 41) do relatório anterior precisa ter **desfecho** no novo (concluído, em andamento com novo %, replanejado com motivo e novo prazo, ou cancelado com motivo).
   - **Comparação:** indicadores-chave da semana (balanço da fila, volumes, base WiFeed etc.) podem ser comparados com os da semana anterior. O valor anterior aparece sempre **identificado como "semana anterior"** e com a fonte citada como "relatório da semana NN" (nunca pelo caminho do arquivo); nunca substitui o dado atual.
   - **Mudanças de plano:** desvio em relação ao que foi prometido entra com o motivo (`docs/regras_metricas.md` §8).
2. **`semanas/<anterior>/feedback.md`** *(se existir)* — parecer do Isvi e observações do Liomar. **Toda observação precisa ser tratada** no novo relatório: no tópico correspondente e na tabela *Acompanhamento das observações da semana anterior* do Resumo Executivo (`docs/especificacao_relatorio.md`).
3. **`docs/licoes_aprendidas.md`** — regras e pendências acumuladas da Coordenação.

---

## Etapa principal: Relatório consolidado do setor

1. **Fontes:** minerar diretamente `fontes/voalle/` (Liomar, Isac e David), `fontes/autotickets/`, os commits do `autotickets-v2` e `fontes/investigacoes/`. Se existir `individuais/<pessoa>.*` (enviado pelo colega ou gerado antes), usar como fonte complementar daquela pessoa.
2. **Tópicos dinâmicos e condicionais:** antes de escrever, aplicar os critérios de "Classes de Tópicos" (`docs/especificacao_relatorio.md`) às fontes da semana e à semana anterior: escolher os 3 a 5 **Destaques Analíticos**, separar os **Fatos Notáveis**, decidir os **subtópicos livres** e incluir os **tópicos condicionais** que tiverem fonte (8.4). Ler os `_ANALISE_*.md` das pastas de fontes e respeitar as ressalvas.
3. **Profundidade analítica (proibido resumir excessivamente):** cada tópico e subtópico com métricas, causas raízes, soluções, tabelas e contexto técnico.
4. **Detalhamento por pessoa:** o Tópico 2 traz a visão completa de cada colaborador (atividades, distribuição do tempo, capacitação, Voalle × Pontomais), sem depender de relatório individual.
5. **Ações conjuntas:** demanda com mais de um colaborador vira relato unificado, indicando a participação de cada um.
6. **Saída:** escrever **só o `.md`** (`semanas/<semana>/report_ti_<Domingo>_<Sábado>.md`) e gerar o `.html` com `python3 scripts/md_para_html.py <arquivo.md>`; o `.pdf` sai na finalização. Statcards e barras entram no `.md` como marcadores `<!-- KPI: … -->` e `<!-- BARS: … -->` (sintaxe na docstring do script); CPF mascarado vai escapado (`\*\*\*.456.789-\*\*`). Não editar o `.html` à mão: corrigir o `.md` e gerar de novo.

---

## Etapa opcional: Relatórios individuais (somente se pedido)

Executar **apenas** para as pessoas pedidas no prompt ou em `PARAMETROS.md`. Sem pedido, não gerar e não perguntar.

- **Conteúdo:** recorte do consolidado para a pessoa, mais o detalhamento completo dos protocolos e commits dela, seguindo a estrutura de tópicos aplicável.
- **Saída:** `individuais/<pessoa>.md`, `.html` (com o CSS em `../../../templates/report.css`) e `.pdf`.
- Se já existir `individuais/<pessoa>.*` enviado pelo colega, **não sobrescrever**: avisar o usuário.

---

## Finalização

1. `python3 scripts/validar_indice.py semanas/<semana>/report_ti_*.md semanas/<semana>/report_ti_*.html` — corrigir qualquer âncora quebrada.
   `python3 scripts/validar_relatorio.py semanas/<semana>/report_ti_*.md` — nomes/caminhos de arquivo citados no texto, termos técnicos ou negativos sobre o AutoTickets (aviso), termos proibidos, seções obrigatórias, Destaques Analíticos (3 a 5), tabela de acompanhamento com uma linha por observação do `feedback.md` anterior, tópico condicional 8.4 e dados que nunca podem aparecer (CPF/CNPJ sem máscara, senhas, RTMP).
2. `python3 scripts/md_para_html.py semanas/<semana>/report_ti_<...>.md` e depois `bash scripts/renderizar_pdf.sh semanas/<semana>/report_ti_<...>.html` (e para cada individual gerado). Conferir o PDF visualmente (tabelas, quebras de página, cards).
3. Atualizar a seção de status do `PARAMETROS.md` da semana (o que foi gerado e o que ficou pendente).
4. Commitar (o hook bloqueia apenas chaves de API e dados do WhatsApp).
5. Quando chegar o parecer da Coordenação: salvar em `semanas/<semana>/feedback.md` e registrar as lições novas em `docs/licoes_aprendidas.md`.
