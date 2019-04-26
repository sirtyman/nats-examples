from enum import Enum


CORE_UUID = 'CORE'


class Endpoints(Enum):
    FRONTEND = 'FRONTEND'


class RoutingLayer(object):
    def __init__(self):
        self.client_uuid = CORE_UUID
        self.subject = "{}.{}".format(self.client_uuid, Endpoints.FRONTEND)
