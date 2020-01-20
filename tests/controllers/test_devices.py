"""
Unit Tests.

This library is responsible for testing app.controllers.devices.
"""

from nose.plugins.attrib import attr
from unittest.mock import patch, MagicMock

from app.controllers.devices import DevicesController
from tests.controllers import TestControllers
from app import exceptions


class TestDevicesController(TestControllers):
    """
    Testing app.controllers.devices.DevicesController.
    """

    @attr(unit_test=True)
    @patch('app.models.device.Device.list')
    def test_search_ok(self, model):
        """
        Testing app.controllers.devices.DevicesController.
        Testing the search method with a valid response.
        """
        mock = MagicMock()
        mock.to_json.return_value = {"lorem": "ipsum"}
        model.return_value = [
            mock,
            mock,
            mock,
        ]
        for counter, device in enumerate(DevicesController.search()):
            self.assertEqual(device, mock)
        self.assertEqual(counter, 2)

    @attr(unit_test=True)
    @patch('app.models.device.Device.list')
    def test_search_error(self, model):
        """
        Testing app.controllers.devices.DevicesController.
        Testing the search method with an error.
        """
        error = exceptions.runtime.RuntimeException()
        model.side_effect = error
        with self.assertRaises(exceptions.runtime.RuntimeException):
            for _ in DevicesController.search():
                pass

    @attr(unit_test=True)
    @patch('app.models.device.Device.find')
    def test_describe_ok(self, model):
        """
        Testing app.controllers.devices.DevicesController.
        Testing the describe method with a valid response.
        """
        mock = MagicMock()
        model.return_value = mock
        device = DevicesController.describe("123")
        self.assertEqual(device, mock)

    @attr(unit_test=True)
    @patch('app.models.device.Device.find')
    def test_describe_int(self, model):
        """
        Testing app.controllers.devices.DevicesController.
        Testing the describe method with an integer param.
        """
        mock = MagicMock()
        model.return_value = mock
        with self.assertRaises(exceptions.form.BadDeviceIdException):
            DevicesController.describe(123)

    @attr(unit_test=True)
    @patch('app.models.device.Device.find')
    def test_describe_error(self, model):
        """
        Testing app.controllers.devices.DevicesController.
        Testing the describe method with an error.
        """
        error = exceptions.runtime.RuntimeException()
        model.side_effect = error
        with self.assertRaises(exceptions.runtime.RuntimeException):
            DevicesController.describe("123")
