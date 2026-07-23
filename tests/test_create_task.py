"""Testes para o endpoint de criação de tarefas."""


class TestCreateTask:
    """Testes de criação de tarefas."""

    def test_create_task_success(self, client):
        """Deve criar uma tarefa com sucesso e retornar 201."""
        payload = {
            "title": "Estudar Python",
            "description": "Estudar conceitos avançados de Python",
            "completed": False,
        }
        response = client.post("/tasks/", json=payload)

        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Estudar Python"
        assert data["description"] == "Estudar conceitos avançados de Python"
        assert data["completed"] is False

    def test_create_task_minimal(self, client):
        """Deve criar uma tarefa apenas com o título obrigatório."""
        payload = {"title": "Tarefa mínima"}
        response = client.post("/tasks/", json=payload)

        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Tarefa mínima"
        assert data["description"] is None
        assert data["completed"] is False

    def test_create_task_with_completion(self, client):
        """Deve criar uma tarefa já marcada como concluída."""
        payload = {
            "title": "Tarefa concluída",
            "description": "Esta tarefa já foi finalizada",
            "completed": True,
        }
        response = client.post("/tasks/", json=payload)

        assert response.status_code == 201
        data = response.json()
        assert data["completed"] is True

    def test_create_task_invalid_empty_title(self, client):
        """Deve retornar 422 quando o título está vazio."""
        payload = {"title": "", "description": "Descrição qualquer"}
        response = client.post("/tasks/", json=payload)

        assert response.status_code == 422

    def test_create_task_invalid_missing_title(self, client):
        """Deve retornar 422 quando o título está ausente."""
        payload = {"description": "Sem título"}
        response = client.post("/tasks/", json=payload)

        assert response.status_code == 422

    def test_create_task_invalid_wrong_type(self, client):
        """Deve retornar 422 quando o tipo do campo está errado."""
        payload = {"title": 123}
        response = client.post("/tasks/", json=payload)

        assert response.status_code == 422
