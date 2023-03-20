from typing import List, Optional
from fastapi import APIRouter, Depends
from managers.auth import is_admin, oauth2_scheme

from managers.user import UserManager
from models.enums import RoleType
from shemas.response.user import UserOut

router = APIRouter(tags=["Users"])


@router.get("/users/", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], response_model=List[UserOut])
async def get_users(email: Optional[str] = None):
    if email:
        return await UserManager.get_user_by_email(email)
    return await UserManager.get_all_users()


@router.put("/users/{user_id}/make-admin", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=204)
async def make_admin(user_id: int):
    await UserManager.change_role(RoleType.admin, user_id)
    

@router.put("/users/{user_id}/make-approver", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=204)
async def make_admin(user_id: int):
    await UserManager.change_role(RoleType.approver, user_id)