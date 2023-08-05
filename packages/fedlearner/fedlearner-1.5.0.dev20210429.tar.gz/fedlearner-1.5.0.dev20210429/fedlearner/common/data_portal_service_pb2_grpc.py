# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fedlearner.common import common_pb2 as fedlearner_dot_common_dot_common__pb2
from fedlearner.common import data_portal_service_pb2 as fedlearner_dot_common_dot_data__portal__service__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DataPortalMasterServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDataPortalManifest = channel.unary_unary(
                '/fedlearner.common.DataPortalMasterService/GetDataPortalManifest',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=fedlearner_dot_common_dot_data__portal__service__pb2.DataPortalManifest.FromString,
                )
        self.RequestNewTask = channel.unary_unary(
                '/fedlearner.common.DataPortalMasterService/RequestNewTask',
                request_serializer=fedlearner_dot_common_dot_data__portal__service__pb2.NewTaskRequest.SerializeToString,
                response_deserializer=fedlearner_dot_common_dot_data__portal__service__pb2.NewTaskResponse.FromString,
                )
        self.FinishTask = channel.unary_unary(
                '/fedlearner.common.DataPortalMasterService/FinishTask',
                request_serializer=fedlearner_dot_common_dot_data__portal__service__pb2.FinishTaskRequest.SerializeToString,
                response_deserializer=fedlearner_dot_common_dot_common__pb2.Status.FromString,
                )


class DataPortalMasterServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetDataPortalManifest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RequestNewTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FinishTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataPortalMasterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDataPortalManifest': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDataPortalManifest,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=fedlearner_dot_common_dot_data__portal__service__pb2.DataPortalManifest.SerializeToString,
            ),
            'RequestNewTask': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestNewTask,
                    request_deserializer=fedlearner_dot_common_dot_data__portal__service__pb2.NewTaskRequest.FromString,
                    response_serializer=fedlearner_dot_common_dot_data__portal__service__pb2.NewTaskResponse.SerializeToString,
            ),
            'FinishTask': grpc.unary_unary_rpc_method_handler(
                    servicer.FinishTask,
                    request_deserializer=fedlearner_dot_common_dot_data__portal__service__pb2.FinishTaskRequest.FromString,
                    response_serializer=fedlearner_dot_common_dot_common__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fedlearner.common.DataPortalMasterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataPortalMasterService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetDataPortalManifest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fedlearner.common.DataPortalMasterService/GetDataPortalManifest',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            fedlearner_dot_common_dot_data__portal__service__pb2.DataPortalManifest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RequestNewTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fedlearner.common.DataPortalMasterService/RequestNewTask',
            fedlearner_dot_common_dot_data__portal__service__pb2.NewTaskRequest.SerializeToString,
            fedlearner_dot_common_dot_data__portal__service__pb2.NewTaskResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FinishTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fedlearner.common.DataPortalMasterService/FinishTask',
            fedlearner_dot_common_dot_data__portal__service__pb2.FinishTaskRequest.SerializeToString,
            fedlearner_dot_common_dot_common__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
