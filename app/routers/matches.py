from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.match import MatchCreate, MatchRead, Match
from app.db import get_async_session
from app.api_docs.request_examples import example_create_match
from typing import List

router = APIRouter(prefix="/matches", tags=["Матчи"])

@router.post("/",
             status_code=status.HTTP_201_CREATED,
             response_model=MatchRead,
             summary="Добавить матч")
async def create_match(
    match: MatchCreate = example_create_match,
    session: AsyncSession = Depends(get_async_session)
):
    db_match = Match(**match.model_dump())
    session.add(db_match)
    await session.commit()
    await session.refresh(db_match)
    return db_match

@router.get("/",
            status_code=status.HTTP_200_OK,
            response_model=List[MatchRead],
            summary="Получить все матчи")
async def read_matches(
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(select(Match))
    matches = result.scalars().all()
    
    if not matches:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Матчи не найдены"
        )
    return matches