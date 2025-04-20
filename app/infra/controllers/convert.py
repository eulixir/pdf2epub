from fastapi import APIRouter, status, File, Form, UploadFile
from fastapi.responses import FileResponse
from app.domain.services import convert_pdf
import tempfile
import os
import asyncio

router = APIRouter(prefix="/convert", tags=["convert"])


@router.post(
    "/",
    response_class=FileResponse,
    status_code=status.HTTP_200_OK,
    summary="Convert PDF to EPUB",
    description="Converts a PDF file to EPUB format with metadata",
    responses={
        200: {
            "description": "Successful conversion",
            "content": {
                "application/epub+zip": {
                    "schema": {"type": "string", "format": "binary"}
                }
            },
        }
    },
)
async def convert_file(
    file: UploadFile = File(..., description="The PDF file to convert"),
    title: str = Form(..., description="Title of the document"),
    author: str = Form(..., description="Author of the document"),
    output_format: str = Form(
        default="epub", description="Output format (default: epub)"
    ),
):
    file_content = await file.read()
    epub_bytes = await convert_pdf(file_content, output_format, title, author)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".epub") as temp_file:
        temp_file.write(epub_bytes)
        temp_file.flush()
        return FileResponse(
            temp_file.name,
            media_type="application/epub+zip",
            filename=f"{title}.epub",
            background=lambda: cleanup_file(temp_file.name),
        )


async def cleanup_file(file_path: str):
    await asyncio.sleep(1)
    try:
        os.unlink(file_path)
    except OSError:
        pass
