from sqlalchemy.orm import Session
from .models import Exercicio
from .schemas import ExercicioCriar

# Função para obter um exercício pelo ID
def obter_exercicio_por_id(db: Session, exercicio_id: int):
    return db.query(Exercicio).filter(Exercicio.id == exercicio_id).first()

# Função para criar um exercício
def criar_exercicio(db: Session, exercicio: ExercicioCriar):
    db_exercicio = Exercicio(**exercicio.dict())
    db.add(db_exercicio)
    db.commit()
    db.refresh(db_exercicio)
    return db_exercicio

# Função para criar exercícios 
def criar_exercicios_iniciais(db: Session):
    exercicios = [
          {"nome": "flexao", "url_video": "http......", "descricao": "exercicio flexão"},
        {"nome": "flexao", "url_video": "http......", "descricao": "exercicio flexão"},
        {"nome": "flexao", "url_video": "http......", "descricao": "exercicio flexão"},
        {"nome": "flexao", "url_video": "http......", "descricao": "exercicio flexão"},
        {"nome": "flexao", "url_video": "http......", "descricao": "exercicio flexão"},
        {"nome": "flexao", "url_video": "http......", "descricao": "exercicio flexão"},
    
    ]
    for exercicio in exercicios:
        db_exercicio = Exercicio(**exercicio)
        db.add(db_exercicio)
    db.commit()
    return {"mensagem": "Exercícios criados com sucesso"}

# Função get pelo ID
def obter_exercicio(db: Session, exercicio_id: int):
    return obter_exercicio_por_id(db, exercicio_id)

# Função get
def obter_exercicios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Exercicio).offset(skip).limit(limit).all()

# Função put
def atualizar_exercicio(db: Session, exercicio_id: int, dados_exercicio: ExercicioCriar):
    db_exercicio = obter_exercicio_por_id(db, exercicio_id)
    if db_exercicio:
        db_exercicio.nome = dados_exercicio.nome
        db_exercicio.url_video = dados_exercicio.url_video
        db_exercicio.descricao = dados_exercicio.descricao
        db.commit()
        db.refresh(db_exercicio)
        return db_exercicio
    return None

# Função delete


def deletar_exercicio(db: Session, exercicio_id: int):
    db_exercicio = obter_exercicio_por_id(db, exercicio_id)
    if db_exercicio:
        db.delete(db_exercicio)
        db.commit()
        return {"mensagem": "Exercício deletado com sucesso"}
    return {"mensagem": "Exercício não encontrado"}
