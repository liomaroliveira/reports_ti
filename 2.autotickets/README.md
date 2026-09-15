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

## 🎯 Principais Frentes e Módulos do AutoTickets
- **Integrações de Rede e NOC:** Telemetria óptica, RADIUS logs em tempo real, sync de IPs CGNAT, monitoramento ping e alertas.
- **Módulo de Atendimento e Tickets:** Desacoplamento e otimização de modais do Voalle, busca de clientes, filtros avançados e chat omnichannel.
- **Arquitetura e Frontend:** Modernização de stack (React 19, Tailwind v4, componentes atômicos, design system Apple Bento Grid e temas acessíveis).
- **Testes e Qualidade:** Suíte de testes E2E com Playwright e auditoria visual automatizada.
