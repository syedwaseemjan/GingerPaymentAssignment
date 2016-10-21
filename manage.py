from flask.ext.script import Manager

from gingerpayments.api import create_app
from gingerpayments.extensions import db
from gingerpayments.models import Admin

manager = Manager(create_app())

@manager.command
def test():
	pass

@manager.command
def create_db():
    db.create_all()

@manager.command
def init_db():
	create_admin()

@manager.command
def create_admin():
    admin = Admin()
    admin.email = "admin@gingerassignment.com"
    admin.password = "test123"
    admin.active = True
    db.session.add(admin)

    db.session.commit()

if __name__ == "__main__":
    manager.run()