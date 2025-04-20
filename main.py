from fastapi import FastAPI
from app.infra.controllers.healthcheck import router as health_router

app = FastAPI(
    title="PDF to EPUB Converter",
    description="A service to convert PDF files to EPUB format",
    version="1.0.0"
)

app.include_router(health_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    ) 