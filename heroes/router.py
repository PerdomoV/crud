from sqlmodel import Session
from heroes.model import HeroRead, HeroUpdate, HeroCreate, Hero
from db.db import engine
from fastapi import APIRouter, HTTPException

hero_router = APIRouter()

@hero_router.get('/heroes/{id}', response_model=HeroRead)
def read_hero_by_id(id: int):
    with Session(engine) as session:
        hero = session.get(Hero, id)
        if not hero:
            raise HTTPException(status_code=404, detail='Heroe no encontrado')
        else:
            return hero

@hero_router.post('/heroes/', response_model=HeroCreate)
def create_hero(hero: HeroCreate):
    with Session(engine) as session:
        new_hero = Hero.from_orm(hero)
        session.add(new_hero)
        session.commit()
        session.refresh(new_hero)
        return new_hero

@hero_router.put('/heroes/{id}', response_model=HeroUpdate)
def update_hero(id: str, hero: HeroUpdate):
    with Session(engine) as session:
        hero_to_update = session.get(Hero, id)
        if not hero_to_update:
            raise HTTPException(status_code=404, detail='Hero Not Found')
        hero_data = hero.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(hero_to_update, key, value)
        session.add(hero_to_update)
        session.commit()
        session.refresh(hero_to_update)
        return hero_to_update

@hero_router.delete('/heroes/{id}')
def delete_hero(id: str):
    with Session(engine) as session:
        hero_to_delete = session.get(Hero, id)
        if not hero_to_delete:
            raise HTTPException(status_code=404, detail='Hero Not Found')
        session.delete(hero_to_delete)
        session.commit()
        return {'ok': True}