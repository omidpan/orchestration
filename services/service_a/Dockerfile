# Stage 1: Build stage
FROM python:3.12-slim AS builder

# Set working directory
WORKDIR /app

# Install build dependencies (optional for some Python packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/app/dependencies -r requirements.txt

# Copy application source code
COPY . .

# Stage 2: Final stage
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependencies and source code from the builder stage
COPY --from=builder /app/dependencies /usr/local/lib/python3.12/site-packages
COPY . .

# Expose the port used by the service
EXPOSE 5001

# Command to run the application
CMD ["python", "app.py"]
