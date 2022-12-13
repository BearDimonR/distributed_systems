# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import cards_pb2 as cards__pb2


class CardsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCard = channel.unary_unary(
                '/Cards/GetCard',
                request_serializer=cards__pb2.CardRequest.SerializeToString,
                response_deserializer=cards__pb2.CardResponse.FromString,
                )
        self.ReactOnCard = channel.unary_unary(
                '/Cards/ReactOnCard',
                request_serializer=cards__pb2.ReactOnCardRequest.SerializeToString,
                response_deserializer=cards__pb2.CardResponse.FromString,
                )


class CardsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetCard(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReactOnCard(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CardsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCard': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCard,
                    request_deserializer=cards__pb2.CardRequest.FromString,
                    response_serializer=cards__pb2.CardResponse.SerializeToString,
            ),
            'ReactOnCard': grpc.unary_unary_rpc_method_handler(
                    servicer.ReactOnCard,
                    request_deserializer=cards__pb2.ReactOnCardRequest.FromString,
                    response_serializer=cards__pb2.CardResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Cards', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Cards(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetCard(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Cards/GetCard',
            cards__pb2.CardRequest.SerializeToString,
            cards__pb2.CardResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReactOnCard(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Cards/ReactOnCard',
            cards__pb2.ReactOnCardRequest.SerializeToString,
            cards__pb2.CardResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)