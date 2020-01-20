"""
Application API.

These classes are only responsible for authenticating
the request and handling exceptions on behalf of the client.
"""

# pylint: disable=invalid-name

from flask_restful import Api

from app.api.devices import DevicesResource,\
                            DeviceResource
from app.api.tests import TestResource
from app.api.applications import ApplicationsResource,\
                                 ApplicationResource

api = Api()

# Devices API.
api.add_resource(ApplicationResource,
                 "/v1/applications/<application_id>")
api.add_resource(ApplicationsResource,
                 "/v1/applications")

# Tests API.
api.add_resource(TestResource,
                 "/v1/devices/<device_id>/applications/<application_id>")
# api.add_resource(TestResource,
#                  "/v1/applications/<device_id>/devices/<application_id>")

# Applications API.
api.add_resource(DeviceResource,
                 "/v1/devices/<device_id>")
api.add_resource(DevicesResource,
                 "/v1/devices")
