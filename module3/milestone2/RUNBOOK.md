# Milestone 2 Runbook — Iris FastAPI Container

## Service overview
FastAPI service that loads `model.pkl` at startup and exposes:
- `GET /health`
- `POST /predict`

## Local run (Docker)
Build and run the container locally:

```bash
docker build -t milestone2-ml -f module3/milestone2/Dockerfile module3/milestone2
docker run --rm -p 8080:8080 milestone2-ml
