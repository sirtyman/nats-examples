# Copyright 2015-2018 The NATS Authors
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import tornado.ioloop
import tornado.gen
from nats.io.client import Client as NATS
from routing_layer import RoutingLayer

servers = ["nats://127.0.0.1:4222"]


class Client(object):
    def __init__(self, servers):
        self.nc = NATS()
        self.servers = servers
        self.routing_layer = RoutingLayer()

    @tornado.gen.coroutine
    def activate(self):
        yield self.nc.connect(self.servers)

    @tornado.gen.coroutine
    def publish(self, payload):
        yield self.nc.publish(self.routing_layer.subject, payload)
        yield self.nc.flush()


@tornado.gen.coroutine
def main():
    client = Client(servers)
    yield client.activate()

    while True:
        yield client.publish("Hallo Consumer")
        yield tornado.gen.sleep(1)


if __name__ == '__main__':
    tornado.ioloop.IOLoop.current().run_sync(main)