from .. import connection
from sqlalchemy import Column, Integer, String, Text, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship


class BasicAttribute(connection.Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class City(BasicAttribute):
    __tablename__ = "city"

    positions = relationship("Position", back_populates="city")


class Company(BasicAttribute):
    __tablename__ = "company"

    positions = relationship("Position", back_populates="company")


class User(connection.Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    password = Column(String)

    resumes = relationship("Resume", back_populates="user")


class Hobby(connection.Base):
    __tablename__ = "hobby"

    hobbyId = Column(Integer, ForeignKey(
        "hobbycategory.id", ondelete="CASCADE"), primary_key=True)
    resumeId = Column(Integer, ForeignKey(
        "resume.id", ondelete="CASCADE"), primary_key=True)


class HobbyCategory(BasicAttribute):
    __tablename__ = "hobbycategory"

    hobbies = relationship(
        'Resume', secondary="hobby")


class Position(BasicAttribute):
    __tablename__ = "position"

    cityId = Column(Integer, ForeignKey(
        "city.id", ondelete="CASCADE"))
    companyId = Column(Integer, ForeignKey(
        "company.id", ondelete="CASCADE"))
    resumeId = Column(Integer, ForeignKey("resume.id", ondelete="CASCADE"))

    resume = relationship("Resume", back_populates="positions")
    company = relationship("Company", back_populates="positions")
    city = relationship("City", back_populates="positions")


class Resume(connection.Base):
    __tablename__ = "resume"

    id = Column(Integer, primary_key=True, index=True)
    summary = Column(Text)
    userId = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))

    user = relationship("User", back_populates="resumes")
    hobbies = relationship(
        'HobbyCategory', secondary="hobby")
    positions = relationship('Position', back_populates="resume")
