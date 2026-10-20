# 🛠️ Pontos a Melhorar (Backlog do Harness)

Melhorias do próprio processo de geração e problemas conhecidos. Quando uma melhoria virar regra, mova-a para o documento definitivo e marque como concluída aqui.

## Pendentes

- [ ] Completar o `docs/glossario.md` com termos e jargões internos (setores, siglas de equipes, nomes de grupos).
- [ ] Criar `docs/empresa.md` descrevendo setores, filiais e estrutura, para dar contexto à IA.
- [ ] Nomes dos relatórios do AutoTickets: incluir o **período coberto** no nome do arquivo (hoje trazem só a data de geração).
- [ ] AutoTickets: gerar a auditoria Fullcam já com CPF mascarado na origem (e, em geral, todas as exportações — ver `semanas/2026-10-11_2026-10-17/fontes/autotickets/_ANALISE_GERAL.md`).
- [ ] Reinserir em `docs/referencias/` as imagens de exemplo da abertura de tarefas no Voalle, citadas em `docs/classificacao_protocolos.md` (as originais `image/PONTOS_A_MELHORAR/*.png` não estavam no repositório).
- [ ] (Opcional) Mascarar também **telefones de clientes** nas exportações brutas do Voalle (hoje só CPFs são mascarados).

### Avaliação crítica de 2026-10-19 (estrutura do relatório e fontes)

Origem: análise da semana 42 (`semanas/2026-10-11_2026-10-17/fontes/**/_ANALISE_*.md`). Registradas como recomendação; nenhuma foi implementada ainda.

- [x] **Tópicos dinâmicos e condicionais** (implementado em 2026-10-19: "Classes de Tópicos" na especificação, 📈 Destaques Analíticos, 8.4 condicional e subtópicos livres). Hoje o índice é rígido: só "⭐ Fatos Notáveis" muda com os dados.
  - **O que fazer:**
    - Formalizar na especificação uma classe de **tópicos condicionais** (8.4 PPPoE, investigações, módulos novos do AutoTickets): eles aparecem só se houver fonte; sem fonte, uma linha de ausência justificada.
    - Criar uma seção **"Destaques Analíticos da Semana"**, logo após o Resumo Executivo, com 3 a 5 achados gerados pelos dados: maiores variações em relação à semana anterior, picos, novos tipos de demanda, concentração por setor ou POP, recorrências.
    - Reservar "Fatos Notáveis" para anomalias e desvios. Entregas normais (ex.: servidor GPU na semana 41) vão para o Tópico 3.
  - **Por quê:** o relatório fica igual toda semana na forma e "esconde" o que mudou. O Isvi pediu que ele responda "foi bom?", "para onde estamos apontando?", "o que precisa mudar?".
- [ ] **Reduzir texto fixo.**
  - **O que fazer:**
    - Mover os textos institucionais (4.2.1, 4.2.2, 4.1.2, 3.3) para um anexo ou `docs/referencias/` e citá-los com uma linha.
    - Trocar a tabela integral da Fullcam (4.3.2, cerca de 19% do relatório da semana 41) por **top N + variação semanal + anexo**.
    - Corrigir a contradição do WiFeed: o 4.2.1 diz "semanal / 3h semanais" e o 4.5 diz "45 min diários".
  - **Por quê:** de 30% a 35% do relatório da semana 41 se repete toda semana, o que dilui a análise e custa atenção da Direção.
- [x] **Feedback verificável** (implementado em 2026-10-19: `checar_entradas.py` conta as observações, e `validar_relatorio.py` confere a tabela de acompanhamento).
  - **O que fazer:**
    - `checar_entradas.py` passa a listar cada item do `feedback.md` anterior.
    - Um `scripts/validar_relatorio.py` confere se a tabela "Acompanhamento das observações" existe e se tem uma linha por item.
    - Pendências recorrentes (veículos por data/protocolo, quadrante de backups, Windows 10 × 11, Wazuh/filiais) ganham **status persistente** em `docs/licoes_aprendidas.md` (aberto/atendido, desde quando).
  - **Por quê:** hoje o efeito do feedback depende só da IA obedecer. Na semana 41:
    - os itens foram tratados de forma espalhada, sem a tabela;
    - o pedido de veículos por data/protocolo não foi atendido;
    - o quadrante de backups trouxe números sem fonte (24 instâncias, 168 jobs = 24 × 7);
    - há uma citação atribuída ao Isvi que ele não fez.
    - Além disso, o `feedback.md` da semana 41 está vazio, então a semana 42 não terá observações a tratar.
- [x] **Validador de conteúdo** (`scripts/validar_relatorio.py`, 2026-10-19; títulos fora da especificação ainda não são conferidos).
  - **O que fazer:** conferir:
    - termos proibidos ("resolutividade", "resolubilidade");
    - títulos fora da especificação e parênteses que quebram âncoras (3.x na semana 41);
    - presença de fonte citada nos quadrantes obrigatórios (backups, disponibilidade);
    - CPF/IP/nome de cliente em tabelas.
  - **Por quê:** os erros da semana 41 eram todos detectáveis mecanicamente.
