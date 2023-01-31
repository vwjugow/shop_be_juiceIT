from flask_lambda import FlaskLambda

from .models import db


def create_app(config_filename=None):
    app = FlaskLambda(__name__, instance_relative_config=False)
    app.config.from_pyfile(config_filename)
    app.app_context().push()
    initialize_extensions(app)
    register_blueprints(app)
    return app


def initialize_extensions(app):
    db.init_app(app)
    db.create_all()


def register_blueprints(app):
    from project.views.shop_items import shop_items_blueprint
    from project.views.main import main_blueprint

    app.register_blueprint(shop_items_blueprint)
    app.register_blueprint(main_blueprint)
