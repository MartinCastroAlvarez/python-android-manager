"""
Unit Tests.

This library is responsible for testing app.api.devices.
"""

from nose.plugins.attrib import attr
from unittest.mock import patch, MagicMock

from tests.api import TestPublicApi
from app import exceptions


class TestDevicesResource(TestPublicApi):
    """
    Testing app.api.devices.DevicesResource.
    """

    @attr(unit_test=True)
    @patch('app.controllers.devices.DevicesController.search')
    def test_get_ok(self, controller):
        """
        Testing app.api.devices.DevicesResource.
        Testing the GET method with a valid response.
        """
        mock = MagicMock()
        mock.to_json.return_value = {"lorem": "ipsum"}
        controller.return_value = [
            mock,
            mock,
            mock,
        ]
        response = self.client.get("/v1/devices").get_json()
        controller.assert_called_once()
        self.assertIn("lorem", str(response))
        self.assertIn("ipsum", str(response))
        self.assertIn("devices", response)
        mock.to_json.assert_called()

    @attr(unit_test=True)
    @patch('app.controllers.devices.DevicesController.search')
    def test_get_error(self, controller):
        """
        Testing app.api.devices.DevicesResource.
        Testing the GET method with an error.
        """
        error = exceptions.runtime.RuntimeException()
        controller.side_effect = error
        response = self.client.get("/v1/devices").get_json()
        self.assertEqual(response, error.to_json())
        controller.assert_called_once()


class TestDeviceResource(TestPublicApi):
    """
    Testing app.api.devices.DeviceResource.
    """

    @attr(unit_test=True)
    @patch('app.controllers.devices.DevicesController.describe')
    def test_get_ok(self, controller):
        """
        Testing app.api.devices.DeviceResource.
        Testing the GET method with a valid response.
        """
        mock = MagicMock()
        mock.to_json.return_value = {"lorem": "ipsum"}
        controller.return_value = mock
        response = self.client.get("/v1/devices/123123123").get_json()
        controller.assert_called_once()
        self.assertIn("lorem", str(response))
        self.assertIn("ipsum", str(response))
        self.assertIn("device", response)
        mock.to_json.assert_called_once()

    @attr(unit_test=True)
    @patch('app.controllers.devices.DevicesController.describe')
    def test_get_error(self, controller):
        """
        Testing app.api.devices.DeviceResource.
        Testing the GET method with an error.
        """
        error = exceptions.runtime.RuntimeException()
        controller.side_effect = error
        response = self.client.get("/v1/devices/123123123").get_json()
        self.assertEqual(response, error.to_json())
        controller.assert_called_once()
