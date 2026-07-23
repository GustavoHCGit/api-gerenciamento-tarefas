"""Testes para os endpoints de listagem e leitura de tarefas."""


class TestReadTasks:
    """Testes de listagem e leitura de tarefas."""

    def test_list_tasks_empty(self, client):
        """Deve retornar lista vazia quando não há tarefas."""
        response = client.get("/tasks/")
        assert response.status_code == 200
        assert response.json() == []

    def test_list_tasks_with_items(self, client):
        """Deve retornar todas as tarefas cadastradas."""
        # Criar duas tarefas
        client.post("/tasks/", json={"title": "Tarefa A"})
        client.post("/tasks/", json={"title": "Tarefa B", "description": "Detalhes"})

        response = client.get("/tasks/")

        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2
        titles = [t["title"] for t in data]
        assert "Tarefa A" in titles
        assert "Tarefa B" in titles

    def test_read_task_by_id(self, client):
        """Deve retornar uma tarefa específica pelo ID."""
        create_resp = client.post("/tasks/", json={"title": "Buscar esta tarefa"})
        task_id = create_resp.json()["id"]

        response = client.get(f"/tasks/{task_id}")

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == task_id
        assert data["title"] == "Buscar esta tarefa"

    def test_read_task_not_found(self, client):
        """Deve retornar 404 quando a tarefa não existe."""
        response = client.get("/tasks/99999")

        assert response.status_code == 404
        assert "não encontrada" in response.json()["detail"]

    def test_read_task_invalid_id(self, client):
        """Deve retornar 422 para ID inválido (número negativo ou zero)."""
        response = client.get("/tasks/0")

        assert response.status_code == 422
