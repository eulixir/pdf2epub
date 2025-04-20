from pdfminer.high_level import extract_text
import asyncio
from io import BytesIO


async def extract_text_from_pdf(file_content: bytes) -> str:
    return await asyncio.to_thread(_extract_text, file_content)


def _extract_text(file_content: bytes) -> str:
    with BytesIO(file_content) as fp:
        return extract_text(fp)
