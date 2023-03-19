
from typing import Optional
from fastapi import HTTPException
import jwt
from datetime import datetime, timedelta
from decouple import config
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.requests import Request

from db import databases
from models import user


class AuthManager:

    @staticmethod
    def encode_token(self, user):
        try: 
            payload = {
                "sub": user["id"],
                "exp": datetime.utcnow() + timedelta(minutes=120)
            }
            return jwt.encode(payload, config("SECRET_KEY"), algorithm="HS256")
        except Exception as ex:
            #Log the exception
            return ex
        
        
class CustomHTTPBAREAR(HTTPBearer):

    async def __call__(
            self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        res = await super().__call__(request)

        try:
            payload = jwt.decode(res.credentials, config("SECRET_KEY"), algorithms=["HS256"])
            user_data = await databases.fetch_one(user.select().where(user.c.id == payload["sub"]))
            request.state.user = user_data
            return user_data
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, "Token is expired")
        except jwt.InvalidTokenError:
            raise HTTPException(401, "Invalid Token")