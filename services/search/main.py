from flask import Flask

from src import middlewares, routes


def main() -> Flask:
    app = Flask(__name__)

    routes.register(app)

    return app


def run():
    app = main()
    app.run("0.0.0.0", 9005)


if __name__ == "__main__":
    run()
