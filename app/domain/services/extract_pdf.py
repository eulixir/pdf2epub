from pdfminer.high_level import extract_text
import asyncio
async def extract_text_from_pdf(file_path: str) -> str:
    return await asyncio.to_thread(extract_text, file_path)
