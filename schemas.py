import datetime
from pydantic import BaseModel


class PostBase(BaseModel):
    id: int
    text: str
    created_date: datetime.datetime
    rubrics: str
    class Config:
        orm_mode = True

class DeleteResponse(BaseModel):
    detail: str
