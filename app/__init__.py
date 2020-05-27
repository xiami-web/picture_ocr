import os
from flask import Flask
from conf.conf_main import CONFIG, Config


def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(CONFIG[config_name])
    Environment = os.getenv('FLASK_CONFIG') or 'DevConfig'
    config = CONFIG.get(Environment)
    config().load_conf(app)

    from app.test import test
    app.register_blueprint(test, url_prefix=Config.URL_PREFIX_API)

    return app