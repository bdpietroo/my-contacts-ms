import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
     Classe de configuração que encapsula todas as variáveis da aplicação.
    """

    # Credenciais da aplicação registradas no Azure AD (carregas a partir do .env)
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    TENANT_ID = os.getenv("TENANT_ID", "common") # 'common' permite login de contas pessoais e corporativas
    FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:8080")

    # Parametros do Fluxo OAuth2
    AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
    REDIRECT_PATH = "/get_token"

    # Parâmetros da API Microsoft Graph
    ENDPOINT = "https://graph.microsoft.com/v1.0/me/contacts"
    SCOPE = ["Contacts.Read"] # Permissão para ler os contatos do usuário
