from fastapi import APIRouter, Depends
from starlette.requests import Request

from managers.auth import oauth2_scheme
from managers.complaint import ComplaintManager

router = APIRouter(tags=["Complaints"])

@router.get("/complaints/", dependencies=[Depends(oauth2_scheme)])
async def get_complaints(requst: Request):
    user = requst.state.user
    return await ComplaintManager.get_comlaints(user)