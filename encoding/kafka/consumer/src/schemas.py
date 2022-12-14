from pydantic import BaseModel


class LanguageBase(BaseModel):
    language: str

    class Config:
        orm_mode = True

class LanguageCreate(LanguageBase):
    pass
