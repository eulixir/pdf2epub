from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.infra.controllers import health_router, convert_router

app = FastAPI(
    title="PDF to EPUB Converter",
    description="A service to convert PDF files to EPUB format",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(health_router)
app.include_router(convert_router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="PDF to EPUB Converter",
        version="1.0.0",
        description="A service to convert PDF files to EPUB format",
        routes=app.routes,
    )
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    ) 