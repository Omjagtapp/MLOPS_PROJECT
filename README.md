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


## Documentation: Reproducibility and ML Lifecycle Reliability

Reproducibility is a foundational requirement in machine learning systems because models depend heavily on their execution environment. Differences in Python versions, library versions, or hidden dependencies can cause models to behave inconsistently across development, testing, and production environments. Without reproducibility, it becomes difficult to debug errors, validate experiments, or reliably deploy models.

This project addresses reproducibility by pinning all dependencies to exact versions in `requirements.txt` and standardizing the development environment using Python 3.11. This ensures that anyone cloning the repository can recreate the same environment in a short amount of time, whether locally or in a CI pipeline.

GitHub Actions further strengthens ML lifecycle reliability by validating the environment in a clean system on every push. This helps catch dependency and configuration issues early, before they affect model training or deployment. Consistent environments across data preparation, training, evaluation, and deployment reduce operational risk and improve long-term maintainability in MLOps workflows.
**Python version:** 3.11

