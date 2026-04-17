# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Set Python path
ENV PYTHONPATH=src

# Run the app
CMD ["python", "-m", "fileflow.main"]