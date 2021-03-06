import os

from flask import Flask

from addressbook.extensions import db
from addressbook.utils import register_blueprints
from wtforms.ext.sqlalchemy import fields

'''
There is a bug in wtform fields and this function is a fix for it.
Before it gets merged, we will need to patch this function ourself.
'''
def patched_get_pk_from_identity(obj):
    cls, key, token = fields.identity_key(instance=obj)
    return ':'.join(fields.text_type(x) for x in key)


fields.get_pk_from_identity = patched_get_pk_from_identity


def create_app(package_name, package_path, settings_override=None,
               register_security_blueprint=True):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the OnlineAddressBook platform.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param register_security_blueprint: flag to specify if the Flask-Security
                                        Blueprint should be registered.
                                        Defaults to `True`.
    """
    app = Flask(package_name, instance_relative_config=True)

    app.config.from_object('addressbook.settings')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)

    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    if db_uri and db_uri != "sqlite:///:memory:":
        db_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', db_uri))
        db_uri = 'sqlite:///{}'.format(db_path)
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    db.init_app(app)

    register_blueprints(app, package_name, package_path)

    return app
