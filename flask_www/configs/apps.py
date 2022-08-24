def related_app(app):
    @app.template_filter('daytime')
    def _format_datetime(value, _type=None):  # 템플릿단 얘시: what_date|daytime("full")
        if _type == "full":
            _format = '%Y-%m-%d %H:%M:%S %p'
        elif _type == "medium":
            _format = '%Y-%m-%d %H:%M %p'
        else:
            _format = '%Y-%m-%d'
        return value.strftime(_format)

    @app.template_filter('ko_datetime')
    def korean_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
        return value.strftime(fmt)
