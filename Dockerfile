FROM python:3.10-slim

# Install system dependencies including certs
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libffi-dev libssl-dev \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
