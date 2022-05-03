from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

# Swagger specific items
SWAGGER_URL = '/documentation'
SWAGGER_JSON = '/static/swagger.json'
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    SWAGGER_JSON,
    config={
        'app_name': 'The Ultimate Book Api'
    }
)

def create_app():
    app = Flask(__name__)

    from blueprints.api import bp_api

    app.register_blueprint(bp_api, url_prefix='/api/v1.0.0')
    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)
    return app


if __name__ == '__main__':
    create_app().run(debug=True)
