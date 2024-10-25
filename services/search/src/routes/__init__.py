from .search import search_blueprint
from flask import Flask


def register(app: Flask) -> None:
    app.register_blueprint(search_blueprint)
