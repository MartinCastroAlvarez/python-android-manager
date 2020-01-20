"""
Device API.

This resource is responsible for interacting
with existing devices: Listing, downloading, executing, etc.
"""

import logging

from flask_restful import Resource

from app.exceptions import MontevideoException
from app.controllers.devices import DevicesController
from app.api import constants

logger = logging.getLogger(__name__)


class DevicesResource(Resource):
    """
    Devices list resource.
    This resource is used to interact with multiple devices.
    """

    def get(self) -> dict:
        """
        GET list of available devices.

        NOTE: Since this is a demo, no authentication or
              authorization is validated here.
        """
        try:
            return {
                constants.PLATFORMS: [
                    device.to_json()
                    for device in DevicesController.search()
                ]
            }
        except MontevideoException as error:
            logger.exception("List Devices | sf_error=%s", error)
            return error.to_json()


class DeviceResource(Resource):
    """
    Device instance resource.
    This resource is used to interact with one single device.
    """

    def get(self, device_id: str) -> dict:
        """
        GET device information.

        NOTE: Since this is a demo, no authentication or
              authorization is validated here.
        """
        try:
            device = DevicesController.describe(device_id=device_id)
            return {
                constants.PLATFORM: device.to_json()
            }
        except MontevideoException as error:
            logger.exception("Describe Device | sf_error=%s", error)
            return error.to_json()
