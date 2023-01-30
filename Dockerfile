# Use Alpine Linux with Python 3.7 as the base image
FROM python:3.9.15-slim-buster

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory to /app
WORKDIR /app

# Add the current directory to /app in the image
ADD . /app

# Create virtual env
RUN python3 -m venv venv
RUN . venv/bin/activate

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Expose the port that the app will run on
EXPOSE 5000

# Specify the command to run when a container is created from the image
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]