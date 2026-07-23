"""Rotas da API para gerenciamento de tarefas."""
from typing import List

from fastapi import APIRouter, HTTPException, status

from app.models.task_model import (
    create_task,
    delete_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
)
from app.schemas.task_schemas import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["Tarefas"])


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_new_task(task: TaskCreate):
    """Cria uma nova tarefa no sistema."""
    try:
        return create_task(task)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno ao criar a tarefa.",
        )


@router.get("/", response_model=List[TaskResponse])
def list_tasks():
    """Lista todas as tarefas cadastradas."""
    try:
        return get_all_tasks()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno ao listar as tarefas.",
        )


@router.get("/{task_id}", response_model=TaskResponse)
def read_task(task_id: int):
    """Retorna os detalhes de uma tarefa específica pelo seu ID."""
    if task_id < 1:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="O ID da tarefa deve ser um número positivo.",
        )

    task = get_task_by_id(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada.",
        )
    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_existing_task(task_id: int, task: TaskUpdate):
    """Atualiza uma tarefa existente pelo seu ID."""
    if task_id < 1:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="O ID da tarefa deve ser um número positivo.",
        )

    result = update_task(task_id, task)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada.",
        )
    return result


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_task(task_id: int):
    """Remove uma tarefa do sistema pelo seu ID."""
    if task_id < 1:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="O ID da tarefa deve ser um número positivo.",
        )

    deleted = delete_task(task_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada.",
        )
