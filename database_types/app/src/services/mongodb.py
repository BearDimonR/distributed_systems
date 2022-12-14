
from . import base
from pymongo.database import Database
from .. import connection


class MongoDBService(base.BaseService):

    db: Database = connection.get_mongo_session()

    @classmethod
    def get_resume(cls, resume_id: int):
        return cls.db['users'].find_one({'resumes._id': resume_id})

    @classmethod
    def get_resume_hobbies(cls, resume_id: int):
        return cls.db['users'].find_one({'resumes._id': resume_id}, {'resumes.hobbies': 1})['resumes'][0]['hobbies']

    @classmethod
    def get_resume_cities(cls, resume_id: int):
        return list(map(lambda x: x['city'], cls.db['users'].find_one({'resumes._id': resume_id}, {'resumes.positions.city': 1})['resumes'][0]['positions']))

    @classmethod
    def get_city_hobbies(cls, city_id: int):
        return cls.db['users'].find_one({'resumes.positions.city._id': city_id}, {'resumes.hobbies': 1})['resumes'][0]['hobbies']

    @classmethod
    def get_coworkers_list(cls):
        return list(cls.db['users'].aggregate([
            {'$project': { '_id': 1, 'resumes.positions.city': 1 } },
            {'$unwind': {'path': "$resumes"}},
            {'$unwind': {'path': "$resumes.positions"}},
            {'$group': { '_id': "$resumes.positions.city._id", 'userIds': { '$addToSet': '$_id' } }},
        ]))
