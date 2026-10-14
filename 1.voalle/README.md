# 📁 1. Dados e Exportações do ERP Voalle (1.voalle)

Este diretório armazena os relatórios de tarefas, chamados, solicitações internas, ordens de serviço e apontamentos de tempo exportados do ERP Voalle, organizados por colaborador de TI.

---

## 👥 Estrutura de Subdiretórios por Colaborador

```text
1.voalle/
├── liomar/    # Exportações de Liomar Antonio de Oliveira (#107184)
├── isac/      # Exportações de Isac Costa Silva (#94562)
├── david/     # Exportações de David Brasil Fernandes (#116367)
└── 2026-06/   # Históricos e exportações legadas arquivadas
```

---

## 📄 Padrão de Nomenclatura e Formatos Suportados

Os arquivos exportados pelo ERP Voalle devem ser salvos dentro da pasta de cada colaborador, podendo estar nos formatos **HTML**, **PDF** ou **CSV**:

- `[Nome]-[Data-Inicio]_[Data-Fim].html` (ex.: `Liomar-2026-10-04_2026-10-10.html`)
- `[Nome]-[Data-Inicio]_[Data-Fim].pdf` (ex.: `David-2026-10-04_2026-10-10.pdf`)
- `[Nome]-[Data-Inicio]_[Data-Fim].csv`

---

## 🔍 Campos e Indicadores Chave para Mapeamento

Ao processar os arquivos do Voalle, a IA deve extrair:

- **Número do Protocolo e Título da Tarefa:** Identificação e escopo do atendimento.
- **Tipo de Solicitação:** (TI) Sol. Interna, (NOC), (N2-TI), Manutenção Programada, Infraestrutura, etc.
- **Datas e Horários:** Data de lançamento (DT), Hora de início e fim.
- **Horas Trabalhadas (HT):** Tempo total dedicado à demanda para consolidação de produtividade.
- **Progresso (%):** Percentual de conclusão da tarefa (0% a 100%).
- **Descrição e Relato Técnico:** Detalhamento da solução aplicada, peças substituídas (ex.: SSDs, fontes, switches, roteadores ONT Datacom) e configurações de rede (IPs, VLANs, interfaces).
- **Confronto com Ponto:** Cruzar o somatório de HT com o registro de ponto real no Pontomais, justificando qualquer divergência identificada.

