FROM python:3.11.3

# Set the working directory in the container
WORKDIR /app

# Add sample application
ADD app.py /tmp/app.py

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Flask application to the container
COPY . .

# Expose the port your Flask application runs on
EXPOSE 5000

# Define the command to run your Flask application
CMD ["python", "app.py"]