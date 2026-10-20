# 🎓 Lições Aprendidas (Feedbacks da Coordenação)

Consolidado dos pareceres de Isvi Neemias. Os pareceres completos ficam em `semanas/<semana>/feedback.md`. As regras de cálculo derivadas destes feedbacks estão em `docs/regras_metricas.md`.

> Ao receber um novo feedback: salvar em `semanas/<semana>/feedback.md`, adicionar aqui uma seção com as lições e pendências, e atualizar `docs/regras_metricas.md` se mudar alguma regra.

---

## Semana 2026-10-04 a 2026-10-10 (feedback em `semanas/2026-10-04_2026-10-10/feedback.md`)

### Correções e orientações
- **Fullcam:** a regra do módulo pegou um contrato sem câmera (96660, DAVID BRASIL FERNANDES, faturas de cerca de R$ 10/mês, sem etiqueta do serviço). Ignorar o registro até a correção → `docs/regras_metricas.md` §11.
- **Apontamentos (play aberto):** o Liomar teve 274h17 apontadas com solicitações deixadas em play. Combinado: **fechar os relatos no fim do expediente** e **pausar ao focar em outra atividade** → `docs/regras_metricas.md` §3.
- **Frota:** o Isvi levou o problema ao Edriano (COO), e Frota fica em Suprimentos e Logística. Continuar registrando cada ocorrência (horário combinado × liberado, impacto).

### Pendências a acompanhar nos próximos relatórios
- ⚠️ **Slack × AutoTickets:** reunião de escopo no fim do mês. Adiantar o armazenamento seguro (criptografia, retenção indeterminada, acesso com MFA simultâneo de 3 entre 6: TI, Isvi, Edriano – COO, Saulo – CEO, RH e DP). **Exibir com marca de atenção** no tópico apropriado (3 ou 9.3) até ser concluída.
- **Descrição de cargos:** protocolo 3218356 (documentos institucionais com o RH). O Isvi refaz os cargos do TI para validar com o RH até o fim de novembro.
- **Gincana de pentest:** até 9h por pessoa na semana de 18 a 24/10, começando por compras.teninternet.com.br (continuidade do incidente 3218766). Relatório à parte, com falhas, risco, correções e melhorias; resumo no semanal. Depois: sistemas do Isvi, outro de Daniel, Ciclos (Edriano) e os de terceiros (Voalle, PliQ, Fortics, Power BIs).

### Mudanças no harness (2026-10-19)
- Tópicos dinâmicos (📈 Destaques Analíticos) e condicionais (8.4 PPPoE) → `docs/especificacao_relatorio.md`, "Classes de Tópicos".
- `scripts/validar_relatorio.py` confere a tabela de acompanhamento do feedback (uma linha por observação).
- Voalle por **Lançamento**. O formato-alvo do AutoTickets é o pacote semanal em JSON (`docs/formato_exportacao_autotickets.md`).

---

## Semana 2026-09-28 a 2026-10-04 (feedback em `semanas/2026-09-28_2026-10-04/feedback.md`)

### O propósito do relatório
O relatório deve responder "foi bom?", "para onde estamos apontando?", "o que precisa mudar?" — não apenas "o que fizemos". As 8 funções: registrar fatos, apresentar resultados, analisar situações, dar visibilidade, apoiar decisões, acompanhar evolução, criar histórico e recomendar ações. "O óbvio precisa ser dito."

### Correções aplicadas ao harness
- Período Domingo a Sábado, com período operacional efetivo Segunda a Sexta.
- "Resolutividade" → "Balanço da fila (saídas ÷ entradas)".
- Horas Voalle × Pontomais com justificativa da divergência.
- Todo apoio ao campo com protocolo; totais do texto = totais das tabelas.
- Reincidência com janela de 30 dias.
- Índice sem seções inexistentes.
- Disponibilidade sem "achismo"; ocorrências de sistema à parte.
- Backups com o quadrante de 4 pilares.

### Pendências e orientações a acompanhar nos próximos relatórios
- **Wazuh/VPN:** status das filiais, percentual e novo prazo; registrar a mudança de prioridade com o motivo.
- **Teste de restauração:** estruturar rotina (ex.: 1–2 VMs por mês em rodízio), em caráter secundário.
- **Prioridade principal:** evolução do serviço de **telefonia fixa**.
- **Veículos:** David envia report semanal direto à Coordenação (data, protocolo, horário combinado × recebido, impacto).
- **Windows 10 × 11:** definir padrão para novas instalações e informar situação das licenças.
- **Slack × AutoTickets (#3210508):** alinhamento de LGPD e regras do Slack antes de produção.
- **ChatSeguro:** cancelamento solicitado em 30/09 (aviso de 30 dias).
- **Chave OpenAI:** Coordenação ofereceu gerar chave para o AutoTickets.
