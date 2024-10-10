# Use the official Python image as the base image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing pyc files and to buffer stdout/stderr streams
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the Django application code to the container
COPY . .

# Expose the port the Django app runs on
EXPOSE 8000

# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
