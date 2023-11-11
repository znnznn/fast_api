from typing import Optional

from fastapi_users import schemas, models
from fastapi_users.schemas import PYDANTIC_V2
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    id: models.ID
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    # if PYDANTIC_V2:  # pragma: no cover
    #     model_config = ConfigDict(from_attributes=True)  # type: ignore
    # else:  # pragma: no cover

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str
    name: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass