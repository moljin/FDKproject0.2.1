from flask import Blueprint, render_template

from flask_www.boards.articles.models import Article
from flask_www.configs import db

NAME = 'commons'
common_bp = Blueprint(NAME, __name__)


@common_bp.route('/')
def index():
    dbs = db
    return render_template('index.html', dbs=dbs, tms=Article.query.all())
