# -*- coding: utf-8 -*-
"""
    tests.factories
    ~~~~~~~~~~~~~~~

    GingerPayments test factories module
"""

from datetime import datetime

from factory import Factory, Sequence, LazyAttribute
from passlib.hash import bcrypt

from gingerpayments.extensions import db
from gingerpayments.models import *


def create_sqlalchemy_model_function(Factory):

    def _create(cls, model_class, *args, **kwargs):
        entity = model_class(*args, **kwargs)
        db.session.add(entity)
        db.session.commit()
        return entity


class AdminFactory(Factory):
    class Meta:
        model = Admin
    email = Sequence(lambda n: 'user{0}@gingerpayments.com'.format(n))
    password = LazyAttribute(lambda a: bcrypt.encrypt('password'))
    active = True


class PersonFactory(Factory):
    class Meta:
        model = Person
    first_name = Sequence(lambda n: 'Person First Name {0}'.format(n))
    last_name = Sequence(lambda n: 'Person Last Name {0}'.format(n))


class AddressFactory(Factory):
    class Meta:
        model = Address
    address = Sequence(lambda n: 'Address {0}'.format(n))

class EmailFactory(Factory):
    class Meta:
        model = Email
    email = Sequence(lambda n: 'user{0}@gingerpayments.com'.format(n))

class PhoneFactory(Factory):
    class Meta:
        model = Phone
    phone = Sequence(lambda n: 'Phone Number {0}'.format(n))

class GroupFactory(Factory):
    class Meta:
        model = Group
    name = Sequence(lambda n: 'Group Number {0}'.format(n))

