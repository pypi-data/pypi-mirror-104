"""
Main interface for secretsmanager service client

Usage::

    ```python
    import boto3
    from mypy_boto3_secretsmanager import SecretsManagerClient

    client: SecretsManagerClient = boto3.client("secretsmanager")
    ```
"""
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import ClientMeta

from mypy_boto3_secretsmanager.literals import ListSecretsPaginatorName, SortOrderType
from mypy_boto3_secretsmanager.paginator import ListSecretsPaginator
from mypy_boto3_secretsmanager.type_defs import (
    CancelRotateSecretResponseTypeDef,
    CreateSecretResponseTypeDef,
    DeleteResourcePolicyResponseTypeDef,
    DeleteSecretResponseTypeDef,
    DescribeSecretResponseTypeDef,
    FilterTypeDef,
    GetRandomPasswordResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetSecretValueResponseTypeDef,
    ListSecretsResponseTypeDef,
    ListSecretVersionIdsResponseTypeDef,
    PutResourcePolicyResponseTypeDef,
    PutSecretValueResponseTypeDef,
    RemoveRegionsFromReplicationResponseTypeDef,
    ReplicaRegionTypeTypeDef,
    ReplicateSecretToRegionsResponseTypeDef,
    RestoreSecretResponseTypeDef,
    RotateSecretResponseTypeDef,
    RotationRulesTypeTypeDef,
    StopReplicationToReplicaResponseTypeDef,
    TagTypeDef,
    UpdateSecretResponseTypeDef,
    UpdateSecretVersionStageResponseTypeDef,
    ValidateResourcePolicyResponseTypeDef,
)

