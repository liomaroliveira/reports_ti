# 📱 Harness de Comunicações e Históricos do WhatsApp (3.whatsapp_histories)

Este diretório gerencia a extração, sincronização semanal e análise inteligente das comunicações do **WhatsApp Business** do setor de TI da **Ten Internet**.

---

## 🏛️ Decisão Arquitetural: Banco de Dados SQLite (`.db`) vs. Extração Massiva em `.txt`

### 💡 Por que manter a base em SQLite (`database/msgstore.db`) é a melhor abordagem?

Após a análise do volume de dados (mais de **340 conversas ativas** e quase **40.000 mensagens**), a abordagem ideal para uso de Inteligência Artificial e geração dos relatórios executivos de TI é manter o banco SQLite como **Fonte Única da Verdade (Single Source of Truth)** em vez de re-exportar centenas de arquivos `.txt` toda semana.

| Critério | Manter em SQLite (`msgstore.db`) 🏆 | Ficar extraindo 340+ arquivos `.txt` ❌ |
| :--- | :--- | :--- |
| **Precisão Temporal** | **Cirúrgica:** Filtra via SQL com precisão de segundos (`WHERE timestamp BETWEEN start AND end`). | **Lenta e Imprecisa:** Requer percorrer e fazer parsing de 340 arquivos linha por linha. |
| **Consumo de Contexto (IA)** | **Mínimo:** Carrega apenas as mensagens da semana solicitada para a memória da IA. | **Excessivo:** Pode estourar limites de tokens e saturar buscas contextuais. |
| **Integridade do Git** | **Limpa:** O banco SQLite fica local (ignorado no `.gitignore`), evitando commits pesados. | **Poluída:** Diffs massivos no Git toda semana alterando centenas de arquivos de texto. |
| **Categorização Dinâmica** | **Instantânea:** Agrupa por tópicos (Campo, TI Interno, NOC, Coordenação) via query. | **Rígida:** Mistura assuntos e dificulta triagem de atendimentos operacionais. |
| **Sob Demanda** | Gera arquivos `.txt` ou `.md` apenas quando você ou a IA precisarem inspecionar um chat. | Gera cópias estáticas repetidas de conversas arquivadas há anos. |

---

## 📁 Estrutura do Diretório

```text
3.whatsapp_histories/
├── README.md                      # Este tutorial e manual de operações
├── key_64digits.txt               # Chave de 64 dígitos para descriptografia automática
├── input/                         # 📥 Onde você cola o novo backup semanal do celular
│   └── msgstore.db.crypt15        # (Arquivo mais recente gerado no celular)
├── database/                      # 🗄️ Banco de dados mestre SQLite descriptografado
│   └── msgstore.db                # (Atualizado automaticamente pelo script de sincronização)
├── scripts/                       # 🛠️ Harness de scripts de automação
│   ├── sync_backup.py             # Sincroniza o backup da pasta input/ para o database/
│   ├── query_history.py           # Consulta conversas por período semanal e por categoria
│   └── export_all_chats.py        # Exportador completo para .txt (caso queira auditar tudo)
├── exports/                       # 📄 Extratos gerados por semana (.md ou .json)
└── conversas_exportadas/          # 🗂️ Histórico inicial de conversas individuais em .txt
```

---

## 🔄 Rotina Semanal de Atualização (Passo a Passo para o Usuário)

Toda segunda-feira de manhã (ou quando desejar atualizar os dados para a IA), siga estes 3 passos simples:

### Passo 1: Gerar o Backup no Celular
1. No celular (WhatsApp Business), toque em **⋮ (três pontinhos)** > **Configurações**;
2. Vá em **Conversas** > **Backup de conversas**;
3. Toque no botão verde **Fazer backup**;
4. Aguarde a barra de progresso terminar (cerca de 30 a 60 segundos).

> [!NOTE]
> Como a criptografia de ponta a ponta com a chave de 64 dígitos já foi ativada uma vez, todos os backups futuros já serão gerados automaticamente com essa mesma chave. Você não precisa digitar a chave novamente no celular.

### Passo 2: Copiar o Arquivo para o Computador
1. Conecte o celular via cabo USB (ou envie o arquivo via Google Drive / Compartilhamento local);
2. No celular, acesse a pasta:
   ```text
   Armazenamento Principal > Android > media > com.whatsapp.w4b > WhatsApp > Databases
   ```
