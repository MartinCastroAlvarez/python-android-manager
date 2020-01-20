"""
Device models.

This class is responsible for interacting
with the database. No authentication or business
logic is performed here.
"""

import os
import time
import logging
import typing

import functools

from Crypto.Hash import SHA256

from app.exceptions import existence, runtime
from app.models.utils import avd

logger = logging.getLogger(__name__)


class Device:
    """
    Device model.
    """

    TYPE = "type"
    MODEL = "model"
    NAME = "name"
    ID = "id"

    def __init__(self, name: str, type_: str, model: str) -> None:
        """
        Device Constructor.
        """
        logger.info("New Device. | sf_name=%s | sf_device=%s | sf_model=%s",
                    name, type_, model)
        self.name: str = name
        self.model: str = model
        self.type_: str = type_

    @property
    @functools.lru_cache()
    def pk(self) -> str:
        """
        ID getter.
        """
        return self.get_id(self.name, self.type_, self.model)

    @staticmethod
    def get_id(*args) -> str:
        """
        Static method responsible for transforming a name
        into a unique ID.
        """
        sha256 = SHA256.new()
        sha256.update("".join(args).encode('utf-8'))
        return sha256.hexdigest()

    def __str__(self) -> str:
        """
        String serializer.
        """
        return "<Device: '{}'>".format(self.name)

    def to_json(self) -> dict:
        """
        JSON serializer.
        """
        return {
            self.NAME: self.name,
            self.TYPE: self.type_,
            self.MODEL: self.model,
            self.ID: self.pk,
        }

    @classmethod
    def list(cls) -> typing.Generator['Device', None, None]:
        """
        Public class method responsibe for searching
        for all applications.
        """
        output, _ = avd("devices", "-l")
        for line in output.decode('utf-8').split("\n")[1:]:
            if line:
                columns = line.split()
                yield cls(name=columns[0],
                          type_=columns[2],
                          model=columns[3])

    @classmethod
    def find(cls, device_id: str) -> 'Device':
        """
        Public class method responsible for searching
        for one device by ID.

        Since this is just a demo, it will iterate over
        all files in the file system.
        In production, it should send a query to an external database.
        """
        logger.info("Finding Device. | sf_id=%s", device_id)
        for device in cls.list():
            if device.pk == device_id:
                return device
        raise existence.DeviceNotFoundException(device_id)

    def uninstall(self, package: str) -> str:
        """
        Public class method responsibe for uninstalling
        an APK from a device.

        Reference:
        https://stackoverflow.com/questions/12483720
        """
        logger.info("Uninstall. | sf_device=%s | sf_package=%s", self, package)
        output, error = avd("shell", "pm", "clear", package)
        if error:
            raise runtime.AndroidDeploymentException(error.decode('utf-8'))
        return output.decode('utf-8')

    def install(self, apk: str) -> str:
        """
        Public class method responsibe for deploying
        an APK into a device.

        Reference:
        https://adbshell.com/commands/adb-install
        """
        logger.info("Deploy. | sf_device=%s | sf_apk=%s", self, apk)
        output, error = avd("install", apk)
        if error:
            raise runtime.AndroidDeploymentException(error.decode('utf-8'))
        return output.decode('utf-8')

    def go_home(self) -> None:
        """
        Public class method responsibe for
        closing all running apps.

        Reference:
        http://adbcommand.com/adbshell/am
        """
        logger.info("Home. | sf_device=%s", self)
        avd("adb", "shell", "am", "kill-all")

    def open(self, package: str) -> None:
        """
        Public class method responsibe for opening
        an app on the target device.

        Reference:
        https://stackoverflow.com/questions/4567904
        """
        logger.info("Open. | sf_device=%s | sf_package=%s", self, package)
        avd("shell", "monkey",
            "-p", package,
            "-c" "android.intent.category.LAUNCHER", "1")

    def capture(self, path: str) -> None:
        """
        Public class method responsibe for
        capturing the screen on the device.

        Reference:
        https://blog.shvetsov.com/2013/02/grab-android-screenshot-to-computer-via.html
        """
        logger.info("Screenshot. | sf_device=%s | sf_path=%s", self, path)
        local_path: str = "/sdcard/screenshot-{}.png".format(time.time())
        avd("shell", "screencap", local_path)
        avd("pull", local_path, path)
        avd("rm", local_path)
        if not os.path.isfile(path):
            raise runtime.AndroidScreenshotException(path)
