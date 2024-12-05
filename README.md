# DocAI Platform

A modern document analysis platform with React frontend and Flask backend.

![Document AI Interface](https://your-screenshot-url.com)

## Features

- PDF document processing with OCR support
- Vector-based semantic search
- LLM-powered question answering
- Real-time chat interface
- JWT authentication
- Modern, responsive UI

## Quick Start

### Prerequisites

- Docker and Docker Compose
- Node.js 16+ (for local development)
- Python 3.8+ (for local development)

### Setup

1. Clone:
```bash
git clone https://github.com/huzaifa525/docai-platform.git
cd docai-platform
```

2. Configure environment:
```bash
cp backend/.env.example backend/.env
# Edit .env with your API keys
```

3. Run with Docker:
```bash
docker-compose up --build
```

Access at:
- Frontend: http://localhost:3000
- API: http://localhost:5000

## Development Setup

### Frontend
```bash
cd frontend
npm install
npm start
```

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Unix
venv\Scripts\activate    # Windows
pip install -r requirements.txt
python run.py
```

## Architecture

### Frontend
- React with modern hooks
- Tailwind CSS for styling
- Axios for API communication
- Lucide React for icons

### Backend
- Flask REST API
- JWT authentication
- SentenceTransformer for embeddings
- DeepSeek API integration
- PyMuPDF & Tesseract for document processing

## API Endpoints

```
POST /api/v1/documents
- Upload PDF document

POST /api/v1/query
- Send questions about documents

POST /api/v1/config/apikey
- Update API configuration
```

## Deployment

Optimized for deployment on any container platform:

```bash
# Build images
docker-compose build

# Push to registry
docker-compose push

# Deploy
docker-compose -f docker-compose.prod.yml up -d
```

## License

MIT © [Your Name]