3. Copie o arquivo mais recente (geralmente chamado `msgstore.db.crypt15`) e cole dentro da pasta:
   ```text
   /home/liomarti/dev/reports_ti/3.whatsapp_histories/input/
   ```

### Passo 3: Executar a Sincronização
No terminal do projeto, execute o script de sincronização:
```bash
python3 3.whatsapp_histories/scripts/sync_backup.py
```
*(Ou simplesmente diga para a IA: **"Atualizei o backup do WhatsApp, sincronize os dados"**).*

O script irá:
1. Detectar o backup mais recente em `input/`;
2. Descriptografar automaticamente usando a chave de 64 dígitos;
3. Atualizar o banco SQLite mestre em `database/msgstore.db`;
4. Exibir o resumo de mensagens e última atividade dos canais de TI.

---

## 🔍 Como a IA e o Usuário Consultam os Dados da Semana

O utilitário `query_history.py` permite extrair exatamente o que o setor de TI precisa para cada tópico do relatório semanal:

### 1. Resumo Executivo da Semana (Métricas Gerais)
Gera o panorama com total de atendimentos por categoria e volume de mensagens:
```bash
python3 3.whatsapp_histories/scripts/query_history.py --start 2026-09-07 --end 2026-09-13 --format summary
```

### 2. Suporte ao Técnico de Campo (Tópico 6 do Relatório)
Filtra apenas os grupos operacionais de campo (*ServiceDesk Suporte ao técnico*, *Projetos TEN - Apoio ao Técnico*, *Ativações Rede Megas*, equipes volantes):
```bash
python3 3.whatsapp_histories/scripts/query_history.py --start 2026-09-07 --end 2026-09-13 --category campo --format md --output 3.whatsapp_histories/exports/extrato-campo.md
```

### 3. Suporte Interno / Informática e Setores (Tópico 5 do Relatório)
Filtra as demandas de hardware, acessos, manutenção e solicitações dos setores da empresa (*Tecnologia TEN*, *Manutenção de computadores*, Marketing, Cobrança, Financeiro, Estoque):
```bash
python3 3.whatsapp_histories/scripts/query_history.py --start 2026-09-07 --end 2026-09-13 --category interno --format md --output 3.whatsapp_histories/exports/extrato-interno.md
```

### 4. Incidentes de Rede e Infraestrutura (Tópico 4 do Relatório)
Filtra tratativas com parceiros de engenharia de rede (*Made4NOC*, *Consultoria*, *PliQCX*):
```bash
python3 3.whatsapp_histories/scripts/query_history.py --start 2026-09-07 --end 2026-09-13 --category incidentes --format md --output 3.whatsapp_histories/exports/extrato-incidentes.md
```

### 5. Alinhamentos Estratégicos com a Coordenação
Filtra as decisões e orientações diretas trocadas com o Coordenador de TI (*Isvi Neemias*):
```bash
python3 3.whatsapp_histories/scripts/query_history.py --start 2026-09-07 --end 2026-09-13 --category coordenacao --format md
```

---

## 🤖 Regras Obrigatórias para a IA (Consolidação de Relatórios)

Ao elaborar os relatórios semanais (`0.individual_report/` e `4.weekly_reports/`):
1. **Verificação de Base:** A IA deve checar se a data máxima de `message.timestamp` em `database/msgstore.db` cobre o período semanal a ser reportado. Caso o banco esteja desatualizado e exista um novo arquivo em `input/`, executar `sync_backup.py`.
2. **Uso de Queries Cirúrgicas:** A IA não deve ler arquivos de texto completos de semanas anteriores; deve sempre invocar `query_history.py` com o intervalo semanal exato (`--start YYYY-MM-DD --end YYYY-MM-DD`).
3. **Alimentação Direta dos Tópicos:**
   - As mensagens de `--category campo` alimentam o **Tópico 6 (Suporte ao Técnico de Campo)** (contabilizando protocolos de provisionamento de ONT, suporte a CTOs e trocas de estrutura).
   - As mensagens de `--category interno` alimentam o **Tópico 5 (Suporte Interno)** (manutenções de notebooks, e-mails, acessos, impressoras).
   - As mensagens de `--category incidentes` alimentam o **Tópico 4 (Incidentes Tratados)** (rompimentos de rota, falhas de energia, mitigação Made4NOC).
   - As orientações de Liomar ao time ou decisões de Isvi alimentam os **Tópicos 1, 2 e 8**.