- [x] **Exigir fonte para o quadrante de backups (8.2)** (pasta `fontes/infraestrutura/backups/` criada pelo `nova_semana.sh` e conferida pelo checklist, 2026-10-19).
  - **O que fazer:** criar `fontes/infraestrutura/backups/` (exportação do Proxmox Backup/PBS ou print dos jobs) e listar essa fonte no `checar_entradas.py`.
  - **Por quê:** sem fonte, o quadrante vira estimativa, que é exatamente o "achismo" que o Isvi apontou.
- [ ] **AutoTickets como fonte única determinística** (formato especificado em `docs/formato_exportacao_autotickets.md`; pendências em `semanas/2026-10-11_2026-10-17/_PENDENCIAS_AUTOTICKETS.md`).
  - **O que fazer:**
    - Quando os 4 bloqueios do CSV de Tarefas Executadas forem corrigidos (`fontes/autotickets/tarefas_executadas/_ANALISE_FONTE.md`), substituir a exportação do Voalle pelo CSV do AutoTickets.
    - Pedir ao AutoTickets um "pacote da semana" (todos os módulos em CSV + `manifest.json` com período, contagens e somas) e fazer o `checar_entradas.py` conferir o manifest.
  - **Por quê:** menos exportações manuais, menos divergência entre formatos e números reproduzíveis.
- [ ] **Apontamentos longos no Voalle.**
  - **O que fazer:** alerta automático para apontamentos acima de 8h ou que atravessam noite ou fim de semana, com correção antes da consolidação.
  - **Por quê:** os 3217119 (120h) e 3218766 (90h) do Liomar na semana 42 repetem a "distorção de 234h" da semana 41 e invalidam o confronto Voalle × Pontomais.
- [ ] *(Rebaixado: repositório de uso interno — decisão de 2026-10-19; o pre-commit só avisa)* **Histórico já publicado com dados sensíveis.**
  - **O que fazer:** avaliar mascarar esses arquivos e reescrever o histórico, como foi feito em 2026-10-19.
  - **Por quê:** o `mascarar_dados.py --check` acusa dados sensíveis em arquivos já commitados e enviados ao GitHub:
    - semana 40: CSVs de `acompanhamento_protocolos` com stream keys RTMP e senha de Wi-Fi de cliente; PDFs do Voalle (David, Isac);
    - semana 41: `fontes/voalle/isac.html` e `david.html` com senhas; CNPJ de MEI no CSV Fullcam e no relatório entregue;
    - semana 1–13/09: PDF do Voalle do Liomar.

## Problemas conhecidos (não são erros novos)

- Relatórios já entregues têm âncoras quebradas no índice (`python3 scripts/validar_indice.py semanas/*/report_ti_*`): semana 2026-10-04 (3.1–3.3), semana 2026-09-28 (3.x no `.md`; 1.4, 5.1 e 6.1 no `.html`) e semana 2026-09-01 (4.1–4.6 no `.md`). A causa (títulos com parênteses no índice da especificação) foi corrigida em `docs/especificacao_relatorio.md`; os arquivos entregues foram mantidos como estavam.
- As exportações HTML do Voalle referenciam pastas `*_files/` (CSS/JS do Voalle) que nunca foram versionadas. O conteúdo textual está completo.
- O lint de Markdown do VS Code mostra avisos de espaçamento e estilo de lista: cosméticos, sem efeito para as IAs.

## Concluídos

- [x] Caminho do AutoTickets configurável (`AUTOTICKETS_REPO`, com padrão `~/dev/autotickets_v2`) em `scripts/checar_entradas.py` (2026-10-19).
- [x] Máscara de CPF/CNPJ sem pontuação, e-mails de clientes, URLs RTMP e senhas em `scripts/mascarar_dados.py`, no pre-commit (inclusive PDFs) e no `checar_entradas.py` (2026-10-19).
- [x] Módulos `tarefas_executadas` e `anomalias_pppoe` no checklist e tópico condicional **8.4 Anomalias de Tráfego PPPoE** na especificação e no template (2026-10-19).

- [x] Contagem agrupada de demandas recorrentes → `docs/regras_metricas.md` §2.
- [x] Regras de abertura de protocolo → `docs/classificacao_protocolos.md`.
- [x] Lições do feedback de 2026-09-28 a 2026-10-04 → `docs/licoes_aprendidas.md` e `docs/regras_metricas.md`.
- [x] Diretório com informações distintas para consulta no harness → `docs/`.
- [x] Reorganização por semana, `AGENTS.md` como fonte única, templates e scripts (2026-10-19).
- [x] Remoção de dados sensíveis do histórico e recriação do repositório no GitHub (2026-10-19).
