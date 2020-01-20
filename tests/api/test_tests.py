"""
Unit Tests.

This library is responsible for testing app.api.tests.
"""

from nose.plugins.attrib import attr
from unittest.mock import patch, MagicMock

from tests.api import TestPublicApi
from app import exceptions


class TestTestResource(TestPublicApi):
    """
    Testing app.api.tests.TestResource.
    """

    @attr(unit_test=True)
    @patch('app.controllers.tests.TestsController.test')
    def test_post_ok(self, controller):
        """
        Testing app.api.tests.TestResource.
        Testing the POST method with a valid response.
        """
        mock = MagicMock()
        mock.to_json.return_value = {"lorem": "ipsum"}
        controller.return_value = mock
        response = self.client.post("/v1/devices/123/applications/123").get_json()
        controller.assert_called_once()
        self.assertIn("lorem", str(response))
        self.assertIn("ipsum", str(response))
        self.assertIn("test", response)
        mock.to_json.assert_called_once()

    @attr(unit_test=True)
    @patch('app.controllers.tests.TestsController.test')
    def test_post_error(self, controller):
        """
        Testing app.api.tests.TestResource.
        Testing the POST method with an error.
        """
        error = exceptions.runtime.RuntimeException()
        controller.side_effect = error
        response = self.client.post("/v1/devices/123/applications/123").get_json()
        self.assertEqual(response, error.to_json())
        controller.assert_called_once()
