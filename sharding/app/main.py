from fastapi import FastAPI
from typing import List
from src import schemas, service, connection

app = FastAPI()

@app.get("/master/get", response_model=List[schemas.CountryStats])
def get_country_stats_master(year: str):
    db = next(connection.get_session(connection.master))
    return service.get_country_stats(db, year)

@app.get("/master/get/partition", response_model=List[schemas.CountryStats])
def get_country_stats_master(year: str, partition: str):
    db = next(connection.get_session(connection.master))
    return service.get_country_stats_partition(db, year, partition)

@app.post("/master/post", response_model=schemas.CountryStats)
def create_country_stats_master(country_stats: schemas.CountryStatsCreate):
    db = next(connection.get_session(connection.master))
    return service.create_country_stats(db, country_stats)
