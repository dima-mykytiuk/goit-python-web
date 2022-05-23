from fastapi import status, HTTPException
from src.store.models import db, NhlResults


async def get_nhl_match(match_id: int):
    match = await NhlResults.get(match_id)
    if match is None:
        raise HTTPException(status_code=404, detail=f'Match with id: {match_id} not found!')
    return match


async def update_nhl_match(match_id: int, match):
    match_for_update = await NhlResults.get(match_id)
    if match_for_update is None:
        raise HTTPException(status_code=404, detail=f'Match with id: {match_id} not found!')
    await match_for_update.update(nhl_match=match.nhl_match, score=match.score, match_date=match.match_date).apply()
    return match_for_update


async def create_nhl_match(match):
    new_match = await NhlResults.create(nhl_match=match.nhl_match, score=match.score, match_date=match.match_date)
    return new_match


async def get_all_nhl_matches():
    all_matches = await db.all(NhlResults.query)
    return all_matches


async def delete_nhl_match(match_id: int):
    match_for_delete = await NhlResults.get(match_id)
    if match_for_delete is None:
        raise HTTPException(status_code=404, detail=f'Match with id: {match_id} not found!')
    await match_for_delete.delete()
    return match_for_delete
