"""Configuração compartilhada dos testes com fixtures isoladas."""
import os
import sqlite3
import sys
import tempfile

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def isolated_db():
    """Fixture autouse que garante um banco de dados limpo para cada teste."""
    temp_file = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    db_path = temp_file.name
    temp_file.close()

    # Sobrescrever variável de ambiente ANTES de qualquer import do projeto
    os.environ["DATABASE_URL"] = f"sqlite:///{db_path}"

    # Remover módulos do projeto do cache para garantir recarga limpa
    modules_to_remove = [
        k for k in sys.modules.keys()
        if k.startswith("app") or k.startswith("main")
    ]
    for mod in modules_to_remove:
        del sys.modules[mod]

    # Criar a tabela
    conn = sqlite3.connect(db_path)
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
    conn.close()

    yield db_path

    # Limpeza
    os.environ.pop("DATABASE_URL", None)

    if os.path.exists(db_path):
        try:
            os.unlink(db_path)
        except OSError:
            pass

    # Remover módulos novamente
    modules_to_remove = [
        k for k in sys.modules.keys()
        if k.startswith("app") or k.startswith("main")
    ]
    for mod in modules_to_remove:
        del sys.modules[mod]


@pytest.fixture
def client(isolated_db):
    """Cria um cliente de teste da aplicação."""
    from main import create_application

    app = create_application()
    with TestClient(app) as c:
        yield c
