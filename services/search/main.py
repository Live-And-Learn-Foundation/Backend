from flask import Flask
from flask_cors import CORS

from src import init_cache
from src import routes


def main() -> Flask:
    app = Flask(__name__)

    init_cache(app)

    CORS(app)

    routes.register(app)

    return app


def run():
    app = main()
    app.run("0.0.0.0", 9005)


if __name__ == "__main__":
    run()
