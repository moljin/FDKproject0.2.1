import os

from flask_www.configs import app, DevelopmentConfig, ProductionConfig

if __name__ == '__main__':
    # is_gunicorn = "gunicorn" in os.environ.get("SERVER_SOFTWARE", "")
    # if is_gunicorn is False:
    #     config_name = DevelopmentConfig()
    # else:
    #     config_name = ProductionConfig()
    # app.config.from_object(config_name)
    app.run(host='0.0.0.0', port=5000)