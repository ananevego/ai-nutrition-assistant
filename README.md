# AI Nutrition Assistant

AI Nutrition Assistant is a small FastAPI project for calculating daily calories and macros.

The project is also used as a practical DevOps learning playground: Docker, HTTP basics, CI/CD, infrastructure as code, deployment, and observability will be added step by step.

## Current Features

- FastAPI backend
- Nutrition macro calculation endpoint
- Basic HTML interface
- Dockerfile for containerized API runtime
- Docker Compose configuration for local development

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- Docker
- Docker Compose

## Project Structure

```text
.
├── backend
│   ├── app
│   │   ├── schemas
│   │   │   └── nutrition.py
│   │   ├── static
│   │   │   └── index.html
│   │   ├── calculator.py
│   │   ├── config.py
│   │   └── main.py
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── requirements.txt
├── .gitignore
└── README.md
```

## Run Locally With Python

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API: <http://127.0.0.1:8000>

Swagger docs: <http://127.0.0.1:8000/docs>

## Run With Docker Compose

```bash
cd backend
docker compose up --build
```

API: <http://127.0.0.1:8000>

## Environment Variables

You can override the app metadata without touching code:

```bash
APP_NAME=My Nutrition App
APP_VERSION=2.0.0
```

The container defaults are documented in [`backend/.env.example`](/Users/egorananev/Desktop/projects/ai-nutrition-assistant/backend/.env.example).

## Run Tests

From the repository root:

```bash
backend/venv/bin/python -m pytest -q
```

## API Example

```bash
curl -X POST http://127.0.0.1:8000/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "weight": 80,
    "height": 180,
    "age": 30,
    "activity_level": "medium",
    "goal": "maintain"
  }'
```

## DevOps Learning Roadmap

- Prepare a clean git repository
- Improve Docker image and Compose workflow
- Add tests and code quality checks
- Add CI pipeline with GitHub Actions
- Add PostgreSQL and migrations
- Add Telegram bot integration
- Deploy the application
- Describe infrastructure with Terraform
- Add logs, healthchecks, and monitoring
