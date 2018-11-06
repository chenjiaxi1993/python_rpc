# coding=utf-8
# single_pi_client.py
import grpc

from proto import pi_pb2, pi_pb2_grpc
from concurrent import futures


def pi(client, k):
    """
    Calculate pi
    :param client:
    :param k:
    :return:
    """
    return client.Calc(pi_pb2.PiRequest(n=k)).value


def main():
    _HOST = "127.0.0.1"
    _PORT = "8080"
    channel = grpc.insecure_channel(_HOST + ":" + _PORT)
    # client is thread-safe
    client = pi_pb2_grpc.PiCaculatorStub(channel)
    # call RPC method by multiple thread
    pool = futures.ThreadPoolExecutor(max_workers=4)
    results = []
    for i in range(1, 1000):
        results.append((i, pool.submit(pi, client, i)))
    # wait until all tasks are completed
    pool.shutdown()
    # for i, future in results:
    #     print(i, future.result())


if __name__ == "__main__":
    main()
