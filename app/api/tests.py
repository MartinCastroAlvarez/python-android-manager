"""
Device API.

This resource is responsible for interacting
with existing devices: Listing, downloading, executing, etc.
"""

import logging

from flask_restful import Resource

from app.controllers.tests import TestsController
from app.exceptions import MontevideoException
from app.api import constants

logger = logging.getLogger(__name__)


class TestResource(Resource):
    """
    Test instance resource.
    This resource is used to run an application on a device.
    """

    def post(self, application_id: str, device_id: str) -> dict:
        """
        Run application on device.

        NOTE: Since this is a demo, no authentication or
              authorization is validated here.
        """
        try:
            test = TestsController.test(application_id=application_id,
                                        device_id=device_id)
            return {
                constants.TEST: test.to_json()
            }
        except MontevideoException as error:
            logger.exception("Test Application | sf_error=%s", error)
            return error.to_json()
