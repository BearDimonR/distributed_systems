from fastapi import FastAPI
from src import schemas, service, connection
from typing import List

app = FastAPI()


@app.get("/get/all")
def get_language_master():
    db = next(connection.get_session())
    return service.get_all_languages(db)


@app.get("/get/{id}", response_model=schemas.Language)
def get_language_master(id: int):
    db = next(connection.get_session())
    return service.get_language(db, id)

@app.post("/post", response_model=schemas.LanguageCreate)
def create_language_master(language: schemas.LanguageCreate):
    db = next(connection.get_session())
    return service.create_language(language)