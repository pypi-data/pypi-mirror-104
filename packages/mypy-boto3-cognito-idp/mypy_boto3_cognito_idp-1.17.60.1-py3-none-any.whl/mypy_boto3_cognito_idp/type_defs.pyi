"""
Main interface for cognito-idp service type definitions.

Usage::

    ```python
    from mypy_boto3_cognito_idp.type_defs import AccountRecoverySettingTypeTypeDef

    data: AccountRecoverySettingTypeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_cognito_idp.literals import (
    AccountTakeoverEventActionType,
    AdvancedSecurityModeType,
    AliasAttributeType,
    AttributeDataType,
    ChallengeName,
    ChallengeNameType,
    ChallengeResponse,
    CompromisedCredentialsEventActionType,
    CustomEmailSenderLambdaVersionType,
    CustomSMSSenderLambdaVersionType,
    DefaultEmailOptionType,
    DeliveryMediumType,
    DomainStatusType,
    EmailSendingAccountType,
    EventFilterType,
    EventResponseType,
    EventType,
    ExplicitAuthFlowsType,
    FeedbackValueType,
    IdentityProviderTypeType,
    OAuthFlowType,
    PreventUserExistenceErrorTypes,
    RecoveryOptionNameType,
    RiskDecisionType,
    RiskLevelType,
    StatusType,
    TimeUnitsType,
    UserImportJobStatusType,
    UsernameAttributeType,
    UserPoolMfaType,
    UserStatusType,
    VerifiedAttributeType,
    VerifySoftwareTokenResponseType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountRecoverySettingTypeTypeDef",
    "AccountTakeoverActionTypeTypeDef",
    "AccountTakeoverActionsTypeTypeDef",
    "AccountTakeoverRiskConfigurationTypeTypeDef",
    "AdminCreateUserConfigTypeTypeDef",
    "AnalyticsConfigurationTypeTypeDef",
    "AttributeTypeTypeDef",
    "AuthEventTypeTypeDef",
    "AuthenticationResultTypeTypeDef",
    "ChallengeResponseTypeTypeDef",
    "CodeDeliveryDetailsTypeTypeDef",
    "CompromisedCredentialsActionsTypeTypeDef",
    "CompromisedCredentialsRiskConfigurationTypeTypeDef",
    "CustomDomainConfigTypeTypeDef",
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    "DeviceConfigurationTypeTypeDef",
    "DeviceTypeTypeDef",
    "DomainDescriptionTypeTypeDef",
    "EmailConfigurationTypeTypeDef",
    "EventContextDataTypeTypeDef",
    "EventFeedbackTypeTypeDef",
    "EventRiskTypeTypeDef",
    "GroupTypeTypeDef",
    "HttpHeaderTypeDef",
    "IdentityProviderTypeTypeDef",
    "LambdaConfigTypeTypeDef",
    "MFAOptionTypeTypeDef",
    "MessageTemplateTypeTypeDef",
    "NewDeviceMetadataTypeTypeDef",
    "NotifyConfigurationTypeTypeDef",
    "NotifyEmailTypeTypeDef",
    "NumberAttributeConstraintsTypeTypeDef",
    "PasswordPolicyTypeTypeDef",
    "ProviderDescriptionTypeDef",
    "RecoveryOptionTypeTypeDef",
    "ResourceServerScopeTypeTypeDef",
    "ResourceServerTypeTypeDef",
    "RiskConfigurationTypeTypeDef",
    "RiskExceptionConfigurationTypeTypeDef",
    "SchemaAttributeTypeTypeDef",
    "SmsConfigurationTypeTypeDef",
    "SmsMfaConfigTypeTypeDef",
    "SoftwareTokenMfaConfigTypeTypeDef",
    "StringAttributeConstraintsTypeTypeDef",
    "TokenValidityUnitsTypeTypeDef",
    "UICustomizationTypeTypeDef",
    "UserImportJobTypeTypeDef",
    "UserPoolAddOnsTypeTypeDef",
    "UserPoolClientDescriptionTypeDef",
    "UserPoolClientTypeTypeDef",
    "UserPoolDescriptionTypeTypeDef",
    "UserPoolPolicyTypeTypeDef",
    "UserPoolTypeTypeDef",
    "UserTypeTypeDef",
    "UsernameConfigurationTypeTypeDef",
    "VerificationMessageTemplateTypeTypeDef",
    "AdminCreateUserResponseTypeDef",
    "AdminGetDeviceResponseTypeDef",
    "AdminGetUserResponseTypeDef",
    "AdminInitiateAuthResponseTypeDef",
    "AdminListDevicesResponseTypeDef",
    "AdminListGroupsForUserResponseTypeDef",
    "AdminListUserAuthEventsResponseTypeDef",
    "AdminRespondToAuthChallengeResponseTypeDef",
    "AnalyticsMetadataTypeTypeDef",
    "AssociateSoftwareTokenResponseTypeDef",
    "ConfirmDeviceResponseTypeDef",
    "ContextDataTypeTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "CreateResourceServerResponseTypeDef",
    "CreateUserImportJobResponseTypeDef",
    "CreateUserPoolClientResponseTypeDef",
    "CreateUserPoolDomainResponseTypeDef",
    "CreateUserPoolResponseTypeDef",
    "DescribeIdentityProviderResponseTypeDef",
    "DescribeResourceServerResponseTypeDef",
    "DescribeRiskConfigurationResponseTypeDef",
    "DescribeUserImportJobResponseTypeDef",
    "DescribeUserPoolClientResponseTypeDef",
    "DescribeUserPoolDomainResponseTypeDef",
    "DescribeUserPoolResponseTypeDef",
    "DeviceSecretVerifierConfigTypeTypeDef",
    "ForgotPasswordResponseTypeDef",
    "GetCSVHeaderResponseTypeDef",
    "GetDeviceResponseTypeDef",
    "GetGroupResponseTypeDef",
    "GetIdentityProviderByIdentifierResponseTypeDef",
    "GetSigningCertificateResponseTypeDef",
    "GetUICustomizationResponseTypeDef",
    "GetUserAttributeVerificationCodeResponseTypeDef",
    "GetUserPoolMfaConfigResponseTypeDef",
    "GetUserResponseTypeDef",
    "InitiateAuthResponseTypeDef",
    "ListDevicesResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListResourceServersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUserImportJobsResponseTypeDef",
    "ListUserPoolClientsResponseTypeDef",
    "ListUserPoolsResponseTypeDef",
    "ListUsersInGroupResponseTypeDef",
    "ListUsersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ProviderUserIdentifierTypeTypeDef",
    "ResendConfirmationCodeResponseTypeDef",
    "RespondToAuthChallengeResponseTypeDef",
    "SMSMfaSettingsTypeTypeDef",
    "SetRiskConfigurationResponseTypeDef",
    "SetUICustomizationResponseTypeDef",
    "SetUserPoolMfaConfigResponseTypeDef",
    "SignUpResponseTypeDef",
    "SoftwareTokenMfaSettingsTypeTypeDef",
    "StartUserImportJobResponseTypeDef",
    "StopUserImportJobResponseTypeDef",
    "UpdateGroupResponseTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "UpdateResourceServerResponseTypeDef",
    "UpdateUserAttributesResponseTypeDef",
    "UpdateUserPoolClientResponseTypeDef",
    "UpdateUserPoolDomainResponseTypeDef",
    "UserContextDataTypeTypeDef",
    "VerifySoftwareTokenResponseTypeDef",
)

AccountRecoverySettingTypeTypeDef = TypedDict(
    "AccountRecoverySettingTypeTypeDef",
    {"RecoveryMechanisms": List["RecoveryOptionTypeTypeDef"]},
    total=False,
)

AccountTakeoverActionTypeTypeDef = TypedDict(
    "AccountTakeoverActionTypeTypeDef",
    {"Notify": bool, "EventAction": AccountTakeoverEventActionType},
)

AccountTakeoverActionsTypeTypeDef = TypedDict(
    "AccountTakeoverActionsTypeTypeDef",
    {
        "LowAction": "AccountTakeoverActionTypeTypeDef",
        "MediumAction": "AccountTakeoverActionTypeTypeDef",
        "HighAction": "AccountTakeoverActionTypeTypeDef",
    },
    total=False,
)

_RequiredAccountTakeoverRiskConfigurationTypeTypeDef = TypedDict(
    "_RequiredAccountTakeoverRiskConfigurationTypeTypeDef",
    {"Actions": "AccountTakeoverActionsTypeTypeDef"},
)
_OptionalAccountTakeoverRiskConfigurationTypeTypeDef = TypedDict(
    "_OptionalAccountTakeoverRiskConfigurationTypeTypeDef",
    {"NotifyConfiguration": "NotifyConfigurationTypeTypeDef"},
    total=False,
)

class AccountTakeoverRiskConfigurationTypeTypeDef(
    _RequiredAccountTakeoverRiskConfigurationTypeTypeDef,
    _OptionalAccountTakeoverRiskConfigurationTypeTypeDef,
):
    pass

AdminCreateUserConfigTypeTypeDef = TypedDict(
    "AdminCreateUserConfigTypeTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": "MessageTemplateTypeTypeDef",
    },
    total=False,
)

AnalyticsConfigurationTypeTypeDef = TypedDict(
    "AnalyticsConfigurationTypeTypeDef",
    {
        "ApplicationId": str,
        "ApplicationArn": str,
        "RoleArn": str,
        "ExternalId": str,
        "UserDataShared": bool,
    },
    total=False,
)

_RequiredAttributeTypeTypeDef = TypedDict("_RequiredAttributeTypeTypeDef", {"Name": str})
_OptionalAttributeTypeTypeDef = TypedDict(
    "_OptionalAttributeTypeTypeDef", {"Value": str}, total=False
)

class AttributeTypeTypeDef(_RequiredAttributeTypeTypeDef, _OptionalAttributeTypeTypeDef):
    pass

AuthEventTypeTypeDef = TypedDict(
    "AuthEventTypeTypeDef",
    {
        "EventId": str,
        "EventType": EventType,
        "CreationDate": datetime,
        "EventResponse": EventResponseType,
        "EventRisk": "EventRiskTypeTypeDef",
        "ChallengeResponses": List["ChallengeResponseTypeTypeDef"],
        "EventContextData": "EventContextDataTypeTypeDef",
        "EventFeedback": "EventFeedbackTypeTypeDef",
    },
    total=False,
)

AuthenticationResultTypeTypeDef = TypedDict(
    "AuthenticationResultTypeTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": "NewDeviceMetadataTypeTypeDef",
    },
    total=False,
)

ChallengeResponseTypeTypeDef = TypedDict(
    "ChallengeResponseTypeTypeDef",
    {"ChallengeName": ChallengeName, "ChallengeResponse": ChallengeResponse},
    total=False,
)

CodeDeliveryDetailsTypeTypeDef = TypedDict(
    "CodeDeliveryDetailsTypeTypeDef",
    {"Destination": str, "DeliveryMedium": DeliveryMediumType, "AttributeName": str},
    total=False,
)

CompromisedCredentialsActionsTypeTypeDef = TypedDict(
    "CompromisedCredentialsActionsTypeTypeDef",
    {"EventAction": CompromisedCredentialsEventActionType},
)

_RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef = TypedDict(
    "_RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef",
    {"Actions": "CompromisedCredentialsActionsTypeTypeDef"},
)
_OptionalCompromisedCredentialsRiskConfigurationTypeTypeDef = TypedDict(
    "_OptionalCompromisedCredentialsRiskConfigurationTypeTypeDef",
    {"EventFilter": List[EventFilterType]},
    total=False,
)

class CompromisedCredentialsRiskConfigurationTypeTypeDef(
    _RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef,
    _OptionalCompromisedCredentialsRiskConfigurationTypeTypeDef,
):
    pass

CustomDomainConfigTypeTypeDef = TypedDict("CustomDomainConfigTypeTypeDef", {"CertificateArn": str})

CustomEmailLambdaVersionConfigTypeTypeDef = TypedDict(
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    {"LambdaVersion": CustomEmailSenderLambdaVersionType, "LambdaArn": str},
)

CustomSMSLambdaVersionConfigTypeTypeDef = TypedDict(
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    {"LambdaVersion": CustomSMSSenderLambdaVersionType, "LambdaArn": str},
)

DeviceConfigurationTypeTypeDef = TypedDict(
    "DeviceConfigurationTypeTypeDef",
    {"ChallengeRequiredOnNewDevice": bool, "DeviceOnlyRememberedOnUserPrompt": bool},
    total=False,
)

DeviceTypeTypeDef = TypedDict(
    "DeviceTypeTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List["AttributeTypeTypeDef"],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)

DomainDescriptionTypeTypeDef = TypedDict(
    "DomainDescriptionTypeTypeDef",
    {
        "UserPoolId": str,
        "AWSAccountId": str,
        "Domain": str,
        "S3Bucket": str,
        "CloudFrontDistribution": str,
        "Version": str,
        "Status": DomainStatusType,
        "CustomDomainConfig": "CustomDomainConfigTypeTypeDef",
    },
    total=False,
)

EmailConfigurationTypeTypeDef = TypedDict(
    "EmailConfigurationTypeTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": EmailSendingAccountType,
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)

EventContextDataTypeTypeDef = TypedDict(
    "EventContextDataTypeTypeDef",
    {"IpAddress": str, "DeviceName": str, "Timezone": str, "City": str, "Country": str},
    total=False,
)

_RequiredEventFeedbackTypeTypeDef = TypedDict(
    "_RequiredEventFeedbackTypeTypeDef", {"FeedbackValue": FeedbackValueType, "Provider": str}
)
_OptionalEventFeedbackTypeTypeDef = TypedDict(
    "_OptionalEventFeedbackTypeTypeDef", {"FeedbackDate": datetime}, total=False
)

class EventFeedbackTypeTypeDef(
    _RequiredEventFeedbackTypeTypeDef, _OptionalEventFeedbackTypeTypeDef
):
    pass

EventRiskTypeTypeDef = TypedDict(
    "EventRiskTypeTypeDef",
    {
        "RiskDecision": RiskDecisionType,
        "RiskLevel": RiskLevelType,
        "CompromisedCredentialsDetected": bool,
    },
    total=False,
)

GroupTypeTypeDef = TypedDict(
    "GroupTypeTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

HttpHeaderTypeDef = TypedDict(
    "HttpHeaderTypeDef", {"headerName": str, "headerValue": str}, total=False
)

IdentityProviderTypeTypeDef = TypedDict(
    "IdentityProviderTypeTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": IdentityProviderTypeType,
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

LambdaConfigTypeTypeDef = TypedDict(
    "LambdaConfigTypeTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
        "CustomSMSSender": "CustomSMSLambdaVersionConfigTypeTypeDef",
        "CustomEmailSender": "CustomEmailLambdaVersionConfigTypeTypeDef",
        "KMSKeyID": str,
    },
    total=False,
)

MFAOptionTypeTypeDef = TypedDict(
    "MFAOptionTypeTypeDef",
    {"DeliveryMedium": DeliveryMediumType, "AttributeName": str},
    total=False,
)

MessageTemplateTypeTypeDef = TypedDict(
    "MessageTemplateTypeTypeDef",
    {"SMSMessage": str, "EmailMessage": str, "EmailSubject": str},
    total=False,
)

NewDeviceMetadataTypeTypeDef = TypedDict(
    "NewDeviceMetadataTypeTypeDef", {"DeviceKey": str, "DeviceGroupKey": str}, total=False
)

_RequiredNotifyConfigurationTypeTypeDef = TypedDict(
    "_RequiredNotifyConfigurationTypeTypeDef", {"SourceArn": str}
)
_OptionalNotifyConfigurationTypeTypeDef = TypedDict(
    "_OptionalNotifyConfigurationTypeTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "BlockEmail": "NotifyEmailTypeTypeDef",
        "NoActionEmail": "NotifyEmailTypeTypeDef",
        "MfaEmail": "NotifyEmailTypeTypeDef",
    },
    total=False,
)

class NotifyConfigurationTypeTypeDef(
    _RequiredNotifyConfigurationTypeTypeDef, _OptionalNotifyConfigurationTypeTypeDef
):
    pass

_RequiredNotifyEmailTypeTypeDef = TypedDict("_RequiredNotifyEmailTypeTypeDef", {"Subject": str})
_OptionalNotifyEmailTypeTypeDef = TypedDict(
    "_OptionalNotifyEmailTypeTypeDef", {"HtmlBody": str, "TextBody": str}, total=False
)

class NotifyEmailTypeTypeDef(_RequiredNotifyEmailTypeTypeDef, _OptionalNotifyEmailTypeTypeDef):
    pass

NumberAttributeConstraintsTypeTypeDef = TypedDict(
    "NumberAttributeConstraintsTypeTypeDef", {"MinValue": str, "MaxValue": str}, total=False
)

PasswordPolicyTypeTypeDef = TypedDict(
    "PasswordPolicyTypeTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)

ProviderDescriptionTypeDef = TypedDict(
    "ProviderDescriptionTypeDef",
    {
        "ProviderName": str,
        "ProviderType": IdentityProviderTypeType,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

RecoveryOptionTypeTypeDef = TypedDict(
    "RecoveryOptionTypeTypeDef", {"Priority": int, "Name": RecoveryOptionNameType}
)

ResourceServerScopeTypeTypeDef = TypedDict(
    "ResourceServerScopeTypeTypeDef", {"ScopeName": str, "ScopeDescription": str}
)

ResourceServerTypeTypeDef = TypedDict(
    "ResourceServerTypeTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List["ResourceServerScopeTypeTypeDef"],
    },
    total=False,
)

RiskConfigurationTypeTypeDef = TypedDict(
    "RiskConfigurationTypeTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "CompromisedCredentialsRiskConfiguration": "CompromisedCredentialsRiskConfigurationTypeTypeDef",
        "AccountTakeoverRiskConfiguration": "AccountTakeoverRiskConfigurationTypeTypeDef",
        "RiskExceptionConfiguration": "RiskExceptionConfigurationTypeTypeDef",
        "LastModifiedDate": datetime,
    },
    total=False,
)

RiskExceptionConfigurationTypeTypeDef = TypedDict(
    "RiskExceptionConfigurationTypeTypeDef",
    {"BlockedIPRangeList": List[str], "SkippedIPRangeList": List[str]},
    total=False,
)

SchemaAttributeTypeTypeDef = TypedDict(
    "SchemaAttributeTypeTypeDef",
    {
        "Name": str,
        "AttributeDataType": AttributeDataType,
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": "NumberAttributeConstraintsTypeTypeDef",
        "StringAttributeConstraints": "StringAttributeConstraintsTypeTypeDef",
    },
    total=False,
)

_RequiredSmsConfigurationTypeTypeDef = TypedDict(
    "_RequiredSmsConfigurationTypeTypeDef", {"SnsCallerArn": str}
)
_OptionalSmsConfigurationTypeTypeDef = TypedDict(
    "_OptionalSmsConfigurationTypeTypeDef", {"ExternalId": str}, total=False
)

class SmsConfigurationTypeTypeDef(
    _RequiredSmsConfigurationTypeTypeDef, _OptionalSmsConfigurationTypeTypeDef
):
    pass

SmsMfaConfigTypeTypeDef = TypedDict(
    "SmsMfaConfigTypeTypeDef",
    {"SmsAuthenticationMessage": str, "SmsConfiguration": "SmsConfigurationTypeTypeDef"},
    total=False,
)

SoftwareTokenMfaConfigTypeTypeDef = TypedDict(
    "SoftwareTokenMfaConfigTypeTypeDef", {"Enabled": bool}, total=False
)

StringAttributeConstraintsTypeTypeDef = TypedDict(
    "StringAttributeConstraintsTypeTypeDef", {"MinLength": str, "MaxLength": str}, total=False
)

TokenValidityUnitsTypeTypeDef = TypedDict(
    "TokenValidityUnitsTypeTypeDef",
    {"AccessToken": TimeUnitsType, "IdToken": TimeUnitsType, "RefreshToken": TimeUnitsType},
    total=False,
)

UICustomizationTypeTypeDef = TypedDict(
    "UICustomizationTypeTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ImageUrl": str,
        "CSS": str,
        "CSSVersion": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

UserImportJobTypeTypeDef = TypedDict(
    "UserImportJobTypeTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": UserImportJobStatusType,
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)

UserPoolAddOnsTypeTypeDef = TypedDict(
    "UserPoolAddOnsTypeTypeDef", {"AdvancedSecurityMode": AdvancedSecurityModeType}
)

UserPoolClientDescriptionTypeDef = TypedDict(
    "UserPoolClientDescriptionTypeDef",
    {"ClientId": str, "UserPoolId": str, "ClientName": str},
    total=False,
)

UserPoolClientTypeTypeDef = TypedDict(
    "UserPoolClientTypeTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "ClientId": str,
        "ClientSecret": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "RefreshTokenValidity": int,
        "AccessTokenValidity": int,
        "IdTokenValidity": int,
        "TokenValidityUnits": "TokenValidityUnitsTypeTypeDef",
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[ExplicitAuthFlowsType],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[OAuthFlowType],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeTypeDef",
        "PreventUserExistenceErrors": PreventUserExistenceErrorTypes,
    },
    total=False,
)

UserPoolDescriptionTypeTypeDef = TypedDict(
    "UserPoolDescriptionTypeTypeDef",
    {
        "Id": str,
        "Name": str,
        "LambdaConfig": "LambdaConfigTypeTypeDef",
        "Status": StatusType,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

UserPoolPolicyTypeTypeDef = TypedDict(
    "UserPoolPolicyTypeTypeDef", {"PasswordPolicy": "PasswordPolicyTypeTypeDef"}, total=False
)

UserPoolTypeTypeDef = TypedDict(
    "UserPoolTypeTypeDef",
    {
        "Id": str,
        "Name": str,
        "Policies": "UserPoolPolicyTypeTypeDef",
        "LambdaConfig": "LambdaConfigTypeTypeDef",
        "Status": StatusType,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "SchemaAttributes": List["SchemaAttributeTypeTypeDef"],
        "AutoVerifiedAttributes": List[VerifiedAttributeType],
        "AliasAttributes": List[AliasAttributeType],
        "UsernameAttributes": List[UsernameAttributeType],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": "VerificationMessageTemplateTypeTypeDef",
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": UserPoolMfaType,
        "DeviceConfiguration": "DeviceConfigurationTypeTypeDef",
        "EstimatedNumberOfUsers": int,
        "EmailConfiguration": "EmailConfigurationTypeTypeDef",
        "SmsConfiguration": "SmsConfigurationTypeTypeDef",
        "UserPoolTags": Dict[str, str],
        "SmsConfigurationFailure": str,
        "EmailConfigurationFailure": str,
        "Domain": str,
        "CustomDomain": str,
        "AdminCreateUserConfig": "AdminCreateUserConfigTypeTypeDef",
        "UserPoolAddOns": "UserPoolAddOnsTypeTypeDef",
        "UsernameConfiguration": "UsernameConfigurationTypeTypeDef",
        "Arn": str,
        "AccountRecoverySetting": "AccountRecoverySettingTypeTypeDef",
    },
    total=False,
)

UserTypeTypeDef = TypedDict(
    "UserTypeTypeDef",
    {
        "Username": str,
        "Attributes": List["AttributeTypeTypeDef"],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": UserStatusType,
        "MFAOptions": List["MFAOptionTypeTypeDef"],
    },
    total=False,
)

UsernameConfigurationTypeTypeDef = TypedDict(
    "UsernameConfigurationTypeTypeDef", {"CaseSensitive": bool}
)

VerificationMessageTemplateTypeTypeDef = TypedDict(
    "VerificationMessageTemplateTypeTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": DefaultEmailOptionType,
    },
    total=False,
)

AdminCreateUserResponseTypeDef = TypedDict(
    "AdminCreateUserResponseTypeDef", {"User": "UserTypeTypeDef"}, total=False
)

AdminGetDeviceResponseTypeDef = TypedDict(
    "AdminGetDeviceResponseTypeDef", {"Device": "DeviceTypeTypeDef"}
)

_RequiredAdminGetUserResponseTypeDef = TypedDict(
    "_RequiredAdminGetUserResponseTypeDef", {"Username": str}
)
_OptionalAdminGetUserResponseTypeDef = TypedDict(
    "_OptionalAdminGetUserResponseTypeDef",
    {
        "UserAttributes": List["AttributeTypeTypeDef"],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": UserStatusType,
        "MFAOptions": List["MFAOptionTypeTypeDef"],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
    },
    total=False,
)

class AdminGetUserResponseTypeDef(
    _RequiredAdminGetUserResponseTypeDef, _OptionalAdminGetUserResponseTypeDef
):
    pass

AdminInitiateAuthResponseTypeDef = TypedDict(
    "AdminInitiateAuthResponseTypeDef",
    {
        "ChallengeName": ChallengeNameType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
    },
    total=False,
)

AdminListDevicesResponseTypeDef = TypedDict(
    "AdminListDevicesResponseTypeDef",
    {"Devices": List["DeviceTypeTypeDef"], "PaginationToken": str},
    total=False,
)

AdminListGroupsForUserResponseTypeDef = TypedDict(
    "AdminListGroupsForUserResponseTypeDef",
    {"Groups": List["GroupTypeTypeDef"], "NextToken": str},
    total=False,
)

AdminListUserAuthEventsResponseTypeDef = TypedDict(
    "AdminListUserAuthEventsResponseTypeDef",
    {"AuthEvents": List["AuthEventTypeTypeDef"], "NextToken": str},
    total=False,
)

AdminRespondToAuthChallengeResponseTypeDef = TypedDict(
    "AdminRespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": ChallengeNameType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
    },
    total=False,
)

AnalyticsMetadataTypeTypeDef = TypedDict(
    "AnalyticsMetadataTypeTypeDef", {"AnalyticsEndpointId": str}, total=False
)

AssociateSoftwareTokenResponseTypeDef = TypedDict(
    "AssociateSoftwareTokenResponseTypeDef", {"SecretCode": str, "Session": str}, total=False
)

ConfirmDeviceResponseTypeDef = TypedDict(
    "ConfirmDeviceResponseTypeDef", {"UserConfirmationNecessary": bool}, total=False
)

_RequiredContextDataTypeTypeDef = TypedDict(
    "_RequiredContextDataTypeTypeDef",
    {
        "IpAddress": str,
        "ServerName": str,
        "ServerPath": str,
        "HttpHeaders": List["HttpHeaderTypeDef"],
    },
)
_OptionalContextDataTypeTypeDef = TypedDict(
    "_OptionalContextDataTypeTypeDef", {"EncodedData": str}, total=False
)

class ContextDataTypeTypeDef(_RequiredContextDataTypeTypeDef, _OptionalContextDataTypeTypeDef):
    pass

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef", {"Group": "GroupTypeTypeDef"}, total=False
)

CreateIdentityProviderResponseTypeDef = TypedDict(
    "CreateIdentityProviderResponseTypeDef", {"IdentityProvider": "IdentityProviderTypeTypeDef"}
)

CreateResourceServerResponseTypeDef = TypedDict(
    "CreateResourceServerResponseTypeDef", {"ResourceServer": "ResourceServerTypeTypeDef"}
)

CreateUserImportJobResponseTypeDef = TypedDict(
    "CreateUserImportJobResponseTypeDef", {"UserImportJob": "UserImportJobTypeTypeDef"}, total=False
)

CreateUserPoolClientResponseTypeDef = TypedDict(
    "CreateUserPoolClientResponseTypeDef",
    {"UserPoolClient": "UserPoolClientTypeTypeDef"},
    total=False,
)

CreateUserPoolDomainResponseTypeDef = TypedDict(
    "CreateUserPoolDomainResponseTypeDef", {"CloudFrontDomain": str}, total=False
)

CreateUserPoolResponseTypeDef = TypedDict(
    "CreateUserPoolResponseTypeDef", {"UserPool": "UserPoolTypeTypeDef"}, total=False
)

DescribeIdentityProviderResponseTypeDef = TypedDict(
    "DescribeIdentityProviderResponseTypeDef", {"IdentityProvider": "IdentityProviderTypeTypeDef"}
)

DescribeResourceServerResponseTypeDef = TypedDict(
    "DescribeResourceServerResponseTypeDef", {"ResourceServer": "ResourceServerTypeTypeDef"}
)

DescribeRiskConfigurationResponseTypeDef = TypedDict(
    "DescribeRiskConfigurationResponseTypeDef",
    {"RiskConfiguration": "RiskConfigurationTypeTypeDef"},
)

DescribeUserImportJobResponseTypeDef = TypedDict(
    "DescribeUserImportJobResponseTypeDef",
    {"UserImportJob": "UserImportJobTypeTypeDef"},
    total=False,
)

DescribeUserPoolClientResponseTypeDef = TypedDict(
    "DescribeUserPoolClientResponseTypeDef",
    {"UserPoolClient": "UserPoolClientTypeTypeDef"},
    total=False,
)

DescribeUserPoolDomainResponseTypeDef = TypedDict(
    "DescribeUserPoolDomainResponseTypeDef",
    {"DomainDescription": "DomainDescriptionTypeTypeDef"},
    total=False,
)

DescribeUserPoolResponseTypeDef = TypedDict(
    "DescribeUserPoolResponseTypeDef", {"UserPool": "UserPoolTypeTypeDef"}, total=False
)

DeviceSecretVerifierConfigTypeTypeDef = TypedDict(
    "DeviceSecretVerifierConfigTypeTypeDef", {"PasswordVerifier": str, "Salt": str}, total=False
)

ForgotPasswordResponseTypeDef = TypedDict(
    "ForgotPasswordResponseTypeDef",
    {"CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef"},
    total=False,
)

GetCSVHeaderResponseTypeDef = TypedDict(
    "GetCSVHeaderResponseTypeDef", {"UserPoolId": str, "CSVHeader": List[str]}, total=False
)

GetDeviceResponseTypeDef = TypedDict("GetDeviceResponseTypeDef", {"Device": "DeviceTypeTypeDef"})

GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef", {"Group": "GroupTypeTypeDef"}, total=False
)

GetIdentityProviderByIdentifierResponseTypeDef = TypedDict(
    "GetIdentityProviderByIdentifierResponseTypeDef",
    {"IdentityProvider": "IdentityProviderTypeTypeDef"},
)

GetSigningCertificateResponseTypeDef = TypedDict(
    "GetSigningCertificateResponseTypeDef", {"Certificate": str}, total=False
)

GetUICustomizationResponseTypeDef = TypedDict(
    "GetUICustomizationResponseTypeDef", {"UICustomization": "UICustomizationTypeTypeDef"}
)

GetUserAttributeVerificationCodeResponseTypeDef = TypedDict(
    "GetUserAttributeVerificationCodeResponseTypeDef",
    {"CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef"},
    total=False,
)

GetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "GetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": "SmsMfaConfigTypeTypeDef",
        "SoftwareTokenMfaConfiguration": "SoftwareTokenMfaConfigTypeTypeDef",
        "MfaConfiguration": UserPoolMfaType,
    },
    total=False,
)

_RequiredGetUserResponseTypeDef = TypedDict(
    "_RequiredGetUserResponseTypeDef",
    {"Username": str, "UserAttributes": List["AttributeTypeTypeDef"]},
)
_OptionalGetUserResponseTypeDef = TypedDict(
    "_OptionalGetUserResponseTypeDef",
    {
        "MFAOptions": List["MFAOptionTypeTypeDef"],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
    },
    total=False,
)

class GetUserResponseTypeDef(_RequiredGetUserResponseTypeDef, _OptionalGetUserResponseTypeDef):
    pass

InitiateAuthResponseTypeDef = TypedDict(
    "InitiateAuthResponseTypeDef",
    {
        "ChallengeName": ChallengeNameType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
    },
    total=False,
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {"Devices": List["DeviceTypeTypeDef"], "PaginationToken": str},
    total=False,
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef", {"Groups": List["GroupTypeTypeDef"], "NextToken": str}, total=False
)

_RequiredListIdentityProvidersResponseTypeDef = TypedDict(
    "_RequiredListIdentityProvidersResponseTypeDef",
    {"Providers": List["ProviderDescriptionTypeDef"]},
)
_OptionalListIdentityProvidersResponseTypeDef = TypedDict(
    "_OptionalListIdentityProvidersResponseTypeDef", {"NextToken": str}, total=False
)

class ListIdentityProvidersResponseTypeDef(
    _RequiredListIdentityProvidersResponseTypeDef, _OptionalListIdentityProvidersResponseTypeDef
):
    pass

_RequiredListResourceServersResponseTypeDef = TypedDict(
    "_RequiredListResourceServersResponseTypeDef",
    {"ResourceServers": List["ResourceServerTypeTypeDef"]},
)
_OptionalListResourceServersResponseTypeDef = TypedDict(
    "_OptionalListResourceServersResponseTypeDef", {"NextToken": str}, total=False
)

class ListResourceServersResponseTypeDef(
    _RequiredListResourceServersResponseTypeDef, _OptionalListResourceServersResponseTypeDef
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ListUserImportJobsResponseTypeDef = TypedDict(
    "ListUserImportJobsResponseTypeDef",
    {"UserImportJobs": List["UserImportJobTypeTypeDef"], "PaginationToken": str},
    total=False,
)

ListUserPoolClientsResponseTypeDef = TypedDict(
    "ListUserPoolClientsResponseTypeDef",
    {"UserPoolClients": List["UserPoolClientDescriptionTypeDef"], "NextToken": str},
    total=False,
)

ListUserPoolsResponseTypeDef = TypedDict(
    "ListUserPoolsResponseTypeDef",
    {"UserPools": List["UserPoolDescriptionTypeTypeDef"], "NextToken": str},
    total=False,
)

ListUsersInGroupResponseTypeDef = TypedDict(
    "ListUsersInGroupResponseTypeDef",
    {"Users": List["UserTypeTypeDef"], "NextToken": str},
    total=False,
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {"Users": List["UserTypeTypeDef"], "PaginationToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ProviderUserIdentifierTypeTypeDef = TypedDict(
    "ProviderUserIdentifierTypeTypeDef",
    {"ProviderName": str, "ProviderAttributeName": str, "ProviderAttributeValue": str},
    total=False,
)

ResendConfirmationCodeResponseTypeDef = TypedDict(
    "ResendConfirmationCodeResponseTypeDef",
    {"CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef"},
    total=False,
)

RespondToAuthChallengeResponseTypeDef = TypedDict(
    "RespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": ChallengeNameType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
    },
    total=False,
)

SMSMfaSettingsTypeTypeDef = TypedDict(
    "SMSMfaSettingsTypeTypeDef", {"Enabled": bool, "PreferredMfa": bool}, total=False
)

SetRiskConfigurationResponseTypeDef = TypedDict(
    "SetRiskConfigurationResponseTypeDef", {"RiskConfiguration": "RiskConfigurationTypeTypeDef"}
)

SetUICustomizationResponseTypeDef = TypedDict(
    "SetUICustomizationResponseTypeDef", {"UICustomization": "UICustomizationTypeTypeDef"}
)

SetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "SetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": "SmsMfaConfigTypeTypeDef",
        "SoftwareTokenMfaConfiguration": "SoftwareTokenMfaConfigTypeTypeDef",
        "MfaConfiguration": UserPoolMfaType,
    },
    total=False,
)

_RequiredSignUpResponseTypeDef = TypedDict(
    "_RequiredSignUpResponseTypeDef", {"UserConfirmed": bool, "UserSub": str}
)
_OptionalSignUpResponseTypeDef = TypedDict(
    "_OptionalSignUpResponseTypeDef",
    {"CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef"},
    total=False,
)

class SignUpResponseTypeDef(_RequiredSignUpResponseTypeDef, _OptionalSignUpResponseTypeDef):
    pass

SoftwareTokenMfaSettingsTypeTypeDef = TypedDict(
    "SoftwareTokenMfaSettingsTypeTypeDef", {"Enabled": bool, "PreferredMfa": bool}, total=False
)

StartUserImportJobResponseTypeDef = TypedDict(
    "StartUserImportJobResponseTypeDef", {"UserImportJob": "UserImportJobTypeTypeDef"}, total=False
)

StopUserImportJobResponseTypeDef = TypedDict(
    "StopUserImportJobResponseTypeDef", {"UserImportJob": "UserImportJobTypeTypeDef"}, total=False
)

UpdateGroupResponseTypeDef = TypedDict(
    "UpdateGroupResponseTypeDef", {"Group": "GroupTypeTypeDef"}, total=False
)

UpdateIdentityProviderResponseTypeDef = TypedDict(
    "UpdateIdentityProviderResponseTypeDef", {"IdentityProvider": "IdentityProviderTypeTypeDef"}
)

UpdateResourceServerResponseTypeDef = TypedDict(
    "UpdateResourceServerResponseTypeDef", {"ResourceServer": "ResourceServerTypeTypeDef"}
)

UpdateUserAttributesResponseTypeDef = TypedDict(
    "UpdateUserAttributesResponseTypeDef",
    {"CodeDeliveryDetailsList": List["CodeDeliveryDetailsTypeTypeDef"]},
    total=False,
)

UpdateUserPoolClientResponseTypeDef = TypedDict(
    "UpdateUserPoolClientResponseTypeDef",
    {"UserPoolClient": "UserPoolClientTypeTypeDef"},
    total=False,
)

UpdateUserPoolDomainResponseTypeDef = TypedDict(
    "UpdateUserPoolDomainResponseTypeDef", {"CloudFrontDomain": str}, total=False
)

UserContextDataTypeTypeDef = TypedDict(
    "UserContextDataTypeTypeDef", {"EncodedData": str}, total=False
)

VerifySoftwareTokenResponseTypeDef = TypedDict(
    "VerifySoftwareTokenResponseTypeDef",
    {"Status": VerifySoftwareTokenResponseType, "Session": str},
    total=False,
)
