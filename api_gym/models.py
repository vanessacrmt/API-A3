from sqlalchemy import Column, Integer, String
from .database import Base

class Exercicio(Base):
    _tablename_ = "exercicios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    url_video = Column(String)
    descricao = Column(String)

class User(Base):
    _tablename_ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
