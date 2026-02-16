# -------------------------
# 1) Builder stage
# -------------------------
FROM python:3.11-slim AS builder

WORKDIR /build

# Install deps into a portable folder (/install)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir --prefix=/install -r requirements.txt

# -------------------------
# 2) Runtime stage (small)
# -------------------------
FROM python:3.11-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy installed deps from builder
COPY --from=builder /install /usr/local

# Copy app artifacts
COPY app/ /app/app/
COPY app/app.py /app/app.py
COPY app/model.pkl /app/model.pkl

EXPOSE 8080

# Cloud Run style
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8080"]
