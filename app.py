from fastapi import FastAPI
from db.db import create_db_and_tables
from heroes.router import hero_router

create_db_and_tables()
app = FastAPI()
app.include_router(hero_router, prefix='/api')

