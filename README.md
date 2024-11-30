# weaviate-docker

## Prerequisites

- Install Docker
- Install Python

## Setup using Docker Compose

1. Clone the repository
2. Run `docker compose up -d`

## Test Weaviate using Python

1. Setup Python virtual environment
    - Run `python -m venv .venv`    
    - Run `source .venv/bin/activate`

2. Install Python dependencies
    - Run `pip install -r requirements.txt`

3. Run `python rag.py`

### Describe rag.py

- `rag.py` is a Python script that uses Weaviate and OpenAI to perform a semantic search and generate a response based on the nearest text for the query.
- It also creates a collection in Weaviate if it doesn't exist and deletes it if it does.

### Clean up

- Run `docker compose down`
- Delete the Python virtual environment
    - Run `deactivate`
    - Run `rm -rf .venv`