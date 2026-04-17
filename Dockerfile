# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Set Python path
ENV PYTHONPATH=src

# Make scripts executable
RUN chmod +x scripts/*.sh

# Default entrypoint
ENTRYPOINT ["python", "-m", "fileflow.main"]

# Default command
CMD []