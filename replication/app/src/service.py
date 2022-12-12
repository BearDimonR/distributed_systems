from sqlalchemy.orm import Session

from . import models, schemas


def get_language(db: Session, language_id: int):
    return db.query(models.Language).filter(models.Language.language_id == language_id).first()


def create_language(db: Session, continent: schemas.LanguageCreate):
    db_language = models.Language(language=continent.language)
    db.add(db_language)
    db.commit()
    db.refresh(db_language)
    return db_language
