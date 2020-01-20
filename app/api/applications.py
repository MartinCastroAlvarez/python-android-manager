"""
Application API.

This resource is responsible for interacting
with existing applications: Listing, downloading, executing, etc.
"""

import logging

from flask_restful import Resource

from app.controllers.applications import ApplicationsController
from app.exceptions import MontevideoException
from app.api import constants

logger = logging.getLogger(__name__)


class ApplicationsResource(Resource):
    """
    Applications list resource.
    This resource is used to interact with multiple applications.
    """

    def get(self) -> dict:
        """
        GET list of available applications.

        NOTE: Since this is a demo, no authentication or
              authorization is validated here.
        """
        try:
            return {
                constants.APPLICATIONS: [
                    application.to_json()
                    for application in ApplicationsController.search()
                ]
            }
        except MontevideoException as error:
            logger.exception("List Applications | sf_error=%s", error)
            return error.to_json()


class ApplicationResource(Resource):
    """
    Application instance resource.
    This resource is used to interact with one single application.
    """

    def get(self, application_id: str) -> dict:
        """
        GET application information.

        NOTE: Since this is a demo, no authentication or
              authorization is validated here.
        """
        try:
            application = ApplicationsController.describe(application_id=application_id)
            return {
                constants.APPLICATION: application.to_json()
            }
        except MontevideoException as error:
            logger.exception("Describe Application | sf_error=%s", error)
            return error.to_json()
