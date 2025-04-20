from fastapi import APIRouter, status
from pydantic import BaseModel
from app.domain.services import convert_pdf
router = APIRouter(prefix="/convert", tags=["convert"])

class ConvertRequest(BaseModel):
    file_path: str
    output_format: str = "epub"

class ConvertResponse(BaseModel):
    file: bytes

@router.post(
    "/",
    response_model=ConvertResponse,
    status_code=status.HTTP_200_OK,
    summary="Convert file endpoint",
    description="Converts a file from one format to another"
)
async def convert_file(request: ConvertRequest) -> ConvertResponse:    
    file = await convert_pdf(request.file_path, request.output_format, request.title, request.author)
    
    return ConvertResponse(
        file=file,
    )

