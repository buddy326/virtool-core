import enum
from datetime import datetime
from typing import List, Any, Optional

from virtool_core.models.basemodel import BaseModel
from virtool_core.models.searchresult import SearchResult
from virtool_core.models.task import TaskNested
from virtool_core.models.upload import Upload
from virtool_core.models.user import UserNested


class ReferenceClonedFrom(BaseModel):
    id: str
    name: str


class ReferenceDataType(str, enum.Enum):
    barcode = "barcode"
    genome = "genome"


class ReferenceRights(BaseModel):
    build: bool
    modify: bool
    modify_otu: bool
    remove: bool


class ReferenceGroup(ReferenceRights):
    id: str
    created_at: datetime


class ReferenceUser(ReferenceRights):
    administrator: bool
    handle: str
    id: str
    created_at: datetime


class ReferenceContributor(UserNested):
    count: int


class ReferenceRemotesFrom(BaseModel):
    errors: List[Any]
    slug: str


class ReferenceInstalled(BaseModel):
    body: str
    created_at: datetime
    filename: str
    html_url: str
    id: int
    name: str
    newer: bool
    published_at: datetime
    ready: bool
    size: int
    user: UserNested


class ReferenceRelease(BaseModel):
    body: str
    content_type: str
    download_url: str
    etag: str
    filename: str
    html_url: str
    id: int
    name: str
    newer: bool
    published_at: datetime
    retrieved_at: datetime
    size: int


class ReferenceBuild(BaseModel):
    created_at: datetime
    id: str
    version: int
    user: UserNested
    has_json: bool


class ReferenceNested(BaseModel):
    id: str


class AnalysisReference(ReferenceNested):
    name: str


class ReferenceMinimal(AnalysisReference):
    cloned_from: ReferenceClonedFrom = None
    created_at: datetime
    data_type: ReferenceDataType
    groups: List[ReferenceGroup]
    installed: ReferenceInstalled = None
    internal_control: Optional[str]
    latest_build: Optional[ReferenceBuild]
    organism: str
    otu_count: int
    release: ReferenceRelease = None
    remotes_from: ReferenceRemotesFrom = None
    task: Optional[TaskNested]
    updating: bool = None
    unbuilt_change_count: int
    user: UserNested
    users: List[ReferenceUser]
    imported_from: Optional[Upload] = None


class Reference(ReferenceMinimal):
    contributors: List[ReferenceContributor]
    description: str
    restrict_source_types: bool
    source_types: List[str]
    targets: Optional[List[dict]]


class ReferenceSearchResult(SearchResult):
    documents: List[ReferenceMinimal]
    official_installed: bool
