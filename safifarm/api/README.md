# Safi Farm API

The backend API for the Safi Farm management system.

## Architecture

The API follows a clean architecture pattern with the following structure:

- `core/`: Core functionality and configurations
- `models/`: SQLAlchemy database models
- `schemas/`: Pydantic schemas for request/response validation
- `services/`: Business logic and data processing
- `routes/`: API endpoints and route handlers

## Development

### Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix
   # or
   .\venv\Scripts\activate  # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

### Running the API

For development:
```bash
uvicorn safifarm.api.main:app --reload
```

The API will be available at `http://localhost:8000`
API documentation will be at `http://localhost:8000/docs`

### Testing

Run tests with pytest:
```bash
pytest
```

Generate coverage report:
```bash
pytest --cov=safifarm.api tests/
``` 