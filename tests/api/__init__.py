"""
Unit Tests.
"""

import unittest

from app import create_app


class TestPublicApi(unittest.TestCase):
    """
    Public API resources tests.
    """

    def setUp(self):
        """
        Executed prior to each test.
        """
        self.app = create_app()
        self.client = self.app.test_client()
