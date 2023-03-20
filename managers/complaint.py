from db import database
from models import complaint
from models.enums import RoleType, State


class ComplaintManager:
    
    @staticmethod
    async def get_complaint(user):
        q = complaint.select()
        if user["role"] == RoleType.complainer:
            q = q.where(complaint.c.complainer_id == user["id"])
        elif user["role"] == RoleType.approver:
            q = q.where(complaint.c.state == State.pending)
        return await database.fetch_all(q)
    
    @staticmethod
    async def create_complaint(complaint_data):
        id_= await database.execute(compile.insert().values(complaint_data))
        return await database.fetch_one(complaint.select().where(complaint.c.id == id_))