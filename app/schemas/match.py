from datetime import date
from pydantic import BaseModel, Field

class MatchCreate(BaseModel):
    tournament_id: int = Field(description="ID турнира")
    team1_id: int = Field(description="ID первой команды")
    team2_id: int = Field(description="ID второй команды")
    winner_id: int | None = Field(
        default=None, 
        description="ID победившей команды (опционально)"
    )
    match_date: date = Field(description="Дата проведения матча")

    class Config:
        json_schema_extra = {
            "example": {
                "tournament_id": 1,
                "team1_id": 10,
                "team2_id": 20,
                "winner_id": 10,
                "match_date": "2024-01-01"
            }
        }