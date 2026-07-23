"""Testes para os endpoints raiz e health check."""


class TestRootEndpoints:
    """Testes dos endpoints auxiliares."""

    def test_root_endpoint(self, client):
        """Deve retornar informações da API no endpoint raiz."""
        response = client.get("/")

        assert response.status_code == 200
        data = response.json()
        assert "mensagem" in data
        assert "documentacao" in data
        assert data["versao"] == "1.0.0"

    def test_health_check(self, client):
        """Deve retornar status healthy."""
        response = client.get("/health")

        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
