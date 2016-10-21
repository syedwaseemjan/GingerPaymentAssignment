# -*- coding: utf-8 -*-
"""
    tests.api
    ~~~~~~~~~

    api tests package
"""

from gingerpayments.api import create_app

from .. import GingerAppTestCase, settings


class GingerApiTestCase(GingerAppTestCase):

    def _create_app(self):
        return create_app(settings, register_security_blueprint=True)

    def setUp(self):
        super(GingerApiTestCase, self).setUp()
        self._login()
