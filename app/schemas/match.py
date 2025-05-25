from datetime import date
from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field as SQLField

class MatchCreate(BaseModel):
    team1: str = Field(..., example="Team Alpha")
    team2: str = Field(..., example="Team Beta")
    match_date: date = Field(..., example="2024-09-01")
    winner: str | None = Field(None, example="Team Alpha")

class MatchRead(MatchCreate):
    id: int

class Match(SQLModel, MatchRead, table=True):
    id: int | None = SQLField(default=None, primary_key=True)