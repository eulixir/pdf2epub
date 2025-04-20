from app.domain.services.extract_pdf import extract_text_from_pdf
from app.domain.services.epub import text_to_epub


async def convert_pdf(
    file_content: bytes, format: str, title: str, author: str
) -> bytes:
    text = await extract_text_from_pdf(file_content)

    match format:
        case "epub":
            return text_to_epub(text, title, author)
        case "mobi":
            return await _convert_mobi(text)
        case _:
            raise ValueError(f"Invalid format: {format}")


async def _convert_mobi(text: str) -> bytes:
    raise NotImplementedError("MOBI conversion not implemented yet")
