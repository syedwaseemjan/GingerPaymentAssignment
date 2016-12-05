# -*- coding: utf-8 -*-
"""
    tests.api
    ~~~~~~~~~

    api tests package
"""

from addressbook.api import create_app

from .. import AddressBookAppTestCase, settings


class GingerApiTestCase(AddressBookAppTestCase):

    def _create_app(self):
        return create_app(settings, register_security_blueprint=True)

    def setUp(self):
        super(GingerApiTestCase, self).setUp()
        self._login()
