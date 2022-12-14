
from . import base
from .. import connection
from neo4j import Session


class Neo4jService(base.BaseService):

    db: Session = connection.get_neo4j_session()

    @classmethod
    def get_resume(cls, resume_id: int):
        return list(cls.db.run("""
            MATCH (a:resume)
            WHERE a.id = $resume_id 
            RETURN DISTINCT a""", resume_id=resume_id))

    @classmethod
    def get_resume_hobbies(cls, resume_id: int):
        return list(cls.db.run("""
            MATCH (a:resume)-[:HAS_HOBBY]-(b:hobby)
            WHERE a.id = $resume_id 
            RETURN DISTINCT b""", resume_id=resume_id))

    @classmethod
    def get_resume_cities(cls, resume_id: int):
        return list(cls.db.run("""
            MATCH (a:resume)-[:HAS_POSITION]-(b:position),
            (b)-[:IN]-(c:city)
            WHERE a.id = $resume_id 
            RETURN DISTINCT c""", resume_id=resume_id))

    @classmethod
    def get_city_hobbies(cls, city_id: int):
        return list(cls.db.run("""
            MATCH (a:resume)-[:HAS_POSITION]-(b:position),
            (a)-[:HAS_HOBBY]-(d:hobby),
            (b)-[:IN]-(c:city)
            WHERE c.id = $city_id 
            RETURN DISTINCT d""", city_id=city_id))

    @classmethod
    def get_coworkers_list(cls):
        return list(cls.db.run("""
            MATCH (f:user)-[:HAS_RESUME]-(a:resume),
            (a)-[:HAS_POSITION]-(b:position),
            (b)-[:FOR]-(e:company),
            (b)-[:IN]-(c:city),
            RETURN DISTINCT e.name, f.login"""))
