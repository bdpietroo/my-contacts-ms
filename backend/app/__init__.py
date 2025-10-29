from flask import Flask
from flask_cors import CORS
from flask_session import Session
from .config import Config
import os
from werkzeug.middleware.proxy_fix import ProxyFix

def create_app():
    """
    Cria e configura a aplicação Flask

    Returns:
        app (Flask): A aplicação Flask configurada
    
    """
    app = Flask(__name__)
    # Carrega as configurações a partir do objeto Config em Config.py
    app.config.from_object(Config)
    
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    app.config["SESSION_COOKIE_SAMESITE"] = "None"
    app.config["SESSION_COOKIE_SECURE"] = True

    app.config["SECRET_KEY"] = os.urandom(24) # Necessário para assinar o cookie da sessão


    # Configura sessões do lado do servidor para lidar com os tokens grandes da MSAL
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_USE_SIGNER"] = True

    Session(app)

    frontend_url = app.config.get("FRONTEND_URL", "http://localhost:8080")

    CORS(app, supports_credentials=True, origins=[frontend_url])

    with app.app_context():
        # Importa e registra o Blueprint das rotas
        from . import routes
        app.register_blueprint(routes.bp)

    return app
