from typing import Optional
from sqlmodel import Field, SQLModel

class Adventure(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    campaign_id: int

class Campaign(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    party: str

class Character(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    campaign_id: int
    character_class: str
    secrets: str

class Location(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    campaign_id: int

class NPC(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    campaign_id: int

class Objective(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    campaign_id: int
    hidden: bool
    term: str

class Session(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    campaign_id: int

class Scene(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    campaign_id: int
    session_id: int
    kind: str
    location_id: Optional[int] = None
    outcome: Optional[str] = None
    previous_scene_id: Optional[int] = None

