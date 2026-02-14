# -------- Builder stage --------
FROM python:3.11-slim AS builder
WORKDIR /build

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# -------- Runtime stage --------
FROM python:3.11-slim
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Copy application code + model
COPY app/ /app/

# Ensure user-installed binaries are on PATH
ENV PATH=/root/.local/bin:$PATH

# Cloud Run / container platforms expect port 8080
EXPOSE 8080

# Start the FastAPI app (file is app.py, variable is app)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
