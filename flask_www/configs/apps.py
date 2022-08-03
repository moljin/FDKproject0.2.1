def related_app(app):

    @app.template_filter('ko_datetime')
    def korean_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
        return value.strftime(fmt)