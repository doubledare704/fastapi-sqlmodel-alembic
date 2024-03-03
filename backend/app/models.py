from typing import Optional

from sqlmodel import Field, SQLModel


class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: Optional[int] = None


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)


class HeroCreate(HeroBase):
    pass


class HeroUpdate(HeroCreate):
    pass
