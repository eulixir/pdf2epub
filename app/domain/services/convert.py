from app.domain.services.extract_pdf import extract_text_from_pdf
from ebooklib import epub
import re
from io import BytesIO

async def convert_pdf(file_content: bytes, format: str, title: str, author: str) -> bytes:
    text = await extract_text_from_pdf(file_content)
    
    match format:
        case "epub":
            return text_to_epub(text, title, author)
        case "mobi":
            return await _convert_mobi(text)
        case _:
            raise ValueError(f"Invalid format: {format}")

def split_into_chapters(text):
    chapter_regex = re.compile(r'(^Chapter\s+\d+|^CHAPTER\s+\d+|^\d+\s*$)', re.MULTILINE)
    parts = chapter_regex.split(text)
    chapters = []

    if len(parts) > 1:
        for i in range(1, len(parts), 2):
            title = parts[i].strip()
            content = parts[i+1].strip()
            chapters.append((title, content))
    else:
        chapters.append(("Chapter 1", text.strip()))
    return chapters

def text_to_epub(text, title, author):
    book = epub.EpubBook()
    book.set_title(title)
    book.add_author(author)

    chapters = split_into_chapters(text)

    epub_chapters = []
    for idx, (chapter_title, chapter_content) in enumerate(chapters, start=1):
        paragraphs = [f"<p>{p.strip()}</p>" for p in chapter_content.split("\n") if p.strip()]
        html_content = f"<h1>{chapter_title}</h1>" + "\n".join(paragraphs)

        c = epub.EpubHtml(title=chapter_title, file_name=f'chap_{idx}.xhtml', lang='en')
        c.content = html_content
        book.add_item(c)
        epub_chapters.append(c)

    book.toc = tuple(epub_chapters)
    book.spine = ['nav'] + epub_chapters

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    epub_bytes = BytesIO()
    epub.write_epub(epub_bytes, book, {})
    return epub_bytes.getvalue()

async def _convert_mobi(text: str) -> bytes:
    raise NotImplementedError("MOBI conversion not implemented yet")

