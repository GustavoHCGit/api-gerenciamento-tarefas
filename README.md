# API de Gerenciamento de Tarefas

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Testes](https://img.shields.io/badge/Testes-21%20passando-green.svg)](tests/)

Uma API RESTful moderna para gerenciamento de tarefas, desenvolvida com **FastAPI** e **Python**. Este projeto demonstra boas práticas de desenvolvimento backend, incluindo arquitetura em camadas, validação de dados com Pydantic, persistência com SQLite, testes automatizados e tratamento robusto de erros.

## Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|---|---|---|
| Python | 3.9+ | Linguagem de programação principal |
| FastAPI | 0.111.0 | Framework web de alta performance |
| Pydantic | 2.7.1 | Validação e serialização de dados |
| Uvicorn | 0.29.0 | Servidor ASGI para produção |
| SQLite | Embutido | Banco de dados relacional leve |
| pytest | 8.2.1 | Framework de testes automatizados |
| httpx | 0.27.0 | Cliente HTTP para testes da API |

## Funcionalidades

A API implementa um CRUD completo para gerenciamento de tarefas com as seguintes operações:

| Método | Endpoint | Descrição | Status Code |
|---|---|---|---|
| `POST` | `/tasks/` | Cria uma nova tarefa | 201 Created |
| `GET` | `/tasks/` | Lista todas as tarefas | 200 OK |
| `GET` | `/tasks/{id}` | Obtém detalhes de uma tarefa | 200 OK |
| `PUT` | `/tasks/{id}` | Atualiza uma tarefa existente | 200 OK |
| `DELETE` | `/tasks/{id}` | Remove uma tarefa | 204 No Content |

Endpoints auxiliares:

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/` | Informações da API |
| `GET` | `/health` | Verificação de saúde |
| `GET` | `/docs` | Documentação interativa (Swagger UI) |
| `GET` | `/redoc` | Documentação alternativa (ReDoc) |

## Estrutura do Projeto

```
api-gerenciamento-tarefas/
├── app/
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py          # Configurações e variáveis de ambiente
│   ├── models/
│   │   ├── __init__.py
│   │   └── task_model.py        # Operações CRUD no banco de dados
│   ├── routes/
│   │   ├── __init__.py
│   │   └── tasks.py             # Rotas/Endpoints da API
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── task_schemas.py      # Schemas Pydantic (validação)
│   ├── tests/
│   │   └── __init__.py
│   ├── __init__.py
│   └── database.py              # Gerenciamento de conexão com o banco
├── tests/
│   ├── conftest.py              # Configuração e fixtures dos testes
│   ├── test_create_task.py      # Testes de criação
│   ├── test_read_tasks.py       # Testes de leitura
│   ├── test_update_task.py      # Testes de atualização
│   ├── test_delete_task.py      # Testes de remoção
│   └── test_root.py             # Testes dos endpoints auxiliares
├── main.py                      # Ponto de entrada da aplicação
├── requirements.txt             # Dependências do projeto
├── pytest.ini                   # Configuração do pytest
├── .env.example                 # Modelo de variáveis de ambiente
├── .gitignore                   # Arquivos ignorados pelo Git
└── README.md                    # Documentação do projeto
```

## Arquitetura

O projeto segue o padrão de **arquitetura em camadas**, separando responsabilidades para facilitar manutenção e escalabilidade:

- **Config (`app/config/`)**: Gerencia variáveis de ambiente e configurações globais da aplicação.
- **Database (`app/database.py`)**: Centraliza a criação e gerenciamento de conexões com o banco de dados.
- **Schemas (`app/schemas/`)**: Define os modelos de validação de dados de entrada e saída usando Pydantic.
- **Models (`app/models/`)**: Implementa a camada de acesso a dados (CRUD operations) de forma isolada.
- **Routes (`app/routes/`)**: Define os endpoints HTTP e coordena a lógica entre schemas e models.

## Como Executar

### 1. Pré-requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)

### 2. Instalação

```bash
# Clonar o repositório
git clone https://github.com/GustavoHCGit/api-gerenciamento-tarefas.git
cd api-gerenciamento-tarefas

# Criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate          # Linux/macOS
# venv\Scripts\activate           # Windows

# Instalar dependências
pip install -r requirements.txt
```

### 3. Configuração de Variáveis de Ambiente

```bash
# Copiar o modelo de configuração
cp .env.example .env

# Editar o arquivo .env conforme necessário
# Valores padrão já funcionam para desenvolvimento local
```

### 4. Iniciar o Servidor

```bash
uvicorn main:app --reload
```

A API ficará disponível em `http://127.0.0.1:8000`.

## Exemplos de Uso

### Criar uma Tarefa

```bash
curl -X POST http://localhost:8000/tasks/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudar FastAPI",
    "description": "Criar uma API RESTful completa",
    "completed": false
  }'
```

**Resposta:**
```json
{
  "id": 1,
  "title": "Estudar FastAPI",
  "description": "Criar uma API RESTful completa",
  "completed": false
}
```

### Listar Todas as Tarefas

```bash
curl http://localhost:8000/tasks/
```

**Resposta:**
```json
[
  {
    "id": 1,
    "title": "Estudar FastAPI",
    "description": "Criar uma API RESTful completa",
    "completed": false
  }
]
```

### Atualizar uma Tarefa

```bash
curl -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Estudar FastAPI",
    "description": "API completa com testes e boas práticas",
    "completed": true
  }'
```

### Remover uma Tarefa

```bash
curl -X DELETE http://localhost:8000/tasks/1
```

## Testes Automatizados

O projeto inclui 21 testes automatizados que cobrem todos os endpoints e cenários de erro. Para executá-los:

```bash
# Instalar dependências de teste (já inclusas no requirements.txt)
pip install -r requirements.txt

# Executar todos os testes
python -m pytest tests/ -v

# Executar com cobertura detalhada
python -m pytest tests/ -v --tb=long
```

Os testes cobrem os seguintes cenários:

| Arquivo | Casos Testados |
|---|---|
| `test_create_task.py` | Criação com sucesso, dados mínimos, conclusão, validação de erro |
| `test_read_tasks.py` | Lista vazia, listagem com itens, busca por ID, não encontrado, ID inválido |
| `test_update_task.py` | Atualização com sucesso, não encontrado, ID inválido, dados inválidos |
| `test_delete_task.py` | Remoção com sucesso, não encontrado, ID inválido, remoção da lista |
| `test_root.py` | Endpoint raiz, health check |

## Tratamento de Erros

A API retorna respostas de erro padronizadas com códigos HTTP adequados:

| Código | Cenário | Exemplo de Resposta |
|---|---|---|
| `404` | Tarefa não encontrada | `{"detail": "Tarefa com ID 999 não encontrada."}` |
| `422` | Dados de entrada inválidos | `{"detail": "Erro de validação nos dados enviados.", "erros": [...]}` |
| `422` | ID inválido (<=0) | `{"detail": "O ID da tarefa deve ser um número positivo."}` |
| `500` | Erro interno do servidor | `{"detail": "Ocorreu um erro interno no servidor."}` |

## Documentação Interativa

Após iniciar o servidor, acesse a documentação automática gerada pelo FastAPI:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

A documentação inclui exemplos de schemas, modelos de dados e permite testar os endpoints diretamente no navegador.

## Boas Práticas Aplicadas

- **Separação de responsabilidades**: Código organizado em camadas (rotas, modelos, schemas, configuração).
- **Validação de dados**: Uso de Pydantic para validar entradas com regras claras.
- **Tratamento de erros**: Respostas HTTP padronizadas com mensagens descritivas.
- **Variáveis de ambiente**: Configurações sensíveis centralizadas no arquivo `.env`.
- **Testes automatizados**: Cobertura completa dos endpoints com pytest e TestClient.
- **Documentação automática**: Swagger UI e ReDoc gerados automaticamente pelo FastAPI.

---

Desenvolvido por [Gustavo Henrique Constante Neto](https://github.com/GustavoHCGit)
