# coding=utf-8
# pi_server.py
import math
import time
import grpc
import json
from concurrent import futures
from proto import pi_pb2, pi_pb2_grpc


class PiCalculatorServicer(pi_pb2_grpc.PiCaculatorServicer):
    """
    Implemented PiCaculatorServicer
    """

    def Calc(self, request, context):
        """
        Calculate pi
        :param request:
        :param context:
        :return:
        """
        # Error handling
        if request.n <= 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("request number should be positive")
            context.set_details(
                json.dumps({
                    "biz_err_code": 10086,
                    "msg": "Customized Error"
                }))
            context.send_initial_metadata([("binary-metadata-bin", "Value")])
            return pi_pb2.PiResponse()
        s = 0.0
        for i in range(request.n):
            s += 1.0 / (2 * i + 1) / (2 * i + 1)
        # simulate I/O for multi-thread calls
        time.sleep(0.01)
        # return a PiResponse
        return pi_pb2.PiResponse(value=math.sqrt(8 * s))


def main():
    _HOST = "127.0.0.1"
    _PORT = "8080"
    # multi-thread server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # instantiate PiCalculatorServicer
    servicer = PiCalculatorServicer()
    # register local service
    pi_pb2_grpc.add_PiCaculatorServicer_to_server(servicer, server)
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
