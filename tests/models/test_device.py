"""
Unit Tests.

This library is responsible for testing app.models.devices.
"""

from nose.plugins.attrib import attr
from unittest.mock import patch, MagicMock

from app.models.device import Device
from tests.models import TestModels
from app import exceptions


class TestDevicesModel(TestModels):
    """
    Testing app.models.device.Device.
    """

    @attr(unit_test=True)
    def test_constructor(self):
        """
        Testing app.models.device.Device.
        Testing the model constructor.
        """
        device = Device("lorem", "ipsum", "dolor")
        self.assertEqual(device.name, "lorem")
        self.assertEqual(device.type_, "ipsum")
        self.assertEqual(device.model, "dolor")

    @attr(unit_test=True)
    def test_pk(self):
        """
        Testing app.models.device.Device.
        Testing the model id generator.
        """
        device1 = Device("lorem", "ipsum", "dolor")
        device2 = Device("queen", "iron", "maiden")
        device3 = Device("lorem", "iron", "maiden")
        device4 = Device("lorem", "ipsum", "dolor")
        self.assertNotEqual(device1.pk, device2.pk)
        self.assertNotEqual(device1.pk, device3.pk)
        self.assertNotEqual(device2.pk, device3.pk)
        self.assertEqual(device1.pk, device4.pk)

    @attr(unit_test=True)
    def test_repr(self):
        """
        Testing app.models.device.Device.
        Testing the model string serialized..
        """
        device = Device("lorem", "ipsum", "dolor")
        print(device)  # Should not fail.

    @attr(unit_test=True)
    def test_json(self):
        """
        Testing app.models.device.Device.
        Testing the json serializer
        """
        device = Device("lorem", "ipsum", "dolor")
        j = device.to_json()
        self.assertIn(Device.NAME, j)
        self.assertIn(Device.TYPE, j)
        self.assertIn(Device.MODEL, j)
        self.assertIn(Device.ID, j)
        self.assertIn("lorem", str(j))
        self.assertIn("ipsum", str(j))
        self.assertIn("", str(j))

    @attr(unit_test=True)
    @patch('app.models.device.avd')
    def test_list(self, avd):
        """
        Testing app.models.device.Device.
        Testing the list method.
        """
        avd.return_value = "\n".join([
            "The Header",
            "lorem ipsum dolor sit amet",
            "lorem ipsum dolor sit amet",
            "lorem ipsum dolor sit amet",
        ]).encode('utf-8'), ""
        for counter, device in enumerate(Device.list()):
            self.assertIsInstance(device, Device)
        avd.assert_called_once()
        self.assertEqual(counter, 2)

    @attr(unit_test=True)
    @patch('app.models.device.Device.list')
    def test_find(self, search):
        """
        Testing app.models.device.Device.
        Testing the find method.
        """
        mock = MagicMock()
        mock.pk = "lorem"
        search.return_value = [
            mock,
            mock,
            mock,
        ]
        device = Device.find("lorem")
        self.assertEqual(device, mock)

    @attr(unit_test=True)
    @patch('app.models.device.Device.list')
    def test_find_404(self, search):
        """
        Testing app.models.device.Device.
        Testing the find method with an invalid id.
        """
        mock = MagicMock()
        mock.pk = "lorem"
        search.return_value = [
            mock,
            mock,
            mock,
        ]
        with self.assertRaises(exceptions.existence.DeviceNotFoundException):
            Device.find("ipsum")

    @attr(unit_test=True)
    @patch('app.models.device.avd')
    def test_uninstall(self, avd):
        """
        Testing app.models.device.Device.
        Testing the uninstall function.
        """
        output = "\n".join([
            "lorem.ipsum.dolor.sit.amet",
        ]).strip()
        avd.return_value = output.encode('utf-8'), ""
        device = Device("lorem", "ipsum", "dolor")
        self.assertEqual(device.uninstall("lorem.ipsum"), "lorem.ipsum.dolor.sit.amet")
        avd.assert_called_once()

    @attr(unit_test=True)
    @patch('app.models.device.avd')
    def test_uninstall_error(self, avd):
        """
        Testing app.models.device.Device.
        Testing the uninstall function with errors.
        """
        avd.return_value = "test".encode('utf-8'), "error".encode('utf-8')
        device = Device("lorem", "ipsum", "dolor")
        with self.assertRaises(exceptions.runtime.AndroidDeploymentException):
            device.uninstall("lorem.ipsum")

    @attr(unit_test=True)
    @patch('app.models.device.avd')
    def test_install(self, avd):
        """
        Testing app.models.device.Device.
        Testing the install function.
        """
        output = "\n".join([
            "lorem.ipsum.dolor.sit.amet",
        ]).strip()
        avd.return_value = output.encode('utf-8'), ""
        device = Device("lorem", "ipsum", "dolor")
        self.assertEqual(device.install("lorem.ipsum"), "lorem.ipsum.dolor.sit.amet")
        avd.assert_called_once()

    @attr(unit_test=True)
    @patch('app.models.device.avd')
    def test_install_error(self, avd):
        """
        Testing app.models.device.Device.
        Testing the uninstall function with errors.
        """
        avd.return_value = "test".encode('utf-8'), "error".encode('utf-8')
        device = Device("lorem", "ipsum", "dolor")
        with self.assertRaises(exceptions.runtime.AndroidDeploymentException):
            device.install("lorem.ipsum")

    @attr(unit_test=True)
    @patch('app.models.device.avd')
    def test_go_home(self, avd):
        """
        Testing app.models.device.Device.
        Testing the go home function.
        """
        device = Device("lorem", "ipsum", "dolor")
        device.go_home()
        avd.assert_called_once()

    @attr(unit_test=True)
    @patch('app.models.device.avd')
    def test_open(self, avd):
        """
        Testing app.models.device.Device.
        Testing the open home function.
        """
        device = Device("lorem", "ipsum", "dolor")
        device.open("lorem.ipsum")
        avd.assert_called_once()

    @attr(unit_test=True)
    @patch('os.path.isfile')
    @patch('app.models.device.avd')
    def test_capture(self, avd, isfile):
        """
        Testing app.models.device.Device.
        Testing the screenshot function.
        """
        isfile.return_value = True
        device = Device("lorem", "ipsum", "dolor")
        device.capture("lorem.ipsum")
        avd.assert_called()

    @attr(unit_test=True)
    @patch('os.path.isfile')
    @patch('app.models.device.avd')
    def test_capture_error(self, avd, isfile):
        """
        Testing app.models.device.Device.
        Testing the screenshot function with errors.
        """
        isfile.return_value = False
        device = Device("lorem", "ipsum", "dolor")
        with self.assertRaises(exceptions.runtime.AndroidScreenshotException):
            device.capture("lorem.ipsum")
