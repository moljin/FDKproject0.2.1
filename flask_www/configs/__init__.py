from flask import Flask

from flask_www.configs.config import TEMPLATE_ROOT, STATIC_ROOT
from flask_www.configs.routes import routes_init


def create_app(config_name=None):
    application = Flask(__name__, template_folder=TEMPLATE_ROOT, static_folder=STATIC_ROOT)
    routes_init(application)

    return application


app = create_app()
