from fastapi import FastAPI
from src import schemas, service, connection

app = FastAPI()


@app.get("/master/get/{id}", response_model=schemas.Language)
def get_language_master(id: int):
    db = next(connection.get_session(connection.master))
    return service.get_language(db, id)


@app.post("/master/post", response_model=schemas.Language)
def create_language_master(language: schemas.LanguageCreate):
    db = next(connection.get_session(connection.master))
    return service.create_language(db, language)


@app.get("/second_master/get/{id}", response_model=schemas.Language)
def get_language_second_master(id: int):
    db = next(connection.get_session(connection.second_master))
    return service.get_language(db, id)


@app.post("/second_master/post", response_model=schemas.Language)
def create_language_second_master(language: schemas.LanguageCreate):
    db = next(connection.get_session(connection.second_master))
    return service.create_language(db, language)


@app.get("/slave/get/{id}", response_model=schemas.Language)
def get_language_slave(id: int):
    db = next(connection.get_session(connection.slave))
    return service.get_language(db, id)


@app.post("/slave/post", response_model=schemas.Language)
def create_language_slave(language: schemas.LanguageCreate):
    db = next(connection.get_session(connection.slave))
    return service.create_language(db, language)
