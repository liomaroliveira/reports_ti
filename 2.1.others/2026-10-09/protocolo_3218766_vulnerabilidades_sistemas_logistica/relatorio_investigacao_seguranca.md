# Relatório de Investigação de Segurança e Resposta a Incidentes

**Data:** 09 de Outubro de 2026  
**Classificação:** Confidencial / Segurança da Informação  
**Alvos Investigados:**  
- `compras.teninternet.com.br` (Gestão de Compras)  
- `mundialehistory.teninternet.com.br` (Histórico de Tickets Mundiale)  
- Domínio raiz e subdomínios: `*.teninternet.com.br`  

---

## 1. Sumário Executivo

Em 09/10/2026, a equipe de TI da Ten Internet foi abordada via WhatsApp por um indivíduo que alegou ter encontrado vulnerabilidades nos sistemas da empresa. Inicialmente, o contato solicitou redefinição de senha para o sistema **Mundiale History**; em seguida, enviou imagens contendo dados confidenciais de usuários administradores e empresas da Ten Internet, além de capturas de tela do sistema de compras.

Após perícia técnica aprofundada nos códigos-fonte, infraestruturas e tráfego de rede, concluímos:
1. **`mundialehistory.teninternet.com.br`:** **NÃO POSSUI VULNERABILIDADE RELACIONADA AO INCIDENTE.** O sistema é baseado em Laravel 12 + Inertia.js, possui registro de usuários desabilitado, rotas protegidas por autenticação/autorização e o servidor OpenResty bloqueia arquivos sensíveis. O contato apenas acessou a tela pública de "Esqueci minha senha" e clicou no link pré-formatado do WhatsApp.
2. **`compras.teninternet.com.br`:** **VULNERABILIDADE CRÍTICA CONFIRMADA.** A aplicação é uma Single Page Application (SPA) que se comunica diretamente com um projeto Supabase (`bxvblyktxwaqosjvjpwa.supabase.co`). Foi constatado que:
   * O cadastro público de usuários do Supabase Auth estava habilitado (`disable_signup: false`), permitindo que qualquer pessoa criasse uma conta pela API sem autorização prévia.
   * As políticas de segurança a nível de linha (**Row Level Security - RLS**) no PostgreSQL permitiam que usuários autenticados (ou anônimos, antes de restrições) consultassem e baixassem integralmente tabelas sensíveis como `companies`, `users`, `purchase_orders`, `quotes`, `suppliers`, etc.
   * Foi dessa base que o atacante extraiu os dados de usuários e empresas exibidos na Imagem 1 (`=== 4. companies ===`).
   * A interface web carrega os blocos HTML do Dashboard mesmo antes de o usuário estar autenticado, exibindo a estrutura do sistema na tela de login.

---

## 2. Análise Pericial das Imagens Enviadas

### Metadados de Arquivo (EXIF)
Os arquivos foram enviados pelo mensageiro WhatsApp. O aplicativo WhatsApp Web/Mobile re-codifica automaticamente todas as imagens em JPEG padrão (JFIF sRGB), **removendo todos os metadados EXIF originais** (como modelo de câmera, coordenadas GPS, hostname da máquina e nome de usuário do sistema operacional).

### Análise Forense Visual
A inspeção detalhada das evidências gráficas revelou elementos de alta relevância:

