# 🚀 API de Gerenciamento de Tarefas (FastAPI)



Uma API RESTful moderna e robusta desenvolvida com **FastAPI** para o gerenciamento eficiente de tarefas. Este projeto demonstra boas práticas de desenvolvimento, incluindo validação de dados com Pydantic e persistência com SQLite.



## 📑 Documentação da API

A API possui documentação interativa automática. Após rodar o projeto localmente, acesse:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Recomendado para testes)
- 
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- 


## 🛠️ Tecnologias Utilizadas

- **Python 3.9+**
- 
- **FastAPI**: Framework de alta performance.
- 
- **Pydantic**: Validação de esquemas de dados.
- 
- **SQLite**: Banco de dados relacional leve.
- 
- **Uvicorn**: Servidor ASGI para produção.
- 


## 🚀 Funcionalidades (Endpoints)

| Método | Endpoint | Descrição |

| --- | --- | --- |

| `POST` | `/tasks/` | Cria uma nova tarefa |

| `GET` | `/tasks/` | Lista todas as tarefas |

| `GET` | `/tasks/{id}` | Obtém detalhes de uma tarefa específica |

| `PUT` | `/tasks/{id}` | Atualiza uma tarefa existente |

| `DELETE` | `/tasks/{id}` | Remove uma tarefa do sistema |



## 🔧 Como Executar

1. **Clone o repositório**:
2. 
```bash

git clone https://github.com/GustavoHCGit/api-gerenciamento-tarefas.git

cd api-gerenciamento-tarefas

```



2. **Configure o ambiente**:
3. 
```bash

python -m venv venv

source venv/bin/activate  # Windows: .\venv\Scripts\activate

pip install -r requirements.txt

```



3. **Inicie o servidor**:
4. 
```bash

uvicorn main:app --reload

```



---

Desenvolvido por [Gustavo Henrique Constante Neto](https://github.com/GustavoHCGit)











