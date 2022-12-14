from . import models, schemas, connection

def create_language(language_create: schemas.LanguageCreate):
    db = next(connection.get_session())
    db_language = models.Language(language=language_create.language)
    db.add(db_language)
    db.commit()
    db.refresh(db_language)
    return db_language
