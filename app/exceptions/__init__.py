"""
Application exceptions.
All exceptions must inherit from the class in this library.
"""

import logging

logger = logging.getLogger()


class MontevideoException(Exception):
    """
    Core class for all app exceptions.
    """

    CODE = 500
    SUBCODE = 5000
    MESSAGE = "Unexpected Error"

    RESPONSE_CODE = "code"
    RESPONSE_TYPE = "type"
    RESPONSE_SUBCODE = "subcode"
    RESPONSE_ERROR = "error"

    def __init__(self, *errors) -> None:
        """
        Initializing exception with custom errors.
        """
        Exception.__init__(self, *errors)
        self.__errors = errors
        logger.error("APP ERROR | sf_type=%s | sf_errors=%s", self, errors)

    @property
    def code(self) -> int:
        """
        Status code getter.
        """
        return self.CODE

    @property
    def subcode(self) -> int:
        """
        Subcode getter.
        """
        return self.SUBCODE

    def to_str(self) -> str:
        """
        String serializer.
        """
        return " ".join([
            self.MESSAGE,
            "".join([
                str(error)
                for error in self.__errors
            ])
        ]).strip()

    def to_json(self) -> dict:
        """
        JSON serializer.
        """
        return {
            self.RESPONSE_CODE: self.code,
            self.RESPONSE_TYPE: "{}".format(self.__class__.__name__),
            self.RESPONSE_SUBCODE: self.subcode,
            self.RESPONSE_ERROR: self.to_str(),
        }
