"""
Main interface for personalize service client

Usage::

    ```python
    import boto3
    from mypy_boto3_personalize import PersonalizeClient

    client: PersonalizeClient = boto3.client("personalize")
    ```
"""
from typing import Any, Dict, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_personalize.literals import (
    IngestionMode,
    ListBatchInferenceJobsPaginatorName,
    ListCampaignsPaginatorName,
    ListDatasetExportJobsPaginatorName,
    ListDatasetGroupsPaginatorName,
    ListDatasetImportJobsPaginatorName,
    ListDatasetsPaginatorName,
    ListEventTrackersPaginatorName,
    ListFiltersPaginatorName,
    ListRecipesPaginatorName,
    ListSchemasPaginatorName,
    ListSolutionsPaginatorName,
    ListSolutionVersionsPaginatorName,
    RecipeProvider,
    TrainingMode,
)
from mypy_boto3_personalize.paginator import (
    ListBatchInferenceJobsPaginator,
    ListCampaignsPaginator,
    ListDatasetExportJobsPaginator,
    ListDatasetGroupsPaginator,
    ListDatasetImportJobsPaginator,
    ListDatasetsPaginator,
    ListEventTrackersPaginator,
    ListFiltersPaginator,
    ListRecipesPaginator,
    ListSchemasPaginator,
    ListSolutionsPaginator,
    ListSolutionVersionsPaginator,
)
from mypy_boto3_personalize.type_defs import (
    BatchInferenceJobConfigTypeDef,
    BatchInferenceJobInputTypeDef,
    BatchInferenceJobOutputTypeDef,
    CampaignConfigTypeDef,
    CreateBatchInferenceJobResponseTypeDef,
    CreateCampaignResponseTypeDef,
    CreateDatasetExportJobResponseTypeDef,
    CreateDatasetGroupResponseTypeDef,
    CreateDatasetImportJobResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateEventTrackerResponseTypeDef,
    CreateFilterResponseTypeDef,
    CreateSchemaResponseTypeDef,
    CreateSolutionResponseTypeDef,
    CreateSolutionVersionResponseTypeDef,
    DatasetExportJobOutputTypeDef,
    DataSourceTypeDef,
    DescribeAlgorithmResponseTypeDef,
    DescribeBatchInferenceJobResponseTypeDef,
    DescribeCampaignResponseTypeDef,
    DescribeDatasetExportJobResponseTypeDef,
    DescribeDatasetGroupResponseTypeDef,
    DescribeDatasetImportJobResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeEventTrackerResponseTypeDef,
    DescribeFeatureTransformationResponseTypeDef,
    DescribeFilterResponseTypeDef,
    DescribeRecipeResponseTypeDef,
    DescribeSchemaResponseTypeDef,
    DescribeSolutionResponseTypeDef,
    DescribeSolutionVersionResponseTypeDef,
    GetSolutionMetricsResponseTypeDef,
    ListBatchInferenceJobsResponseTypeDef,
    ListCampaignsResponseTypeDef,
    ListDatasetExportJobsResponseTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListEventTrackersResponseTypeDef,
    ListFiltersResponseTypeDef,
    ListRecipesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListSolutionsResponseTypeDef,
    ListSolutionVersionsResponseTypeDef,
    SolutionConfigTypeDef,
    UpdateCampaignResponseTypeDef,
)

