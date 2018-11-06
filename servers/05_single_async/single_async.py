# coding=utf-8
# single_async.py

import asyncore
import json
import struct
import socket
from io import StringIO

_HOST = "127.0.0.1"
_PORT = 8080


class RPCHandler(asyncore.dispatcher_with_send):
    """
    Handle client connection
    """

    def __init__(self, sock, addr):
        asyncore.dispatcher_with_send.__init__(self, sock=sock)
        self.addr = addr
        self.handlers = {"ping": self.ping}
        # read buffer is maintained by user
        # write buffer is maintained by asyncore
        self.rbuf = StringIO()

    def handle_connect(self):
        """
        Callback when new connection is accepted.
        :return:
        """
        pass

    def handle_close(self):
        """
        Callback before connection is closed.
        :return:
        """
        print(self.addr, "bye")
        self.close()

    def handle_read(self):
        """
        Callback when read event occurs.
        :return:
        """
        while True:
            try:
                content = self.recv(1024)
                if content:
                    self.rbuf.write(content.decode('utf-8'))
                if len(content) < 1024:
                    break
            except Exception as e:
                print(e)
        self.handle_rpc()

    def handle_rpc(self):
        """
        Unpack read message and handle with it.
        :return:
        """
        while True:  # loop handling
            self.rbuf.seek(0)
            length_prefix = self.rbuf.read(4)
            if len(length_prefix) < 4:  # half-package
                break

            try:
                length, = struct.unpack("I", length_prefix.encode("utf-8"))
            except Exception as e:
                print(e.__traceback__)
            body = self.rbuf.read(length)
            if len(body) < length:  # half-package
                break

            request = json.loads(body)
            input = request["in"]
            params = request["params"]
            handler = self.handlers[input]
            handler(params)
            # cut read buffer
            left = self.rbuf.getvalue()[length + 4:]
            self.rbuf = StringIO()
            self.rbuf.write(left)
        # move position to EOF
        self.rbuf.seek(0, 2)

    def ping(self, params):
        self.send_result("pong", params)

    def send_result(self, out, result):
        response = json.dumps({"out": out, "result": result})
        length_prefix = struct.pack("I", len(response))
        self.send(length_prefix)
        self.send(response.encode('utf-8'))


class RPCServer(asyncore.dispatcher):
    """
    RPC Server using `asyncore` to handle connection async.
    """

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(1)

    def handle_accept(self):
        """
        Callback when new connection is accepted.
        """
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print(repr(addr), "comes")
            RPCHandler(sock, addr)


if __name__ == '__main__':
    RPCServer(_HOST, _PORT)
    # select events and handle them
    asyncore.loop()
