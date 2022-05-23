from fastapi import status, HTTPException
from src.store.models import db, EPLResults


async def get_epl_match(match_id: int):
    match = await EPLResults.get(match_id)
    if match is None:
        raise HTTPException(status_code=404, detail=f'Match with id: {match_id} not found!')
    return match


async def update_epl_match(match_id: int, match):
    match_for_update = await EPLResults.get(match_id)
    if match_for_update is None:
        raise HTTPException(status_code=404, detail=f'Match with id: {match_id} not found!')
    await match_for_update.update(epl_match=match.epl_match, score=match.score, match_date=match.match_date).apply()
    return match_for_update


async def create_epl_match(match):
    new_match = await EPLResults.create(epl_match=match.epl_match, score=match.score, match_date=match.match_date)
    return new_match


async def get_all_epl_matches():
    all_matches = await db.all(EPLResults.query)
    return all_matches


async def delete_epl_match(match_id: int):
    match_for_delete = await EPLResults.get(match_id)
    if match_for_delete is None:
        raise HTTPException(status_code=404, detail=f'Match with id: {match_id} not found!')
    await match_for_delete.delete()
    return match_for_delete
