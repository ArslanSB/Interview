from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session
from typing import Generator
import os

# Database URL - usa psycopg2 para PostgreSQL síncrono
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/app_db"
)

# Crear el motor síncrono
engine = create_engine(
    DATABASE_URL,
    # echo=True,
    pool_pre_ping=True,
)

# Crear el session maker síncrono
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


# Base para los modelos
class Base(DeclarativeBase):
    pass


# Dependency para obtener la sesión de base de datos
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


# Función para cerrar la conexión
def close_db():
    engine.dispose()
