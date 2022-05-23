from datetime import date

from pydantic import BaseModel


class ResultEPLModel(BaseModel):
    epl_match: str
    score: str
    match_date: date


class ResultEPLResponse(BaseModel):
    id: int
    epl_match: str
    score: str
    match_date: date
    
    class Config:
        orm_mode = True
