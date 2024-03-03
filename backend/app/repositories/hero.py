from typing import Annotated

from fastapi import Depends, HTTPException
from sqlalchemy import update
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import get_session
from app.models import Hero, HeroUpdate


class HeroRepository:
    def __init__(self, db_session: Annotated[AsyncSession, Depends(get_session)]):
        self.db_session = db_session

    async def create_hero(self, hero: Hero) -> Hero:
        self.db_session.add(hero)
        await self.db_session.commit()
        await self.db_session.refresh(hero)
        return hero

    async def get_all(self) -> list[Hero]:
        result = await self.db_session.execute(select(Hero))
        heroes = result.scalars().all()
        return heroes

    async def update_hero(self, hero_update: HeroUpdate, hero_id: int) -> Hero:
        result = await self.db_session.execute(select(Hero).where(Hero.id == hero_id))
        hero = result.scalars().first()
        if hero is None:
            raise HTTPException(status_code=404, detail="Hero not found")

        await self.db_session.execute(update(Hero).filter_by(id=hero_id).values(**hero_update.model_dump()))
        await self.db_session.commit()
        await self.db_session.refresh(hero)
        return hero

    async def delete_hero(self, hero_id: int) -> None:
        statement = select(Hero).where(Hero.id == hero_id)
        results = await self.db_session.execute(statement)
        hero = results.scalars().first()
        if hero is not None:
            await self.db_session.delete(hero)
            await self.db_session.commit()

    async def get_hero(self, hero_id: int) -> Hero:
        result = await self.db_session.execute(select(Hero).where(Hero.id == hero_id))
        hero = result.scalars().first()
        return hero
