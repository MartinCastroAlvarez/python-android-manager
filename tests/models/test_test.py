"""
Unit Tests.

This library is responsible for testing app.models.tests.
"""

from nose.plugins.attrib import attr
from unittest.mock import patch, MagicMock

from tests.models import TestModels

from app.models.test import Test, Status, Artifact
from app.models.application import Application
from app.models.device import Device
from app import exceptions


class TestTestsModel(TestModels):
    """
    Testing app.models.test.Test.
    """

    @attr(unit_test=True)
    def test_constructor(self):
        """
        Testing app.models.test.Test.
        Testing the model constructor.
        """
        app = Application("lorem")
        device = Device(name="ipsum", type_="dolor", model="sit")
        test = Test(application=app, device=device)
        self.assertIsInstance(test.timestamp, float)
        self.assertIsInstance(test.error, dict)
        self.assertIsInstance(test.artifacts, list)
        self.assertIsInstance(test.status, Status)
        self.assertIsInstance(test.application, Application)
        self.assertIsInstance(test.device, Device)

    @attr(unit_test=True)
    def test_pk(self):
        """
        Testing app.models.test.Test.
        Testing the model id generator.
        """
        app1 = Application("lorem")
        app2 = Application("ipsum")
        device1 = Device(name="lorem", type_="dolor", model="sit")
        device2 = Device(name="ipsum", type_="dolor", model="sit")
        test1 = Test(app1, device1)
        test2 = Test(app1, device2)
        test3 = Test(app2, device1)
        test4 = Test(app2, device1)
        self.assertNotEqual(test1.pk, test2.pk)
        self.assertNotEqual(test1.pk, test3.pk)
        self.assertNotEqual(test1.pk, test4.pk)
        self.assertNotEqual(test2.pk, test3.pk)
        self.assertNotEqual(test2.pk, test4.pk)
        self.assertNotEqual(test3.pk, test4.pk)

    @attr(unit_test=True)
    def test_repr(self):
        """
        Testing app.models.test.Test.
        Testing the model string serialized..
        """
        app = Application("lorem")
        device = Device(name="ipsum", type_="dolor", model="sit")
        test = Test(application=app, device=device)
        print(test)  # Should not fail.

    @attr(unit_test=True)
    @patch('app.models.application.Application.to_json')
    @patch('app.models.device.Device.to_json')
    def test_json(self, application, device):
        """
        Testing app.models.test.Test.
        Testing the json serializer
        """
        application.return_value = {
            "value": "sit",
        }
        device.return_value = {
            "value": "amet",
        }
        app = Application("sit")
        device = Device(name="amet", type_="amet2", model="amet3")
        test = Test(application=app, device=device)
        test.artifacts.append(Artifact("lorem"))
        test.artifacts.append(Artifact("ipsum"))
        test.artifacts.append(Artifact("dolor"))
        j = test.to_json()
        self.assertIn(Test.DEVICE, j)
        self.assertIn(Test.APPLICATION, j)
        self.assertIn(Test.DEVICE, j)
        self.assertIn(Test.ERROR, j)
        self.assertIn(Test.STATUS, j)
        self.assertIn(Test.ID, j)
        self.assertIn(Test.TIMESTAMP, j)
        self.assertIn("lorem", str(j))
        self.assertIn("ipsum", str(j))
        self.assertIn("dolor", str(j))
        self.assertIn("sit", str(j))
        self.assertIn("amet", str(j))


class TestArtifact(TestModels):
    """
    Testing app.models.test.Artifact.
    """

    @attr(unit_test=True)
    def test_constructor(self):
        """
        Testing app.models.test.Artifact.
        Testing the model constructor.
        """
        artifact = Artifact("lorem")
        self.assertEqual(artifact.path, "lorem")

    @attr(unit_test=True)
    def test_repr(self):
        """
        Testing app.models.test.Test.
        Testing the model string serialized..
        """
        artifact = Artifact("lorem")
        print(artifact)  # Should not fail.
