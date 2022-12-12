from . import connection
from sqlalchemy import Column, Integer, Date, DECIMAL


class CountryStats(connection.Base):
    __tablename__ = "country_stats"

    country_id = Column(Integer, primary_key=True, index=True)
    year = Column(Date, primary_key=True, index=True)
    population = Column(Integer)
    gdp = Column(DECIMAL)
