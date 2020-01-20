"""
Application models.

This class is responsible for interacting
with the database. No authentication or business
logic is performed here.
"""

import os
import logging
import typing
import functools

from Crypto.Hash import SHA256

from app.exceptions import existence, runtime
from app import config
from app.models.utils import aapt

logger = logging.getLogger(__name__)


class Application:
    """
    Application model.
    """

    LAST_MODIFIED = "last_modified"
    TYPE = "type"
    PACKAGE = "package"
    NAME = "name"
    ID = "id"

    def __init__(self, name: str) -> None:
        """
        Application Constructor.
        """
        logger.info("New Application. | sf_name=%s", name)
        self.name: str = name

    @property
    @functools.lru_cache()
    def pk(self) -> str:
        """
        ID getter.
        """
        return self.get_id(self.name)

    def get_application_type(self) -> str:
        """
        Type getter.
        """
        return self.name.split(".")[-1]

    def get_last_modified_date(self) -> str:
        """
        Last modified date getter.
        """
        stats: object = os.stat(self.get_path())
        return stats.st_mtime

    def get_path(self) -> str:
        """
        APK path getter.
        """
        return os.path.join(config.APKS_ROOT, self.name)

    @staticmethod
    def get_id(name: str) -> str:
        """
        Static method responsible for transforming a name
        into a unique ID.
        """
        sha256 = SHA256.new()
        sha256.update(name.encode('utf-8'))
        return sha256.hexdigest()

    def __str__(self) -> str:
        """
        String serializer.
        """
        return "<Application: '{}'>".format(self.name)

    def to_json(self) -> dict:
        """
        JSON serializer.
        """
        return {
            self.NAME: self.name,
            self.TYPE: self.get_application_type(),
            self.LAST_MODIFIED: self.get_last_modified_date(),
            self.PACKAGE: self.get_package_name(),
            self.ID: self.pk,
        }

    @classmethod
    def list(cls) -> typing.Generator['Application', None, None]:
        """
        Public class method responsibe for searching
        for all applications.
        """
        logger.info("Listing Applications.")
        for name in os.listdir(config.APKS_ROOT):
            path: str = os.path.join(config.APKS_ROOT, name)
            if path and os.path.isfile(path):
                extension = path.split(".")[-1]
                if extension in config.SUPPORTED_APPS:
                    yield cls(name=name)

    @classmethod
    def find(cls, application_id: str) -> 'Application':
        """
        Public class method responsible for searching
        for one application by ID.

        Since this is just a demo, it will iterate over
        all files in the file system.
        In production, it should send a query to an external database.
        """
        logger.info("Finding Application. | sf_id=%s", application_id)
        for app in cls.list():
            if app.pk == application_id:
                return app
        raise existence.ApplicationNotFoundException(application_id)

    @functools.lru_cache()
    def get_package_name(self) -> str:
        """
        Public class method responsibe for fetching
        the package name.
        """
        output, _ = aapt("dump", "badging", self.get_path(), "|",
                         "grep", "package:", "name")
        for line in output.decode('utf-8').split("\n")[:1]:
            columns = line.split()
            if len(columns) > 1 and "name=" in line:
                return columns[1].replace("name=", "")[1: -1]
        raise runtime.AndroidManagerException(output.decode('utf-8'))
