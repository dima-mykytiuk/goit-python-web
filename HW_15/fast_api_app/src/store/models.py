from gino_starlette import Gino
from src.config import config

db = Gino(
    user=config['postgres']['db_user'],
    password=config['postgres']['db_password'],
    host=config['postgres']['db_host'],
    port=config['postgres']['db_port'],
    database=config['postgres']['db_database'],
)
    
    
class NhlResults(db.Model):
    __tablename__ = "nhl_results"
    id = db.Column(db.Integer, primary_key=True, index=True)
    nhl_match = db.Column(db.String, nullable=False)
    score = db.Column(db.String, unique=False, nullable=True)
    match_date = db.Column(db.Date, nullable=False)
    
    
class EPLResults(db.Model):
    __tablename__ = "epl_results"
    id = db.Column(db.Integer, primary_key=True, index=True)
    epl_match = db.Column(db.String, nullable=False)
    score = db.Column(db.String, unique=False, nullable=True)
    match_date = db.Column(db.Date, nullable=False)