from fastapi import FastAPI
from src.services import mysql_service, mongodb_service, neo4j_service

app = FastAPI()


## mariadb api

@app.get("/relational/resume/{id}", tags=["relational"])
def get_resume(id: int):
    return mysql_service.get_resume(resume_id=id)


@app.get("/relational/resume/{id}/hobbies", tags=["relational"])
def get_resume_hobbies(id: int):
    return mysql_service.get_resume_hobbies(resume_id=id)


@app.get("/relational/resume/{id}/cities", tags=["relational"])
def get_resume_cities(id: int):
   return mysql_service.get_resume_cities(resume_id=id)


@app.get("/relational/city/{id}/hobbies", tags=["relational"])
def get_city_hobbies(id: int):
    return mysql_service.get_city_hobbies(city_id=id)


@app.get("/relational/user/institution", tags=["relational"])
def get_resume_hobbies():
    return mysql_service.get_coworkers_list()


## mongo api

@app.get("/document/resume/{id}", tags=["document"])
def get_resume(id: int):
    return mongodb_service.get_resume(resume_id=id)


@app.get("/document/resume/{id}/hobbies", tags=["document"])
def get_resume_hobbies(id: int):
    return mongodb_service.get_resume_hobbies(resume_id=id)


@app.get("/document/resume/{id}/cities", tags=["document"])
def get_resume_cities(id: int):
   return mongodb_service.get_resume_cities(resume_id=id)


@app.get("/document/city/{id}/hobbies", tags=["document"])
def get_city_hobbies(id: int):
    return mongodb_service.get_city_hobbies(city_id=id)


@app.get("/document/user/institution", tags=["document"])
def get_resume_hobbies():
    return mongodb_service.get_coworkers_list()


## mongo api

@app.get("/graph/resume/{id}", tags=["graph"])
def get_resume(id: int):
    return neo4j_service.get_resume(resume_id=id)


@app.get("/graph/resume/{id}/hobbies", tags=["graph"])
def get_resume_hobbies(id: int):
    return neo4j_service.get_resume_hobbies(resume_id=id)


@app.get("/graph/resume/{id}/cities", tags=["graph"])
def get_resume_cities(id: int):
   return neo4j_service.get_resume_cities(resume_id=id)


@app.get("/graph/city/{id}/hobbies", tags=["graph"])
def get_city_hobbies(id: int):
    return neo4j_service.get_city_hobbies(city_id=id)


@app.get("/graph/user/institution", tags=["graph"])
def get_resume_hobbies():
    return neo4j_service.get_coworkers_list()