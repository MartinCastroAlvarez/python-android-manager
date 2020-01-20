"""
Tests controllers.

These functions are responsible for validating
the request and interacting with the models.
"""

import time
import logging

from app.controllers.applications import ApplicationsController
from app.controllers.devices import DevicesController
from app.models.test import Test, Status, Artifact
from app.exceptions import runtime
from app import config

logger = logging.getLogger(__name__)


class TestsController:
    """
    TEsts business logic.

    This controller allows the client to test
    applications on any device.
    """

    @classmethod
    def test(cls, application_id: str, device_id: str) -> Test:
        """
        Business method to test an application on a device.
        """
        logger.debug("Test | sf_device_id=%s | sf_application=%s",
                     device_id, application_id)
        test = Test(device=DevicesController.describe(device_id),
                    application=ApplicationsController.describe(application_id))
        artifact: Artifact = Artifact.build()
        try:
            test.device.go_home()
            test.device.uninstall(package=test.application.get_package_name())
            test.device.install(apk=test.application.get_path())
            test.device.open(package=test.application.get_package_name())
            time.sleep(config.TEST_SLEEP_CAPTURE)
            test.device.capture(path=artifact.path)
            test.device.go_home()
        except runtime.RuntimeException as error:
            logger.exception("Error. | sf_test=%s", test.pk)
            test.status = Status.ERROR
            test.error = error.to_json()
        else:
            logger.debug("End. | sf_test=%s", test.pk)
            test.status = Status.SUCCESS
            test.artifacts.append(artifact)
        return test
