"""
Test models.

This class is responsible for interacting
with the database. No authentication or business
logic is performed here.
"""

import os
import enum
import time
import typing
import logging

from app.models.device import Device
from app.models.application import Application
from app import config

logger = logging.getLogger(__name__)


class Status(enum.Enum):
    """
    Status Enum.
    """
    SUCCESS = "success"
    ERROR = "failed"
    UNKNOWN = "unknown"


class Artifact:
    """
    Artifact model.
    """

    PATH = "path"

    def __init__(self, path: str) -> None:
        """
        Application Constructor.
        """
        self.path: str = path

    def __str__(self) -> str:
        """
        String serializer.
        """
        return "<Artifaction: '{}'>".format(self.path)

    def to_json(self) -> dict:
        """
        Json serializer.
        """
        return {
            self.PATH: self.path,
        }

    @classmethod
    def build(cls) -> 'Artifact':
        """
        Method responsible for generating an empty artifact.
        """
        return cls(os.path.join(config.ARTIFACTS_ROOT,
                                "{}.png".format(time.time())))


class Test:
    """
    Test model.
    """

    ID = "id"
    ARTIFACTS = "artifacts"
    APPLICATION = "application"
    DEVICE = "device"
    STATUS = "status"
    ERROR = "error"
    TIMESTAMP = "ts"

    def __init__(self, application: Application, device: Device) -> None:
        """
        Application Constructor.
        """
        self.timestamp: float = time.time()
        self.application: Application = application
        self.device: Device = device
        self.artifacts: typing.List[Artifacat] = []
        self.error: dict = {}
        self.status: Status = Status.UNKNOWN
        logger.info("New Test. | sf_ts=%s | sf_app=%s | sf_device=%s",
                    self.timestamp, application, device)

    @property
    def pk(self) -> str:
        """
        ID getter.
        """
        return "{}-{}-{}".format(self.device.pk,
                                 self.application.pk,
                                 self.timestamp)

    def __str__(self) -> str:
        """
        String serializer.
        """
        return "<Test: '{}'>".format(self.pk)

    def to_json(self) -> dict:
        """
        JSON serializer.
        """
        return {
            self.ID: self.pk,
            self.DEVICE: self.device.to_json(),
            self.APPLICATION: self.application.to_json(),
            self.STATUS: self.status.value,
            self.ERROR: self.error,
            self.TIMESTAMP: self.timestamp,
            self.ARTIFACTS: [
                a.to_json()
                for a in self.artifacts
            ]
        }
