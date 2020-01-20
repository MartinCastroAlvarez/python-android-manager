"""
Application Exceptions.
All exceptions in this library correspond to a problem of existence.
"""

from app.exceptions import MontevideoException


class ExistenceException(MontevideoException):
    """
    Exceptions related to resources not being found.
    """
    CODE = 404
    MESSAGE = "Resource Not Found"


class ApplicationNotFoundException(ExistenceException):
    """
    Application was not found.
    """
    SUBCODE = 4041
    MESSAGE = "Application Not Found"


class DeviceNotFoundException(ExistenceException):
    """
    Device was not found.
    """
    SUBCODE = 4042
    MESSAGE = "Device Not Found"
