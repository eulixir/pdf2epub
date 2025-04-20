from app.domain.services.extract_pdf import extract_text_from_pdf
from ebooklib import epub
import asyncio

async def convert_pdf(file_path: str, format: str, title: str, author: str) -> str:
    
    text = await extract_text_from_pdf(file_path)
    
    match format:
        case "epub":
            return await _convert_epub(title, text, author)
        case "mobi":
            return await _convert_mobi(text)
        case _:
            raise ValueError(f"Invalid format: {format}")


async def _convert_epub(title: str, text: str, author: str) -> bytes:
    book = epub.EpubBook()
    book.set_title(title)
    book.add_author(author)

    chapter = epub.EpubHtml(title='Capítulo 1', file_name='capitulo1.xhtml', lang='pt')
    chapter.content = f'<h1>Capítulo 1</h1><p>{text.replace("\n", "<br/>")}</p>'

    book.add_item(chapter)
    book.spine = ['nav', chapter]
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    
    return book



def _convert_mobi(text: str) -> str:
    # not implemented yet
    pass