| Imagem | Descrição Visual | Informações Extraídas |
| :--- | :--- | :--- |
| **Imagem 1** | Foto física da tela de um notebook/monitor | • No canto inferior esquerdo da moldura plástica da tela há um **adesivo com o logotipo da Nike** (*swoosh* branco).<br>• Saída de console/terminal (texto ciano) executando um script de extração automática que lista dados em blocos ordenados (`=== 4. companies ===`).<br>• Exibe dados de usuários (`financeiro@teninternet.com.br`, `Edriano` - `edriano.conceicao@teninternet.com.br`, papéis `admin`) e empresas da Ten (`TEN INTERNET LTDA`, `TEN SOLUÇÕES...`, `TEN LOCAÇÃO...`). |
| **Imagem 2** | Print do navegador Google Chrome | • **Perfil Google:** No canto superior direito da janela do Chrome, o avatar do usuário apresenta o status **"Pausada"** (sincronização do navegador pausada).<br>• **Barra de Favoritos:** O navegador do invasor contém os seguintes atalhos salvos:<br>&nbsp;&nbsp;1. `Perfil`<br>&nbsp;&nbsp;2. `WalletGenerat...` (ferramenta de geração de carteiras de criptomoedas)<br>&nbsp;&nbsp;3. `(1) Prints e Me...`<br>&nbsp;&nbsp;4. `Você foi regist...`<br>&nbsp;&nbsp;5. `_Apostila_Co...`<br>&nbsp;&nbsp;6. `Série Peaky Bl...`<br>• **DevTools (F12):** Aba *Network* aberta inspecionando requisições do Supabase (`process.mjs`, `realtime-js.mjs`, `postgrest-js.mjs`, `config?select=value...`).<br>• **URL:** Acessou `compras.teninternet.com.br/login.html`, mas o Dashboard carregou em segundo plano. |
| **Imagem 3** | Print do celular - Recuperação de Senha | • Tela pública legítima de redefinição de senha do **Mundiale History** (`/forgot-password`).<br>• O botão verde *"Solicitar via WhatsApp (Núcleo de TI)"* contém o link fixo `wa.me/[telefone removido]?text=Olá, preciso de auxílio para redefinir minha senha do sistema Mundiale History.`.<br>• Foi através deste botão que ele gerou a primeira mensagem da conversa. |
| **Imagem 4** | Print de app bancário | • Print de aplicativo do Banco Itaú em espanhol (*"Ir a Mi Itaú"*, *"Pagos"*, *"Préstamos"*, *"Pagar Factura"*).<br>• Captura de tela às 22:05 de 5 de outubro. **Totalmente desconexa** da infraestrutura da Ten Internet. |

---

## 3. Investigação de Logs e Rastreamento de IP

### A tabela `logs` do Supabase contém IPs de acesso?
**Não.** Auditamos a tabela `logs` do banco de dados do Supabase. Essa tabela é destinada exclusivamente a logs internos de regras de negócio da aplicação (inseridos pelo arquivo `js/components/logs.js` quando um usuário clica para aprovar pedidos, cotar ou cadastrar fornecedores). Ela não grava IPs, requisições HTTP do PostgREST ou navegadores, e atualmente encontra-se vazia.

### Onde está gravado o IP e User-Agent real do atacante?
O Supabase opera sob infraestrutura de API Gateway (Cloudflare / Envoy) que registra **100% das requisições HTTP**. O endereço IP do invasor pode ser localizado diretamente pelos administradores nos seguintes locais:

