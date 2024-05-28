# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install mariadb libraries
RUN apt-get update \
    && apt -y install libmariadb3 libmariadb-dev \
    && apt -y install gcc

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip3 install --prefer-binary --no-cache-dir --upgrade -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
#ENV NAME pokepy-fast-api-docker

# Set the maintainer label
LABEL maintainer="Viktor Donovic <viktor.donovic@zuyd.nl>"

#WORKDIR /app

# Run main.py when the container launches
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