__all__ = ("PersonalizeClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class PersonalizeClient:
    """
    [Personalize.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.can_paginate)
        """

    def create_batch_inference_job(
        self,
        jobName: str,
        solutionVersionArn: str,
        jobInput: "BatchInferenceJobInputTypeDef",
        jobOutput: "BatchInferenceJobOutputTypeDef",
        roleArn: str,
        filterArn: str = None,
        numResults: int = None,
        batchInferenceJobConfig: "BatchInferenceJobConfigTypeDef" = None,
    ) -> CreateBatchInferenceJobResponseTypeDef:
        """
        [Client.create_batch_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.create_batch_inference_job)
        """

    def create_campaign(
        self,
        name: str,
        solutionVersionArn: str,
        minProvisionedTPS: int,
        campaignConfig: "CampaignConfigTypeDef" = None,
    ) -> CreateCampaignResponseTypeDef:
        """
        [Client.create_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.create_campaign)
        """

    def create_dataset(
        self, name: str, schemaArn: str, datasetGroupArn: str, datasetType: str
    ) -> CreateDatasetResponseTypeDef:
        """
        [Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.create_dataset)
        """

    def create_dataset_export_job(
        self,
        jobName: str,
        datasetArn: str,
        roleArn: str,
        jobOutput: "DatasetExportJobOutputTypeDef",
        ingestionMode: IngestionMode = None,
    ) -> CreateDatasetExportJobResponseTypeDef:
        """
        [Client.create_dataset_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.create_dataset_export_job)
        """

    def create_dataset_group(
        self, name: str, roleArn: str = None, kmsKeyArn: str = None
    ) -> CreateDatasetGroupResponseTypeDef:
        """
        [Client.create_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.create_dataset_group)
        """

    def create_dataset_import_job(
        self, jobName: str, datasetArn: str, dataSource: "DataSourceTypeDef", roleArn: str
    ) -> CreateDatasetImportJobResponseTypeDef:
        """
        [Client.create_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.create_dataset_import_job)
        """

    def create_event_tracker(
        self, name: str, datasetGroupArn: str
    ) -> CreateEventTrackerResponseTypeDef:
        """
        [Client.create_event_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.create_event_tracker)
        """

    def create_filter(
        self, name: str, datasetGroupArn: str, filterExpression: str
    ) -> CreateFilterResponseTypeDef:
        """
        [Client.create_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.create_filter)
        """

    def create_schema(self, name: str, schema: str) -> CreateSchemaResponseTypeDef:
        """
        [Client.create_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.create_schema)
        """

    def create_solution(
        self,
        name: str,
        datasetGroupArn: str,
        performHPO: bool = None,
        performAutoML: bool = None,
        recipeArn: str = None,
        eventType: str = None,
        solutionConfig: "SolutionConfigTypeDef" = None,
    ) -> CreateSolutionResponseTypeDef:
        """
        [Client.create_solution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.create_solution)
        """

    def create_solution_version(
        self, solutionArn: str, trainingMode: TrainingMode = None
    ) -> CreateSolutionVersionResponseTypeDef:
        """
        [Client.create_solution_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.create_solution_version)
        """

    def delete_campaign(self, campaignArn: str) -> None:
        """
        [Client.delete_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.delete_campaign)
        """

    def delete_dataset(self, datasetArn: str) -> None:
        """
        [Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.delete_dataset)
        """

    def delete_dataset_group(self, datasetGroupArn: str) -> None:
        """
        [Client.delete_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.delete_dataset_group)
        """

    def delete_event_tracker(self, eventTrackerArn: str) -> None:
        """
        [Client.delete_event_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.delete_event_tracker)
        """

    def delete_filter(self, filterArn: str) -> None:
        """
        [Client.delete_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.delete_filter)
        """

    def delete_schema(self, schemaArn: str) -> None:
        """
        [Client.delete_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.delete_schema)
        """

    def delete_solution(self, solutionArn: str) -> None:
        """
        [Client.delete_solution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.delete_solution)
        """

    def describe_algorithm(self, algorithmArn: str) -> DescribeAlgorithmResponseTypeDef:
        """
        [Client.describe_algorithm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_algorithm)
        """

    def describe_batch_inference_job(
        self, batchInferenceJobArn: str
    ) -> DescribeBatchInferenceJobResponseTypeDef:
        """
        [Client.describe_batch_inference_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_batch_inference_job)
        """

    def describe_campaign(self, campaignArn: str) -> DescribeCampaignResponseTypeDef:
        """
        [Client.describe_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_campaign)
        """

    def describe_dataset(self, datasetArn: str) -> DescribeDatasetResponseTypeDef:
        """
        [Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_dataset)
        """

    def describe_dataset_export_job(
        self, datasetExportJobArn: str
    ) -> DescribeDatasetExportJobResponseTypeDef:
        """
        [Client.describe_dataset_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_dataset_export_job)
        """

    def describe_dataset_group(self, datasetGroupArn: str) -> DescribeDatasetGroupResponseTypeDef:
        """
        [Client.describe_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_dataset_group)
        """

    def describe_dataset_import_job(
        self, datasetImportJobArn: str
    ) -> DescribeDatasetImportJobResponseTypeDef:
        """
        [Client.describe_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_dataset_import_job)
        """

    def describe_event_tracker(self, eventTrackerArn: str) -> DescribeEventTrackerResponseTypeDef:
        """
        [Client.describe_event_tracker documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_event_tracker)
        """

    def describe_feature_transformation(
        self, featureTransformationArn: str
    ) -> DescribeFeatureTransformationResponseTypeDef:
        """
        [Client.describe_feature_transformation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_feature_transformation)
        """

    def describe_filter(self, filterArn: str) -> DescribeFilterResponseTypeDef:
        """
        [Client.describe_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_filter)
        """

    def describe_recipe(self, recipeArn: str) -> DescribeRecipeResponseTypeDef:
        """
        [Client.describe_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_recipe)
        """

    def describe_schema(self, schemaArn: str) -> DescribeSchemaResponseTypeDef:
        """
        [Client.describe_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_schema)
        """

    def describe_solution(self, solutionArn: str) -> DescribeSolutionResponseTypeDef:
        """
        [Client.describe_solution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_solution)
        """

    def describe_solution_version(
        self, solutionVersionArn: str
    ) -> DescribeSolutionVersionResponseTypeDef:
        """
        [Client.describe_solution_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.describe_solution_version)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.generate_presigned_url)
        """

    def get_solution_metrics(self, solutionVersionArn: str) -> GetSolutionMetricsResponseTypeDef:
        """
        [Client.get_solution_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.get_solution_metrics)
        """

    def list_batch_inference_jobs(
        self, solutionVersionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListBatchInferenceJobsResponseTypeDef:
        """
        [Client.list_batch_inference_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.list_batch_inference_jobs)
        """

    def list_campaigns(
        self, solutionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListCampaignsResponseTypeDef:
        """
        [Client.list_campaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.list_campaigns)
        """

    def list_dataset_export_jobs(
        self, datasetArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetExportJobsResponseTypeDef:
        """
        [Client.list_dataset_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.list_dataset_export_jobs)
        """

    def list_dataset_groups(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        [Client.list_dataset_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.list_dataset_groups)
        """

    def list_dataset_import_jobs(
        self, datasetArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetImportJobsResponseTypeDef:
        """
        [Client.list_dataset_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.list_dataset_import_jobs)
        """

    def list_datasets(
        self, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.list_datasets)
        """

    def list_event_trackers(
        self, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListEventTrackersResponseTypeDef:
        """
        [Client.list_event_trackers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.list_event_trackers)
        """

    def list_filters(
        self, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListFiltersResponseTypeDef:
        """
        [Client.list_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.list_filters)
        """

    def list_recipes(
        self, recipeProvider: RecipeProvider = None, nextToken: str = None, maxResults: int = None
    ) -> ListRecipesResponseTypeDef:
        """
        [Client.list_recipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.list_recipes)
        """

    def list_schemas(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListSchemasResponseTypeDef:
        """
        [Client.list_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.list_schemas)
        """

    def list_solution_versions(
        self, solutionArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListSolutionVersionsResponseTypeDef:
        """
        [Client.list_solution_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.list_solution_versions)
        """

    def list_solutions(
        self, datasetGroupArn: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListSolutionsResponseTypeDef:
        """
        [Client.list_solutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.list_solutions)
        """

    def update_campaign(
        self,
        campaignArn: str,
        solutionVersionArn: str = None,
        minProvisionedTPS: int = None,
        campaignConfig: "CampaignConfigTypeDef" = None,
    ) -> UpdateCampaignResponseTypeDef:
        """
        [Client.update_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Client.update_campaign)
        """

    @overload
    def get_paginator(
        self, operation_name: ListBatchInferenceJobsPaginatorName
    ) -> ListBatchInferenceJobsPaginator:
        """
        [Paginator.ListBatchInferenceJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs)
        """

    @overload
    def get_paginator(self, operation_name: ListCampaignsPaginatorName) -> ListCampaignsPaginator:
        """
        [Paginator.ListCampaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListCampaigns)
        """

    @overload
    def get_paginator(
        self, operation_name: ListDatasetExportJobsPaginatorName
    ) -> ListDatasetExportJobsPaginator:
        """
        [Paginator.ListDatasetExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListDatasetExportJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: ListDatasetGroupsPaginatorName
    ) -> ListDatasetGroupsPaginator:
        """
        [Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: ListDatasetImportJobsPaginatorName
    ) -> ListDatasetImportJobsPaginator:
        """
        [Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs)
        """

    @overload
    def get_paginator(self, operation_name: ListDatasetsPaginatorName) -> ListDatasetsPaginator:
        """
        [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListDatasets)
        """

    @overload
    def get_paginator(
        self, operation_name: ListEventTrackersPaginatorName
    ) -> ListEventTrackersPaginator:
        """
        [Paginator.ListEventTrackers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers)
        """

    @overload
    def get_paginator(self, operation_name: ListFiltersPaginatorName) -> ListFiltersPaginator:
        """
        [Paginator.ListFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListFilters)
        """

    @overload
    def get_paginator(self, operation_name: ListRecipesPaginatorName) -> ListRecipesPaginator:
        """
        [Paginator.ListRecipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListRecipes)
        """

    @overload
    def get_paginator(self, operation_name: ListSchemasPaginatorName) -> ListSchemasPaginator:
        """
        [Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListSchemas)
        """

    @overload
    def get_paginator(
        self, operation_name: ListSolutionVersionsPaginatorName
    ) -> ListSolutionVersionsPaginator:
        """
        [Paginator.ListSolutionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions)
        """

    @overload
    def get_paginator(self, operation_name: ListSolutionsPaginatorName) -> ListSolutionsPaginator:
        """
        [Paginator.ListSolutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListSolutions)
        """
