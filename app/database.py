"""Gerenciamento de conexão com o banco de dados SQLite."""
import sqlite3
from contextlib import contextmanager

from app.config.settings import settings


def get_db_path() -> str:
    """Retorna o caminho do banco de dados a partir da DATABASE_URL."""
    return settings.DATABASE_URL.replace("sqlite:///", "")


@contextmanager
def get_db_connection():
    """Context manager que fornece uma conexão com o banco de dados."""
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
    finally:
        conn.close()


def init_db() -> None:
    """Inicializa as tabelas do banco de dados, se ainda não existirem."""
    with get_db_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN NOT NULL DEFAULT FALSE
            )
            """
        )
        conn.commit()
