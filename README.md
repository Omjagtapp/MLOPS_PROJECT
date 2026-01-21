# MLOPS_PROJECT – Milestone 0

![CI](https://github.com/Omjagtapp/MLOPS_PROJECT/actions/workflows/ci.yml/badge.svg)

## What this repo contains
Milestone 0 setup for Machine Learning Lifecycle Development & Ops (MLOps):
- Python virtual environment
- Pinned dependencies for reproducibility
- Basic import test (`tests/test_imports.py`)
- GitHub Actions CI to run tests on every push/PR

## Setup (local)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -q

