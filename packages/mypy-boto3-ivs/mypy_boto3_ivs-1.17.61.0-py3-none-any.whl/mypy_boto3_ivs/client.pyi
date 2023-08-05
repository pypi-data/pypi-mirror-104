"""
Main interface for ivs service client

Usage::

    ```python
    import boto3
    from mypy_boto3_ivs import IVSClient

    client: IVSClient = boto3.client("ivs")
    ```
"""
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_ivs.literals import (
    ChannelLatencyMode,
    ChannelType,
    ListChannelsPaginatorName,
    ListPlaybackKeyPairsPaginatorName,
    ListRecordingConfigurationsPaginatorName,
    ListStreamKeysPaginatorName,
    ListStreamsPaginatorName,
)
from mypy_boto3_ivs.paginator import (
    ListChannelsPaginator,
    ListPlaybackKeyPairsPaginator,
    ListRecordingConfigurationsPaginator,
    ListStreamKeysPaginator,
    ListStreamsPaginator,
)
from mypy_boto3_ivs.type_defs import (
    BatchGetChannelResponseTypeDef,
    BatchGetStreamKeyResponseTypeDef,
    CreateChannelResponseTypeDef,
    CreateRecordingConfigurationResponseTypeDef,
    CreateStreamKeyResponseTypeDef,
    DestinationConfigurationTypeDef,
    GetChannelResponseTypeDef,
    GetPlaybackKeyPairResponseTypeDef,
    GetRecordingConfigurationResponseTypeDef,
    GetStreamKeyResponseTypeDef,
    GetStreamResponseTypeDef,
    ImportPlaybackKeyPairResponseTypeDef,
    ListChannelsResponseTypeDef,
    ListPlaybackKeyPairsResponseTypeDef,
    ListRecordingConfigurationsResponseTypeDef,
    ListStreamKeysResponseTypeDef,
    ListStreamsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    UpdateChannelResponseTypeDef,
)

__all__ = ("IVSClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ChannelNotBroadcasting: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PendingVerification: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    StreamUnavailable: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IVSClient:
    """
    [IVS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def batch_get_channel(self, arns: List[str]) -> BatchGetChannelResponseTypeDef:
        """
        [Client.batch_get_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.batch_get_channel)
        """
    def batch_get_stream_key(self, arns: List[str]) -> BatchGetStreamKeyResponseTypeDef:
        """
        [Client.batch_get_stream_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.batch_get_stream_key)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.can_paginate)
        """
    def create_channel(
        self,
        name: str = None,
        latencyMode: ChannelLatencyMode = None,
        type: ChannelType = None,
        authorized: bool = None,
        recordingConfigurationArn: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateChannelResponseTypeDef:
        """
        [Client.create_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.create_channel)
        """
    def create_recording_configuration(
        self,
        destinationConfiguration: "DestinationConfigurationTypeDef",
        name: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateRecordingConfigurationResponseTypeDef:
        """
        [Client.create_recording_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.create_recording_configuration)
        """
    def create_stream_key(
        self, channelArn: str, tags: Dict[str, str] = None
    ) -> CreateStreamKeyResponseTypeDef:
        """
        [Client.create_stream_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.create_stream_key)
        """
    def delete_channel(self, arn: str) -> None:
        """
        [Client.delete_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.delete_channel)
        """
    def delete_playback_key_pair(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_playback_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.delete_playback_key_pair)
        """
    def delete_recording_configuration(self, arn: str) -> None:
        """
        [Client.delete_recording_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.delete_recording_configuration)
        """
    def delete_stream_key(self, arn: str) -> None:
        """
        [Client.delete_stream_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.delete_stream_key)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.generate_presigned_url)
        """
    def get_channel(self, arn: str) -> GetChannelResponseTypeDef:
        """
        [Client.get_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.get_channel)
        """
    def get_playback_key_pair(self, arn: str) -> GetPlaybackKeyPairResponseTypeDef:
        """
        [Client.get_playback_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.get_playback_key_pair)
        """
    def get_recording_configuration(self, arn: str) -> GetRecordingConfigurationResponseTypeDef:
        """
        [Client.get_recording_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.get_recording_configuration)
        """
    def get_stream(self, channelArn: str) -> GetStreamResponseTypeDef:
        """
        [Client.get_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.get_stream)
        """
    def get_stream_key(self, arn: str) -> GetStreamKeyResponseTypeDef:
        """
        [Client.get_stream_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.get_stream_key)
        """
    def import_playback_key_pair(
        self, publicKeyMaterial: str, name: str = None, tags: Dict[str, str] = None
    ) -> ImportPlaybackKeyPairResponseTypeDef:
        """
        [Client.import_playback_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.import_playback_key_pair)
        """
    def list_channels(
        self,
        filterByName: str = None,
        filterByRecordingConfigurationArn: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListChannelsResponseTypeDef:
        """
        [Client.list_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.list_channels)
        """
    def list_playback_key_pairs(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListPlaybackKeyPairsResponseTypeDef:
        """
        [Client.list_playback_key_pairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.list_playback_key_pairs)
        """
    def list_recording_configurations(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListRecordingConfigurationsResponseTypeDef:
        """
        [Client.list_recording_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.list_recording_configurations)
        """
    def list_stream_keys(
        self, channelArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListStreamKeysResponseTypeDef:
        """
        [Client.list_stream_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.list_stream_keys)
        """
    def list_streams(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListStreamsResponseTypeDef:
        """
        [Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.list_streams)
        """
    def list_tags_for_resource(
        self, resourceArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.list_tags_for_resource)
        """
    def put_metadata(self, channelArn: str, metadata: str) -> None:
        """
        [Client.put_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.put_metadata)
        """
    def stop_stream(self, channelArn: str) -> Dict[str, Any]:
        """
        [Client.stop_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.stop_stream)
        """
    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.tag_resource)
        """
    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.untag_resource)
        """
    def update_channel(
        self,
        arn: str,
        name: str = None,
        latencyMode: ChannelLatencyMode = None,
        type: ChannelType = None,
        authorized: bool = None,
        recordingConfigurationArn: str = None,
    ) -> UpdateChannelResponseTypeDef:
        """
        [Client.update_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Client.update_channel)
        """
    @overload
    def get_paginator(self, operation_name: ListChannelsPaginatorName) -> ListChannelsPaginator:
        """
        [Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Paginator.ListChannels)
        """
    @overload
    def get_paginator(
        self, operation_name: ListPlaybackKeyPairsPaginatorName
    ) -> ListPlaybackKeyPairsPaginator:
        """
        [Paginator.ListPlaybackKeyPairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Paginator.ListPlaybackKeyPairs)
        """
    @overload
    def get_paginator(
        self, operation_name: ListRecordingConfigurationsPaginatorName
    ) -> ListRecordingConfigurationsPaginator:
        """
        [Paginator.ListRecordingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Paginator.ListRecordingConfigurations)
        """
    @overload
    def get_paginator(self, operation_name: ListStreamKeysPaginatorName) -> ListStreamKeysPaginator:
        """
        [Paginator.ListStreamKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Paginator.ListStreamKeys)
        """
    @overload
    def get_paginator(self, operation_name: ListStreamsPaginatorName) -> ListStreamsPaginator:
        """
        [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/ivs.html#IVS.Paginator.ListStreams)
        """
