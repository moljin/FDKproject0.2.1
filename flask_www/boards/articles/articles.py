from flask import Blueprint, request, redirect, url_for, render_template

from flask_www.boards.articles.forms import ArticleForm
from flask_www.boards.articles.models import Article
from flask_www.configs import db

NAME = 'articles'
articles_bp = Blueprint(NAME, __name__, url_prefix='/boards/article')


@articles_bp.route('/create', methods=['GET', 'POST'])
def article_create():
    form = ArticleForm()
    if request.method == 'POST':# and form.validate_on_submit():
        image_path = form.image_path.data
        subject = form.subject.data
        content = request.form.get('content')

        new_article = Article()
        new_article.image_path = image_path
        new_article.subject = subject
        new_article.content = content

        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for('commons.index'))
    return render_template('boards/articles/article_create.html', form=form)