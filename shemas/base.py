from pydantic import BaseModel

from models.enums import State


class BaseComplaint(BaseModel):
    title: str
    description: str
    photo_url: str
    amount: float
    