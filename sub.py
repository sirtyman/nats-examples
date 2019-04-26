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
import routing_layer
from nats.io.client import Client as NATS


@tornado.gen.coroutine
def handler(msg):
    print("[Received: {0}] {1}".format(msg.subject, msg.data))
    print("Deserialize the data and process")


@tornado.gen.coroutine
def main():
    nc = NATS()
    servers = ["nats://127.0.0.1:4222"]

    rl = routing_layer.RoutingLayer()

    yield nc.connect(servers)
    yield nc.subscribe(subject=rl.subject, queue='', cb=handler)


if __name__ == '__main__':
    main()
    tornado.ioloop.IOLoop.current().start()
