"""
Flask Main Application.
"""

import logging

from flask import Flask

from app import config
from app.api import api

logger = logging.getLogger(__name__)


def create_app() -> Flask:  # pylint: disable=too-many-statements
    """
    Flask Factory pattern.

    Reference:
    http://flask.pocoo.org/docs/1.0/patterns/appfactories/
    """
    montevideo = Flask(__name__)
    montevideo.url_map.strict_slashes = False

    # Secret Key is required by Flask-Session.
    montevideo.secret_key = config.SECRET

    # Setting debug mode.
    montevideo.debug = bool(config.DEBUG)

    # Updating logger messages.
    logging.basicConfig(level=config.LOG_LEVEL, format=config.LOG_FORMAT)

    # Registering app views.
    api.init_app(montevideo)

    # End of app factory.
    logger.info("App started!")
    return montevideo
