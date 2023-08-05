"""
Main interface for macie2 service client

Usage::

    ```python
    import boto3
    from mypy_boto3_macie2 import Macie2Client

    client: Macie2Client = boto3.client("macie2")
    ```
"""
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_macie2.literals import (
    DescribeBucketsPaginatorName,
    FindingPublishingFrequency,
    FindingsFilterAction,
    FindingType,
    GetUsageStatisticsPaginatorName,
    GroupBy,
    JobStatus,
    JobType,
    ListClassificationJobsPaginatorName,
    ListCustomDataIdentifiersPaginatorName,
    ListFindingsFiltersPaginatorName,
    ListFindingsPaginatorName,
    ListInvitationsPaginatorName,
    ListMembersPaginatorName,
    ListOrganizationAdminAccountsPaginatorName,
    MacieStatus,
    TimeRange,
)
from mypy_boto3_macie2.paginator import (
    DescribeBucketsPaginator,
    GetUsageStatisticsPaginator,
    ListClassificationJobsPaginator,
    ListCustomDataIdentifiersPaginator,
    ListFindingsFiltersPaginator,
    ListFindingsPaginator,
    ListInvitationsPaginator,
    ListMembersPaginator,
    ListOrganizationAdminAccountsPaginator,
)
from mypy_boto3_macie2.type_defs import (
    AccountDetailTypeDef,
    BatchGetCustomDataIdentifiersResponseTypeDef,
    BucketCriteriaAdditionalPropertiesTypeDef,
    BucketSortCriteriaTypeDef,
    ClassificationExportConfigurationTypeDef,
    CreateClassificationJobResponseTypeDef,
    CreateCustomDataIdentifierResponseTypeDef,
    CreateFindingsFilterResponseTypeDef,
    CreateInvitationsResponseTypeDef,
    CreateMemberResponseTypeDef,
    DeclineInvitationsResponseTypeDef,
    DeleteInvitationsResponseTypeDef,
    DescribeBucketsResponseTypeDef,
    DescribeClassificationJobResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    FindingCriteriaTypeDef,
    FindingStatisticsSortCriteriaTypeDef,
    GetAdministratorAccountResponseTypeDef,
    GetBucketStatisticsResponseTypeDef,
    GetClassificationExportConfigurationResponseTypeDef,
    GetCustomDataIdentifierResponseTypeDef,
    GetFindingsFilterResponseTypeDef,
    GetFindingsPublicationConfigurationResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetFindingStatisticsResponseTypeDef,
    GetInvitationsCountResponseTypeDef,
    GetMacieSessionResponseTypeDef,
    GetMasterAccountResponseTypeDef,
    GetMemberResponseTypeDef,
    GetUsageStatisticsResponseTypeDef,
    GetUsageTotalsResponseTypeDef,
    JobScheduleFrequencyTypeDef,
    ListClassificationJobsResponseTypeDef,
    ListCustomDataIdentifiersResponseTypeDef,
    ListFindingsFiltersResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListJobsFilterCriteriaTypeDef,
    ListJobsSortCriteriaTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutClassificationExportConfigurationResponseTypeDef,
    S3JobDefinitionTypeDef,
    SecurityHubConfigurationTypeDef,
    SortCriteriaTypeDef,
    TestCustomDataIdentifierResponseTypeDef,
    UpdateFindingsFilterResponseTypeDef,
    UsageStatisticsFilterTypeDef,
    UsageStatisticsSortByTypeDef,
)

