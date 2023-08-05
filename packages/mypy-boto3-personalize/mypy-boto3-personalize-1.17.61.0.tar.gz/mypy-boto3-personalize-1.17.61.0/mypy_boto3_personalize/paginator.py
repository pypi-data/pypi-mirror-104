"""
Main interface for personalize service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_personalize import PersonalizeClient
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
        ListSolutionVersionsPaginator,
        ListSolutionsPaginator,
    )

    client: PersonalizeClient = boto3.client("personalize")

    list_batch_inference_jobs_paginator: ListBatchInferenceJobsPaginator = client.get_paginator("list_batch_inference_jobs")
    list_campaigns_paginator: ListCampaignsPaginator = client.get_paginator("list_campaigns")
    list_dataset_export_jobs_paginator: ListDatasetExportJobsPaginator = client.get_paginator("list_dataset_export_jobs")
    list_dataset_groups_paginator: ListDatasetGroupsPaginator = client.get_paginator("list_dataset_groups")
    list_dataset_import_jobs_paginator: ListDatasetImportJobsPaginator = client.get_paginator("list_dataset_import_jobs")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_event_trackers_paginator: ListEventTrackersPaginator = client.get_paginator("list_event_trackers")
    list_filters_paginator: ListFiltersPaginator = client.get_paginator("list_filters")
    list_recipes_paginator: ListRecipesPaginator = client.get_paginator("list_recipes")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    list_solution_versions_paginator: ListSolutionVersionsPaginator = client.get_paginator("list_solution_versions")
    list_solutions_paginator: ListSolutionsPaginator = client.get_paginator("list_solutions")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_personalize.literals import RecipeProvider
from mypy_boto3_personalize.type_defs import (
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
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListBatchInferenceJobsPaginator",
    "ListCampaignsPaginator",
    "ListDatasetExportJobsPaginator",
    "ListDatasetGroupsPaginator",
    "ListDatasetImportJobsPaginator",
    "ListDatasetsPaginator",
    "ListEventTrackersPaginator",
    "ListFiltersPaginator",
    "ListRecipesPaginator",
    "ListSchemasPaginator",
    "ListSolutionVersionsPaginator",
    "ListSolutionsPaginator",
)


class ListBatchInferenceJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListBatchInferenceJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs)
    """

    def paginate(
        self, solutionVersionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBatchInferenceJobsResponseTypeDef]:
        """
        [ListBatchInferenceJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListBatchInferenceJobs.paginate)
        """


class ListCampaignsPaginator(Boto3Paginator):
    """
    [Paginator.ListCampaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListCampaigns)
    """

    def paginate(
        self, solutionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCampaignsResponseTypeDef]:
        """
        [ListCampaigns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListCampaigns.paginate)
        """


class ListDatasetExportJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasetExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListDatasetExportJobs)
    """

    def paginate(
        self, datasetArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetExportJobsResponseTypeDef]:
        """
        [ListDatasetExportJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListDatasetExportJobs.paginate)
        """


class ListDatasetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetGroupsResponseTypeDef]:
        """
        [ListDatasetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListDatasetGroups.paginate)
        """


class ListDatasetImportJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs)
    """

    def paginate(
        self, datasetArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetImportJobsResponseTypeDef]:
        """
        [ListDatasetImportJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListDatasetImportJobs.paginate)
        """


class ListDatasetsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListDatasets)
    """

    def paginate(
        self, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetsResponseTypeDef]:
        """
        [ListDatasets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListDatasets.paginate)
        """


class ListEventTrackersPaginator(Boto3Paginator):
    """
    [Paginator.ListEventTrackers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers)
    """

    def paginate(
        self, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventTrackersResponseTypeDef]:
        """
        [ListEventTrackers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListEventTrackers.paginate)
        """


class ListFiltersPaginator(Boto3Paginator):
    """
    [Paginator.ListFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListFilters)
    """

    def paginate(
        self, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFiltersResponseTypeDef]:
        """
        [ListFilters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListFilters.paginate)
        """


class ListRecipesPaginator(Boto3Paginator):
    """
    [Paginator.ListRecipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListRecipes)
    """

    def paginate(
        self, recipeProvider: RecipeProvider = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecipesResponseTypeDef]:
        """
        [ListRecipes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListRecipes.paginate)
        """


class ListSchemasPaginator(Boto3Paginator):
    """
    [Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListSchemas)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchemasResponseTypeDef]:
        """
        [ListSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListSchemas.paginate)
        """


class ListSolutionVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSolutionVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions)
    """

    def paginate(
        self, solutionArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSolutionVersionsResponseTypeDef]:
        """
        [ListSolutionVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListSolutionVersions.paginate)
        """


class ListSolutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListSolutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListSolutions)
    """

    def paginate(
        self, datasetGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSolutionsResponseTypeDef]:
        """
        [ListSolutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/personalize.html#Personalize.Paginator.ListSolutions.paginate)
        """
