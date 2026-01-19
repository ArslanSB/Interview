from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
import logging, time

from database import get_db
from models import ClientModel
from domain import Client

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s',
                    handlers=[stream_handler])

logger = logging.getLogger("011h")

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/clients", response_model=List[Client])
def get_all_clients(db: Session = Depends(get_db)):
    """Obtener todos los clientes con sus direcciones"""
    st = time.perf_counter_ns()
    query = select(ClientModel)
    
    result = db.execute(query)
    clients_models = result.scalars().unique().all()
    
    clients_domain = [client_model.to_domain() for client_model in clients_models]
    
    et = time.perf_counter_ns()
    logger.info(f"Tiempo de consulta: {(et - st) / 1e6} ms")
    return clients_domain