import os

from flask import Flask

from gingerpayments.extensions import db
from gingerpayments.utils import register_blueprints

def create_app(package_name, package_path, settings_override=None,
               register_security_blueprint=True):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the GingerPayments platform.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param register_security_blueprint: flag to specify if the Flask-Security
                                        Blueprint should be registered. Defaults
                                        to `True`.
    """
    app = Flask(package_name, instance_relative_config=True)

    app.config.from_object('gingerpayments.settings')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)

    if app.config['SQLALCHEMY_DATABASE_URI'] != "sqlite:///:memory:":
        db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'payments_ginger.db'))
        db_uri = 'sqlite:///{}'.format(db_path)
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    db.init_app(app)

    register_blueprints(app, package_name, package_path)

    return app