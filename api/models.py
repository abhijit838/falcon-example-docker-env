from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import Column, Integer, String

# Base declarative model to map child models to respective tables
Base = declarative_base()


class Person(Base):
    """
    Person model, represents table columns and generic request-response body parameters
    @__tablename__:string - Name of the table to be mapped to the model:Person
    @id:int - id of record - primary key
    @name:str - Name of the person
    @age:int - Age of the person
    """
    __tablename__ = 'person'

    def __init__(self, id=None, name=None, age=None):
        self.id = id
        self.name = name
        self.age = age

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)