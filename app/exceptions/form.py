"""
Application Exceptions.

All exceptions in this library correspond to user input.
"""

from app.exceptions import MontevideoException


class BadUserInputException(MontevideoException):
    """
    Exceptions related to user inptu.
    """
    CODE = 400
    MESSAGE = "Bad User Input"


class BadApplicationIdException(BadUserInputException):
    """
    Application ID is invalid.
    """
    SUBCODE = 4001
    MESSAGE = "Invalid Application ID"


class BadDeviceIdException(BadUserInputException):
    """
    Device ID is invalid.
    """
    SUBCODE = 4002
    MESSAGE = "Invalid Device ID"