__all__ = ("SecretsManagerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    DecryptionFailure: Type[BotocoreClientError]
    EncryptionFailure: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    PreconditionNotMetException: Type[BotocoreClientError]
    PublicPolicyException: Type[BotocoreClientError]
    ResourceExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class SecretsManagerClient:
    """
    [SecretsManager.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions
    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.can_paginate)
        """
    def cancel_rotate_secret(self, SecretId: str) -> CancelRotateSecretResponseTypeDef:
        """
        [Client.cancel_rotate_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.cancel_rotate_secret)
        """
    def create_secret(
        self,
        Name: str,
        ClientRequestToken: str = None,
        Description: str = None,
        KmsKeyId: str = None,
        SecretBinary: Union[bytes, IO[bytes]] = None,
        SecretString: str = None,
        Tags: List["TagTypeDef"] = None,
        AddReplicaRegions: List[ReplicaRegionTypeTypeDef] = None,
        ForceOverwriteReplicaSecret: bool = None,
    ) -> CreateSecretResponseTypeDef:
        """
        [Client.create_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.create_secret)
        """
    def delete_resource_policy(self, SecretId: str) -> DeleteResourcePolicyResponseTypeDef:
        """
        [Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.delete_resource_policy)
        """
    def delete_secret(
        self,
        SecretId: str,
        RecoveryWindowInDays: int = None,
        ForceDeleteWithoutRecovery: bool = None,
    ) -> DeleteSecretResponseTypeDef:
        """
        [Client.delete_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.delete_secret)
        """
    def describe_secret(self, SecretId: str) -> DescribeSecretResponseTypeDef:
        """
        [Client.describe_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.describe_secret)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.generate_presigned_url)
        """
    def get_random_password(
        self,
        PasswordLength: int = None,
        ExcludeCharacters: str = None,
        ExcludeNumbers: bool = None,
        ExcludePunctuation: bool = None,
        ExcludeUppercase: bool = None,
        ExcludeLowercase: bool = None,
        IncludeSpace: bool = None,
        RequireEachIncludedType: bool = None,
    ) -> GetRandomPasswordResponseTypeDef:
        """
        [Client.get_random_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.get_random_password)
        """
    def get_resource_policy(self, SecretId: str) -> GetResourcePolicyResponseTypeDef:
        """
        [Client.get_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.get_resource_policy)
        """
    def get_secret_value(
        self, SecretId: str, VersionId: str = None, VersionStage: str = None
    ) -> GetSecretValueResponseTypeDef:
        """
        [Client.get_secret_value documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.get_secret_value)
        """
    def list_secret_version_ids(
        self,
        SecretId: str,
        MaxResults: int = None,
        NextToken: str = None,
        IncludeDeprecated: bool = None,
    ) -> ListSecretVersionIdsResponseTypeDef:
        """
        [Client.list_secret_version_ids documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.list_secret_version_ids)
        """
    def list_secrets(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
        SortOrder: SortOrderType = None,
    ) -> ListSecretsResponseTypeDef:
        """
        [Client.list_secrets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.list_secrets)
        """
    def put_resource_policy(
        self, SecretId: str, ResourcePolicy: str, BlockPublicPolicy: bool = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        [Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.put_resource_policy)
        """
    def put_secret_value(
        self,
        SecretId: str,
        ClientRequestToken: str = None,
        SecretBinary: Union[bytes, IO[bytes]] = None,
        SecretString: str = None,
        VersionStages: List[str] = None,
    ) -> PutSecretValueResponseTypeDef:
        """
        [Client.put_secret_value documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.put_secret_value)
        """
    def remove_regions_from_replication(
        self, SecretId: str, RemoveReplicaRegions: List[str]
    ) -> RemoveRegionsFromReplicationResponseTypeDef:
        """
        [Client.remove_regions_from_replication documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.remove_regions_from_replication)
        """
    def replicate_secret_to_regions(
        self,
        SecretId: str,
        AddReplicaRegions: List[ReplicaRegionTypeTypeDef],
        ForceOverwriteReplicaSecret: bool = None,
    ) -> ReplicateSecretToRegionsResponseTypeDef:
        """
        [Client.replicate_secret_to_regions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.replicate_secret_to_regions)
        """
    def restore_secret(self, SecretId: str) -> RestoreSecretResponseTypeDef:
        """
        [Client.restore_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.restore_secret)
        """
    def rotate_secret(
        self,
        SecretId: str,
        ClientRequestToken: str = None,
        RotationLambdaARN: str = None,
        RotationRules: "RotationRulesTypeTypeDef" = None,
    ) -> RotateSecretResponseTypeDef:
        """
        [Client.rotate_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.rotate_secret)
        """
    def stop_replication_to_replica(self, SecretId: str) -> StopReplicationToReplicaResponseTypeDef:
        """
        [Client.stop_replication_to_replica documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.stop_replication_to_replica)
        """
    def tag_resource(self, SecretId: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.tag_resource)
        """
    def untag_resource(self, SecretId: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.untag_resource)
        """
    def update_secret(
        self,
        SecretId: str,
        ClientRequestToken: str = None,
        Description: str = None,
        KmsKeyId: str = None,
        SecretBinary: Union[bytes, IO[bytes]] = None,
        SecretString: str = None,
    ) -> UpdateSecretResponseTypeDef:
        """
        [Client.update_secret documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.update_secret)
        """
    def update_secret_version_stage(
        self,
        SecretId: str,
        VersionStage: str,
        RemoveFromVersionId: str = None,
        MoveToVersionId: str = None,
    ) -> UpdateSecretVersionStageResponseTypeDef:
        """
        [Client.update_secret_version_stage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.update_secret_version_stage)
        """
    def validate_resource_policy(
        self, ResourcePolicy: str, SecretId: str = None
    ) -> ValidateResourcePolicyResponseTypeDef:
        """
        [Client.validate_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Client.validate_resource_policy)
        """
    def get_paginator(self, operation_name: ListSecretsPaginatorName) -> ListSecretsPaginator:
        """
        [Paginator.ListSecrets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/secretsmanager.html#SecretsManager.Paginator.ListSecrets)
        """
