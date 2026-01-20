from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Optional
import logging, time
from functools import wraps

from database import get_db
from models import ClientModel
from domain import Client

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                    handlers=[stream_handler])

logger = logging.getLogger("011h")


def timer(func):
    """Decorador que calcula el tiempo de ejecución de una función"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        execution_time = (end_time - start_time) / 1e6  # Convertir a milisegundos
        logger.info(f"Función '{func.__name__}' ejecutada en {execution_time:.3f} ms")
        return result
    return wrapper


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/clients", response_model=List[Client])
@timer
def get_all_clients(email: Optional[str] = None, db: Session = Depends(get_db)):
    """Obtener todos los clientes con sus direcciones, opcionalmente filtrados por email"""
    query = select(ClientModel)
    
    if email:
        query = query.where(ClientModel.email.ilike(f"%{email}%"))
    
    result = db.execute(query)
    clients_models = result.scalars().unique().all()
    
    clients_domain = [client_model.to_domain() for client_model in clients_models]
    
    return clients_domain