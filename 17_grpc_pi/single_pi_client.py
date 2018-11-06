# coding=utf-8
# single_pi_client.py
import grpc

from proto import pi_pb2, pi_pb2_grpc


def main():
    _HOST = "127.0.0.1"
    _PORT = "8080"
    # use client stub
    # TODO@(chenjiaxi01): the detail of channel
    channel = grpc.insecure_channel(_HOST + ":" + _PORT)
    client = pi_pb2_grpc.PiCaculatorStub(channel)
    # call RPC method
    for i in range(10):
        try:
            print("pi(%d) = %.10f" %
                  (i, client.Calc(pi_pb2.PiRequest(n=i)).value))
            # client.Calc(pi_pb2.PiRequest(n=i))
        except grpc.RpcError as e:
            print("RpcError: ", e.code(), e.details(), e.initial_metadata())


if __name__ == "__main__":
    main()
