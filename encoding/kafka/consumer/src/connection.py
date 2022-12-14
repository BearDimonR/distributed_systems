from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_USER = os.environ.get('DATABASE_USER', 'root')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'pass')
DATABASE_NAME = os.environ.get('DATABASE_NAME', 'nation')
DATABASE_HOST = os.environ.get('DATABASE_HOST', '127.0.0.1')

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:3306/{DATABASE_NAME}'
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True, pool_size=10)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
