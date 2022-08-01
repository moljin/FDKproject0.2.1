import datetime
import os
from os.path import join, dirname

from pytz import timezone
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_ROOT = os.path.join(BASE_DIR, 'templates')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


dotenv_path = join(dirname(__file__), '.env')  # Path to .env file
load_dotenv(dotenv_path)


# def development_env():
#     dotenv_path = join(dirname(__file__), '.env')  # Path to .env file
#     print("def development_env(): dotenv_path", dotenv_path)
#     load_dotenv(dotenv_path)
#     flask_env = os.environ.get("FLASK_ENV")
#     return flask_env


class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = 'thisissecretkey'
    SESSION_COOKIE_NAME = 'FDK_project0.2.1'
    TIMEZONE = datetime.datetime.now(timezone('Asia/Seoul'))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class DevelopmentConfig(Config):
    DEBUG = True

    SEND_FILE_MAX_AGE_DEFAULT = 1  # 개발환경에서 캐시 파일 1초마다 reload 할 수 있도록 한거다.
    TEMPLATES_AUTO_RELOAD = True  # DEBUG = True이면 자동으로 켜진다. 굳이 안써도 된다면서.....
    WTF_CSRF_ENABLED = True  # False로 하면 좋으나 체크하기위해 True

    MYSQL_DATABASE_USER = 'root2'
    MYSQL_DATABASE_PASSWORD = '981011'
    MYSQL_DATABASE_DB = 'fdkproject0.2'
    MYSQL_DATABASE_HOST = 'localhost'
    MYSQL_DATABASE_PORT = '3306'

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}:{MYSQL_DATABASE_PORT}/{MYSQL_DATABASE_DB}?charset=utf8"


class ProductionConfig(Config):
    print("product")
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'moljin@981011'
    MYSQL_DATABASE_DB = 'fdkproject0.2'
    MYSQL_DATABASE_HOST = '112.186.157.226'
    MYSQL_DATABASE_PORT = '56033'

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_DATABASE_USER}:{MYSQL_DATABASE_PASSWORD}@{MYSQL_DATABASE_HOST}:{MYSQL_DATABASE_PORT}/{MYSQL_DATABASE_DB}?charset=utf8"


class TestingConfig(Config):
    __test__ = False
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "sqlite_test.db")}'

