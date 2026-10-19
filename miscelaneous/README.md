# 📦 Base de Conhecimento Fora do Escopo dos Relatórios (miscelaneous)

> [!WARNING]
> **REGRA MANDATÓRIA DO HARNESS:**
> Nada neste diretório é fonte de dados dos relatórios semanais. A IA **NÃO DEVE LER** este diretório durante a geração dos relatórios (individuais ou consolidados), nem no fallback.

---

## 📂 Conteúdo do Diretório

```text
miscelaneous/
├── README.md              # Este documento
└── whatsapp_histories/    # Conhecimento técnico: como extrair o banco do WhatsApp (msgstore.db) direto do aparelho
```

---

## 🔍 Descrição

1. **`whatsapp_histories/`:**
   - Guardado **apenas a título de conhecimento**: tutorial e scripts que descriptografam o backup `msgstore.db.crypt15` exportado do celular e consultam as mensagens via SQLite, sem os limites da exportação manual do aplicativo.
   - Não contém conversas, backups, bancos ou chaves — esses arquivos ficam somente na máquina local e são bloqueados pelo `.gitignore`.
