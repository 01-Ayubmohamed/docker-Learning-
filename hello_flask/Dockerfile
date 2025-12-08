 #stage 1: Build Stage 

FROM python:3.8-slim AS build

WORKDIR /app 

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

COPY . . 

RUN pip install flask mysqlclient 

 # stage 2: Production Stage 

FROM python:3.8-slim 

WORKDIR /app 

COPY --from=build /app /app 

EXPOSE 5002

CMD ["python", "app.py"]
















# FROM python:3.8-slim     # Using a lightweight Python image
# WORKDIR /app             # Setting the working directory in the container
# COPY . .                 # Copying the current directory contents into the container
# RUN pip install flask    # Installing Flask % Installing MySQL client library
# EXPOSE 5002              # Exposing port 5002 for the Flask app
# CMD ["python", "app.py"] # Command to run the Flask application 

# To build the Docker image, use:
# docker build -t hello_flask .
# "docker build" is the command to build a Docker image from a Dockerfile
# "-t" flag tags the image with the name 'hello_flask'
# "." specifies the current directory as the build context. 

# docker run -d -p 5002:5002 hello-flask, 
# This command runs the Docker container in detached mode (-d), which means it runs in the background
# The -p 5002:5002 option maps port 5002 of the host machine to port 5002 of the container, 
# allowing access to the Flask app from outside the container.

# 'docker run -d --name mydb --network my-custom-network -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:8'
# This command runs a MySQL container named 'mydb' in detached mode
# It connects the container to a custom Docker network named 'my-custom-network'    
# The -e flag sets the environment variable MYSQL_ROOT_PASSWORD to
# 'my-secret-pw', which is required to set the root password for MySQL.

# 'docker run -d --name myapp --network my-custom-network -p 5002:5002 hello-flask-mysql'
# This command runs the Flask application container named 'myapp' in detached mode
# It connects the container to the same custom Docker network 'my-custom-network'
# The -p 5002:5002 option maps port 5002 of the host machine to port 5002 of the container,
# allowing access to the Flask app from outside the container.
# This setup allows the Flask application to communicate with the MySQL database container
# using the shared Docker network.
# Note: Ensure that both containers are on the same Docker network to enable communication between them.




