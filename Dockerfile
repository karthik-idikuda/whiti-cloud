FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Whiti agents
COPY whiti_daemon.py .
COPY whiti_worker.py .
COPY agents/ ./agents/

# Copy config
COPY config/ ./config/

# Create necessary directories
RUN mkdir -p /app/logs /app/memory

# Expose port for health checks
EXPOSE 8080

# Health check endpoint
COPY health_server.py .
RUN echo '#!/bin/bash\npython health_server.py &\npython whiti_daemon.py' > start.sh && chmod +x start.sh

# Start Whiti
CMD ["./start.sh"]
