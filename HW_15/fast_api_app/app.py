from fastapi import FastAPI

from src.store.models import db
from src.router import nhl_matches, epl_matches

app = FastAPI(title='The API')


def get_app():
    db.init_app(app)
    app.include_router(nhl_matches.router)
    app.include_router(epl_matches.router)
    return app


@app.get("/")
def read_root():
    return 'Welcome to API, You can see documentations on http://127.0.0.1:8000/docs'


app = get_app()
