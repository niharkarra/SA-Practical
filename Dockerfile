FROM python:3.11.3

# COPY . /app

# Add sample application
ADD application.py /tmp/application.py

# Set the working directory in the container
# WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask application runs on
EXPOSE 5000

# Define the command to run your Flask application
CMD ["python", "/tmp/application.py"]