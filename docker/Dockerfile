# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy main script
COPY main.py .

# Set default environment variables
ENV TOPIC="data science"
ENV COMPLEXITY="medium"

# Run the script
CMD ["python", "main.py"]
