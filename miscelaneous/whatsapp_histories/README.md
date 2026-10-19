# 📱 Extração do Banco de Dados do WhatsApp (msgstore.db)

> [!NOTE]
> **Guardado apenas como conhecimento.** Este diretório documenta como extrair todas as conversas do WhatsApp diretamente do backup criptografado do aparelho, sem os limites da exportação manual do aplicativo (que exporta uma conversa por vez e corta o histórico).
>
> **Não é fonte de dados dos relatórios semanais** e não deve ser lido pela IA durante a geração deles.

---

## 💡 Por que extrair o banco em vez de exportar conversas pelo app?

| Critério | Banco SQLite (`msgstore.db`) 🏆 | Exportação manual pelo app ❌ |
| :--- | :--- | :--- |
| **Cobertura** | Todas as conversas e grupos de uma vez (testado com 340+ conversas e ~40.000 mensagens). | Uma conversa por vez, com limite de mensagens. |
| **Precisão temporal** | Filtro por SQL com precisão de segundos (`WHERE timestamp BETWEEN ...`). | Parsing de arquivos `.txt` linha por linha. |
| **Consumo de contexto (IA)** | Carrega só o período e as categorias pedidas. | Arquivos inteiros, estoura limite de tokens. |
| **Categorização** | Agrupamento por grupo/categoria via query. | Assuntos misturados. |

---

## 📁 Estrutura

```text
whatsapp_histories/
├── README.md                  # Este tutorial (versionado)
├── scripts/                   # Versionados
│   ├── sync_backup.py         # Descriptografa o .crypt15 de input/ para database/msgstore.db
│   ├── query_history.py       # Consulta mensagens por período e categoria
│   └── export_all_chats.py    # Exporta todas as conversas para .txt
│
│   # ↓ Somente locais — bloqueados pelo .gitignore (dados pessoais e chave)
├── key_64digits.txt           # Chave de 64 dígitos do backup criptografado
├── contatos_conhecidos.json   # Mapa opcional {"55DDDNUMERO": "Nome"} para nomear remetentes
├── input/                     # Onde se coloca o msgstore.db.crypt15 copiado do celular
├── database/                  # msgstore.db descriptografado
├── vcards/                    # (opcional) .vcf para enriquecer nomes de contatos
├── exports/                   # Saídas do query_history.py
└── conversas_exportadas/      # Saídas do export_all_chats.py
```

---

## 🔑 Pré-requisitos (uma única vez)

1. **Ativar o backup criptografado de ponta a ponta com chave de 64 dígitos** no celular:
   WhatsApp ▸ ⋮ ▸ Configurações ▸ Conversas ▸ Backup de conversas ▸ Backup criptografado de ponta a ponta ▸ *Usar chave de criptografia de 64 dígitos*.
   Anote a chave e salve-a em `key_64digits.txt` (uma linha, 64 caracteres hexadecimais). **Nunca versione este arquivo.**
2. **Instalar o descriptografador** `wadecrypt` (pacote `wa-crypt-tools`) no `.venv` da raiz do repositório:
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install wa-crypt-tools
   ```

---

## 🔄 Passo a passo da extração

### 1. Gerar o backup no celular
WhatsApp ▸ ⋮ ▸ Configurações ▸ Conversas ▸ Backup de conversas ▸ **Fazer backup**. Com a chave de 64 dígitos ativada, todo backup novo já sai criptografado com ela.

### 2. Copiar o arquivo para o computador
No celular, copie o arquivo mais recente de:
```text
Armazenamento interno > Android > media > com.whatsapp.w4b > WhatsApp > Databases > msgstore.db.crypt15
```
(`com.whatsapp.w4b` é o WhatsApp Business; no WhatsApp comum é `com.whatsapp`.)
Cole em `miscelaneous/whatsapp_histories/input/`.

### 3. Descriptografar
```bash
python3 miscelaneous/whatsapp_histories/scripts/sync_backup.py
```
O script pega o `.crypt15` mais recente de `input/`, descriptografa com a chave e grava `database/msgstore.db`, exibindo um resumo das mensagens.

### 4. Consultar
```bash
# Panorama de um período
python3 miscelaneous/whatsapp_histories/scripts/query_history.py --start 2026-09-07 --end 2026-09-13 --format summary

# Uma categoria em Markdown (campo | interno | coordenacao | incidentes | all)
python3 miscelaneous/whatsapp_histories/scripts/query_history.py --start 2026-09-07 --end 2026-09-13 \
  --category campo --format md --output miscelaneous/whatsapp_histories/exports/extrato-campo.md

# Exportar todas as conversas para .txt
python3 miscelaneous/whatsapp_histories/scripts/export_all_chats.py
```

As categorias são definidas por regras de nome de grupo em `CATEGORY_RULES` dentro de `query_history.py`.
