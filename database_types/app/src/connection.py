from sqlalchemy import create_engine
import os
from pymongo import MongoClient
from neo4j import GraphDatabase
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_USER = os.environ.get('DATABASE_USER', 'root')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'pass')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'linkedin')

RELATIONAL_HOST = os.environ.get('RELATIONAL_HOST', 'localhost')
GRAPH_HOST = os.environ.get('GRAPH_HOST', 'localhost')
DOC_HOST = os.environ.get('DOC_HOST', 'localhost')

mysql = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{RELATIONAL_HOST}:3306/{DATABASE_NAME}'
mongodb = f'mongodb://{DATABASE_USER}:{DATABASE_PASSWORD}@{RELATIONAL_HOST}:27017'
neo4j = f'neo4j://{RELATIONAL_HOST}:7687'

Base = declarative_base()


def get_relational_session():
    SQLALCHEMY_DATABASE_URI = mysql
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True, pool_size=10)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_mongo_session():
    client = MongoClient(mongodb)
    return client['linkedin']

def get_neo4j_session():
    db = GraphDatabase.driver(neo4j, auth=(DATABASE_USER, DATABASE_PASSWORD))
    return db.session()