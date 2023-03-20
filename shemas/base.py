from pydantic import BaseModel

from models.enums import State


class UserBase(BaseModel):
    email: str

class BaseComplaint(BaseModel):
    title: str
    description: str
    photo_url: str
    amount: float
    