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

O AutoTickets gera relatórios automáticos especializados que devem ser analisados para compor o **Subtópico 3.1.4 (Impacto Operacional e Métricas de Produtividade das Automações)**:

```text
2.autotickets/
├── colaborador_x_ticket/                  # Cruzamento analítico de produtividade: volume de tickets por colaborador
├── fullcam_automacao_inadimplencia/       # Relatórios de suspensão/reativação automática por inadimplência no Fullcam (.md, .csv, .html)
├── fullcam_automacao_instalacao_camera/   # Relatórios da esteira automática de provisionamento e instalação de câmeras
├── fullcam_lucros_prejuizos/              # Indicadores de perdas financeiras evitadas e faturamento garantido por automações
├── problemas_recorrentes/                 # Mineração de falhas crônicas e apontamentos repetitivos no parque
├── produtividade_geral/                   # Horas técnicas de esforço humano economizadas e ganhos de escala
├── wifeed_daily_update_voucher/           # Auditoria da automação diária de sincronização de vouchers WiFeed (clientes adimplentes, variação diária e churn)
└── old/                                   # Arquivos tratados e exportações de semanas anteriores
```

---

## 🎯 Principais Frentes e Módulos do AutoTickets
- **Métricas de Produtividade & ROI de Software:** Quantificação em horas humanas do trabalho manual eliminado por automações (ex.: rotina diária do WiFeed poupando intervenção humana do TI e mantendo a base 100% adimplente).
- **Integrações de Rede e NOC:** Telemetria óptica, RADIUS logs em tempo real, sync de IPs CGNAT, monitoramento ping e alertas.
- **Módulo de Atendimento e Tickets:** Desacoplamento e otimização de modais do Voalle, busca de clientes, filtros avançados e chat omnichannel.
- **Arquitetura e Qualidade:** Arquitetura Local-First (Duplo Cursor Monotônico), Orquestrador Multi-Provedor com telemetria de tokens de IA, Servidor MCP Oficial (`laravel/mcp`) e design Glassmorphism.

