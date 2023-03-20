from fastapi import APIRouter

from managers.user import UserManager
from shemas.request.user import UserLoginIn, UserRegisterIn


router = APIRouter(tags=["Auth"])

@router.post("/register/", status_code=201)
async def register(user_data: UserRegisterIn):
    token = UserManager.register(user_data)
    return {"token": token}


@router.post("/login/", status_code=200)
async def login(user_data: UserLoginIn):
    token = UserManager.login(user_data)
    return {"token": token}
