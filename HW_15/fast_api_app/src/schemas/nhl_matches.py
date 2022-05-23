from datetime import date

from pydantic import BaseModel


class ResultNHLModel(BaseModel):
    nhl_match: str
    score: str
    match_date: date


class ResultNHLResponse(BaseModel):
    id: int
    nhl_match: str
    score: str
    match_date: date
    
    class Config:
        orm_mode = True
        