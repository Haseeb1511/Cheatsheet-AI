# Base image: slim Python 3.9 version (smaller and faster)
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Environment variable: Don't write .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Environment variable: Enable output buffering (set to 1 for stdout to show immediately)
ENV PYTHONUNBUFFERED=1

# Copy all files from host to container working directory
COPY . .

# Install dependencies and upgrade the pip
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask app
EXPOSE 5000

# Default command to run the app
CMD ["python", "app.py"]
