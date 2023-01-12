from dynaconf import FlaskDynaconf
from flask import Flask
from flask_cors import CORS


def create_app(**config):
    app = Flask(__name__)
    FlaskDynaconf(app)  # config managed by Dynaconf
    app.config.load_extensions(
        "EXTENSIONS"
    )  # Load extensions from settings.toml
    app.config.update(config)  # Override with passed config
    CORS(app)
    return app


def create_app_wsgi():
    # workaround for Flask issue
    # that doesn't allow **config
    # to be passed to create_app
    # https://github.com/pallets/flask/issues/4170
    app = create_app()
    return app
