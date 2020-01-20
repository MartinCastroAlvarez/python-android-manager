"""
Application Model Utils.
"""

import typing
import logging
import subprocess

from app import config
from app.exceptions import runtime

logger = logging.getLogger(__name__)


def avd(*args) -> typing.Tuple[bytes]:
    """
    Method responsible for executing AVD commands
    on available devices.
    """
    command = [
        "{}/adb".format(config.AVD_ROOT),
        *args,
    ]
    logger.info("AVD Request. | sf_cmd=%s", command)
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        raise runtime.AndroidManagerException(error.decode('utf-8'))
    logger.info("AVD Response. | sf_output=%s | sf_stderr=%s",
                output, error)
    return output, error


def aapt(*args) -> typing.Tuple[bytes]:
    """
    Method responsible for executing AAPT commands.
    """
    command = [
        "{}/aapt".format(config.AAPT_ROOT),
        *args,
    ]
    logger.info("AAPT Request. | sf_cmd=%s", command)
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        raise runtime.AndroidManagerException(error.decode('utf-8'))
    logger.info("AAPT Response. | sf_output=%s | sf_stderr=%s",
                output, error)
    return output, error
