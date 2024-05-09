from flask import Flask
from src.external.infra.framework.flask.routes.user_route import user_route_bp


app = Flask(__name__)


app.register_blueprint(user_route_bp)
