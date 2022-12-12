from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_USER = os.environ.get('DATABASE_USER', 'root')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'pass')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'nation')

MASTER_HOST = os.environ.get('MASTER_HOST', '127.0.0.1')
SECOND_MASTER_HOST = os.environ.get('SECOND_MASTER_HOST', '127.0.0.1')
SLAVE_HOST = os.environ.get('SLAVE_HOST', '127.0.0.1')

master = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{MASTER_HOST}:3306/{DATABASE_NAME}'
second_master = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{SECOND_MASTER_HOST}:3306/{DATABASE_NAME}'
slave = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{SLAVE_HOST}:3306/{DATABASE_NAME}'

Base = declarative_base()


def get_session(uri):
    SQLALCHEMY_DATABASE_URI = uri
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True, pool_size=10)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
