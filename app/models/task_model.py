"""Operações CRUD no banco de dados para tarefas."""
import sqlite3
from typing import List, Optional

from app.database import get_db_connection
from app.schemas.task_schemas import TaskCreate, TaskUpdate


def create_task(task_data: TaskCreate) -> dict:
    """Cria uma nova tarefa no banco de dados."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)",
            (task_data.title, task_data.description, task_data.completed),
        )
        conn.commit()
        task_id = cursor.lastrowid

    return {
        "id": task_id,
        "title": task_data.title,
        "description": task_data.description,
        "completed": task_data.completed,
    }


def get_all_tasks() -> List[dict]:
    """Retorna todas as tarefas do banco de dados."""
    with get_db_connection() as conn:
        rows = conn.execute("SELECT * FROM tasks ORDER BY id DESC").fetchall()
    return [dict(row) for row in rows]


def get_task_by_id(task_id: int) -> Optional[dict]:
    """Retorna uma tarefa pelo seu ID, ou None se não encontrada."""
    with get_db_connection() as conn:
        row = conn.execute(
            "SELECT * FROM tasks WHERE id = ?", (task_id,)
        ).fetchone()
    if row is None:
        return None
    return dict(row)


def update_task(task_id: int, task_data: TaskUpdate) -> Optional[dict]:
    """Atualiza uma tarefa existente. Retorna None se a tarefa não existir."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?",
            (task_data.title, task_data.description, task_data.completed, task_id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            return None

    return {
        "id": task_id,
        "title": task_data.title,
        "description": task_data.description,
        "completed": task_data.completed,
    }


def delete_task(task_id: int) -> bool:
    """Remove uma tarefa do banco de dados. Retorna False se não encontrada."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        return cursor.rowcount > 0
