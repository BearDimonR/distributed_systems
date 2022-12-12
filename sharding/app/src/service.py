from sqlalchemy.orm import Session

from . import models, schemas

def get_country_stats(db: Session, year: str):
    return db.query(models.CountryStats)\
        .filter(models.CountryStats.year == year)\
        .all()

def get_country_stats_partition(db: Session, year: str, partition: str):
    return db.execute(f'SELECT * FROM {models.CountryStats.__tablename__} PARTITION ({partition}) WHERE year={year};').all()

def create_country_stats(db: Session, country_stats: schemas.CountryStatsCreate):
    db_country_stats = models.CountryStats(**country_stats.dict())
    db.add(db_country_stats)
    db.commit()
    db.refresh(db_country_stats)
    return db_country_stats