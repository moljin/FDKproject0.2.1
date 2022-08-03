from flask import Blueprint, request, redirect, url_for, render_template

from flask_www.boards.articles.forms import ArticleForm
from flask_www.boards.articles.models import Article
from flask_www.configs import db
from flask_www.configs.utils import save_file

NAME = 'articles'
articles_bp = Blueprint(NAME, __name__, url_prefix='/boards/article')


@articles_bp.route('/create', methods=['GET', 'POST'])
def article_create():
    form = ArticleForm()
    if request.method == 'POST':# and form.validate_on_submit():
        image_file = form.image_path.data
        subject = form.subject.data
        content = request.form.get('content')

        new_article = Article()
        from flask_www.configs import app
        if image_file:
            relative_path, _ = save_file(app.config["TIMEZONE"], image_file)
            new_article.image_path = relative_path
        new_article.subject = subject
        new_article.content = content

        db.session.add(new_article)
        db.session.commit()
        return redirect(url_for('commons.index'))
    return render_template('boards/articles/article_create.html', form=form)


@articles_bp.route('/detail/<int:_id>', methods=['GET'])
def article_detail(_id):
    # board = TestBoard.query.get_or_404(_id)
    article_obj = db.session.query(Article).filter_by(id=_id).first()
    return render_template('boards/articles/article_detail.html', article=article_obj)
