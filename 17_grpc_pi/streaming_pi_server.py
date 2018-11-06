# coding=utf-8
import math
import random
import time
import grpc
from concurrent import futures

from streaming_proto import streaming_pi_pb2, streaming_pi_pb2_grpc


class PiCalculatorServicer(streaming_pi_pb2_grpc.PiCaculatorServicer):
    """
    Implemented PiCaculatorServicer
    """

    def Calc(self, request_iterator, context):
        """
        Calculate pi in streaming request
        :param request_iterator: an iterator argument responding to
            a stream RPC request
        :param context:
        :return:
        """
        # request is an iterator argument responding to a stream RPC request
        for request in request_iterator:
            # response probability is 50%
            if random.randint(0, 1) == 1:
                continue
            s = 0.0
            for i in range(request.n):
                s += 1.0 / (2 * i + 1) / (2 * i + 1)
            # response is a generator
            yield streaming_pi_pb2.PiResponse(n=i, value=math.sqrt(8 * s))


def main():
    _HOST = "127.0.0.1"
    _PORT = "8080"
    # multi-thread server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # instantiate PiCalculatorServicer
    servicer = PiCalculatorServicer()
    # register local service
    streaming_pi_pb2_grpc.add_PiCaculatorServicer_to_server(servicer, server)
    # listen
    server.add_insecure_port(_HOST + ":" + _PORT)
    # start to serve
    server.start()
    try:
        time.sleep(1000)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    main()
