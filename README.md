# MLOPS_PROJECT – Milestone 0

![CI](https://github.com/Omjagtapp/MLOPS_PROJECT/actions/workflows/ci.yml/badge.svg)

## What this repo contains
Milestone 0 setup for Machine Learning Lifecycle Development & Ops (MLOps):
- Python virtual environment
- Pinned dependencies for reproducibility
- Basic import test (`tests/test_imports.py`)
- GitHub Actions CI to run tests on every push/PR

## Setup (local)
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -q
```
```md
## Documentation: Reproducibility and ML Lifecycle Reliability
Reproducibility is a foundational requirement in machine learning systems because models depend heavily on their execution environment. Differences in Python versions, library versions, or hidden dependencies can cause inconsistent behavior across development, testing, and production.

This project ensures reproducibility by pinning all dependencies to exact versions in `requirements.txt` and standardizing the environment using **Python 3.11**. This allows the same setup to be recreated locally and in CI.

GitHub Actions validates the environment on every push, improving ML lifecycle reliability by detecting issues early and reducing deployment risk.

**Python version:** 3.11
