# PDF to EPUB Converter

A FastAPI-based service that converts PDF files to EPUB format with smart chapter detection and text formatting.

## Features

- Convert PDF files to EPUB format
- Smart chapter detection
- Automatic text formatting and cleanup
- REST API interface
- Support for metadata (title, author)
- Async processing
- Temporary file handling
- Modular and maintainable codebase

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- pdfminer.six
- ebooklib
- python-multipart

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pdf2epub.git
cd pdf2epub
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
make run
```

2. Access the API documentation at:
```
http://localhost:8000/docs
```

3. Convert a PDF file using the API:
```bash
curl -X POST \
  -F "file=@/path/to/your/file.pdf" \
  -F "title=My Document" \
  -F "author=John Doe" \
  -F "output_format=epub" \
  http://localhost:8000/convert/
```

## API Endpoints

### Health Check
- `GET /health/`
  - Returns service status

### Convert PDF
- `POST /convert/`
  - Converts PDF to EPUB
  - Parameters:
    - `file`: PDF file to convert
    - `title`: Document title
    - `author`: Document author
    - `output_format`: Output format (default: epub)

## Project Structure

```
app/
├── domain/
│   └── services/
│       ├── convert.py          # Main conversion orchestration
│       ├── extract_pdf.py      # PDF text extraction
│       ├── text_processor.py   # Text cleaning and formatting
│       ├── chapter_processor.py # Chapter detection and splitting
│       └── epub.py            # EPUB file generation
├── infra/
│   └── controllers/
│       ├── convert.py         # API endpoints for conversion
│       └── healthcheck.py     # Health check endpoint
└── main.py                    # Application entry point
```

## Code Organization

The project follows a clean architecture approach with clear separation of concerns:

- **Domain Services**: Core business logic organized into specialized modules
  - `convert.py`: Orchestrates the conversion process
  - `extract_pdf.py`: Handles PDF text extraction
  - `text_processor.py`: Manages text cleaning and formatting
  - `chapter_processor.py`: Detects and splits chapters
  - `epub.py`: Handles EPUB file generation

- **Infrastructure**: API endpoints and external interfaces
  - `convert.py`: REST API endpoints for file conversion
  - `healthcheck.py`: Service health monitoring

## Development

1. Install development dependencies:
```bash
pip install -r requirements.txt
```

2. Run tests:
```bash
make test
```

3. Run linter:
```bash
make lint
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License