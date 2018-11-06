# coding=utf-8
# blocking_multithread.py

import json
import struct
import socket
import thread

_HOST = "127.0.0.1"
_PORT = 8080


def handle_conn(conn, addr, handlers):
    """

    :param conn:
    :param addr:
    :param handlers:
    :return:
    """
    print(addr, "comes")
    while True:
        length_prefix = conn.recv(4)
        if not length_prefix:
            print(addr, "bye")
            conn.close()
            break

        length, = struct.unpack("I", length_prefix)
        body = conn.recv(length)
        request = json.loads(body)
        input = request["in"]
        params = request["params"]
        print(input, params)
        handler = handlers[input]
        handler(conn, params)


def loop(sock, handlers):
    """

    :param sock:
    :param handlers:
    :return:
    """
    while True:
        conn, addr = sock.accept()
        # create new thread to handle connection
        thread.start_new_thread(handle_conn, (conn, addr, handlers))


def ping(conn, params):
    """

    :param conn:
    :param params:
    :return:
    """
    send_result(conn, "pong", params)


def send_result(conn, out, result):
    """

    :param conn:
    :param out:
    :param result:
    :return:
    """
    response = json.dumps({"out": out, "result": result})
    length_prefix = struct.pack("I", len(response))
    conn.send(length_prefix)
    conn.sendall(response.encode('utf-8'))


if __name__ == '__main__':
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((_HOST, _PORT))
    sock.listen(1)
    # register request handler
    handlers = {"ping": ping}
    loop(sock, handlers)
