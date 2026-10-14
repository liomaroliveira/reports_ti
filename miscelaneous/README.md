# 📦 Repositório Frio e Arquivos Legados (miscelaneous)

> [!WARNING]
> **REGRA MANDATÓRIA DO HARNESS:**
> Os arquivos e subdiretórios contidos neste diretório **NÃO DEVEM SER LIDOS AUTOMATICAMENTE** durante a execução do fluxo semanal de geração de relatórios pelo `PROMPT.md`.
>
> Este diretório funciona como um backup frio de ferramentas, documentações legadas e históricos que só devem ser consultados **quando o usuário solicitar expressamente** nas instruções contextuais da semana.

---

## 📂 Conteúdo do Diretório

```text
miscelaneous/
├── README.md              # Este manual de diretrizes
├── litellm_gateway/       # Documentação operacional, scripts, compose e backups do gateway LiteLLM
└── whatsapp_histories/    # Harness legado de comunicações de WhatsApp (banco SQLite msgstore.db, backups crypt15, chaves e scripts de extração)
```

---

## 🔍 Descrição dos Subdiretórios

1. **`litellm_gateway/`:**
   - Contém manuais de operação (`LITELLM_OPERATIONS_MANUAL.md`), configurações de modelos YAML, scripts de sincronização para VM e rotinas de backup da base PostgreSQL do LiteLLM.
   - Serve para consulta sob demanda quando houver manutenção no gateway de Inteligência Artificial.

2. **`whatsapp_histories/`:**
   - Base histórica de mensagens exportadas e banco relacional descriptografado de comunicações com clientes internos, coordenação e fornecedores (Made4NOC, PliQ).
   - Movido para este repositório frio para evitar sobrecarga de contexto e tokens na execução rotineira do modelo de IA.
