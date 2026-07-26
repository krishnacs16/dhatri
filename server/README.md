# Server

A basic FastAPI server using uv.

## Prerequisites

- Python 3.13+
- uv installed

## Setup

From the server directory, install dependencies:

```bash
uv sync
```

## Run locally

Start the server:

```bash
uv run python main.py
```

Then open:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health

## Available endpoints

- GET / returns a welcome message
- GET /health returns the server status

## Project files

- app.py: FastAPI app definition
- main.py: entry point for running with Uvicorn
