"""
Unit Tests.

This library is responsible for testing app.controllers.applications.
"""

from nose.plugins.attrib import attr
from unittest.mock import patch, MagicMock

from app.controllers.applications import ApplicationsController
from tests.controllers import TestControllers
from app import exceptions


class TestApplicationsController(TestControllers):
    """
    Testing app.controllers.applications.ApplicationsController.
    """

    @attr(unit_test=True)
    @patch('app.models.application.Application.list')
    def test_search_ok(self, model):
        """
        Testing app.controllers.applications.ApplicationsController.
        Testing the search method with a valid response.
        """
        mock = MagicMock()
        mock.to_json.return_value = {"lorem": "ipsum"}
        model.return_value = [
            mock,
            mock,
            mock,
        ]
        for counter, application in enumerate(ApplicationsController.search()):
            self.assertEqual(application, mock)
        self.assertEqual(counter, 2)

    @attr(unit_test=True)
    @patch('app.models.application.Application.list')
    def test_search_error(self, model):
        """
        Testing app.controllers.applications.ApplicationsController.
        Testing the search method with an error.
        """
        error = exceptions.runtime.RuntimeException()
        model.side_effect = error
        with self.assertRaises(exceptions.runtime.RuntimeException):
            for _ in ApplicationsController.search():
                pass

    @attr(unit_test=True)
    @patch('app.models.application.Application.find')
    def test_describe_ok(self, model):
        """
        Testing app.controllers.applications.ApplicationsController.
        Testing the describe method with a valid response.
        """
        mock = MagicMock()
        model.return_value = mock
        application = ApplicationsController.describe("123")
        self.assertEqual(application, mock)

    @attr(unit_test=True)
    @patch('app.models.application.Application.find')
    def test_describe_int(self, model):
        """
        Testing app.controllers.applications.ApplicationsController.
        Testing the describe method with an integer parameter.
        """
        mock = MagicMock()
        model.return_value = mock
        with self.assertRaises(exceptions.form.BadApplicationIdException):
            ApplicationsController.describe(123)

    @attr(unit_test=True)
    @patch('app.models.application.Application.find')
    def test_describe_error(self, model):
        """
        Testing app.controllers.applications.ApplicationsController.
        Testing the describe method with an error.
        """
        error = exceptions.runtime.RuntimeException()
        model.side_effect = error
        with self.assertRaises(exceptions.runtime.RuntimeException):
            ApplicationsController.describe("123")

    @attr(unit_test=True)
    def test_upload(self):
        """
        Testing app.controllers.applications.ApplicationsController.
        Testing the upload method.
        """
        with self.assertRaises(NotImplementedError):
            ApplicationsController.upload()

    @attr(unit_test=True)
    def test_delete(self):
        """
        Testing app.controllers.applications.ApplicationsController.
        Testing the upload method.
        """
        with self.assertRaises(NotImplementedError):
            ApplicationsController.delete()
