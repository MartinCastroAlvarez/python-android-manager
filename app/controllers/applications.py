"""
Application controllers.

These functions are responsible for validating
the request and interacting with the models.
"""

import logging

import typing

from app.models.application import Application
from app.exceptions import form

logger = logging.getLogger(__name__)


class ApplicationsController:
    """
    Applications business logic.

    This controller allows the client to search applications
    and perform other tasks on the models.
    """

    @classmethod
    def search(cls) -> typing.Generator[Application, None, None]:
        """
        Business method to search applications.
        """
        logger.debug("Search Applications")
        for application in Application.list():
            yield application

    @classmethod
    def describe(cls, application_id: str) -> Application:
        """
        Business method to search applications.
        """
        if not isinstance(application_id, str) or not application_id:
            raise form.BadApplicationIdException(application_id)
        logger.debug("Find Application | sf_id=%s", application_id)
        return Application.find(application_id)

    @classmethod
    def upload(cls, *args, **kwargs) -> Application:
        """
        Business method to upload a new application.
        """
        raise NotImplementedError()

    @classmethod
    def delete(cls, *args, **kwargs) -> Application:
        """
        Business method to delete an existing application.
        """
        raise NotImplementedError()
