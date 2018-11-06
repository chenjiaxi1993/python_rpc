# coding=utf-8
# client.py

import json
import time
import struct
import socket

_HOST = "127.0.0.1"
_PORT = 8080


def rpc(sock, input, params):
    """
    Send RPC request.
    :param sock:
    :param input:
    :param params:
    :return:
    """
    response = json.dumps({"in": input, "params": params})
    length_prefix = struct.pack("I", len(response))
    sock.send(length_prefix)
    sock.sendall(response.encode('utf-8'))  # sendall = send + flush
    length_prefix = sock.recv(4)  # response prefix
    length, = struct.unpack("I", length_prefix)
    body = sock.recv(length)  # response body
    response = json.loads(body)
    return response["out"], response["result"]


if __name__ == '__main__':
    s = socket.socket()
    s.connect((_HOST, _PORT))
    for i in range(10):
        out, result = rpc(s, "ping", "ireader %d" % i)
        print(out, result)
        time.sleep(1)
    s.close()
