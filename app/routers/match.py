from fastapi import APIRouter, status, HTTPException
from schemas.match import MatchCreate
import csv
from pathlib import Path
from datetime import datetime

router = APIRouter(prefix="/matches", tags=["Matches"])

CSV_FILE = "matches_history.csv"

def write_match_to_csv(match: MatchCreate):
    file_exists = Path(CSV_FILE).exists()
    
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Записываем заголовок, если файл новый
        if not file_exists:
            writer.writerow([
                "tournament_id", 
                "team1_id", 
                "team2_id", 
                "winner_id", 
                "match_date"
            ])
        
        # Записываем данные матча
        writer.writerow([
            match.tournament_id,
            match.team1_id,
            match.team2_id,
            match.winner_id,
            match.match_date.isoformat()
        ])

@router.post("/", 
    status_code=status.HTTP_201_CREATED, 
    summary="Добавить матч в историю",
    response_description="Данные добавленного матча"
)
async def create_match(match: MatchCreate):
    try:
        write_match_to_csv(match)
        return match
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка при записи в CSV: {str(e)}"
        )