from typing import List

from fastapi import APIRouter, Response, status

from src.repository import epl_matches
from src.schemas.epl_matches import ResultEPLResponse, ResultEPLModel

router = APIRouter(prefix='/epl_results', tags=['EPL results'])


@router.post('/match', status_code=status.HTTP_201_CREATED, response_model=ResultEPLResponse)
async def create_epl_match(nhl_results: ResultEPLModel):
    new_match = await epl_matches.create_epl_match(nhl_results)
    return new_match


@router.get('/all_matches', status_code=status.HTTP_200_OK, response_model=List[ResultEPLResponse])
async def get_all_epl_matches():
    all_matches = await epl_matches.get_all_epl_matches()
    return all_matches


@router.delete('/{id}', status_code=status.HTTP_200_OK)
async def delete_epl_match(match_id: int):
    new_match = await epl_matches.delete_epl_match(match_id)
    return new_match


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ResultEPLResponse)
async def get_epl_match(match_id: int):
    match = await epl_matches.get_epl_match(match_id)
    return match


@router.put('/{id}', status_code=status.HTTP_201_CREATED, response_model=ResultEPLResponse)
async def update_epl_match(match: ResultEPLModel, match_id: int):
    updated_match = await epl_matches.update_epl_match(match_id, match)
    return updated_match
