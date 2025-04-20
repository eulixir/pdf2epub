from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(prefix="/health", tags=["health"])

class HealthResponse(BaseModel):
    status: str
    version: str = "1.0.0"

@router.get(
    "/",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health check endpoint",
    description="Returns the current health status of the service"
)
async def health_check() -> HealthResponse:
    """
    Health check endpoint that returns the current status of the service.
    """
    return HealthResponse(status="healthy")
