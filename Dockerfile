# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files to the container
COPY . .

# Expose the port that the Flask app will be running on
EXPOSE 80

# Set the entry point command to run the Flask app
CMD ["python", "app.py"]

