"""Ponto de entrada da aplicação FastAPI."""
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.config.settings import settings
from app.database import init_db
from app.routes.tasks import router as tasks_router


def create_application() -> FastAPI:
    """Cria e configura a instância principal da aplicação FastAPI."""
    app = FastAPI(
        title=settings.APP_NAME,
        description=(
            "API RESTful para gerenciamento de tarefas. "
            "Permite criar, listar, atualizar e remover tarefas de forma eficiente."
        ),
        version="1.0.0",
    )

    # Registrar rotas
    app.include_router(tasks_router)

    # Inicializar banco de dados na startup
    @app.on_event("startup")
    def on_startup():
        init_db()

    # Tratamento global de erros de validação
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        errors = []
        for error in exc.errors():
            loc = " -> ".join(str(loc) for loc in error["loc"])
            errors.append(
                {
                    "campo": loc.replace("body -> ", ""),
                    "mensagem": error["msg"],
                    "tipo": error["type"],
                }
            )
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "detail": "Erro de validação nos dados enviados.",
                "erros": errors,
            },
        )

    # Tratamento global de erros genéricos
    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "detail": "Ocorreu um erro interno no servidor.",
                "mensagem": "Por favor, tente novamente mais tarde.",
            },
        )

    # Endpoints auxiliares
    @app.get("/", tags=["Geral"])
    def root():
        """Endpoint raiz com informações da API."""
        return {
            "mensagem": f"Bem-vindo à {settings.APP_NAME}",
            "documentacao": "/docs",
            "versao": "1.0.0",
        }

    @app.get("/health", tags=["Geral"])
    def health_check():
        """Endpoint de verificação de saúde da API."""
        return {"status": "healthy"}

    return app


# Instância global para execução direta com uvicorn
app = create_application()
