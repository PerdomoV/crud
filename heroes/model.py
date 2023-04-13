from sqlmodel import SQLModel, Field
from typing import Optional

class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)
    
class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class HeroCreate(HeroBase):
    pass

class HeroRead(HeroBase):
    id: int

class HeroUpdate(HeroBase):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None