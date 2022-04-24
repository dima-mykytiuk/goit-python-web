from aiohttp_jinja2 import template
from HW_12.models import Matches_NHL_Tribuna, Matches_Italian_Football, Matches, db_session


@template('index.html')
async def index(requests):
    return {'title': 'sssss'}


@template('pages/all_ftb_matches.html')
async def all_ftb_matches(requests):
    matches = db_session.query(Matches).all()
    return {'matches': matches}


@template('pages/nhl_matches.html')
async def all_nhl_matches(requests):
    matches = db_session.query(Matches_NHL_Tribuna).all()
    return {'matches': matches}


@template('pages/all_italian_matches.html')
async def all_itl_matches(requests):
    matches = db_session.query(Matches_Italian_Football).all()
    return {'matches': matches}
