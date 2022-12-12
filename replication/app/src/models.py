from . import connection
from sqlalchemy import Column, Integer, String


class Language(connection.Base):
    __tablename__ = "languages"

    language_id = Column(Integer, primary_key=True, index=True)
    language = Column(String, index=True)
