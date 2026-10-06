# 📁 1. Dados e Exportações do ERP Voalle (1.voalle)

Este diretório contém relatórios de tarefas, chamados, solicitações internas, ordens de serviço e apontamentos de tempo exportados do ERP Voalle para cada colaborador de TI.

---

## 📄 Padrão de Nomenclatura dos Arquivos de Entrada

- `[Nome]_[Data-Inicio]-[Data-Fim].pdf` (ex.: `Liomar_2026-09-01_2026-09-15.pdf`)
- `[Nome]-[Data-Inicio]-[Data-Fim].csv`

---

## 🔍 Campos e Indicadores Chave para Mapeamento

Ao processar os arquivos do Voalle, a IA deve extrair:

- **Número do Protocolo e Título da Tarefa:** Identificação e escopo do atendimento.
- **Tipo de Solicitação:** (TI) Sol. Interna, (NOC), (N2-TI), Manutenção Programada, Infraestrutura, etc.
- **Datas e Horários:** Data de lançamento (DT), Hora de início e fim.
- **Horas Trabalhadas (HT):** Tempo total dedicado à demanda.
- **Progresso (%):** Percentual de conclusão da tarefa (0% a 100%).
- **Descrição e Relato Técnico:** Detalhamento da solução aplicada, peças substituídas (ex.: SSDs, cabos CAT6, switches, roteadores ONT Datacom) e configurações de rede (IPs, VLANs, interfaces).

Obs.: Incluído arquivo de preenchimento manual pra primeira análise: `Relatório de Visita Técnica Presencial - Setor TI.md`
