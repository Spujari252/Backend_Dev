FROM python:3.9-slim

WORKDIR /university_api

# set env variables
# PYTHONDONTWRITEBYTECODE Prevents Python from writing pyc files to disc
# PYTHONUNBUFFERED Prevents Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the requirements file to the working directory, Install the Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the application will run
EXPOSE 8080

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]