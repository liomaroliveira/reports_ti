# 🛠️ Pontos a Melhorar (Backlog do Harness)

Melhorias do próprio processo de geração e problemas conhecidos. Quando uma melhoria virar regra, mova-a para o documento definitivo e marque como concluída aqui.

## Pendentes

- [ ] Completar o `docs/glossario.md` com termos e jargões internos (setores, siglas de equipes, nomes de grupos).
- [ ] Criar `docs/empresa.md` descrevendo setores, filiais e estrutura, para dar contexto à IA.
- [ ] Nomes dos relatórios do AutoTickets: incluir o **período coberto** no nome do arquivo (hoje trazem só a data de geração).
- [ ] AutoTickets: gerar a auditoria Fullcam já com CPF mascarado na origem.
- [ ] Reinserir em `docs/referencias/` as imagens de exemplo da abertura de tarefas no Voalle, citadas em `docs/classificacao_protocolos.md` (as originais `image/PONTOS_A_MELHORAR/*.png` não estavam no repositório).
- [ ] (Opcional) Tornar o caminho do `autotickets-v2` configurável por variável de ambiente em `scripts/checar_entradas.py`.
- [ ] (Opcional) Mascarar também **telefones de clientes** nas exportações brutas do Voalle (hoje só CPFs são mascarados).

## Problemas conhecidos (não são erros novos)

- Relatórios já entregues têm âncoras quebradas no índice (`python3 scripts/validar_indice.py semanas/*/report_ti_*`): semana 2026-10-04 (3.1–3.3), semana 2026-09-28 (3.x no `.md`; 1.4, 5.1 e 6.1 no `.html`) e semana 2026-09-01 (4.1–4.6 no `.md`). A causa (títulos com parênteses no índice da especificação) foi corrigida em `docs/especificacao_relatorio.md`; os arquivos entregues foram mantidos como estavam.
- As exportações HTML do Voalle referenciam pastas `*_files/` (CSS/JS do Voalle) que nunca foram versionadas. O conteúdo textual está completo.
- O lint de Markdown do VS Code mostra avisos de espaçamento e estilo de lista: cosméticos, sem efeito para as IAs.

## Concluídos

- [x] Contagem agrupada de demandas recorrentes → `docs/regras_metricas.md` §2.
- [x] Regras de abertura de protocolo → `docs/classificacao_protocolos.md`.
- [x] Lições do feedback de 2026-09-28 a 2026-10-04 → `docs/licoes_aprendidas.md` e `docs/regras_metricas.md`.
- [x] Diretório com informações distintas para consulta no harness → `docs/`.
- [x] Reorganização por semana, `AGENTS.md` como fonte única, templates e scripts (2026-10-19).
- [x] Remoção de dados sensíveis do histórico e recriação do repositório no GitHub (2026-10-19).
