from typing import Optional

import pytest
from pydantic import ValidationError

from virtool_core.models.basemodel import BaseModel
from virtool_core.models.validators import prevent_none_validator


class DummyModel(BaseModel):
    name: str
    id: Optional[int]
    count: Optional[int]

    _prevent_none = prevent_none_validator("count", "id")


def test_prevent_null_validator():

    DummyModel(name="baz")

    DummyModel(name="bar", id=1, count=2)

    with pytest.raises(ValidationError) as count_err:
        DummyModel(name="foo", id=2, count=None)

    assert "Value may not be null" in str(count_err)

    with pytest.raises(ValidationError) as id_err:
        DummyModel(name="bob", id=None)

    assert "Value may not be null" in str(id_err)

    with pytest.raises(ValidationError) as err:
        DummyModel(name="baz_1", id=None, count=None)

    assert "Value may not be null" in str(err)
