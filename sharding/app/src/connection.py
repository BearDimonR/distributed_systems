from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_HOST = os.environ.get('DATABASE_HOST', '127.0.0.1:3306')
DATABASE_USER = os.environ.get('DATABASE_USER', 'root')
DATABASE_PASSWORD =  os.environ.get('DATABASE_PASSWORD', 'pass')
DATABASE_NAME =  os.environ.get('DATABASE_NAME', 'nation')

master = f'mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'

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