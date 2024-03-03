from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from app.models import Hero, HeroCreate, HeroUpdate
from app.services.hero import HeroService

router = APIRouter(tags=["heroes"])


@router.get("/heroes", response_model=list[Hero])
async def get_heroes(s: Annotated[HeroService, Depends(HeroService)]):
    heroes = await s.get_all_heroes()
    return [Hero(name=hero.name, secret_name=hero.secret_name, age=hero.age, id=hero.id) for hero in heroes]


@router.post("/heroes")
async def add_hero(hero: HeroCreate, s: Annotated[HeroService, Depends(HeroService)]):
    return await s.create_new_hero(hero)


@router.patch("/heroes/{hero_id}")
async def update_hero(hero_id: int, hero: HeroUpdate, s: Annotated[HeroService, Depends(HeroService)]):
    return await s.update_hero(hero, hero_id)


@router.get("/heroes/{hero_id}")
async def get_one_hero(hero_id: int, s: Annotated[HeroService, Depends(HeroService)]):
    return await s.get_hero(hero_id)


@router.delete("/heroes/{hero_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hero(hero_id: int, s: Annotated[HeroService, Depends(HeroService)]):
    return await s.delete_hero(hero_id)
