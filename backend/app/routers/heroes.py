from fastapi import APIRouter, Depends
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import get_session
from app.models import Hero, HeroCreate

router = APIRouter(tags=["heroes"])


@router.get("/heroes", response_model=list[Hero])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Hero))
    heroes = result.scalars().all()
    return [Hero(name=hero.name, secret_name=hero.secret_name, age=hero.age, id=hero.id) for hero in heroes]


@router.post("/heroes")
async def add_song(hero: HeroCreate, session: AsyncSession = Depends(get_session)):
    hero = Hero(name=hero.name, secret_name=hero.secret_name, age=hero.age)
    session.add(hero)
    await session.commit()
    await session.refresh(hero)
    return hero
