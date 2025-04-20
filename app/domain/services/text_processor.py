import re

def clean_text(text):
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'-\n', '', text)
    text = re.sub(r'\n(?=[a-z])', ' ', text)
    return text.strip()

def format_paragraph(text):
    text = text.strip()
    if not text:
        return ""
    if text.endswith(('.', '!', '?', ':', ';')):
        return f"<p>{text}</p>"
    return f"<p>{text}.</p>"

def process_paragraphs(text):
    paragraphs = []
    current_paragraph = []
    
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            if current_paragraph:
                paragraphs.append(format_paragraph(' '.join(current_paragraph)))
                current_paragraph = []
        else:
            current_paragraph.append(line)
    
    if current_paragraph:
        paragraphs.append(format_paragraph(' '.join(current_paragraph)))
    
    return paragraphs 