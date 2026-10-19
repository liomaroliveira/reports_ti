# 📁 2. Plataforma e Automações AutoTickets (2.autotickets)

Este diretório gerencia os dados de desenvolvimento, sprints, integrações e entregas da plataforma **AutoTickets**, desenvolvida e mantida por Liomar Oliveira para unificação e automação de fluxos operacionais na Ten Internet.

---

## 💻 Repositório Local de Desenvolvimento
- **Caminho Absoluto:** `/home/liomarti/dev/autotickets-v2`
- **Mecanismo de Mineração de Commits:**  
  Caso não haja arquivo de exportação em `2.autotickets/`, a IA deve inspecionar o histórico de commits do git diretamente no diretório do projeto para o período especificado:
  ```bash
  git -C /home/liomarti/dev/autotickets-v2 log --since="[data_inicio] 00:00:00" --until="[data_fim] 23:59:59" --pretty=format:"%h - %an, %ad : %s" --date=iso
  ```

---

## 📊 Subdiretórios de Relatórios Analíticos de Automação

O AutoTickets gera relatórios automáticos especializados que devem ser analisados para compor o **Macro-Tópico 4 (Plataforma e Automações AutoTickets)** do relatório semanal:

```text
2.autotickets/
├── colaborador_x_ticket/                  # Cruzamento analítico de produtividade: volume de tickets por colaborador (alimenta Tópicos 1 e 2 em conjunto com 1.voalle/)
├── fullcam_automacao_inadimplencia/       # Relatórios de suspensão/reativação automática por inadimplência no Fullcam (.md, .csv, .html -> Subtópico 4.4)
├── fullcam_automacao_instalacao_camera/   # Relatórios da esteira automática de provisionamento e instalação de câmeras (.md, .csv, .html -> Subtópico 4.4)
├── fullcam_lucros_prejuizos/              # Auditoria financeira completa de contratos, faturamento e custos (.csv, .pdf -> Subtópico 4.3 na íntegra)
├── problemas_recorrentes/                 # Mineração de falhas crônicas e apontamentos repetitivos no parque
├── produtividade_geral/                   # Horas técnicas de esforço humano economizadas e ganhos de escala (Subtópico 4.5)
├── wifeed_daily_update_voucher/           # Auditoria da sincronização diária de vouchers WiFeed com gráfico SVG e envios (.md, .html -> Subtópico 4.2 na íntegra)
└── old/                                   # Arquivos tratados e exportações de semanas anteriores
```

---

## 📌 Regras de Ingestão e Tratamento de Dados

1. **Regra de Arquivos Multi-Formato:**
   - Relatórios que compartilham o mesmo nome base em extensões diferentes (ex.: `.md`, `.html`, `.csv`, `.pdf`) são rigorosamente o **mesmo relatório consolidado sobre os mesmos dados brutos**.
   - A IA deve verificar apenas as particularidades entre eles (como gráficos SVG no HTML ou colunas adicionais no CSV) e tratá-los de forma unificada, sem duplicar o processamento ou considerá-los fontes conflitantes.

2. **Cruzamento `colaborador_x_ticket` com `1.voalle/`:**
   - O relatório `colaborador_x_ticket/` é gerado com base no banco de dados do Voalle e serve como **fonte métrica primária** para o Tópico 1 (Balanço da fila: saídas ÷ entradas) e Tópico 2 (produtividade por colaborador, TMA, TMR e taxa de resolubilidade).
   - O diretório `1.voalle/[colaborador]/` complementa com os relatos narrativos detalhados, justificativas de tempo e apontamentos individuais de cada protocolo.

---

## 🎯 Principais Frentes e Módulos do AutoTickets
- **Métricas de Produtividade & ROI de Software:** Quantificação em horas humanas do trabalho manual eliminado por automações (ex.: rotina diária do WiFeed poupando intervenção humana do TI e mantendo a base 100% adimplente).
- **Integrações de Rede e NOC:** Telemetria óptica, RADIUS logs em tempo real, sync de IPs CGNAT, monitoramento ping e alertas.
- **Módulo de Atendimento e Tickets:** Desacoplamento e otimização de modais do Voalle, busca de clientes, filtros avançados e chat omnichannel.
- **Arquitetura e Qualidade:** Arquitetura Local-First (Duplo Cursor Monotônico), Orquestrador Multi-Provedor com telemetria de tokens de IA, Servidor MCP Oficial (`laravel/mcp`) e design Glassmorphism.

