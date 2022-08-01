def routes_init(app):
    from flask_www.commons import common
    app.register_blueprint(common.common_bp)

    from flask_www.boards.articles import articles
    app.register_blueprint(articles.articles_bp)
