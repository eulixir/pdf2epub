import re

def detect_chapter_title(text):
    chapter_patterns = [
        r'^Chapter\s+\d+[\.:]?\s*.*$',
        r'^CHAPTER\s+\d+[\.:]?\s*.*$',
        r'^Part\s+\d+[\.:]?\s*.*$',
        r'^PART\s+\d+[\.:]?\s*.*$',
        r'^Section\s+\d+[\.:]?\s*.*$',
        r'^SECTION\s+\d+[\.:]?\s*.*$',
        r'^\d+[\.]\s*.*$',
        r'^[IVX]+[\.]\s*.*$',
        r'^[ivx]+[\.]\s*.*$'
    ]
    
    for pattern in chapter_patterns:
        if re.match(pattern, text, re.IGNORECASE):
            return True
    return False

def split_into_chapters(text):
    chapters = []
    current_chapter = []
    current_title = "Introduction"
    
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        if detect_chapter_title(line):
            if current_chapter:
                chapters.append({
                    'title': current_title,
                    'content': '\n'.join(current_chapter)
                })
                current_chapter = []
            current_title = line
        else:
            current_chapter.append(line)
    
    if current_chapter:
        chapters.append({
            'title': current_title,
            'content': '\n'.join(current_chapter)
        })
    
    return chapters 