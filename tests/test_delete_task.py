"""Testes para o endpoint de remoção de tarefas."""


class TestDeleteTask:
    """Testes de remoção de tarefas."""

    def test_delete_task_success(self, client):
        """Deve remover uma tarefa com sucesso e retornar 204."""
        create_resp = client.post("/tasks/", json={"title": "Tarefa para deletar"})
        task_id = create_resp.json()["id"]

        response = client.delete(f"/tasks/{task_id}")

        assert response.status_code == 204

        # Verificar que a tarefa não existe mais
        get_resp = client.get(f"/tasks/{task_id}")
        assert get_resp.status_code == 404

    def test_delete_task_not_found(self, client):
        """Deve retornar 404 ao tentar deletar tarefa inexistente."""
        response = client.delete("/tasks/99999")

        assert response.status_code == 404
        assert "não encontrada" in response.json()["detail"]

    def test_delete_task_invalid_id(self, client):
        """Deve retornar 422 para ID inválido."""
        response = client.delete("/tasks/0")

        assert response.status_code == 422

    def test_delete_task_removes_from_list(self, client):
        """Deve deletar a tarefa e ela não deve aparecer mais na lista."""
        create_resp = client.post("/tasks/", json={"title": "Única tarefa"})
        task_id = create_resp.json()["id"]

        # Confirmar que existe
        all_tasks = client.get("/tasks/").json()
        task_ids_before = [t["id"] for t in all_tasks]
        assert task_id in task_ids_before

        # Deletar
        client.delete(f"/tasks/{task_id}")

        # Confirmar que não aparece mais
        all_tasks_after = client.get("/tasks/").json()
        task_ids_after = [t["id"] for t in all_tasks_after]
        assert task_id not in task_ids_after
