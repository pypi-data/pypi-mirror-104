"""
Main interface for appsync service type definitions.

Usage::

    ```python
    from mypy_boto3_appsync.type_defs import AdditionalAuthenticationProviderTypeDef

    data: AdditionalAuthenticationProviderTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Union

from mypy_boto3_appsync.literals import (
    ApiCacheStatus,
    ApiCacheType,
    ApiCachingBehavior,
    AuthenticationType,
    AuthorizationType,
    ConflictDetectionType,
    ConflictHandlerType,
    DataSourceType,
    DefaultAction,
    FieldLogLevel,
    RelationalDatabaseSourceType,
    ResolverKind,
    SchemaStatus,
    TypeDefinitionFormat,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AdditionalAuthenticationProviderTypeDef",
    "ApiCacheTypeDef",
    "ApiKeyTypeDef",
    "AuthorizationConfigTypeDef",
    "AwsIamConfigTypeDef",
    "CachingConfigTypeDef",
    "CognitoUserPoolConfigTypeDef",
    "DataSourceTypeDef",
    "DeltaSyncConfigTypeDef",
    "DynamodbDataSourceConfigTypeDef",
    "ElasticsearchDataSourceConfigTypeDef",
    "FunctionConfigurationTypeDef",
    "GraphqlApiTypeDef",
    "HttpDataSourceConfigTypeDef",
    "LambdaConflictHandlerConfigTypeDef",
    "LambdaDataSourceConfigTypeDef",
    "LogConfigTypeDef",
    "OpenIDConnectConfigTypeDef",
    "PipelineConfigTypeDef",
    "RdsHttpEndpointConfigTypeDef",
    "RelationalDatabaseDataSourceConfigTypeDef",
    "ResolverTypeDef",
    "SyncConfigTypeDef",
    "TypeTypeDef",
    "UserPoolConfigTypeDef",
    "CreateApiCacheResponseTypeDef",
    "CreateApiKeyResponseTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateFunctionResponseTypeDef",
    "CreateGraphqlApiResponseTypeDef",
    "CreateResolverResponseTypeDef",
    "CreateTypeResponseTypeDef",
    "GetApiCacheResponseTypeDef",
    "GetDataSourceResponseTypeDef",
    "GetFunctionResponseTypeDef",
    "GetGraphqlApiResponseTypeDef",
    "GetIntrospectionSchemaResponseTypeDef",
    "GetResolverResponseTypeDef",
    "GetSchemaCreationStatusResponseTypeDef",
    "GetTypeResponseTypeDef",
    "ListApiKeysResponseTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListFunctionsResponseTypeDef",
    "ListGraphqlApisResponseTypeDef",
    "ListResolversByFunctionResponseTypeDef",
    "ListResolversResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTypesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "StartSchemaCreationResponseTypeDef",
    "UpdateApiCacheResponseTypeDef",
    "UpdateApiKeyResponseTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateFunctionResponseTypeDef",
    "UpdateGraphqlApiResponseTypeDef",
    "UpdateResolverResponseTypeDef",
    "UpdateTypeResponseTypeDef",
)

AdditionalAuthenticationProviderTypeDef = TypedDict(
    "AdditionalAuthenticationProviderTypeDef",
    {
        "authenticationType": AuthenticationType,
        "openIDConnectConfig": "OpenIDConnectConfigTypeDef",
        "userPoolConfig": "CognitoUserPoolConfigTypeDef",
    },
    total=False,
)

ApiCacheTypeDef = TypedDict(
    "ApiCacheTypeDef",
    {
        "ttl": int,
        "apiCachingBehavior": ApiCachingBehavior,
        "transitEncryptionEnabled": bool,
        "atRestEncryptionEnabled": bool,
        "type": ApiCacheType,
        "status": ApiCacheStatus,
    },
    total=False,
)

ApiKeyTypeDef = TypedDict(
    "ApiKeyTypeDef", {"id": str, "description": str, "expires": int, "deletes": int}, total=False
)

_RequiredAuthorizationConfigTypeDef = TypedDict(
    "_RequiredAuthorizationConfigTypeDef", {"authorizationType": AuthorizationType}
)
_OptionalAuthorizationConfigTypeDef = TypedDict(
    "_OptionalAuthorizationConfigTypeDef", {"awsIamConfig": "AwsIamConfigTypeDef"}, total=False
)


class AuthorizationConfigTypeDef(
    _RequiredAuthorizationConfigTypeDef, _OptionalAuthorizationConfigTypeDef
):
    pass


AwsIamConfigTypeDef = TypedDict(
    "AwsIamConfigTypeDef", {"signingRegion": str, "signingServiceName": str}, total=False
)

CachingConfigTypeDef = TypedDict(
    "CachingConfigTypeDef", {"ttl": int, "cachingKeys": List[str]}, total=False
)

_RequiredCognitoUserPoolConfigTypeDef = TypedDict(
    "_RequiredCognitoUserPoolConfigTypeDef", {"userPoolId": str, "awsRegion": str}
)
_OptionalCognitoUserPoolConfigTypeDef = TypedDict(
    "_OptionalCognitoUserPoolConfigTypeDef", {"appIdClientRegex": str}, total=False
)


class CognitoUserPoolConfigTypeDef(
    _RequiredCognitoUserPoolConfigTypeDef, _OptionalCognitoUserPoolConfigTypeDef
):
    pass


DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "dataSourceArn": str,
        "name": str,
        "description": str,
        "type": DataSourceType,
        "serviceRoleArn": str,
        "dynamodbConfig": "DynamodbDataSourceConfigTypeDef",
        "lambdaConfig": "LambdaDataSourceConfigTypeDef",
        "elasticsearchConfig": "ElasticsearchDataSourceConfigTypeDef",
        "httpConfig": "HttpDataSourceConfigTypeDef",
        "relationalDatabaseConfig": "RelationalDatabaseDataSourceConfigTypeDef",
    },
    total=False,
)

DeltaSyncConfigTypeDef = TypedDict(
    "DeltaSyncConfigTypeDef",
    {"baseTableTTL": int, "deltaSyncTableName": str, "deltaSyncTableTTL": int},
    total=False,
)

_RequiredDynamodbDataSourceConfigTypeDef = TypedDict(
    "_RequiredDynamodbDataSourceConfigTypeDef", {"tableName": str, "awsRegion": str}
)
_OptionalDynamodbDataSourceConfigTypeDef = TypedDict(
    "_OptionalDynamodbDataSourceConfigTypeDef",
    {"useCallerCredentials": bool, "deltaSyncConfig": "DeltaSyncConfigTypeDef", "versioned": bool},
    total=False,
)


class DynamodbDataSourceConfigTypeDef(
    _RequiredDynamodbDataSourceConfigTypeDef, _OptionalDynamodbDataSourceConfigTypeDef
):
    pass


ElasticsearchDataSourceConfigTypeDef = TypedDict(
    "ElasticsearchDataSourceConfigTypeDef", {"endpoint": str, "awsRegion": str}
)

FunctionConfigurationTypeDef = TypedDict(
    "FunctionConfigurationTypeDef",
    {
        "functionId": str,
        "functionArn": str,
        "name": str,
        "description": str,
        "dataSourceName": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "functionVersion": str,
        "syncConfig": "SyncConfigTypeDef",
    },
    total=False,
)

GraphqlApiTypeDef = TypedDict(
    "GraphqlApiTypeDef",
    {
        "name": str,
        "apiId": str,
        "authenticationType": AuthenticationType,
        "logConfig": "LogConfigTypeDef",
        "userPoolConfig": "UserPoolConfigTypeDef",
        "openIDConnectConfig": "OpenIDConnectConfigTypeDef",
        "arn": str,
        "uris": Dict[str, str],
        "tags": Dict[str, str],
        "additionalAuthenticationProviders": List["AdditionalAuthenticationProviderTypeDef"],
        "xrayEnabled": bool,
        "wafWebAclArn": str,
    },
    total=False,
)

HttpDataSourceConfigTypeDef = TypedDict(
    "HttpDataSourceConfigTypeDef",
    {"endpoint": str, "authorizationConfig": "AuthorizationConfigTypeDef"},
    total=False,
)

LambdaConflictHandlerConfigTypeDef = TypedDict(
    "LambdaConflictHandlerConfigTypeDef", {"lambdaConflictHandlerArn": str}, total=False
)

LambdaDataSourceConfigTypeDef = TypedDict(
    "LambdaDataSourceConfigTypeDef", {"lambdaFunctionArn": str}
)

_RequiredLogConfigTypeDef = TypedDict(
    "_RequiredLogConfigTypeDef", {"fieldLogLevel": FieldLogLevel, "cloudWatchLogsRoleArn": str}
)
_OptionalLogConfigTypeDef = TypedDict(
    "_OptionalLogConfigTypeDef", {"excludeVerboseContent": bool}, total=False
)


class LogConfigTypeDef(_RequiredLogConfigTypeDef, _OptionalLogConfigTypeDef):
    pass


_RequiredOpenIDConnectConfigTypeDef = TypedDict(
    "_RequiredOpenIDConnectConfigTypeDef", {"issuer": str}
)
_OptionalOpenIDConnectConfigTypeDef = TypedDict(
    "_OptionalOpenIDConnectConfigTypeDef",
    {"clientId": str, "iatTTL": int, "authTTL": int},
    total=False,
)


class OpenIDConnectConfigTypeDef(
    _RequiredOpenIDConnectConfigTypeDef, _OptionalOpenIDConnectConfigTypeDef
):
    pass


PipelineConfigTypeDef = TypedDict("PipelineConfigTypeDef", {"functions": List[str]}, total=False)

RdsHttpEndpointConfigTypeDef = TypedDict(
    "RdsHttpEndpointConfigTypeDef",
    {
        "awsRegion": str,
        "dbClusterIdentifier": str,
        "databaseName": str,
        "schema": str,
        "awsSecretStoreArn": str,
    },
    total=False,
)

RelationalDatabaseDataSourceConfigTypeDef = TypedDict(
    "RelationalDatabaseDataSourceConfigTypeDef",
    {
        "relationalDatabaseSourceType": RelationalDatabaseSourceType,
        "rdsHttpEndpointConfig": "RdsHttpEndpointConfigTypeDef",
    },
    total=False,
)

ResolverTypeDef = TypedDict(
    "ResolverTypeDef",
    {
        "typeName": str,
        "fieldName": str,
        "dataSourceName": str,
        "resolverArn": str,
        "requestMappingTemplate": str,
        "responseMappingTemplate": str,
        "kind": ResolverKind,
        "pipelineConfig": "PipelineConfigTypeDef",
        "syncConfig": "SyncConfigTypeDef",
        "cachingConfig": "CachingConfigTypeDef",
    },
    total=False,
)

SyncConfigTypeDef = TypedDict(
    "SyncConfigTypeDef",
    {
        "conflictHandler": ConflictHandlerType,
        "conflictDetection": ConflictDetectionType,
        "lambdaConflictHandlerConfig": "LambdaConflictHandlerConfigTypeDef",
    },
    total=False,
)

TypeTypeDef = TypedDict(
    "TypeTypeDef",
    {
        "name": str,
        "description": str,
        "arn": str,
        "definition": str,
        "format": TypeDefinitionFormat,
    },
    total=False,
)

_RequiredUserPoolConfigTypeDef = TypedDict(
    "_RequiredUserPoolConfigTypeDef",
    {"userPoolId": str, "awsRegion": str, "defaultAction": DefaultAction},
)
_OptionalUserPoolConfigTypeDef = TypedDict(
    "_OptionalUserPoolConfigTypeDef", {"appIdClientRegex": str}, total=False
)


class UserPoolConfigTypeDef(_RequiredUserPoolConfigTypeDef, _OptionalUserPoolConfigTypeDef):
    pass


CreateApiCacheResponseTypeDef = TypedDict(
    "CreateApiCacheResponseTypeDef", {"apiCache": "ApiCacheTypeDef"}, total=False
)

CreateApiKeyResponseTypeDef = TypedDict(
    "CreateApiKeyResponseTypeDef", {"apiKey": "ApiKeyTypeDef"}, total=False
)

CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef", {"dataSource": "DataSourceTypeDef"}, total=False
)

CreateFunctionResponseTypeDef = TypedDict(
    "CreateFunctionResponseTypeDef",
    {"functionConfiguration": "FunctionConfigurationTypeDef"},
    total=False,
)

CreateGraphqlApiResponseTypeDef = TypedDict(
    "CreateGraphqlApiResponseTypeDef", {"graphqlApi": "GraphqlApiTypeDef"}, total=False
)

CreateResolverResponseTypeDef = TypedDict(
    "CreateResolverResponseTypeDef", {"resolver": "ResolverTypeDef"}, total=False
)

CreateTypeResponseTypeDef = TypedDict(
    "CreateTypeResponseTypeDef", {"type": "TypeTypeDef"}, total=False
)

GetApiCacheResponseTypeDef = TypedDict(
    "GetApiCacheResponseTypeDef", {"apiCache": "ApiCacheTypeDef"}, total=False
)

GetDataSourceResponseTypeDef = TypedDict(
    "GetDataSourceResponseTypeDef", {"dataSource": "DataSourceTypeDef"}, total=False
)

GetFunctionResponseTypeDef = TypedDict(
    "GetFunctionResponseTypeDef",
    {"functionConfiguration": "FunctionConfigurationTypeDef"},
    total=False,
)

GetGraphqlApiResponseTypeDef = TypedDict(
    "GetGraphqlApiResponseTypeDef", {"graphqlApi": "GraphqlApiTypeDef"}, total=False
)

GetIntrospectionSchemaResponseTypeDef = TypedDict(
    "GetIntrospectionSchemaResponseTypeDef", {"schema": Union[bytes, IO[bytes]]}, total=False
)

GetResolverResponseTypeDef = TypedDict(
    "GetResolverResponseTypeDef", {"resolver": "ResolverTypeDef"}, total=False
)

GetSchemaCreationStatusResponseTypeDef = TypedDict(
    "GetSchemaCreationStatusResponseTypeDef", {"status": SchemaStatus, "details": str}, total=False
)

GetTypeResponseTypeDef = TypedDict("GetTypeResponseTypeDef", {"type": "TypeTypeDef"}, total=False)

ListApiKeysResponseTypeDef = TypedDict(
    "ListApiKeysResponseTypeDef", {"apiKeys": List["ApiKeyTypeDef"], "nextToken": str}, total=False
)

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {"dataSources": List["DataSourceTypeDef"], "nextToken": str},
    total=False,
)

ListFunctionsResponseTypeDef = TypedDict(
    "ListFunctionsResponseTypeDef",
    {"functions": List["FunctionConfigurationTypeDef"], "nextToken": str},
    total=False,
)

ListGraphqlApisResponseTypeDef = TypedDict(
    "ListGraphqlApisResponseTypeDef",
    {"graphqlApis": List["GraphqlApiTypeDef"], "nextToken": str},
    total=False,
)

ListResolversByFunctionResponseTypeDef = TypedDict(
    "ListResolversByFunctionResponseTypeDef",
    {"resolvers": List["ResolverTypeDef"], "nextToken": str},
    total=False,
)

ListResolversResponseTypeDef = TypedDict(
    "ListResolversResponseTypeDef",
    {"resolvers": List["ResolverTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ListTypesResponseTypeDef = TypedDict(
    "ListTypesResponseTypeDef", {"types": List["TypeTypeDef"], "nextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartSchemaCreationResponseTypeDef = TypedDict(
    "StartSchemaCreationResponseTypeDef", {"status": SchemaStatus}, total=False
)

UpdateApiCacheResponseTypeDef = TypedDict(
    "UpdateApiCacheResponseTypeDef", {"apiCache": "ApiCacheTypeDef"}, total=False
)

UpdateApiKeyResponseTypeDef = TypedDict(
    "UpdateApiKeyResponseTypeDef", {"apiKey": "ApiKeyTypeDef"}, total=False
)

UpdateDataSourceResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseTypeDef", {"dataSource": "DataSourceTypeDef"}, total=False
)

UpdateFunctionResponseTypeDef = TypedDict(
    "UpdateFunctionResponseTypeDef",
    {"functionConfiguration": "FunctionConfigurationTypeDef"},
    total=False,
)

UpdateGraphqlApiResponseTypeDef = TypedDict(
    "UpdateGraphqlApiResponseTypeDef", {"graphqlApi": "GraphqlApiTypeDef"}, total=False
)

UpdateResolverResponseTypeDef = TypedDict(
    "UpdateResolverResponseTypeDef", {"resolver": "ResolverTypeDef"}, total=False
)

UpdateTypeResponseTypeDef = TypedDict(
    "UpdateTypeResponseTypeDef", {"type": "TypeTypeDef"}, total=False
)
