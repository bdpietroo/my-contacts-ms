# backend/app/routes.py (VERSÃO CORRIGIDA COM BLUEPRINT)

from flask import current_app, jsonify, request, redirect, session, Blueprint
from .services import build_msal_app, get_token_from_cache, get_contacts
import msal

# Cria um blueprint para agrupar as rotas 
bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    """
    Rota de teste para verificar se o backend está funcionando
    """
    return "Backend está no ar!"


@bp.route("/login")
def login():
    """
    Inicia o fluxo de login OAuth2 com a Microsoft
    """
    # Acesso seguro às configurações para garantir que a aplicação não quebre.
    scope = current_app.config.get('SCOPE', [])
    redirect_path = current_app.config.get('REDIRECT_PATH', '/get_token')

    # Gera e armazena o fluxo na sessão para verificação no callback.
    session["flow"] = build_msal_app().initiate_auth_code_flow(
        scope,
        redirect_uri=request.host_url.rstrip('/') + redirect_path
    )
    return redirect(session["flow"]["auth_uri"])


@bp.route(current_app.config['REDIRECT_PATH'])
@bp.route("/get_token")  # Rota alternativa para facilitar testes locais
def get_token():
    """
    Obtém um token de acesso usando o código de autorização retornado pela Microsoft

    """
    try:
        # Tenta obter um token de acesso usando o código de autorização
        cache = msal.SerializableTokenCache()
        if session.get("token_cache"):
            cache.deserialize(session["token_cache"])

        # Usa o código de autorização para obter o token de acesso
        build_msal_app(cache=cache).acquire_token_by_auth_code_flow(
            session.get("flow", {}), request.args
        )

        # Salva o token no cache da sessão para uso nas próximas requisições
        session["token_cache"] = cache.serialize()

        # Essa parte não está com um valor padrão caso precise rodar localmente, está pegando somente a configuração do .env
        frontend_url = current_app.config.get("FRONTEND_URL", "http://localhost:8080")
        frontend_contacts_url = f'{frontend_url}/contacts?login_success=true'

        return redirect(frontend_contacts_url)
    except ValueError as e:
        print(f"Erro ao obter token: {e}")
        return jsonify({"error": "Falha na autenticação", "description": str(e)}), 400


@bp.route("/api/contacts")
def contacts():
    """
    Endpoint da API que retorna os contatos do usuário.
    """
    token = get_token_from_cache(current_app.config['SCOPE'])

    # Nega o acesso se não houver token
    if not token or 'access_token' not in token:
        return jsonify({"error": "Usuário não autenticado. Por favor, faça o login."}), 401

    # Busca os contatos na API da Microsoft
    contacts_data = get_contacts(token["access_token"])
    if "error" in contacts_data:
        return jsonify(contacts_data), 500
        
    # Processa e agrupa os contatos por domínio de email
    grouped_contacts = {}
    for contact in contacts_data.get('value', []):
        for email in contact.get('emailAddresses', []):
            address = email.get('address')
            if address:
                domain = address.split('@')[-1]
                grouped_contacts.setdefault(domain, []).append(address)
    
    return jsonify(grouped_contacts)


@bp.route("/logout")
def logout():
    """
    Rota para realizar logout do usuário
    """
    session.clear()

    frontend_url = current_app.config.get("FRONTEND_URL", "http://localhost:8080")

    # Constrói a URL de logout da Microsoft, que redireciona de volta para o frontend
    logout_url = (
        current_app.config['AUTHORITY'] + "/oauth2/v2.0/logout" +
        f"?post_logout_redirect_uri={frontend_url}"
    )

    return redirect(logout_url)