__all__ = ("Macie2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class Macie2Client:
    """
    [Macie2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_invitation(
        self, invitationId: str, administratorAccountId: str = None, masterAccount: str = None
    ) -> Dict[str, Any]:
        """
        [Client.accept_invitation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.accept_invitation)
        """

    def batch_get_custom_data_identifiers(
        self, ids: List[str] = None
    ) -> BatchGetCustomDataIdentifiersResponseTypeDef:
        """
        [Client.batch_get_custom_data_identifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.batch_get_custom_data_identifiers)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.can_paginate)
        """

    def create_classification_job(
        self,
        clientToken: str,
        jobType: JobType,
        name: str,
        s3JobDefinition: "S3JobDefinitionTypeDef",
        customDataIdentifierIds: List[str] = None,
        description: str = None,
        initialRun: bool = None,
        samplingPercentage: int = None,
        scheduleFrequency: "JobScheduleFrequencyTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateClassificationJobResponseTypeDef:
        """
        [Client.create_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.create_classification_job)
        """

    def create_custom_data_identifier(
        self,
        clientToken: str = None,
        description: str = None,
        ignoreWords: List[str] = None,
        keywords: List[str] = None,
        maximumMatchDistance: int = None,
        name: str = None,
        regex: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateCustomDataIdentifierResponseTypeDef:
        """
        [Client.create_custom_data_identifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.create_custom_data_identifier)
        """

    def create_findings_filter(
        self,
        action: FindingsFilterAction,
        findingCriteria: "FindingCriteriaTypeDef",
        name: str,
        clientToken: str = None,
        description: str = None,
        position: int = None,
        tags: Dict[str, str] = None,
    ) -> CreateFindingsFilterResponseTypeDef:
        """
        [Client.create_findings_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.create_findings_filter)
        """

    def create_invitations(
        self, accountIds: List[str], disableEmailNotification: bool = None, message: str = None
    ) -> CreateInvitationsResponseTypeDef:
        """
        [Client.create_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.create_invitations)
        """

    def create_member(
        self, account: AccountDetailTypeDef, tags: Dict[str, str] = None
    ) -> CreateMemberResponseTypeDef:
        """
        [Client.create_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.create_member)
        """

    def create_sample_findings(self, findingTypes: List[FindingType] = None) -> Dict[str, Any]:
        """
        [Client.create_sample_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.create_sample_findings)
        """

    def decline_invitations(self, accountIds: List[str]) -> DeclineInvitationsResponseTypeDef:
        """
        [Client.decline_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.decline_invitations)
        """

    def delete_custom_data_identifier(self, id: str) -> Dict[str, Any]:
        """
        [Client.delete_custom_data_identifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.delete_custom_data_identifier)
        """

    def delete_findings_filter(self, id: str) -> Dict[str, Any]:
        """
        [Client.delete_findings_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.delete_findings_filter)
        """

    def delete_invitations(self, accountIds: List[str]) -> DeleteInvitationsResponseTypeDef:
        """
        [Client.delete_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.delete_invitations)
        """

    def delete_member(self, id: str) -> Dict[str, Any]:
        """
        [Client.delete_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.delete_member)
        """

    def describe_buckets(
        self,
        criteria: Dict[str, BucketCriteriaAdditionalPropertiesTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
        sortCriteria: BucketSortCriteriaTypeDef = None,
    ) -> DescribeBucketsResponseTypeDef:
        """
        [Client.describe_buckets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.describe_buckets)
        """

    def describe_classification_job(self, jobId: str) -> DescribeClassificationJobResponseTypeDef:
        """
        [Client.describe_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.describe_classification_job)
        """

    def describe_organization_configuration(
        self,
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        [Client.describe_organization_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.describe_organization_configuration)
        """

    def disable_macie(self) -> Dict[str, Any]:
        """
        [Client.disable_macie documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.disable_macie)
        """

    def disable_organization_admin_account(self, adminAccountId: str) -> Dict[str, Any]:
        """
        [Client.disable_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.disable_organization_admin_account)
        """

    def disassociate_from_administrator_account(self) -> Dict[str, Any]:
        """
        [Client.disassociate_from_administrator_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.disassociate_from_administrator_account)
        """

    def disassociate_from_master_account(self) -> Dict[str, Any]:
        """
        [Client.disassociate_from_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.disassociate_from_master_account)
        """

    def disassociate_member(self, id: str) -> Dict[str, Any]:
        """
        [Client.disassociate_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.disassociate_member)
        """

    def enable_macie(
        self,
        clientToken: str = None,
        findingPublishingFrequency: FindingPublishingFrequency = None,
        status: MacieStatus = None,
    ) -> Dict[str, Any]:
        """
        [Client.enable_macie documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.enable_macie)
        """

    def enable_organization_admin_account(
        self, adminAccountId: str, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Client.enable_organization_admin_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.enable_organization_admin_account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.generate_presigned_url)
        """

    def get_administrator_account(self) -> GetAdministratorAccountResponseTypeDef:
        """
        [Client.get_administrator_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_administrator_account)
        """

    def get_bucket_statistics(self, accountId: str = None) -> GetBucketStatisticsResponseTypeDef:
        """
        [Client.get_bucket_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_bucket_statistics)
        """

    def get_classification_export_configuration(
        self,
    ) -> GetClassificationExportConfigurationResponseTypeDef:
        """
        [Client.get_classification_export_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_classification_export_configuration)
        """

    def get_custom_data_identifier(self, id: str) -> GetCustomDataIdentifierResponseTypeDef:
        """
        [Client.get_custom_data_identifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_custom_data_identifier)
        """

    def get_finding_statistics(
        self,
        groupBy: GroupBy,
        findingCriteria: "FindingCriteriaTypeDef" = None,
        size: int = None,
        sortCriteria: FindingStatisticsSortCriteriaTypeDef = None,
    ) -> GetFindingStatisticsResponseTypeDef:
        """
        [Client.get_finding_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_finding_statistics)
        """

    def get_findings(
        self, findingIds: List[str], sortCriteria: SortCriteriaTypeDef = None
    ) -> GetFindingsResponseTypeDef:
        """
        [Client.get_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_findings)
        """

    def get_findings_filter(self, id: str) -> GetFindingsFilterResponseTypeDef:
        """
        [Client.get_findings_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_findings_filter)
        """

    def get_findings_publication_configuration(
        self,
    ) -> GetFindingsPublicationConfigurationResponseTypeDef:
        """
        [Client.get_findings_publication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_findings_publication_configuration)
        """

    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        [Client.get_invitations_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_invitations_count)
        """

    def get_macie_session(self) -> GetMacieSessionResponseTypeDef:
        """
        [Client.get_macie_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_macie_session)
        """

    def get_master_account(self) -> GetMasterAccountResponseTypeDef:
        """
        [Client.get_master_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_master_account)
        """

    def get_member(self, id: str) -> GetMemberResponseTypeDef:
        """
        [Client.get_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_member)
        """

    def get_usage_statistics(
        self,
        filterBy: List[UsageStatisticsFilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
        sortBy: UsageStatisticsSortByTypeDef = None,
        timeRange: TimeRange = None,
    ) -> GetUsageStatisticsResponseTypeDef:
        """
        [Client.get_usage_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_usage_statistics)
        """

    def get_usage_totals(self, timeRange: str = None) -> GetUsageTotalsResponseTypeDef:
        """
        [Client.get_usage_totals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.get_usage_totals)
        """

    def list_classification_jobs(
        self,
        filterCriteria: ListJobsFilterCriteriaTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
        sortCriteria: ListJobsSortCriteriaTypeDef = None,
    ) -> ListClassificationJobsResponseTypeDef:
        """
        [Client.list_classification_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.list_classification_jobs)
        """

    def list_custom_data_identifiers(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListCustomDataIdentifiersResponseTypeDef:
        """
        [Client.list_custom_data_identifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.list_custom_data_identifiers)
        """

    def list_findings(
        self,
        findingCriteria: "FindingCriteriaTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None,
        sortCriteria: SortCriteriaTypeDef = None,
    ) -> ListFindingsResponseTypeDef:
        """
        [Client.list_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.list_findings)
        """

    def list_findings_filters(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListFindingsFiltersResponseTypeDef:
        """
        [Client.list_findings_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.list_findings_filters)
        """

    def list_invitations(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListInvitationsResponseTypeDef:
        """
        [Client.list_invitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.list_invitations)
        """

    def list_members(
        self, maxResults: int = None, nextToken: str = None, onlyAssociated: str = None
    ) -> ListMembersResponseTypeDef:
        """
        [Client.list_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.list_members)
        """

    def list_organization_admin_accounts(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListOrganizationAdminAccountsResponseTypeDef:
        """
        [Client.list_organization_admin_accounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.list_organization_admin_accounts)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.list_tags_for_resource)
        """

    def put_classification_export_configuration(
        self, configuration: "ClassificationExportConfigurationTypeDef"
    ) -> PutClassificationExportConfigurationResponseTypeDef:
        """
        [Client.put_classification_export_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.put_classification_export_configuration)
        """

    def put_findings_publication_configuration(
        self,
        clientToken: str = None,
        securityHubConfiguration: "SecurityHubConfigurationTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_findings_publication_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.put_findings_publication_configuration)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.tag_resource)
        """

    def test_custom_data_identifier(
        self,
        regex: str,
        sampleText: str,
        ignoreWords: List[str] = None,
        keywords: List[str] = None,
        maximumMatchDistance: int = None,
    ) -> TestCustomDataIdentifierResponseTypeDef:
        """
        [Client.test_custom_data_identifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.test_custom_data_identifier)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.untag_resource)
        """

    def update_classification_job(self, jobId: str, jobStatus: JobStatus) -> Dict[str, Any]:
        """
        [Client.update_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.update_classification_job)
        """

    def update_findings_filter(
        self,
        id: str,
        action: FindingsFilterAction = None,
        description: str = None,
        findingCriteria: "FindingCriteriaTypeDef" = None,
        name: str = None,
        position: int = None,
    ) -> UpdateFindingsFilterResponseTypeDef:
        """
        [Client.update_findings_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.update_findings_filter)
        """

    def update_macie_session(
        self,
        findingPublishingFrequency: FindingPublishingFrequency = None,
        status: MacieStatus = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_macie_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.update_macie_session)
        """

    def update_member_session(self, id: str, status: MacieStatus) -> Dict[str, Any]:
        """
        [Client.update_member_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.update_member_session)
        """

    def update_organization_configuration(self, autoEnable: bool) -> Dict[str, Any]:
        """
        [Client.update_organization_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Client.update_organization_configuration)
        """

    @overload
    def get_paginator(
        self, operation_name: DescribeBucketsPaginatorName
    ) -> DescribeBucketsPaginator:
        """
        [Paginator.DescribeBuckets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Paginator.DescribeBuckets)
        """

    @overload
    def get_paginator(
        self, operation_name: GetUsageStatisticsPaginatorName
    ) -> GetUsageStatisticsPaginator:
        """
        [Paginator.GetUsageStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Paginator.GetUsageStatistics)
        """

    @overload
    def get_paginator(
        self, operation_name: ListClassificationJobsPaginatorName
    ) -> ListClassificationJobsPaginator:
        """
        [Paginator.ListClassificationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Paginator.ListClassificationJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: ListCustomDataIdentifiersPaginatorName
    ) -> ListCustomDataIdentifiersPaginator:
        """
        [Paginator.ListCustomDataIdentifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Paginator.ListCustomDataIdentifiers)
        """

    @overload
    def get_paginator(self, operation_name: ListFindingsPaginatorName) -> ListFindingsPaginator:
        """
        [Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Paginator.ListFindings)
        """

    @overload
    def get_paginator(
        self, operation_name: ListFindingsFiltersPaginatorName
    ) -> ListFindingsFiltersPaginator:
        """
        [Paginator.ListFindingsFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Paginator.ListFindingsFilters)
        """

    @overload
    def get_paginator(
        self, operation_name: ListInvitationsPaginatorName
    ) -> ListInvitationsPaginator:
        """
        [Paginator.ListInvitations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Paginator.ListInvitations)
        """

    @overload
    def get_paginator(self, operation_name: ListMembersPaginatorName) -> ListMembersPaginator:
        """
        [Paginator.ListMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Paginator.ListMembers)
        """

    @overload
    def get_paginator(
        self, operation_name: ListOrganizationAdminAccountsPaginatorName
    ) -> ListOrganizationAdminAccountsPaginator:
        """
        [Paginator.ListOrganizationAdminAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/macie2.html#Macie2.Paginator.ListOrganizationAdminAccounts)
        """
