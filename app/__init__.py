from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Importando e registrando as rotas
    from app.routes.jogador_routes import jogador_bp
    from app.routes.dupla_routes import dupla_bp
    from app.routes.landing_routes import landing_bp  # new import

    app.register_blueprint(jogador_bp, url_prefix='/jogadores')
    app.register_blueprint(dupla_bp, url_prefix='/duplas')
    app.register_blueprint(landing_bp)  

    return app
    