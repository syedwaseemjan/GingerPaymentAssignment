from flask_login import UserMixin
from passlib.hash import bcrypt
from sqlalchemy.ext.hybrid import hybrid_property
from addressbook.extensions import db
from addressbook.utils import JsonSerializer


class UserJsonSerializer(JsonSerializer):
    __json_public__ = ['id', 'email']


class Admin(UserJsonSerializer, UserMixin, db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    _password = db.Column(db.String(120))
    active = db.Column(db.Boolean())

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = bcrypt.encrypt(value)

    def match_password(self, value):
        return bcrypt.verify(value, self._password)

    @property
    def is_active(self):
        return self.active


class PersonJsonSerializer(JsonSerializer):
    __json_hidden__ = ['groups']


class Person(PersonJsonSerializer, db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))

    emails = db.relationship('Email',
                             backref=db.backref('persons'))

    addresses = db.relationship('Address',
                                backref=db.backref('persons'))

    phones = db.relationship('Phone',
                             backref=db.backref('persons'))


class EmailJsonSerializer(JsonSerializer):
    __json_hidden__ = ['persons']


class Email(EmailJsonSerializer, db.Model):
    __tablename__ = 'emails'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('persons.id'))
    email = db.Column(db.String(255), unique=True)

    def __init__(self, email):
        self.email = email


class AddressJsonSerializer(JsonSerializer):
    __json_hidden__ = ['persons']


class Address(AddressJsonSerializer, db.Model):
    __tablename__ = 'adresses'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('persons.id'))
    address = db.Column(db.String(255))

    def __init__(self, address):
        self.address = address


class PhoneJsonSerializer(JsonSerializer):
    __json_hidden__ = ['persons']


class Phone(PhoneJsonSerializer, db.Model):
    __tablename__ = 'phones'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('persons.id'))
    phone = db.Column(db.String(255), unique=True)

    def __init__(self, phone):
        self.phone = phone
