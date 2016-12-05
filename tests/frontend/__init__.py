# -*- coding: utf-8 -*-
"""
    tests.frontend
    ~~~~~~~~~~~~~~

    frontend tests package
"""

from addressbook.frontend import create_app

from .. import AddressBookAppTestCase, settings


class GingerFrontendTestCase(AddressBookAppTestCase):

    def _create_app(self):
        return create_app(settings)

    def setUp(self):
        super(GingerFrontendTestCase, self).setUp()
        self._login()