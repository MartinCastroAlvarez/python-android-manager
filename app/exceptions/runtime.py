"""
Application Exceptions.

All exceptions in this library correspond to runtime exceptions.
"""

from app.exceptions import MontevideoException


class RuntimeException(MontevideoException):
    """
    Exceptions related to runtime exceptions.
    """
    CODE = 600
    MESSAGE = "Runtime Exception"


class AndroidManagerException(RuntimeException):
    """
    Exception related to Android CLI tools.
    """
    SUBCODE = 6001
    MESSAGE = "Android Manager Exception"


class AndroidDeploymentException(RuntimeException):
    """
    Exception raised when a deployment fails.
    """
    SUBCODE = 6002
    MESSAGE = "Android Deployment Exception"


class AndroidExecutionException(RuntimeException):
    """
    Exception raised when executing an app.
    """
    SUBCODE = 6003
    MESSAGE = "Android Exceution Exception"


class AndroidScreenshotException(RuntimeException):
    """
    Exception raised when taking a screenshot.
    """
    SUBCODE = 6004
    MESSAGE = "Android Screenshot Exception"
