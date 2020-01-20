"""
Unit Tests.

This library is responsible for testing app.controllers.tests.
"""

from nose.plugins.attrib import attr
from unittest.mock import patch, MagicMock

from app.controllers.tests import TestsController
from tests.controllers import TestControllers
from app.models.test import Status
from app import exceptions


class TestTestsController(TestControllers):
    """
    Testing app.controllers.tests.TestsController.
    """

    @attr(unit_test=True)
    @patch('app.controllers.devices.DevicesController.describe')
    @patch('app.controllers.applications.ApplicationsController.describe')
    @patch('app.models.test.Test')
    def test_run_ok(self, model, applications, devices):
        """
        Testing app.controllers.tests.TestsController.
        Testing the test method with a valid response.
        """
        device_mock = MagicMock()
        devices.return_value = device_mock
        app_mock = MagicMock()
        applications.return_value = app_mock
        test = TestsController.test(application_id="lorem",
                                    device_id="ipsum")
        device_mock.capture.assert_called_once()
        device_mock.uninstall.assert_called_once()
        device_mock.install.assert_called_once()
        device_mock.open.assert_called_once()
        device_mock.go_home.assert_called()
        applications.assert_called_once()
        devices.assert_called_once()
        self.assertEqual(test.error, {})
        self.assertEqual(test.status, Status.SUCCESS)

    @attr(unit_test=True)
    @patch('app.controllers.devices.DevicesController.describe')
    @patch('app.controllers.applications.ApplicationsController.describe')
    @patch('app.models.test.Test')
    def test_run_error(self, model, applications, devices):
        """
        Testing app.controllers.tests.TestsController.
        Testing the test method with a valid response.
        """
        device_mock = MagicMock()
        device_mock.capture.side_effect = exceptions.runtime.RuntimeException()
        devices.return_value = device_mock
        app_mock = MagicMock()
        applications.return_value = app_mock
        test = TestsController.test(application_id="lorem",
                                    device_id="ipsum")
        device_mock.capture.assert_called_once()
        device_mock.uninstall.assert_called_once()
        device_mock.install.assert_called_once()
        device_mock.open.assert_called_once()
        device_mock.go_home.assert_called_once()
        applications.assert_called_once()
        devices.assert_called_once()
        self.assertNotEqual(test.error, {})
        self.assertEqual(test.status, Status.ERROR)
