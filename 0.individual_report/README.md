# 📁 0. Relatórios Individuais (0.individual_report)

Este diretório armazena os relatórios de atividades individuais de cada membro da equipe do setor de TI da Ten Internet.

---

## 👥 Estrutura de Subdiretórios por Colaborador
```text
0.individual_report/
├── liomar/    # Liomar Antonio de Oliveira (Analista de TI Sênior / Supervisor)
├── isac/      # Isac Costa Silva (Assistente de TI Pleno)
└── david/     # David Brasil Fernandes (Auxiliar de TI Junior)
```

---

## 📄 Padrão de Nomenclatura dos Arquivos
Os arquivos individuais devem seguir o padrão:
- `[data_inicio]-[data_fim].md` (ex.: `2026-09-07-2026-09-13.md`)
- `[data_inicio]-[data_fim].html` (ex.: `2026-09-07-2026-09-13.html`)
- `[data_inicio]-[data_fim].pdf` (ex.: `2026-09-07-2026-09-13.pdf`)

---

## 🔍 Regra de Fallback e Mineração Ativa
Quando um colaborador **NÃO** tiver entregue seu relatório individual consolidado:
1. A IA deve realizar a varredura nas seguintes fontes de dados:
   - **`1.voalle/`**: Tarefas, chamados, O.S. e apontamentos de horas.
   - **`2.autotickets/`**: Commits no repositório `/home/liomarti/dev/autotickets-v2` e exportações.
   - **`3.whatsapp_histories/`**: Grupos operacionais e contatos diretos.
2. A IA compila e gera o relatório individual do colaborador em seu subdiretório correspondente antes de gerar o relatório semanal consolidado.
