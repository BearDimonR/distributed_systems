from sqlalchemy.orm import Session
from json import dumps
from kafka import KafkaProducer
import os

from . import models, schemas

BOOTSTRAP_SERVER = os.environ.get('BOOTSTRAP_SERVER', 'localhost:9092')

producer = KafkaProducer(
    bootstrap_servers=[BOOTSTRAP_SERVER],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)


def get_language(db: Session, language_id: int):
    return db.query(models.Language).filter(models.Language.language_id == language_id).first()


def get_all_languages(db: Session):
    return db.query(models.Language).all()

def create_language(continent: schemas.LanguageCreate):
    producer.send('language', value=dict(continent))
    return continent
