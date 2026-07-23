"""Testes para o endpoint de atualização de tarefas."""


class TestUpdateTask:
    """Testes de atualização de tarefas."""

    def test_update_task_success(self, client):
        """Deve atualizar uma tarefa existente com sucesso."""
        # Criar tarefa
        create_resp = client.post("/tasks/", json={"title": "Título original"})
        task_id = create_resp.json()["id"]

        # Atualizar
        payload = {
            "title": "Título atualizado",
            "description": "Nova descrição",
            "completed": True,
        }
        response = client.put(f"/tasks/{task_id}", json=payload)

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == task_id
        assert data["title"] == "Título atualizado"
        assert data["description"] == "Nova descrição"
        assert data["completed"] is True

    def test_update_task_not_found(self, client):
        """Deve retornar 404 ao tentar atualizar tarefa inexistente."""
        payload = {"title": "Qualquer título"}
        response = client.put("/tasks/99999", json=payload)

        assert response.status_code == 404
        assert "não encontrada" in response.json()["detail"]

    def test_update_task_invalid_id(self, client):
        """Deve retornar 422 para ID inválido."""
        payload = {"title": "Título"}
        response = client.put("/tasks/-1", json=payload)

        assert response.status_code == 422

    def test_update_task_invalid_data(self, client):
        """Deve retornar 422 com dados inválidos."""
        create_resp = client.post("/tasks/", json={"title": "Tarefa"})
        task_id = create_resp.json()["id"]

        payload = {"title": ""}  # Título vazio
        response = client.put(f"/tasks/{task_id}", json=payload)

        assert response.status_code == 422
