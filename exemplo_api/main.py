from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from exemplo_api.database import SessionLocal, engine
from exemplo_api.models import Base
from exemplo_api.schemas import ExercicioCriar, ExercicioResposta
from exemplo_api.exercicios import (
    criar_exercicios_iniciais,
    criar_exercicio,
    obter_exercicio,
    obter_exercicios,
    atualizar_exercicio,
    deletar_exercicio
)

# Inicialização do banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência para obter a sessão do banco de dados
def obter_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def inicializacao():
    db = SessionLocal()
    exercicios = [
        
        {"nome": "flexao", "url_video": "http......", "descricao": "exercicio flexão"},
        {"nome": "flexao", "url_video": "http......", "descricao": "exercicio flexão"},
        {"nome": "flexao", "url_video": "http......", "descricao": "exercicio flexão"},
        {"nome": "flexao", "url_video": "http......", "descricao": "exercicio flexão"},
        {"nome": "flexao", "url_video": "http......", "descricao": "exercicio flexão"},
       
    ]
    criar_exercicios_iniciais(db, exercicios)
    db.close()

# Endpoints da API
@app.post("/exercicios/", response_model=ExercicioResposta)
def criar_exercicio_endpoint(exercicio: ExercicioCriar, db: Session = Depends(obter_db)):
    return criar_exercicio(db, exercicio)

@app.get("/exercicios/{exercicio_id}", response_model=ExercicioResposta)
def obter_exercicio_endpoint(exercicio_id: int, db: Session = Depends(obter_db)):
    db_exercicio = obter_exercicio(db, exercicio_id)
    if db_exercicio is None:
        raise HTTPException(status_code=404, detail="Exercício não encontrado")
    return db_exercicio

@app.get("/exercicios/", response_model=list[ExercicioResposta])
def obter_exercicios_endpoint(skip: int = 0, limit: int = 10, db: Session = Depends(obter_db)):
    exercicios = obter_exercicios(db, skip=skip, limit=limit)
    return exercicios

@app.put("/exercicios/{exercicio_id}", response_model=ExercicioResposta)
def atualizar_exercicio_endpoint(exercicio_id: int, exercicio: ExercicioCriar, db: Session = Depends(obter_db)):
    db_exercicio = atualizar_exercicio(db, exercicio_id, exercicio)
    if db_exercicio is None:
        raise HTTPException(status_code=404, detail="Exercício não encontrado")
    return db_exercicio

@app.delete("/exercicios/{exercicio_id}", response_model=ExercicioResposta)
def deletar_exercicio_endpoint(exercicio_id: int, db: Session = Depends(obter_db)):
    db_exercicio = deletar_exercicio(db, exercicio_id)
    if db_exercicio is None:
        raise HTTPException(status_code=404, detail="Exercício não encontrado")
    return db_exercicio
