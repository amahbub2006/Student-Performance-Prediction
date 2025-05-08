# Use a lightweight Python image
FROM python:3.10-slim

# Install AWS CLI & system utilities
RUN apt update -y && apt install -y awscli build-essential

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for the web server
EXPOSE 8080

# Run the Flask app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
