"""
Main interface for codeguru-reviewer service client

Usage::

    ```python
    import boto3
    from mypy_boto3_codeguru_reviewer import CodeGuruReviewerClient

    client: CodeGuruReviewerClient = boto3.client("codeguru-reviewer")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_codeguru_reviewer.literals import (
    JobState,
    ListRepositoryAssociationsPaginatorName,
    ProviderType,
    Reaction,
    RepositoryAssociationState,
    TypeType,
)
from mypy_boto3_codeguru_reviewer.paginator import ListRepositoryAssociationsPaginator
from mypy_boto3_codeguru_reviewer.type_defs import (
    AssociateRepositoryResponseTypeDef,
    CodeReviewTypeTypeDef,
    CreateCodeReviewResponseTypeDef,
    DescribeCodeReviewResponseTypeDef,
    DescribeRecommendationFeedbackResponseTypeDef,
    DescribeRepositoryAssociationResponseTypeDef,
    DisassociateRepositoryResponseTypeDef,
    KMSKeyDetailsTypeDef,
    ListCodeReviewsResponseTypeDef,
    ListRecommendationFeedbackResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    ListRepositoryAssociationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    RepositoryTypeDef,
)

__all__ = ("CodeGuruReviewerClient",)


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
    NotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class CodeGuruReviewerClient:
    """
    [CodeGuruReviewer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_repository(
        self,
        Repository: RepositoryTypeDef,
        ClientRequestToken: str = None,
        Tags: Dict[str, str] = None,
        KMSKeyDetails: "KMSKeyDetailsTypeDef" = None,
    ) -> AssociateRepositoryResponseTypeDef:
        """
        [Client.associate_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.associate_repository)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.can_paginate)
        """

    def create_code_review(
        self,
        Name: str,
        RepositoryAssociationArn: str,
        Type: CodeReviewTypeTypeDef,
        ClientRequestToken: str = None,
    ) -> CreateCodeReviewResponseTypeDef:
        """
        [Client.create_code_review documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.create_code_review)
        """

    def describe_code_review(self, CodeReviewArn: str) -> DescribeCodeReviewResponseTypeDef:
        """
        [Client.describe_code_review documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_code_review)
        """

    def describe_recommendation_feedback(
        self, CodeReviewArn: str, RecommendationId: str, UserId: str = None
    ) -> DescribeRecommendationFeedbackResponseTypeDef:
        """
        [Client.describe_recommendation_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_recommendation_feedback)
        """

    def describe_repository_association(
        self, AssociationArn: str
    ) -> DescribeRepositoryAssociationResponseTypeDef:
        """
        [Client.describe_repository_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.describe_repository_association)
        """

    def disassociate_repository(self, AssociationArn: str) -> DisassociateRepositoryResponseTypeDef:
        """
        [Client.disassociate_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.disassociate_repository)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.generate_presigned_url)
        """

    def list_code_reviews(
        self,
        Type: TypeType,
        ProviderTypes: List[ProviderType] = None,
        States: List[JobState] = None,
        RepositoryNames: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListCodeReviewsResponseTypeDef:
        """
        [Client.list_code_reviews documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_code_reviews)
        """

    def list_recommendation_feedback(
        self,
        CodeReviewArn: str,
        NextToken: str = None,
        MaxResults: int = None,
        UserIds: List[str] = None,
        RecommendationIds: List[str] = None,
    ) -> ListRecommendationFeedbackResponseTypeDef:
        """
        [Client.list_recommendation_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_recommendation_feedback)
        """

    def list_recommendations(
        self, CodeReviewArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListRecommendationsResponseTypeDef:
        """
        [Client.list_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_recommendations)
        """

    def list_repository_associations(
        self,
        ProviderTypes: List[ProviderType] = None,
        States: List[RepositoryAssociationState] = None,
        Names: List[str] = None,
        Owners: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListRepositoryAssociationsResponseTypeDef:
        """
        [Client.list_repository_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_repository_associations)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.list_tags_for_resource)
        """

    def put_recommendation_feedback(
        self, CodeReviewArn: str, RecommendationId: str, Reactions: List[Reaction]
    ) -> Dict[str, Any]:
        """
        [Client.put_recommendation_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.put_recommendation_feedback)
        """

    def tag_resource(self, resourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Client.untag_resource)
        """

    def get_paginator(
        self, operation_name: ListRepositoryAssociationsPaginatorName
    ) -> ListRepositoryAssociationsPaginator:
        """
        [Paginator.ListRepositoryAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Paginator.ListRepositoryAssociations)
        """
