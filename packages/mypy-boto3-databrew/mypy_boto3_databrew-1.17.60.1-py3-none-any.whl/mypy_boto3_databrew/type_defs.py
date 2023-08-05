"""
Main interface for databrew service type definitions.

Usage::

    ```python
    from mypy_boto3_databrew.type_defs import ConditionExpressionTypeDef

    data: ConditionExpressionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_databrew.literals import (
    CompressionFormat,
    EncryptionMode,
    InputFormat,
    JobRunState,
    JobType,
    LogSubscription,
    Order,
    OrderedBy,
    OutputFormat,
    ParameterType,
    SampleMode,
    SampleType,
    SessionStatus,
    Source,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ConditionExpressionTypeDef",
    "CsvOptionsTypeDef",
    "CsvOutputOptionsTypeDef",
    "DataCatalogInputDefinitionTypeDef",
    "DatabaseInputDefinitionTypeDef",
    "DatasetParameterTypeDef",
    "DatasetTypeDef",
    "DatetimeOptionsTypeDef",
    "ExcelOptionsTypeDef",
    "FilesLimitTypeDef",
    "FilterExpressionTypeDef",
    "FormatOptionsTypeDef",
    "InputTypeDef",
    "JobRunTypeDef",
    "JobSampleTypeDef",
    "JobTypeDef",
    "JsonOptionsTypeDef",
    "OutputFormatOptionsTypeDef",
    "OutputTypeDef",
    "PathOptionsTypeDef",
    "ProjectTypeDef",
    "RecipeActionTypeDef",
    "RecipeReferenceTypeDef",
    "RecipeStepTypeDef",
    "RecipeTypeDef",
    "RecipeVersionErrorDetailTypeDef",
    "ResponseMetadata",
    "S3LocationTypeDef",
    "SampleTypeDef",
    "ScheduleTypeDef",
    "BatchDeleteRecipeVersionResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateProfileJobResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateRecipeJobResponseTypeDef",
    "CreateRecipeResponseTypeDef",
    "CreateScheduleResponseTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteRecipeVersionResponseTypeDef",
    "DeleteScheduleResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeJobResponseTypeDef",
    "DescribeJobRunResponseTypeDef",
    "DescribeProjectResponseTypeDef",
    "DescribeRecipeResponseTypeDef",
    "DescribeScheduleResponseTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListProjectsResponseTypeDef",
    "ListRecipeVersionsResponseTypeDef",
    "ListRecipesResponseTypeDef",
    "ListSchedulesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PublishRecipeResponseTypeDef",
    "SendProjectSessionActionResponseTypeDef",
    "StartJobRunResponseTypeDef",
    "StartProjectSessionResponseTypeDef",
    "StopJobRunResponseTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdateProfileJobResponseTypeDef",
    "UpdateProjectResponseTypeDef",
    "UpdateRecipeJobResponseTypeDef",
    "UpdateRecipeResponseTypeDef",
    "UpdateScheduleResponseTypeDef",
    "ViewFrameTypeDef",
)

_RequiredConditionExpressionTypeDef = TypedDict(
    "_RequiredConditionExpressionTypeDef", {"Condition": str, "TargetColumn": str}
)
_OptionalConditionExpressionTypeDef = TypedDict(
    "_OptionalConditionExpressionTypeDef", {"Value": str}, total=False
)


class ConditionExpressionTypeDef(
    _RequiredConditionExpressionTypeDef, _OptionalConditionExpressionTypeDef
):
    pass


CsvOptionsTypeDef = TypedDict(
    "CsvOptionsTypeDef", {"Delimiter": str, "HeaderRow": bool}, total=False
)

CsvOutputOptionsTypeDef = TypedDict("CsvOutputOptionsTypeDef", {"Delimiter": str}, total=False)

_RequiredDataCatalogInputDefinitionTypeDef = TypedDict(
    "_RequiredDataCatalogInputDefinitionTypeDef", {"DatabaseName": str, "TableName": str}
)
_OptionalDataCatalogInputDefinitionTypeDef = TypedDict(
    "_OptionalDataCatalogInputDefinitionTypeDef",
    {"CatalogId": str, "TempDirectory": "S3LocationTypeDef"},
    total=False,
)


class DataCatalogInputDefinitionTypeDef(
    _RequiredDataCatalogInputDefinitionTypeDef, _OptionalDataCatalogInputDefinitionTypeDef
):
    pass


_RequiredDatabaseInputDefinitionTypeDef = TypedDict(
    "_RequiredDatabaseInputDefinitionTypeDef", {"GlueConnectionName": str, "DatabaseTableName": str}
)
_OptionalDatabaseInputDefinitionTypeDef = TypedDict(
    "_OptionalDatabaseInputDefinitionTypeDef", {"TempDirectory": "S3LocationTypeDef"}, total=False
)


class DatabaseInputDefinitionTypeDef(
    _RequiredDatabaseInputDefinitionTypeDef, _OptionalDatabaseInputDefinitionTypeDef
):
    pass


_RequiredDatasetParameterTypeDef = TypedDict(
    "_RequiredDatasetParameterTypeDef", {"Name": str, "Type": ParameterType}
)
_OptionalDatasetParameterTypeDef = TypedDict(
    "_OptionalDatasetParameterTypeDef",
    {
        "DatetimeOptions": "DatetimeOptionsTypeDef",
        "CreateColumn": bool,
        "Filter": "FilterExpressionTypeDef",
    },
    total=False,
)


class DatasetParameterTypeDef(_RequiredDatasetParameterTypeDef, _OptionalDatasetParameterTypeDef):
    pass


_RequiredDatasetTypeDef = TypedDict(
    "_RequiredDatasetTypeDef", {"Name": str, "Input": "InputTypeDef"}
)
_OptionalDatasetTypeDef = TypedDict(
    "_OptionalDatasetTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "Format": InputFormat,
        "FormatOptions": "FormatOptionsTypeDef",
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Source": Source,
        "PathOptions": "PathOptionsTypeDef",
        "Tags": Dict[str, str],
        "ResourceArn": str,
    },
    total=False,
)


class DatasetTypeDef(_RequiredDatasetTypeDef, _OptionalDatasetTypeDef):
    pass


_RequiredDatetimeOptionsTypeDef = TypedDict("_RequiredDatetimeOptionsTypeDef", {"Format": str})
_OptionalDatetimeOptionsTypeDef = TypedDict(
    "_OptionalDatetimeOptionsTypeDef", {"TimezoneOffset": str, "LocaleCode": str}, total=False
)


class DatetimeOptionsTypeDef(_RequiredDatetimeOptionsTypeDef, _OptionalDatetimeOptionsTypeDef):
    pass


ExcelOptionsTypeDef = TypedDict(
    "ExcelOptionsTypeDef",
    {"SheetNames": List[str], "SheetIndexes": List[int], "HeaderRow": bool},
    total=False,
)

_RequiredFilesLimitTypeDef = TypedDict("_RequiredFilesLimitTypeDef", {"MaxFiles": int})
_OptionalFilesLimitTypeDef = TypedDict(
    "_OptionalFilesLimitTypeDef", {"OrderedBy": OrderedBy, "Order": Order}, total=False
)


class FilesLimitTypeDef(_RequiredFilesLimitTypeDef, _OptionalFilesLimitTypeDef):
    pass


FilterExpressionTypeDef = TypedDict(
    "FilterExpressionTypeDef", {"Expression": str, "ValuesMap": Dict[str, str]}
)

FormatOptionsTypeDef = TypedDict(
    "FormatOptionsTypeDef",
    {"Json": "JsonOptionsTypeDef", "Excel": "ExcelOptionsTypeDef", "Csv": "CsvOptionsTypeDef"},
    total=False,
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "S3InputDefinition": "S3LocationTypeDef",
        "DataCatalogInputDefinition": "DataCatalogInputDefinitionTypeDef",
        "DatabaseInputDefinition": "DatabaseInputDefinitionTypeDef",
    },
    total=False,
)

JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "Attempt": int,
        "CompletedOn": datetime,
        "DatasetName": str,
        "ErrorMessage": str,
        "ExecutionTime": int,
        "JobName": str,
        "RunId": str,
        "State": JobRunState,
        "LogSubscription": LogSubscription,
        "LogGroupName": str,
        "Outputs": List["OutputTypeDef"],
        "RecipeReference": "RecipeReferenceTypeDef",
        "StartedBy": str,
        "StartedOn": datetime,
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)

JobSampleTypeDef = TypedDict("JobSampleTypeDef", {"Mode": SampleMode, "Size": int}, total=False)

_RequiredJobTypeDef = TypedDict("_RequiredJobTypeDef", {"Name": str})
_OptionalJobTypeDef = TypedDict(
    "_OptionalJobTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionMode,
        "Type": JobType,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "LogSubscription": LogSubscription,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List["OutputTypeDef"],
        "ProjectName": str,
        "RecipeReference": "RecipeReferenceTypeDef",
        "ResourceArn": str,
        "RoleArn": str,
        "Timeout": int,
        "Tags": Dict[str, str],
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)


class JobTypeDef(_RequiredJobTypeDef, _OptionalJobTypeDef):
    pass


JsonOptionsTypeDef = TypedDict("JsonOptionsTypeDef", {"MultiLine": bool}, total=False)

OutputFormatOptionsTypeDef = TypedDict(
    "OutputFormatOptionsTypeDef", {"Csv": "CsvOutputOptionsTypeDef"}, total=False
)

_RequiredOutputTypeDef = TypedDict("_RequiredOutputTypeDef", {"Location": "S3LocationTypeDef"})
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "CompressionFormat": CompressionFormat,
        "Format": OutputFormat,
        "PartitionColumns": List[str],
        "Overwrite": bool,
        "FormatOptions": "OutputFormatOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
    pass


PathOptionsTypeDef = TypedDict(
    "PathOptionsTypeDef",
    {
        "LastModifiedDateCondition": "FilterExpressionTypeDef",
        "FilesLimit": "FilesLimitTypeDef",
        "Parameters": Dict[str, "DatasetParameterTypeDef"],
    },
    total=False,
)

_RequiredProjectTypeDef = TypedDict("_RequiredProjectTypeDef", {"Name": str, "RecipeName": str})
_OptionalProjectTypeDef = TypedDict(
    "_OptionalProjectTypeDef",
    {
        "AccountId": str,
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "ResourceArn": str,
        "Sample": "SampleTypeDef",
        "Tags": Dict[str, str],
        "RoleArn": str,
        "OpenedBy": str,
        "OpenDate": datetime,
    },
    total=False,
)


class ProjectTypeDef(_RequiredProjectTypeDef, _OptionalProjectTypeDef):
    pass


_RequiredRecipeActionTypeDef = TypedDict("_RequiredRecipeActionTypeDef", {"Operation": str})
_OptionalRecipeActionTypeDef = TypedDict(
    "_OptionalRecipeActionTypeDef", {"Parameters": Dict[str, str]}, total=False
)


class RecipeActionTypeDef(_RequiredRecipeActionTypeDef, _OptionalRecipeActionTypeDef):
    pass


_RequiredRecipeReferenceTypeDef = TypedDict("_RequiredRecipeReferenceTypeDef", {"Name": str})
_OptionalRecipeReferenceTypeDef = TypedDict(
    "_OptionalRecipeReferenceTypeDef", {"RecipeVersion": str}, total=False
)


class RecipeReferenceTypeDef(_RequiredRecipeReferenceTypeDef, _OptionalRecipeReferenceTypeDef):
    pass


_RequiredRecipeStepTypeDef = TypedDict(
    "_RequiredRecipeStepTypeDef", {"Action": "RecipeActionTypeDef"}
)
_OptionalRecipeStepTypeDef = TypedDict(
    "_OptionalRecipeStepTypeDef",
    {"ConditionExpressions": List["ConditionExpressionTypeDef"]},
    total=False,
)


class RecipeStepTypeDef(_RequiredRecipeStepTypeDef, _OptionalRecipeStepTypeDef):
    pass


_RequiredRecipeTypeDef = TypedDict("_RequiredRecipeTypeDef", {"Name": str})
_OptionalRecipeTypeDef = TypedDict(
    "_OptionalRecipeTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ProjectName": str,
        "PublishedBy": str,
        "PublishedDate": datetime,
        "Description": str,
        "ResourceArn": str,
        "Steps": List["RecipeStepTypeDef"],
        "Tags": Dict[str, str],
        "RecipeVersion": str,
    },
    total=False,
)


class RecipeTypeDef(_RequiredRecipeTypeDef, _OptionalRecipeTypeDef):
    pass


RecipeVersionErrorDetailTypeDef = TypedDict(
    "RecipeVersionErrorDetailTypeDef",
    {"ErrorCode": str, "ErrorMessage": str, "RecipeVersion": str},
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredS3LocationTypeDef = TypedDict("_RequiredS3LocationTypeDef", {"Bucket": str})
_OptionalS3LocationTypeDef = TypedDict("_OptionalS3LocationTypeDef", {"Key": str}, total=False)


class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass


_RequiredSampleTypeDef = TypedDict("_RequiredSampleTypeDef", {"Type": SampleType})
_OptionalSampleTypeDef = TypedDict("_OptionalSampleTypeDef", {"Size": int}, total=False)


class SampleTypeDef(_RequiredSampleTypeDef, _OptionalSampleTypeDef):
    pass


_RequiredScheduleTypeDef = TypedDict("_RequiredScheduleTypeDef", {"Name": str})
_OptionalScheduleTypeDef = TypedDict(
    "_OptionalScheduleTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "JobNames": List[str],
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "CronExpression": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class ScheduleTypeDef(_RequiredScheduleTypeDef, _OptionalScheduleTypeDef):
    pass


_RequiredBatchDeleteRecipeVersionResponseTypeDef = TypedDict(
    "_RequiredBatchDeleteRecipeVersionResponseTypeDef", {"Name": str}
)
_OptionalBatchDeleteRecipeVersionResponseTypeDef = TypedDict(
    "_OptionalBatchDeleteRecipeVersionResponseTypeDef",
    {"Errors": List["RecipeVersionErrorDetailTypeDef"]},
    total=False,
)


class BatchDeleteRecipeVersionResponseTypeDef(
    _RequiredBatchDeleteRecipeVersionResponseTypeDef,
    _OptionalBatchDeleteRecipeVersionResponseTypeDef,
):
    pass


CreateDatasetResponseTypeDef = TypedDict("CreateDatasetResponseTypeDef", {"Name": str})

CreateProfileJobResponseTypeDef = TypedDict("CreateProfileJobResponseTypeDef", {"Name": str})

CreateProjectResponseTypeDef = TypedDict("CreateProjectResponseTypeDef", {"Name": str})

CreateRecipeJobResponseTypeDef = TypedDict("CreateRecipeJobResponseTypeDef", {"Name": str})

CreateRecipeResponseTypeDef = TypedDict("CreateRecipeResponseTypeDef", {"Name": str})

CreateScheduleResponseTypeDef = TypedDict("CreateScheduleResponseTypeDef", {"Name": str})

DeleteDatasetResponseTypeDef = TypedDict("DeleteDatasetResponseTypeDef", {"Name": str})

DeleteJobResponseTypeDef = TypedDict("DeleteJobResponseTypeDef", {"Name": str})

DeleteProjectResponseTypeDef = TypedDict("DeleteProjectResponseTypeDef", {"Name": str})

DeleteRecipeVersionResponseTypeDef = TypedDict(
    "DeleteRecipeVersionResponseTypeDef", {"Name": str, "RecipeVersion": str}
)

DeleteScheduleResponseTypeDef = TypedDict("DeleteScheduleResponseTypeDef", {"Name": str})

_RequiredDescribeDatasetResponseTypeDef = TypedDict(
    "_RequiredDescribeDatasetResponseTypeDef", {"Name": str, "Input": "InputTypeDef"}
)
_OptionalDescribeDatasetResponseTypeDef = TypedDict(
    "_OptionalDescribeDatasetResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "Format": InputFormat,
        "FormatOptions": "FormatOptionsTypeDef",
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Source": Source,
        "PathOptions": "PathOptionsTypeDef",
        "Tags": Dict[str, str],
        "ResourceArn": str,
    },
    total=False,
)


class DescribeDatasetResponseTypeDef(
    _RequiredDescribeDatasetResponseTypeDef, _OptionalDescribeDatasetResponseTypeDef
):
    pass


_RequiredDescribeJobResponseTypeDef = TypedDict(
    "_RequiredDescribeJobResponseTypeDef", {"Name": str}
)
_OptionalDescribeJobResponseTypeDef = TypedDict(
    "_OptionalDescribeJobResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionMode,
        "Type": JobType,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "LogSubscription": LogSubscription,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List["OutputTypeDef"],
        "ProjectName": str,
        "RecipeReference": "RecipeReferenceTypeDef",
        "ResourceArn": str,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "Timeout": int,
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)


class DescribeJobResponseTypeDef(
    _RequiredDescribeJobResponseTypeDef, _OptionalDescribeJobResponseTypeDef
):
    pass


_RequiredDescribeJobRunResponseTypeDef = TypedDict(
    "_RequiredDescribeJobRunResponseTypeDef", {"JobName": str}
)
_OptionalDescribeJobRunResponseTypeDef = TypedDict(
    "_OptionalDescribeJobRunResponseTypeDef",
    {
        "Attempt": int,
        "CompletedOn": datetime,
        "DatasetName": str,
        "ErrorMessage": str,
        "ExecutionTime": int,
        "RunId": str,
        "State": JobRunState,
        "LogSubscription": LogSubscription,
        "LogGroupName": str,
        "Outputs": List["OutputTypeDef"],
        "RecipeReference": "RecipeReferenceTypeDef",
        "StartedBy": str,
        "StartedOn": datetime,
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)


class DescribeJobRunResponseTypeDef(
    _RequiredDescribeJobRunResponseTypeDef, _OptionalDescribeJobRunResponseTypeDef
):
    pass


_RequiredDescribeProjectResponseTypeDef = TypedDict(
    "_RequiredDescribeProjectResponseTypeDef", {"Name": str}
)
_OptionalDescribeProjectResponseTypeDef = TypedDict(
    "_OptionalDescribeProjectResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "RecipeName": str,
        "ResourceArn": str,
        "Sample": "SampleTypeDef",
        "RoleArn": str,
        "Tags": Dict[str, str],
        "SessionStatus": SessionStatus,
        "OpenedBy": str,
        "OpenDate": datetime,
    },
    total=False,
)


class DescribeProjectResponseTypeDef(
    _RequiredDescribeProjectResponseTypeDef, _OptionalDescribeProjectResponseTypeDef
):
    pass


_RequiredDescribeRecipeResponseTypeDef = TypedDict(
    "_RequiredDescribeRecipeResponseTypeDef", {"Name": str}
)
_OptionalDescribeRecipeResponseTypeDef = TypedDict(
    "_OptionalDescribeRecipeResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ProjectName": str,
        "PublishedBy": str,
        "PublishedDate": datetime,
        "Description": str,
        "Steps": List["RecipeStepTypeDef"],
        "Tags": Dict[str, str],
        "ResourceArn": str,
        "RecipeVersion": str,
    },
    total=False,
)


class DescribeRecipeResponseTypeDef(
    _RequiredDescribeRecipeResponseTypeDef, _OptionalDescribeRecipeResponseTypeDef
):
    pass


_RequiredDescribeScheduleResponseTypeDef = TypedDict(
    "_RequiredDescribeScheduleResponseTypeDef", {"Name": str}
)
_OptionalDescribeScheduleResponseTypeDef = TypedDict(
    "_OptionalDescribeScheduleResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "JobNames": List[str],
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "CronExpression": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class DescribeScheduleResponseTypeDef(
    _RequiredDescribeScheduleResponseTypeDef, _OptionalDescribeScheduleResponseTypeDef
):
    pass


_RequiredListDatasetsResponseTypeDef = TypedDict(
    "_RequiredListDatasetsResponseTypeDef", {"Datasets": List["DatasetTypeDef"]}
)
_OptionalListDatasetsResponseTypeDef = TypedDict(
    "_OptionalListDatasetsResponseTypeDef", {"NextToken": str}, total=False
)


class ListDatasetsResponseTypeDef(
    _RequiredListDatasetsResponseTypeDef, _OptionalListDatasetsResponseTypeDef
):
    pass


_RequiredListJobRunsResponseTypeDef = TypedDict(
    "_RequiredListJobRunsResponseTypeDef", {"JobRuns": List["JobRunTypeDef"]}
)
_OptionalListJobRunsResponseTypeDef = TypedDict(
    "_OptionalListJobRunsResponseTypeDef", {"NextToken": str}, total=False
)


class ListJobRunsResponseTypeDef(
    _RequiredListJobRunsResponseTypeDef, _OptionalListJobRunsResponseTypeDef
):
    pass


_RequiredListJobsResponseTypeDef = TypedDict(
    "_RequiredListJobsResponseTypeDef", {"Jobs": List["JobTypeDef"]}
)
_OptionalListJobsResponseTypeDef = TypedDict(
    "_OptionalListJobsResponseTypeDef", {"NextToken": str}, total=False
)


class ListJobsResponseTypeDef(_RequiredListJobsResponseTypeDef, _OptionalListJobsResponseTypeDef):
    pass


_RequiredListProjectsResponseTypeDef = TypedDict(
    "_RequiredListProjectsResponseTypeDef", {"Projects": List["ProjectTypeDef"]}
)
_OptionalListProjectsResponseTypeDef = TypedDict(
    "_OptionalListProjectsResponseTypeDef", {"NextToken": str}, total=False
)


class ListProjectsResponseTypeDef(
    _RequiredListProjectsResponseTypeDef, _OptionalListProjectsResponseTypeDef
):
    pass


_RequiredListRecipeVersionsResponseTypeDef = TypedDict(
    "_RequiredListRecipeVersionsResponseTypeDef", {"Recipes": List["RecipeTypeDef"]}
)
_OptionalListRecipeVersionsResponseTypeDef = TypedDict(
    "_OptionalListRecipeVersionsResponseTypeDef", {"NextToken": str}, total=False
)


class ListRecipeVersionsResponseTypeDef(
    _RequiredListRecipeVersionsResponseTypeDef, _OptionalListRecipeVersionsResponseTypeDef
):
    pass


_RequiredListRecipesResponseTypeDef = TypedDict(
    "_RequiredListRecipesResponseTypeDef", {"Recipes": List["RecipeTypeDef"]}
)
_OptionalListRecipesResponseTypeDef = TypedDict(
    "_OptionalListRecipesResponseTypeDef", {"NextToken": str}, total=False
)


class ListRecipesResponseTypeDef(
    _RequiredListRecipesResponseTypeDef, _OptionalListRecipesResponseTypeDef
):
    pass


_RequiredListSchedulesResponseTypeDef = TypedDict(
    "_RequiredListSchedulesResponseTypeDef", {"Schedules": List["ScheduleTypeDef"]}
)
_OptionalListSchedulesResponseTypeDef = TypedDict(
    "_OptionalListSchedulesResponseTypeDef", {"NextToken": str}, total=False
)


class ListSchedulesResponseTypeDef(
    _RequiredListSchedulesResponseTypeDef, _OptionalListSchedulesResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PublishRecipeResponseTypeDef = TypedDict("PublishRecipeResponseTypeDef", {"Name": str})

_RequiredSendProjectSessionActionResponseTypeDef = TypedDict(
    "_RequiredSendProjectSessionActionResponseTypeDef", {"Name": str}
)
_OptionalSendProjectSessionActionResponseTypeDef = TypedDict(
    "_OptionalSendProjectSessionActionResponseTypeDef",
    {"Result": str, "ActionId": int},
    total=False,
)


class SendProjectSessionActionResponseTypeDef(
    _RequiredSendProjectSessionActionResponseTypeDef,
    _OptionalSendProjectSessionActionResponseTypeDef,
):
    pass


StartJobRunResponseTypeDef = TypedDict("StartJobRunResponseTypeDef", {"RunId": str})

_RequiredStartProjectSessionResponseTypeDef = TypedDict(
    "_RequiredStartProjectSessionResponseTypeDef", {"Name": str}
)
_OptionalStartProjectSessionResponseTypeDef = TypedDict(
    "_OptionalStartProjectSessionResponseTypeDef", {"ClientSessionId": str}, total=False
)


class StartProjectSessionResponseTypeDef(
    _RequiredStartProjectSessionResponseTypeDef, _OptionalStartProjectSessionResponseTypeDef
):
    pass


StopJobRunResponseTypeDef = TypedDict("StopJobRunResponseTypeDef", {"RunId": str})

UpdateDatasetResponseTypeDef = TypedDict("UpdateDatasetResponseTypeDef", {"Name": str})

UpdateProfileJobResponseTypeDef = TypedDict("UpdateProfileJobResponseTypeDef", {"Name": str})

_RequiredUpdateProjectResponseTypeDef = TypedDict(
    "_RequiredUpdateProjectResponseTypeDef", {"Name": str}
)
_OptionalUpdateProjectResponseTypeDef = TypedDict(
    "_OptionalUpdateProjectResponseTypeDef", {"LastModifiedDate": datetime}, total=False
)


class UpdateProjectResponseTypeDef(
    _RequiredUpdateProjectResponseTypeDef, _OptionalUpdateProjectResponseTypeDef
):
    pass


UpdateRecipeJobResponseTypeDef = TypedDict("UpdateRecipeJobResponseTypeDef", {"Name": str})

UpdateRecipeResponseTypeDef = TypedDict("UpdateRecipeResponseTypeDef", {"Name": str})

UpdateScheduleResponseTypeDef = TypedDict("UpdateScheduleResponseTypeDef", {"Name": str})

_RequiredViewFrameTypeDef = TypedDict("_RequiredViewFrameTypeDef", {"StartColumnIndex": int})
_OptionalViewFrameTypeDef = TypedDict(
    "_OptionalViewFrameTypeDef", {"ColumnRange": int, "HiddenColumns": List[str]}, total=False
)


class ViewFrameTypeDef(_RequiredViewFrameTypeDef, _OptionalViewFrameTypeDef):
    pass
