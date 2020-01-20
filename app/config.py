"""
Application configuration.
"""

import os
import logging

DEBUG = os.environ.get("DEBUG", "")
SECRET = os.environ.get("SECRET", "default-secret-key")

API_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_ROOT = os.path.dirname(API_ROOT)
APP_NAME = os.path.basename(APP_ROOT)

LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
LOG_LEVEL = logging.DEBUG if DEBUG else logging.INFO

ARTIFACTS_ROOT = os.path.join(API_ROOT, "..", "artifacts")

SDK_ROOT = os.environ.get("ANDROID_SDK_ROOT")
AVD_ROOT = os.environ.get("ANDROID_AVD_HOME")
AAPT_ROOT = os.environ.get("ANDROID_AAPT_HOME")
APKS_ROOT = os.path.join(API_ROOT, "..", "apks")
SUPPORTED_APPS = {
    "apk",
}

TEST_SLEEP_CAPTURE = 2
