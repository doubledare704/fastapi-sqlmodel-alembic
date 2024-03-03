from typing import Annotated

from fastapi import Depends, HTTPException

from app.models import Hero, HeroCreate, HeroUpdate
from app.repositories.hero import HeroRepository


class HeroService:
    def __init__(self, r: Annotated[HeroRepository, Depends(HeroRepository)]):
        self.repository = r

    async def get_all_heroes(self) -> list[Hero]:
        return await self.repository.get_all()

    async def create_new_hero(self, hero: HeroCreate) -> Hero:
        hero = Hero(name=hero.name, secret_name=hero.secret_name, age=hero.age)
        return await self.repository.create_hero(hero)

    async def update_hero(self, hero: HeroUpdate, hero_id: int) -> Hero:
        return await self.repository.update_hero(hero, hero_id)

    async def get_hero(self, hero_id: int) -> Hero:
        hero = await self.repository.get_hero(hero_id)
        if hero is None:
            raise HTTPException(status_code=404, detail="Hero not found")
        return hero

    async def delete_hero(self, hero_id: int) -> None:
        await self.repository.delete_hero(hero_id)
