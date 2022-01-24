import os
from typing import Optional

from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from propelauth_fastapi import init_auth
from propelauth_py.user import User

load_dotenv()

app = FastAPI()
auth = init_auth(os.getenv("PROPELAUTH_AUTH_URL"), os.getenv("PROPELAUTH_API_KEY"))

@app.get("/whoami")
def who_am_i(user: User = Depends(auth.require_user)):
    return {"user_id": user.user_id}


@app.get("/whoami_optional")
def who_am_i_optional(user: Optional[User] = Depends(auth.optional_user)):
    if user:
        return {"user_id": user.user_id}
    return {"user_id": None}

