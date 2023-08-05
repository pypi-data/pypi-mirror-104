# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fedlearner.channel import channel_pb2 as fedlearner_dot_channel_dot_channel__pb2


class ChannelStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Call = channel.unary_unary(
                '/fedlearner.bridge.Channel/Call',
                request_serializer=fedlearner_dot_channel_dot_channel__pb2.CallRequest.SerializeToString,
                response_deserializer=fedlearner_dot_channel_dot_channel__pb2.CallResponse.FromString,
                )


class ChannelServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Call(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChannelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Call': grpc.unary_unary_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=fedlearner_dot_channel_dot_channel__pb2.CallRequest.FromString,
                    response_serializer=fedlearner_dot_channel_dot_channel__pb2.CallResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fedlearner.bridge.Channel', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Channel(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fedlearner.bridge.Channel/Call',
            fedlearner_dot_channel_dot_channel__pb2.CallRequest.SerializeToString,
            fedlearner_dot_channel_dot_channel__pb2.CallResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