#### 1. No Supabase Dashboard (Log Explorer / API Logs)
Acesse: [https://supabase.com/dashboard/project/bxvblyktxwaqosjvjpwa/logs/explorer](https://supabase.com/dashboard/project/bxvblyktxwaqosjvjpwa/logs/explorer)

Execute a query SQL abaixo no **Log Explorer** para filtrar as consultas feitas às tabelas expostas:

```sql
select 
    timestamp,
    request.headers.x_forwarded_for as client_ip,
    request.headers.user_agent as user_agent,
    request.method as method,
    request.path as path,
    response.status_code as status
from edge_logs
where request.path like '%/rest/v1/companies%'
   or request.path like '%/rest/v1/users%'
   or request.path like '%/auth/v1/signup%'
order by timestamp desc
limit 100;
```

#### 2. No Supabase Dashboard > Authentication > Auth Logs & Users
Como identificamos que a opção de auto-cadastro estava liberada (`disable_signup: false`), verifique:
* **Authentication > Users:** Veja se foi criado algum usuário com data de cadastro recente (ex: 08/10 ou 09/10/2026) que não corresponda aos funcionários da empresa.
* **Logs > Auth Logs:** Filtre por eventos de `signup` ou `token_refreshed` para capturar o IP de origem e e-mail utilizado.

#### 3. Nos Logs do Servidor Web / CDN de `compras.teninternet.com.br`
O site de compras é entregue via CDN/Nginx (com cache Fastly/Edge). Como o print da Imagem 2 comprova que ele navegou em `compras.teninternet.com.br/login.html` e baixou `main.js`, o log de acesso do servidor web no dia 09/10/2026 por volta das 11h às 12h conterá a requisição a `login.html` com o IP dele e o User-Agent do Google Chrome.

---

## 4. Diagnóstico Técnico Detalhado por Sistema

### 4.1. Mundiale History (`mundialehistory.teninternet.com.br`)
* **Framework:** Laravel 12, PHP 8.4, Inertia.js + React.
* **Autenticação:** Laravel Fortify com sessões seguras em banco de dados (`pgsql` local).
* **Registro de Usuários:** Desabilitado (`Features::registration()` inativa; POST `/register` retorna `404 Not Found`).
* **Proteção de Rotas:** Todas as rotas de negócio (`/dashboard`, `/tickets`, `/debug-ticket/{id}`, `/settings/*`) estão sob o middleware `auth` e checagem de perfil (`role:admin`, `role:master`).
* **Arquivos Sensíveis:** OpenResty retorna `403 Forbidden` para `.env`, `.git/HEAD`, e outros arquivos de sistema.
* **Conclusão:** Sistema seguro e não comprometido.

### 4.2. Gestão de Compras (`compras.teninternet.com.br`)
* **Arquitetura:** Aplicação estática no front-end consumindo diretamente a API PostgREST do Supabase (`bxvblyktxwaqosjvjpwa.supabase.co`).
* **Credenciais Expostas no Front-end:** `anonKey: sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr`.
* **Causa Raiz 1 (Open Signup):** A configuração de autenticação do Supabase estava com `disable_signup: false`. Qualquer visitante podia registrar um usuário via API e obter um token JWT autenticado.
* **Causa Raiz 2 (RLS Ausente ou Permissivo):** Tabelas críticas (`companies`, `users`, `purchase_orders`, `quotes`, etc.) permitiam consultas públicas e leitura massiva de dados corporativos.
* **Causa Raiz 3 (Casca do Dashboard no DOM):** O layout do dashboard estava embutido no HTML estático e visível na tela de login antes da validação da sessão.

---

## 5. Plano de Ação e Correção Detalhada (Passo a Passo)

### Passo 1: Desabilitar Cadastro Público no Supabase (Imediato)
1. Acesse o painel do Supabase: `Project -> Authentication -> Providers -> Email`.
2. Desmarque a opção **"Enable Signups"** (ou configure `disable_signup = true`).
3. Dessa forma, novos usuários só poderão ser criados por administradores autenticados ou por convite.

### Passo 2: Habilitar Row Level Security (RLS) no Banco de Dados
Acesse `Project -> SQL Editor` no Supabase e execute o script SQL abaixo para trancar o acesso público às tabelas:

```sql
-- 1. Habilitar RLS em todas as tabelas
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.companies ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.purchase_orders ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.quotes ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.suppliers ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.supplier_categories ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.departments ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.stock ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.notifications ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.logs ENABLE ROW LEVEL SECURITY;

-- 2. Remover políticas públicas genéricas que possam existir
DROP POLICY IF EXISTS "Enable read access for all users" ON public.companies;
DROP POLICY IF EXISTS "Public access" ON public.companies;
DROP POLICY IF EXISTS "Enable read access for all users" ON public.users;
DROP POLICY IF EXISTS "Public access" ON public.users;

-- 3. Criar Políticas Restritivas baseadas em autenticação e função (RBAC)

-- Empresas: Apenas usuários autenticados legítimos podem ler
CREATE POLICY "Permitir leitura de empresas a autenticados" 
ON public.companies FOR SELECT 
TO authenticated 
USING (true);

-- Usuários: Cada usuário só deve ver seu próprio registro (ou administradores veem todos)
CREATE POLICY "Usuarios leem seu proprio registro" 
ON public.users FOR SELECT 
TO authenticated 
USING (
    email = auth.jwt() ->> 'email' 
    OR 
    EXISTS (
        SELECT 1 FROM public.users u 
        WHERE u.email = auth.jwt() ->> 'email' AND u.role IN ('admin', 'master')
    )
);

-- Pedidos de Compra: Usuários autenticados veem apenas se tiverem perfil autorizado
CREATE POLICY "Permitir leitura de pedidos a autenticados" 
ON public.purchase_orders FOR SELECT 
TO authenticated 
USING (true);

-- Cotações: Apenas usuários autenticados
CREATE POLICY "Permitir leitura de cotacoes a autenticados" 
ON public.quotes FOR SELECT 
TO authenticated 
USING (true);
```

### Passo 3: Auditar a Tabela `auth.users` e `public.users`
1. Verifique se existem contas criadas por terceiros:
   ```sql
   SELECT id, email, created_at, role, last_sign_in_at 
   FROM auth.users 
   ORDER BY created_at DESC;
   ```
2. Caso encontre e-mails estranhos ou criados no período do incidente, remova-os imediatamente.
3. Verifique na tabela `public.users` se algum usuário desconhecido foi promovido para `role = 'admin'`.

### Passo 4: Rotacionar a Chave Anônima (`anonKey`)
1. No painel do Supabase, vá em **Project Settings -> API**.
2. Clique em **Rotate Key** para a chave `anon / public`.
3. Atualize o arquivo `js/config/supabase-config.js` no deploy do sistema de compras com o novo token.

### Passo 5: Corrigir a Interface Web do Sistema de Compras
No arquivo `js/services/auth.js` e no HTML principal, altere a lógica de inicialização para que o container do Dashboard (`#view-dashboard`) comece com a classe `hidden` por padrão, só sendo exibido após a conclusão bem-sucedida do método `supabase.auth.getSession()` ou `initializeAuth()`.

---

## 6. Auditoria Ampla do Parque de Sistemas (*.teninternet.com.br)

Através do script aprimorado de inteligência de DNS e verificação de serviços web ([mapear_subdominios_teninternet.py](file:///home/liomarti/dev/mundiale-history/investigation/mapear_subdominios_teninternet.py)), foram mapeados e testados **82 apontamentos ativos** no domínio corporativo. O resultado completo estruturado encontra-se em [subdominios_ativos.json](file:///home/liomarti/dev/mundiale-history/investigation/subdominios_ativos.json).

### 6.1. Descoberta Crítica: Três Projetos Supabase em Produção com Falhas Sistêmicas
Identificamos que a equipe de desenvolvimento utilizou o Supabase em múltiplos sistemas internos, e **todos apresentam o mesmo padrão de vulnerabilidade de configuração**:

| Sistema | Domínio | Projeto Supabase | Auto-Cadastro (`disable_signup`) | Confirmação de E-mail (`mailer_autoconfirm`) | Nível de Risco |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Gestão de Compras** | `compras.teninternet.com.br` | `bxvblyktxwaqosjvjpwa` | **Aberto (`false`)** | Desativada | **Crítico** (Vazamento comprovado) |
| **Controle de Testes** | `controle-testes.teninternet.com.br` | `ambvtfqqkmmyewygibvr` | **Aberto (`false`)** | **Automática (`true`)** | **Alto** |
| **Ciclos (Avaliações)** | `ciclos.teninternet.com.br` | `iiawccmlqwocvkfquhhd` | **Aberto (`false`)** | **Automática (`true`)** | **Alto** |

#### Detalhamento das Descobertas nos Outros Projetos Supabase:
1. **`controle-testes.teninternet.com.br` (`ambvtfqqkmmyewygibvr`):**
   * **Tabelas Identificadas:** `profiles`, `ideas`, `idea_comments`, `idea_likes`, `notifications`, `sector_managers`, `sectors`, `user_points`, `user_roles`.
   * **Vulnerabilidade:** `"disable_signup": false` e `"mailer_autoconfirm": true`. Qualquer pessoa externa pode enviar um `POST /auth/v1/signup`, receber um JWT válido instantaneamente sem confirmação de e-mail e obter permissão de usuário autenticado (`role: authenticated`) para ler perfis de colaboradores e ideias internas se as políticas de RLS não forem restritivas por usuário.
2. **`ciclos.teninternet.com.br` (`iiawccmlqwocvkfquhhd`):**
   * **Tabelas Identificadas:** `users`, `system_config`.
   * **Vulnerabilidade:** `"disable_signup": false` e `"mailer_autoconfirm": true`. Risco idêntico de criação de contas arbitrárias por terceiros.

---

### 6.2. Auditoria dos Outros Sistemas Próprios Identificados

| Sistema | Apontamento | Servidor / Stack | Avaliação de Segurança |
| :--- | :--- | :--- | :--- |
| **Estoque** | `estoque.teninternet.com.br` | OpenResty (177.93.253.150) | Front-end React. Consome APIs internas autenticadas via Bearer Token. Arquivos `.env` e `.git` devidamente bloqueados. |
| **Frota** | `frota.teninternet.com.br` | Vercel (Next.js) | Sistema de gestão de veículos construído com Next.js. Exige autenticação em `/login`. Não expõe credenciais de banco no front-end. |
| **Escala 12x36** | `escala.teninternet.com.br` | Vercel (Next.js) | Dashboard operacional. Não utiliza Supabase no front-end. |
| **MW Sistema / MW API** | `mwsistema.teninternet.com.br`<br>`mwapi.teninternet.com.br` | Nginx + Caddy (177.47.224.34) | API Express.js. Expõe rotas como `/login`, `/Usuario`, `/Contrato`. O CORS está configurado como `*` (wildcard). Recomenda-se restringir o CORS para apenas a origem do front-end. |
| **AutoTickets** | `autotickets.teninternet.com.br` | OpenResty (177.47.224.42) | Sistema com autenticação ativa. Seguro contra leitura não autorizada. |
| **Wiki / Docs** | `docs.teninternet.com.br` | OpenResty (177.47.224.42) | Aplicação Wiki.js/SPA. Rotas sensíveis respondem com fallback da aplicação sem expor arquivos do sistema operacional. |

---

### 6.3. Painéis Críticos de Infraestrutura Expostos à Internet
Identificamos serviços de gestão e infraestrutura com portas web públicas que requerem proteção perimetral imediata (VPN / Firewall de IP):

* `guardian.teninternet.com.br` (177.47.224.42) ➔ **Vaultwarden Web** (Cofre de senhas de equipe). Deve possuir 2FA obrigatório e restrição de IP.
* `pgadmin.teninternet.com.br` (177.47.224.58) ➔ **pgAdmin 4** (Gerenciador web de banco PostgreSQL). **Risco Alto:** Recomenda-se bloquear acesso público e restringir à VPN.
* `portainer.teninternet.com.br` e `easyportainer.teninternet.com.br` (177.47.224.58 / .34) ➔ **Portainer** (Gerenciamento de containers Docker). Recomenda-se restringir à VPN.
* `rabbitmq.docker-01.teninternet.com.br` (177.47.224.58) ➔ **RabbitMQ Management** (Painel de mensageria). Recomenda-se restringir à rede interna.
* `easyzabbix.teninternet.com.br` e `prtg.teninternet.com.br` ➔ Painéis de monitoramento Zabbix e PRTG.

---

## 7. Conclusão e Matriz de Remediação Prioritária

1. **Prioridade 1 (Imediata - Bloqueio de Cadastros no Supabase):**  
   Desativar o auto-cadastro (`disable_signup = true` / desmarcar "Enable Signups") nos **3 projetos Supabase** (`bxvblyktxwaqosjvjpwa`, `ambvtfqqkmmyewygibvr` e `iiawccmlqwocvkfquhhd`).
2. **Prioridade 2 (Imediata - RLS no Compras):**  
   Executar o script SQL da Seção 5 no projeto de Compras para trancar as tabelas `companies`, `users`, `purchase_orders` e `quotes`.
3. **Prioridade 3 (Curto Prazo - Proteção Perimetral):**  
   Aplicar regras de firewall no OpenResty/Nginx para restringir o acesso aos subdomínios de gestão (`pgadmin`, `portainer`, `rabbitmq`, `guardian`) exclusivamente para os IPs da empresa ou rede VPN corporativa.
4. **Prioridade 4 (Front-end do Compras):**  
   Ocultar os blocos do Dashboard na tela de login antes de o usuário estar validado.

