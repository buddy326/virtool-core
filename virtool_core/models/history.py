from datetime import datetime
from typing import List

from virtool_core.models.reference import ReferenceMinimal
from virtool_core.models.user import UserMinimal
from pydantic import BaseModel


class HistoryIndex(BaseModel):
    id: str
    version: int


class HistoryOTU(BaseModel):
    id: str
    name: str
    version: str


class RemoteID(BaseModel):
    id: str


class HistorySequence(BaseModel):
    _id: str
    accession: str
    definition: str
    host: str
    isolate_id: str
    otu_id: str
    reference: ReferenceMinimal
    remote: RemoteID = None
    segment: str
    sequence: str


class HistoryIsolate(BaseModel):
    default: bool
    id: str
    sequences: List[HistorySequence]
    source_name: str
    source_type: str


class HistorySchema(BaseModel):
    molecule: str
    name: str
    required: bool


class HistoryUser(BaseModel):
    id: str


class HistoryDiff(BaseModel):
    _id: str
    abbreviation: str
    created_at: datetime
    imported: bool
    isolates: List[HistoryIsolate]
    issues: None
    last_indexed_version: int = None
    lower_name: str
    name: str
    reference: ReferenceMinimal
    remote: RemoteID
    schema: List[HistorySchema]
    user: HistoryUser
    verified: bool
    version: int


class HistoryMinimal(BaseModel):
    created_at: datetime
    description: str
    id: str
    index: HistoryIndex
    method_name: str
    otu: HistoryOTU
    reference: ReferenceMinimal
    user: UserMinimal


class History(HistoryMinimal):
    diff: HistoryDiff
