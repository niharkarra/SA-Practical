FROM python:3.11.3

# COPY . /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add sample application
ADD application.py /tmp/application.py

# Set the working directory in the container
# WORKDIR /app

# Expose the port your Flask application runs on
EXPOSE 8000

# Define the command to run your Flask application
ENTRYPOINT ["python", "/tmp/application.py"]