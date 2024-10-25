from flask import Flask

from app import middlewares, routes


def main() -> Flask:
    app = Flask(__name__)

    routes.register(app)

    return app


def run():
    app = main()
    app.run("localhost", 9006)


if __name__ == "__main__":
    run()
