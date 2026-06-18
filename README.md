# API de Gerenciamento de Tarefas

Uma API RESTful simples desenvolvida com FastAPI para gerenciar tarefas. Este projeto permite realizar operações CRUD (Criar, Ler, Atualizar, Excluir) em tarefas, utilizando SQLite como banco de dados.

## Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **FastAPI**: Framework web moderno e rápido para construir APIs com Python.
*   **Pydantic**: Biblioteca para validação de dados e configurações, utilizada para definir os modelos de requisição e resposta da API.
*   **SQLite**: Banco de dados leve e embutido, ideal para projetos pequenos e prototipagem.

## Funcionalidades

A API oferece os seguintes endpoints para gerenciamento de tarefas:

*   `POST /tasks/`: Cria uma nova tarefa.
*   `GET /tasks/`: Lista todas as tarefas existentes.
*   `GET /tasks/{task_id}`: Retorna os detalhes de uma tarefa específica pelo seu ID.
*   `PUT /tasks/{task_id}`: Atualiza uma tarefa existente pelo seu ID.
*   `DELETE /tasks/{task_id}`: Exclui uma tarefa pelo seu ID.

## Como Executar o Projeto

Siga os passos abaixo para configurar e executar a API localmente:

1.  **Clone o repositório** (se ainda não o fez):

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd api_gerenciamento_tarefas
    ```

2.  **Crie e ative um ambiente virtual** (recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: .\venv\Scripts\activate
    ```

3.  **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação FastAPI**:

    ```bash
    uvicorn main:app --reload
    ```

    A API estará disponível em `http://127.0.0.1:8000`.

5.  **Acesse a documentação interativa (Swagger UI)**:

    Você pode testar os endpoints da API diretamente no seu navegador, acessando:

    `http://127.0.0.1:8000/docs`

    Ou a documentação alternativa (ReDoc) em:

    `http://127.0.0.1:8000/redoc`
