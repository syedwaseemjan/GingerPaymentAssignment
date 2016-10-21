# -*- coding: utf-8 -*-
"""
    tests.frontend
    ~~~~~~~~~~~~~~

    frontend tests package
"""

from gingerpayments.frontend import create_app

from .. import GingerAppTestCase, settings


class GingerFrontendTestCase(GingerAppTestCase):

    def _create_app(self):
        return create_app(settings)

    def setUp(self):
        super(GingerFrontendTestCase, self).setUp()
        self._login()
