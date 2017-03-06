# -*- coding:utf-8 -*-
import sys
import json
import traceback
from flask import Flask, Blueprint

__all__ = ['create_app']


def create_app(config_file=None):

    app = Flask(__name__, static_url_path="", static_folder="static")
    configure_app(app=app, config_file=config_file)
    configure_extensions(app)
    configure_blueprints(app)
    configure_filter(app)
    return app


def configure_blueprints(app):
    from api.order_api import order_api
    from view.store_view import store_view
    app.register_blueprint(order_api)
    app.register_blueprint(store_view)


def configure_app(app, config_file=None):
    pass


def configure_extensions(app):
    pass


def configure_filter(app):
    pass


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)

