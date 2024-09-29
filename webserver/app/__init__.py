from flask import Flask


def create_app():

    app = Flask("webserver")

    @app.route("/")
    def root():

        return "Yeah!"

    return app

