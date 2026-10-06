# 📁 0. Relatórios Individuais (0.individual_report)

Este diretório armazena os relatórios de atividades individuais de cada membro da equipe do setor de TI da Ten Internet.

---

## 👥 Estrutura de Subdiretórios por Colaborador

```text
0.individual_report/
├── liomar/    # Liomar Antonio de Oliveira (Analista de TI Sênior)
│   └── old/   # Versões legadas e relatórios de semanas anteriores arquivados
├── isac/      # Isac Costa Silva (Assistente de TI Pleno)
│   └── old/   # Relatórios de semanas anteriores arquivados
└── david/     # David Brasil Fernandes (Auxiliar de TI Junior)
    └── old/   # Relatórios de semanas anteriores arquivados
```

---

## 📄 Padrão de Nomenclatura dos Arquivos

Os arquivos individuais devem seguir o padrão:

- `[data_inicio]_[data_fim].md` (ex.: `2026-09-07_2026-09-13.md`)
- `[data_inicio]_[data_fim].html` (ex.: `2026-09-07_2026-09-13.html`)
- `[data_inicio]_[data_fim].pdf` (ex.: `2026-09-07_2026-09-13.pdf`)

---

## 🔍 Regra de Validação e Fallback

1. **Arquivo Pré-existente no Período:** Quando já houver arquivo dentro do período na pasta do colaborador (seja `.pdf`, `.md` ou `.html`), **NÃO é necessário gerar um novo relatório individual**. O arquivo existente é a fonte oficial das entregas do membro e deve ser lido e considerado diretamente na confecção do relatório semanal em `4.weekly_reports/`.
2. **Mineração Ativa (Fallback):** Quando um colaborador **NÃO** possuir arquivo consolidado para o período:
   - A IA realiza a varredura nas fontes de dados:
     - **`1.voalle/`**: Tarefas, chamados, O.S. e apontamentos de horas.
     - **`2.autotickets/`**: Commits no repositório `/home/liomarti/dev/autotickets-v2` e exportações.
     - **`3.whatsapp_histories/`**: Grupos operacionais e contatos diretos.
   - A IA compila e gera o relatório individual do colaborador em seu subdiretório correspondente antes de gerar o relatório semanal consolidado.
