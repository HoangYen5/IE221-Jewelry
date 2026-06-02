FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY . .

# Ensure the uploads directory exists (FastAPI mounts it in index.py)
RUN mkdir -p uploads

# Expose the port
EXPOSE 8080

# Command to start the application
CMD ["python", "index.py"]
