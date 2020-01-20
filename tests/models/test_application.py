"""
Unit Tests.

This library is responsible for testing app.models.applications.
"""

from nose.plugins.attrib import attr
from unittest.mock import patch, MagicMock

from app.models.application import Application
from tests.models import TestModels
from app import exceptions


class TestApplicationsModel(TestModels):
    """
    Testing app.models.application.Application.
    """

    @attr(unit_test=True)
    def test_constructor(self):
        """
        Testing app.models.application.Application.
        Testing the model constructor.
        """
        app = Application("lorem")
        self.assertEqual(app.name, "lorem")

    @attr(unit_test=True)
    def test_pk(self):
        """
        Testing app.models.application.Application.
        Testing the model id generator.
        """
        app1 = Application("lorem")
        app2 = Application("ipsum")
        app3 = Application("ipsum")
        self.assertNotEqual(app1.pk, app2.pk)
        self.assertEqual(app2.pk, app3.pk)

    @attr(unit_test=True)
    def test_path(self):
        """
        Testing app.models.application.Application.
        Testing the model path getter.
        """
        app1 = Application("lorem")
        app2 = Application("ipsum")
        app3 = Application("ipsum")
        self.assertNotEqual(app1.get_path(), app2.get_path())
        self.assertEqual(app2.get_path(), app3.get_path())

    @attr(unit_test=True)
    @patch('os.stat')
    def test_lmd(self, stat):
        """
        Testing the last modified date getter.
        """
        mock = MagicMock()
        mock.st_mtime = 3
        stat.return_value = mock
        app = Application("lorem")
        self.assertEqual(app.get_last_modified_date(), 3)

    @attr(unit_test=True)
    def test_repr(self):
        """
        Testing app.models.application.Application.
        Testing the model string serialized..
        """
        app = Application("lorem")
        print(app)  # Should not fail.

    @attr(unit_test=True)
    @patch('app.models.application.Application.get_last_modified_date')
    @patch('app.models.application.Application.get_package_name')
    def test_json(self, package, lmd):
        """
        Testing app.models.application.Application.
        Testing the json serializer
        """
        package.return_value = "ipsum"
        lmd.return_value = 33
        app = Application("lorem")
        j = app.to_json()
        self.assertIn(Application.NAME, j)
        self.assertIn(Application.TYPE, j)
        self.assertIn(Application.LAST_MODIFIED, j)
        self.assertIn(Application.PACKAGE, j)
        self.assertIn(Application.ID, j)
        self.assertIn("lorem", str(j))
        self.assertIn("ipsum", str(j))
        self.assertIn("33", str(j))

    @attr(unit_test=True)
    @patch('app.models.application.aapt')
    def test_package(self, aapt):
        """
        Testing app.models.application.Application.
        Testing the package name getter.
        """
        output = "\n".join([
            "package: name='lorem.ipsum.dolor.sit.amet'",
            "package: name='lorem.ipsum.dolor.sit.amet'",
            "package: name='lorem.ipsum.dolor.sit.amet'",
            "package: name='lorem.ipsum.dolor.sit.amet'",
        ]).strip()
        aapt.return_value = output.encode('utf-8'), ""
        app = Application("lorem")
        self.assertEqual(app.get_package_name(), "lorem.ipsum.dolor.sit.amet")
        aapt.assert_called_once()

    @attr(unit_test=True)
    @patch('app.models.application.aapt')
    def test_package_error(self, aapt):
        """
        Testing app.models.application.Application.
        Testing the package name getter with an error.
        """
        output = "\n".join([
            "lorem ipsum",
            "lorem ipsum",
            "lorem ipsum",
            "lorem ipsum",
        ]).strip()
        aapt.return_value = output.encode('utf-8'), ""
        app = Application("lorem")
        with self.assertRaises(exceptions.runtime.AndroidManagerException):
            app.get_package_name()

    @attr(unit_test=True)
    @patch('os.listdir')
    @patch('os.path')
    def test_list(self, path, listdir):
        """
        Testing app.models.application.Application.
        Testing the list method.
        """
        path.isfile.return_value = True
        path.join.return_value = "/my/path.apk"
        listdir.return_value = [
            "lorem.apk",
            "dolor.ios",
            "sit.png"
        ]
        for counter, application in enumerate(Application.list()):
            self.assertIsInstance(application, Application)
        listdir.assert_called_once()
        path.isfile.assert_called()
        self.assertEqual(counter, 2)

    @attr(unit_test=True)
    @patch('app.models.application.Application.list')
    def test_find(self, search):
        """
        Testing app.models.application.Application.
        Testing the find method.
        """
        mock = MagicMock()
        mock.pk = "lorem"
        search.return_value = [
            mock,
            mock,
            mock,
        ]
        application = Application.find("lorem")
        self.assertEqual(application, mock)

    @attr(unit_test=True)
    @patch('app.models.application.Application.list')
    def test_find_404(self, search):
        """
        Testing app.models.application.Application.
        Testing the find method with an invalid id.
        """
        mock = MagicMock()
        mock.pk = "lorem"
        search.return_value = [
            mock,
            mock,
            mock,
        ]
        with self.assertRaises(exceptions.existence.ApplicationNotFoundException):
            Application.find("ipsum")
