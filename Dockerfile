# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the files
COPY . .

# Expose the port
EXPOSE 8000

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]