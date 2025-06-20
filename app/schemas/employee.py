from typing import Union
from uuid import UUID
from pydantic import BaseModel
from app.core.consts import EmployeePosition


class EmployeeBase(BaseModel):
    name: str
    position: EmployeePosition

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Union[str, None] = None
    position: Union[EmployeePosition, None] = None

class EmployeeOut(EmployeeBase):
    id: UUID

    model_config = {"from_attributes": True}

class BaristaOut(BaseModel):
    id: UUID
    name: str

    model_config = {"from_attributes": True}
