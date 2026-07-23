"""Schemas Pydantic para validação de entrada e saída de dados de tarefas."""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    """Schema para criação de uma nova tarefa."""

    title: str = Field(..., min_length=1, max_length=200, description="Título da tarefa")
    description: Optional[str] = Field(
        None, max_length=1000, description="Descrição opcional da tarefa"
    )
    completed: bool = Field(False, description="Indica se a tarefa foi concluída")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Estudar FastAPI",
                "description": "Ler a documentação oficial e criar um CRUD",
                "completed": False,
            }
        }
    )


class TaskUpdate(BaseModel):
    """Schema para atualização de uma tarefa existente."""

    title: str = Field(..., min_length=1, max_length=200, description="Título da tarefa")
    description: Optional[str] = Field(
        None, max_length=1000, description="Descrição opcional da tarefa"
    )
    completed: bool = Field(False, description="Indica se a tarefa foi concluída")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Estudar FastAPI atualizado",
                "description": "Ler a documentação oficial e criar um CRUD",
                "completed": True,
            }
        }
    )


class TaskResponse(BaseModel):
    """Schema de resposta para uma tarefa."""

    id: int
    title: str
    description: Optional[str] = None
    completed: bool

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "Estudar FastAPI",
                "description": "Ler a documentação oficial",
                "completed": False,
            }
        },
    )
