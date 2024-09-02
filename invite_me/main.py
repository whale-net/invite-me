from fastapi import FastAPI

from invite_me import seed_db

app = FastAPI()

seed_db()


@app.get("/")
def root():
    return {"HI": "world"}
