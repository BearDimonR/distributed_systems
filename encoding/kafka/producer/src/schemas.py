from pydantic import BaseModel


class LanguageBase(BaseModel):
    language: str

    class Config:
        orm_mode = True


class Language(LanguageBase):
    language_id: int


class LanguageCreate(LanguageBase):
    pass
