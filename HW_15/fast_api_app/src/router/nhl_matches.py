from typing import List

from fastapi import APIRouter, Response, status

from src.repository import nhl_matches
from src.schemas.nhl_matches import ResultNHLResponse, ResultNHLModel

router = APIRouter(prefix='/nhl_results', tags=['NHL results'])


@router.post('/match', status_code=status.HTTP_201_CREATED, response_model=ResultNHLResponse)
async def create_nhl_match(nhl_results: ResultNHLModel):
    new_match = await nhl_matches.create_nhl_match(nhl_results)
    return new_match


@router.get('/all_matches', status_code=status.HTTP_200_OK, response_model=List[ResultNHLResponse])
async def get_all_nhl_matches():
    all_matches = await nhl_matches.get_all_nhl_matches()
    return all_matches


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_nhl_match(match_id: int):
    new_match = await nhl_matches.delete_nhl_match(match_id)
    return new_match


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ResultNHLResponse)
async def get_nhl_match(match_id: int):
    match = await nhl_matches.get_nhl_match(match_id)
    return match


@router.put('/{id}', status_code=status.HTTP_201_CREATED, response_model=ResultNHLResponse)
async def update_nhl_match(match: ResultNHLModel, match_id: int):
    updated_match = await nhl_matches.update_nhl_match(match_id, match)
    return updated_match
