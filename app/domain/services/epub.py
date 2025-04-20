from ebooklib import epub
from io import BytesIO
from app.domain.services.text_processor import clean_text, process_paragraphs
from app.domain.services.chapter_processor import split_into_chapters


def text_to_epub(text, title, author):
    book = epub.EpubBook()
    book.set_title(title)
    book.add_author(author)

    text = clean_text(text)
    chapters = split_into_chapters(text)

    epub_chapters = []
    for idx, chapter in enumerate(chapters, start=1):
        chapter_title = chapter["title"]
        chapter_content = chapter["content"]

        paragraphs = process_paragraphs(chapter_content)
        html_content = f"<h1>{chapter_title}</h1>" + "\n".join(paragraphs)

        c = epub.EpubHtml(title=chapter_title, file_name=f"chap_{idx}.xhtml", lang="en")
        c.content = html_content
        book.add_item(c)
        epub_chapters.append(c)

    book.toc = tuple(epub_chapters)
    book.spine = ["nav"] + epub_chapters

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    epub_bytes = BytesIO()
    epub.write_epub(epub_bytes, book, {})
    return epub_bytes.getvalue()
