# Meus Contatos MS

![Status](https://img.shields.io/badge/status-concluído-green)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Vue.js](https://img.shields.io/badge/Vue.js-3.x-green.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey.svg)

Uma aplicação web full-stack que permite aos usuários fazer login com sua conta da Microsoft, listar seus contatos e agrupá-los por domínio de e-mail.

## 🚀 Tecnologias Utilizadas

*   **Frontend:** Vue.js 3
*   **Backend:** Python 3 com Flask
*   **Autenticação:** OAuth 2.0 com a API da Microsoft (Microsoft Graph)
*   **Hospedagem:**
    *   Frontend: Firebase Hosting
    *   Backend: Google Cloud Run

## 📋 Pré-requisitos

Antes de começar, você precisará ter as seguintes ferramentas instaladas em sua máquina:
*   [Python 3.10+](https://www.python.org/downloads/)
*   [Node.js e npm](https://nodejs.org/en/)
*   Uma **Conta da Microsoft**.

---

## 📝 Tutorial: Configuração da Aplicação no Portal do Azure

Para que a autenticação com a Microsoft funcione, você precisa registrar sua aplicação e obter as credenciais.

> ⚠️ **Nota sobre a Conta do Azure:** Se você ainda não tem uma assinatura ativa, o Azure pode solicitar que você inicie uma avaliação gratuita. Siga os passos indicados na plataforma para ativar sua conta antes de prosseguir.

1.  **Acesse o Portal do Azure:** Faça login em [portal.azure.com](https://portal.azure.com).

2.  **Vá para "Começar com uma avaliação gratuita do Azure":** clique em `Iniciar` e depois clique `Try Azure for free` e crie sua conta. 

3.  **Vá para "Registos de aplicativos":** Na barra de busca, procure por `Microsoft Entra ID`, clique no serviço e, no menu à esquerda, em gerenciar, clique em **"Registos de aplicativo"**.

4.  **Crie um Novo Registo:** Clique em **"+ Novo registo"**.
    *   **Nome:** Dê um nome claro, como `Meus Contatos MS (Local)`.
    *   **Tipos de conta suportados:** Selecione a opção *"Contas em qualquer diretório organizacional... e contas Microsoft pessoais..."*.

5.  **Configure o URI de Redirecionamento (Passo Crítico):**
    *   Na seção "URI de Redirecionamento", selecione a plataforma **"Web"**.
    *   Insira a URL de callback para o ambiente local: `http://localhost:5000/get_token`.
    *   Clique em **"Registar"**.

6.  **Copie o "ID da Aplicação (cliente)" (Client ID):** Na página de "Visão Geral" da aplicação, copie o valor do campo **"ID da Aplicação (cliente)"**. Este será o seu `CLIENT_ID`. Recomendo anotar em alum lugar.

7.  **Crie o "Segredo do Cliente" (Client Secret):**
    *   No menu à esquerda, vá para **"Certificados e segredos"**.
    *   Clique em **"+ Novo segredo do cliente"**.
    *   Dê uma descrição (ex: `chave_app_contatos`) e clique em "Adicionar".
    *   A página irá recarregar e mostrar o segredo. Copie o **valor**. Este será o seu `CLIENT_SECRET`. Também recomendo anotar em algum lugar.

8.  **Configure as Permissões da API:**
    *   No menu à esquerda, vá para **"Permissões da API"**.
    *   Clique em **"+ Adicionar uma permissão"** -> **"Microsoft Graph"** -> **"Permissões delegadas"**.
    *   Na caixa de busca, procure por `Contacts` e marque a permissão **`Contacts.Read`**.
    *   Clique em **"Adicionar permissões"**.

---

## ⚙️ Configuração do Ambiente Local

Após clonar o projeto, siga os passos abaixo para configurar e executar o projeto 

### 1. Backend (Flask)

1.  **Navegue até a pasta do backend:**
    ```bash
    cd backend
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    *   Na pasta `backend`, crie um arquivo chamado `.env`.
    *   Adicione o seguinte conteúdo a ele, preenchendo com os valores que você obteve no Portal do Azure:

    ```
    # Credenciais da aplicação registrada no Portal do Azure
    CLIENT_ID="SUA_CLIENT_ID_AQUI"
    CLIENT_SECRET="SEU_CLIENT_SECRET_AQUI"
    ```

### 2. Frontend (Vue.js)

1.  **Navegue até a pasta do frontend (em um novo terminal):**
    ```bash
    cd frontend
    ```

2.  **Instale as dependências:**
    ```bash
    npm install
    ```

3.  **Configure as variáveis de ambiente:**
    *   Na pasta `frontend`, crie um arquivo chamado `.env.local`.
    *   Adicione o seguinte conteúdo a ele:

    ```
    # URL base da API do backend para o ambiente de desenvolvimento local
    VUE_APP_API_BASE_URL=http://localhost:5000
    ```

---

## ▶️ Executando a Aplicação

1.  **Inicie o servidor do backend:**
    *   No terminal do backend (com o ambiente virtual ativado), execute:
    ```bash
    flask run
    ```
    *   O backend estará rodando em `http://localhost:5000`.

2.  **Inicie o servidor do frontend:**
    *   No terminal do frontend, execute:
    ```bash
    npm run serve
    ```
    *   A aplicação estará disponível em `http://localhost:8080`.

3.  Abra `http://localhost:8080` no seu navegador e o projeto estará funcionando!
