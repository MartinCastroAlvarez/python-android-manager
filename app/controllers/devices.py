"""
Device controllers.

These functions are responsible for validating
the request and interacting with the models.
"""

import logging

import typing

from app.models.device import Device
from app.exceptions import form

logger = logging.getLogger(__name__)


class DevicesController:
    """
    Devices business logic.

    This controller allows the client to search devices
    and perform other tasks on the models.
    """

    @classmethod
    def search(cls) -> typing.Generator[Device, None, None]:
        """
        Business method to search devices.
        """
        logger.debug("Search Devices")
        for device in Device.list():
            yield device

    @classmethod
    def describe(cls, device_id: str) -> Device:
        """
        Business method to search devices.
        """
        if not isinstance(device_id, str) or not device_id:
            raise form.BadDeviceIdException(device_id)
        logger.debug("Find Device | sf_id=%s", device_id)
        return Device.find(device_id)
