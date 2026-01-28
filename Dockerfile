# Use a lightweight Python 3.11 image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and using buffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set a working directory inside the container
WORKDIR /app

# Install system dependencies (if needed) - basic build tools & certificates
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (better Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code (main.py, train_model.py, model.pkl, tests, etc.)
COPY . .

# Expose the port FastAPI/uvicorn will run on
EXPOSE 8000

# Default command: run the FastAPI app with uvicorn
# If your app object is named `app` in `main.py`, this is correct.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
