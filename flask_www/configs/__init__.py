import os

from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

from flask_www.configs.apps import related_app
from flask_www.configs.config import TEMPLATE_ROOT, STATIC_ROOT, DevelopmentConfig, ProductionConfig
from flask_www.configs.routes import routes_init

csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name=None):
    application = Flask(__name__, template_folder=TEMPLATE_ROOT, static_folder=STATIC_ROOT)

    # is_gunicorn = "gunicorn" in os.environ.get("SERVER_SOFTWARE", "")
    if not config_name:
        print("application.config['DEBUG']", application.config['DEBUG'])
        if application.config['DEBUG']:
            print("if application.config['DEBUG']")
            config_name = DevelopmentConfig()
        else:
            print("else")
            config_name = ProductionConfig()
    #
    #     print("is_gunicorn", is_gunicorn)
    #
    #     if is_gunicorn is False:
    #         config_name = DevelopmentConfig()
    #     else:
    #         config_name = ProductionConfig()

    # print("os.environ['FLASK_ENV']", os.environ['FLASK_ENV'])
    # if os.environ['FLASK_ENV'] == 'development':
    #     config_name = DevelopmentConfig()
    # else:
    #     config_name = ProductionConfig()

    application.config.from_object(config_name)

    csrf.init_app(application)

    db.init_app(application)
    if application.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(application, db, render_as_batch=True)
    else:
        migrate.init_app(application, db)
    # from flask_www.boards.articles import models

    routes_init(application)
    related_app(application)

    return application


app = create_app()
