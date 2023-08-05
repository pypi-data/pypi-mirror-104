# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from fedlearner.common import common_pb2 as fedlearner_dot_common_dot_common__pb2
from fedlearner.common import scheduler_service_pb2 as fedlearner_dot_common_dot_scheduler__service__pb2


class SchedulerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ModelAuth = channel.unary_unary(
                '/fedlearner.common.Scheduler/ModelAuth',
                request_serializer=fedlearner_dot_common_dot_scheduler__service__pb2.ModelAuthRequest.SerializeToString,
                response_deserializer=fedlearner_dot_common_dot_common__pb2.Status.FromString,
                )
        self.SubmitTrainJob = channel.unary_unary(
                '/fedlearner.common.Scheduler/SubmitTrainJob',
                request_serializer=fedlearner_dot_common_dot_scheduler__service__pb2.TrainJobRequest.SerializeToString,
                response_deserializer=fedlearner_dot_common_dot_common__pb2.Status.FromString,
                )
        self.SubmitEvalJob = channel.unary_unary(
                '/fedlearner.common.Scheduler/SubmitEvalJob',
                request_serializer=fedlearner_dot_common_dot_scheduler__service__pb2.EvalJobRequest.SerializeToString,
                response_deserializer=fedlearner_dot_common_dot_common__pb2.Status.FromString,
                )


class SchedulerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ModelAuth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitTrainJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitEvalJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SchedulerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ModelAuth': grpc.unary_unary_rpc_method_handler(
                    servicer.ModelAuth,
                    request_deserializer=fedlearner_dot_common_dot_scheduler__service__pb2.ModelAuthRequest.FromString,
                    response_serializer=fedlearner_dot_common_dot_common__pb2.Status.SerializeToString,
            ),
            'SubmitTrainJob': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitTrainJob,
                    request_deserializer=fedlearner_dot_common_dot_scheduler__service__pb2.TrainJobRequest.FromString,
                    response_serializer=fedlearner_dot_common_dot_common__pb2.Status.SerializeToString,
            ),
            'SubmitEvalJob': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitEvalJob,
                    request_deserializer=fedlearner_dot_common_dot_scheduler__service__pb2.EvalJobRequest.FromString,
                    response_serializer=fedlearner_dot_common_dot_common__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fedlearner.common.Scheduler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Scheduler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ModelAuth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fedlearner.common.Scheduler/ModelAuth',
            fedlearner_dot_common_dot_scheduler__service__pb2.ModelAuthRequest.SerializeToString,
            fedlearner_dot_common_dot_common__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitTrainJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fedlearner.common.Scheduler/SubmitTrainJob',
            fedlearner_dot_common_dot_scheduler__service__pb2.TrainJobRequest.SerializeToString,
            fedlearner_dot_common_dot_common__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitEvalJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fedlearner.common.Scheduler/SubmitEvalJob',
            fedlearner_dot_common_dot_scheduler__service__pb2.EvalJobRequest.SerializeToString,
            fedlearner_dot_common_dot_common__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
