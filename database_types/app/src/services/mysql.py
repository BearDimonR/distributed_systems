
from . import base
from sqlalchemy.orm import Session
from .. import connection
from ..models import mysql


class MySQLService(base.BaseService):

    db: Session = next(connection.get_relational_session())

    @classmethod
    def get_resume(cls, resume_id: int):
        return cls.db.query(mysql.Resume).filter(mysql.Resume.id == resume_id).first()

    @classmethod
    def get_resume_hobbies(cls, resume_id: int):
        return cls.get_resume(resume_id).hobbies

    @classmethod
    def get_resume_cities(cls, resume_id: int):
        return cls.db.query(mysql.City).filter(
            mysql.City.positions.any(resumeId=resume_id)).all()

    @classmethod
    def get_city_hobbies(cls, city_id: int):
        resume_ids = cls.db.query(mysql.Position).filter(
            mysql.Position.cityId == city_id).with_entities(mysql.Position.resumeId).subquery()
        return cls.db.query(mysql.HobbyCategory).filter(
            mysql.HobbyCategory.hobbies.any(mysql.Hobby.resumeId.in_(resume_ids))).all()

    @classmethod
    def get_coworkers_list(cls):
        return cls.db.execute("""
            SELECT C.name, group_concat(DISTINCT U.id) as userIds 
            FROM linkedin.resume R 
                INNER JOIN linkedin.position P ON R.id = P.resumeId 
                INNER JOIN linkedin.company C ON C.id = P.companyId
                INNER JOIN linkedin.user U ON U.id = R.userId
            GROUP BY C.name;
            """
        ).all()
