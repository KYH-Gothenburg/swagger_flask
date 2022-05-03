from flask import Flask


def create_app():
    app = Flask(__name__)

    from blueprints.api import bp_api

    app.register_blueprint(bp_api, url_prefix='/api/v1.0.0')
    return app


if __name__ == '__main__':
    create_app().run(debug=True)
