from pydantic import BaseModel


class CountryStatsBase(BaseModel):
    country_id: int
    year: str
    population: int
    gdp: float

    class Config:
        orm_mode = True

class CountryStats(CountryStatsBase):
    pass

class CountryStatsCreate(CountryStatsBase):
    pass