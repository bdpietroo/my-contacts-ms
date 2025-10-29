import msal 
import requests
from flask import session, current_app

def build_msal_app(cache=None):
    """
    Constrói a aplicação MSAL ConfidentialClientApplication
    """

    client_id = current_app.config.get("CLIENT_ID")
    client_secret = current_app.config.get("CLIENT_SECRET")
    authority = current_app.config.get("AUTHORITY")

    return msal.ConfidentialClientApplication(
        client_id, 
        authority=authority,
        client_credential=client_secret,
        token_cache=cache
    )

def get_token_from_cache(scope=None):
    """
    Busca o token válido do cache de sessão

    Tenta obter o token de forma silenciosa, o que significa que o MSAL
    usará o token armazenado em cache se ainda for válido, sem exigir
    interação do usuário.
    """

    cache = msal.SerializableTokenCache()
    if session.get("token_cache"):
        cache.deserialize(session["token_cache"])

    msal_app = build_msal_app(cache=cache)
    accounts = msal_app.get_accounts()

    # DEBUG: mostrar informações úteis sobre contas para diagnosticar por que não há token
    try:
        print("msal.get_accounts count:", len(accounts))
        if accounts:
            # não imprime informações sensíveis do usuário, só um identificador
            print("first account keys:", list(accounts[0].keys()))
    except Exception as e:
        print("Erro ao logar accounts:", e)

    if not accounts:
        return None

    # Tenta obter o token silenciosamente
    result = msal_app.acquire_token_silent(scope, account=accounts[0])

    # DEBUG: mostrar se o acquire_token_silent obteve algo (sem imprimir access_token)
    try:
        if result and isinstance(result, dict):
            keys = list(result.keys())
            print("acquire_token_silent result keys:", keys)
            # não logar access_token, apenas presença
            if "access_token" in result:
                print("access_token presente no resultado (não exibido)")
        else:
            print("acquire_token_silent não retornou token válido")
    except Exception as e:
        print("Erro ao inspecionar result:", e)

    # Se o token for obtido, atualiza o cache na sessão
    if result:
        session["token_cache"] = cache.serialize()
        return result

    return None

def get_contacts(token: str ):
    """
    Busca os contatos do usuário na Microsoft Graph API

    Args:
        token (str): Token de acesso válido para autenticação na API

    """

    headers = {'Authorization': f'Bearer {token}'}

    # Otimiza a requisição para buscar apenas os campos necessários
    params = {'$select': 'displayName,emailAddresses'}

    try: 
        response = requests.get(current_app.config.get("ENDPOINT"), headers=headers, params=params)
      
        # Levanta um erro HTTP se a requisição falhar
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição Graph API: {e}")
        return {"error": "Falha ao buscar contatos", "description": str(e)}