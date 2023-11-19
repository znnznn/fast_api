from typing import Union

from fastapi import FastAPI, Depends
from starlette.staticfiles import StaticFiles

from pages.routers import router as pages_router
from stocks.router import router as stocks_router
from users.auth import auth_backend
from database import User
from users.mixins import fastapi_users, current_user
from users.schemas import UserRead, UserCreate

app = FastAPI(title="FastAPI")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(stocks_router)
app.include_router(pages_router)


@app.get("/")
def read_root(user: User = Depends(current_user)):
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    print(item_id, q)
    return {"item_id": item_id, "q": q}
