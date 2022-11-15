# *_*coding:utf-8 *_*
# @Author : Reggie
# @Time : 2022/11/15 11:01
import asyncio
import logging

from lib.echo import EchoBase, EchoRequest, EchoResponse, EchoStreamResponse
from grpclib.server import Server
from typing import AsyncIterator
from grpclib.server import CodecBase

class EchoService(EchoBase):
    async def echo(self, echo_request: "EchoRequest") -> "EchoResponse":
        return EchoResponse([echo_request.value for _ in range(echo_request.extra_times)])

    async def echo_stream(self, echo_request: "EchoRequest") -> AsyncIterator["EchoStreamResponse"]:
        for _ in range(echo_request.extra_times):
            yield EchoStreamResponse(echo_request.value)


async def main():
    server = Server([EchoService()])
    await server.start("127.0.0.1", 50051)
    await server.wait_closed()

if __name__ == '__main__':
    stream_handle = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s -- %(levelname)s --"
                                  " %(message)s (%(funcName)s in %(filename)s %(lineno)d)")
    stream_handle.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(stream_handle)
    logger.setLevel(logging.DEBUG)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())