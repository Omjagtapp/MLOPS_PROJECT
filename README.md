# MLOps Project – Milestone 0

![CI](https://github.com/Omjagtapp/MLOPS_PROJECT/actions/workflows/ci.yml/badge.svg)

A reproducible Python development environment for IDS 568, validated using automated CI.

---

## Objective

Milestone 0 establishes a reproducible development environment and continuous integration (CI) foundation for an MLOps project. The goal is to ensure that the project can be reliably set up, tested, and validated in a clean environment.

---

## Prerequisites

- **Operating System:** macOS, Linux, or Windows (WSL)
- **Python Version:** Python 3.11

---

## Quick Start (Fresh Clone Setup)

Follow these steps to recreate the environment from scratch:

1. **Clone the repository**
   ```bash
   git clone https://github.com/Omjagtapp/MLOPS_PROJECT.git
   cd MLOPS_PROJECT
   ```
2. **Create a virtual environment**
  ```bash
  python3 -m venv venv
  ```

3. **Activate the virtual environment**
  ```bash
  source venv/bin/activate
  ```
4.**Install pinned dependencies**
```bash
  pip install -r requirements.txt
  ```
5.**Verify setup with smoke tests**
 ```bash
 pytest -q
  ```

### What This Repository Contains

1.Python virtual environment setup

2.Pinned dependencies for reproducibility

3.Basic smoke test to validate imports

4.GitHub Actions CI pipeline that runs on every push and pull request

### Smoke Tests

The smoke test in this milestone verifies that:

Required Python packages can be imported successfully

The environment is set up correctly

The project is runnable in a clean environment

These tests act as a basic health check, ensuring the system does not fail immediately due to missing
dependencies or configuration issues.

### Reproducibility and ML Lifecycle Reliability

This project applies three core software engineering principles critical to MLOps:

**Dependency Pinning**

All libraries are pinned to exact versions in requirements.txt, eliminating version drift and ensuring
consistent behavior across machines and CI environments.

**Environment Isolation**

Using venv isolates project dependencies from the system Python, preventing conflicts with other projects
and ensuring reliable execution.

**Automated Validation (CI)**

GitHub Actions recreates the environment and runs tests on every push and pull request.
This provides immediate feedback and ensures the codebase remains reproducible and deployable.

Together, these practices create a stable and verifiable foundation for future machine learning development.



### Project Structure
```
.github/workflows/
├── ci.yml              # GitHub Actions CI configuration
tests/
├── test_imports.py     # Smoke test for environment validation
.gitignore              # Ignores local and cache files
README.md               # Project documentation
requirements.txt        # Pinned dependencies for reproducibility
```
###

***Cloud Run vs Cloud Functions (Gen2) – Deployment Comparison***

In this milestone, I deployed the same Iris RandomForest inference model using two serverless approaches: **Cloud Run** and **Cloud Functions (Gen2)**.

**Cloud Run** was used to deploy a containerized FastAPI application built with Docker and stored in Artifact Registry. This approach provides full control over the runtime environment, dependency versions, server configuration, and startup behavior. It closely resembles a production microservice and fits naturally into the deployment stage of the ML lifecycle where scalability, observability, and reproducibility are critical.

**Cloud Functions (Gen2)** was used to deploy a lightweight HTTP-triggered inference endpoint. The model artifact and dependencies are packaged directly with the function source. While Gen2 functions run on Cloud Run internally, the developer experience is simpler and optimized for small, single-purpose endpoints. This approach is faster to deploy but offers less control compared to Cloud Run.

From a **reproducibility and reliability** perspective, both deployments require strict dependency pinning. A scikit-learn version mismatch initially caused runtime warnings, which was resolved by retraining the model under the same version used during deployment. This reinforces the importance of environment consistency across training and serving.

In practice, **Cloud Run** is better suited for production ML services that require fine-grained control and observability, while **Cloud Functions** are ideal for lightweight inference tasks or event-driven ML workflows.










