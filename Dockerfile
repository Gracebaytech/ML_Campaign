# Base Image
FROM python:3.9.12-slim-buster

COPY . /app

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt requirements.txt

# Install the required packages
RUN pip3 install -r requirements.txt
 
 RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy the rest of the application to the working directory
COPY . .

# Set the environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose port 5000
EXPOSE 5000

# Start the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
