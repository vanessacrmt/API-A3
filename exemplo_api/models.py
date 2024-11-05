from sqlalchemy import Column, Integer, String
from .database import Base

class Exercicio(Base):
    __tablename__ = "exercicios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    url_video = Column(String)
    descricao = Column(String)