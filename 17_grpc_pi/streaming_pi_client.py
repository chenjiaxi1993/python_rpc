# coding=utf-8
# streaming_pi_client.py
import grpc

from streaming_proto import streaming_pi_pb2, streaming_pi_pb2_grpc


def generate_request():
    """
    Generate request...
    :return:
    """
    for i in range(1, 1000):
        yield streaming_pi_pb2.PiRequest(n=i)


def main():
    _HOST = "127.0.0.1"
    _PORT = "8080"
    channel = grpc.insecure_channel(_HOST + ":" + _PORT)
    client = streaming_pi_pb2_grpc.PiCaculatorStub(channel)
    response_iterator = client.Calc(generate_request())
    # call RPC method
    for response in response_iterator:
        print("pi(%d) = %.10f" % (response.n, response.value))


if __name__ == "__main__":
    main()
