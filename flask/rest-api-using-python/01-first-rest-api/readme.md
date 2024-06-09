## This is the first rest api build using flask in python. 

- We have used Flask to developed REST API.
- Created endpoints for the resource URL.
- Endpoints creation script is in app.py

## Installation of Flask
`` pip install flask``

## Run Flask app
`` flask run ``
- Local host URL will start listing to the flask app.
- Then we can start using the endpoints defined in the code.

## API Testing
- We can use any approach to test the APIs(Pthon requests module, curl command or API testing application like Postman or Insomnia)
- I have used Insomnia for this project.(Since I have already used Postman so thought of using Insomnia)
- Download link for Insomnia: https://insomnia.rest
- Attached the colelction of requests used for this project.

## Docker
- Docker is a software framework for building, running, and managing images and containers.
- Install Docker Desktop: https://www.docker.com/products/docker-desktop/

## Docker image
- A Docker image is a snapshot of source code, libraries, dependencies, tools, and everything else (except the Operating System kernel!) that a container needs to run.
- We create Docker image through Dockerfile.

## Dockerfile
- Dockerfile defines how the Docker image should be build.
- Once Dockerfile is created, we can use Docker to build the docker image.
- Example:

```
FROM python:3.10 --> base image(internally it can call other base image to install dependencies)
EXPOSE 5000 --> port number to expose our flask application. By defaults it runs on TCP, but we can specify the protocol as TCP or UDP. 
WORKDIR /app --> making the working directory to /app
RUN pip install flask --> install the package required by application
COPY . . --> copy all the contents from local working directory to container working directory
CMD ["flask", "run", "--host", "0.0.0.0"] --> command which should run once container is started(Note: 0.0.0.0 will help in port forwarding)
```

## Build and RUN Docker image
- Once Dockerfile is created we can build the docker image using below command:
``` docker build -t <tag_name> <dockerfile_path>  ```
- Once image is build, we can see it in image section of docker desktop
- We can deploy the image and create a container from RUN button and start consuming the api service.
- We can share the image with other developers.

## Deploy docker through command
Command : ```docker run -d -p 5000:5000 rest-apis-flask-python```

Parameters:
-d runs the container in the background, so that you can close the terminal and the container keeps running.
-p 5000:5000 maps port 5000 in your computer to port 5000 in the container.
rest-apis-flask-python is the image tag that you want to run.

## Docker Compose
- Docker Compose is most useful to start multiple Docker containers at the same time, specifying configuration values for them and dependencies between them.
- USed to start all the services defined in docker-compose.yml file.(same like mta.yaml file)
## docker-compose.yml
- Docker-compose.yml is created in the same folder where Dockerfile is there.
```
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
```
- This small file is all you need to tell Docker Compose that you have a service, called web, which is built using the current directory (by default, that looks for a file called Dockerfile).

Parameters:

- ports: used to map a port in your local computer to one in the container. Since our container runs the Flask app on port 5000, we're targeting that port so that any traffic we access in port 5000 of our computer is sent to the container's port 5000.
- volumes: to map a local directory into a directory within the container. This makes it so you don't have to rebuild the image each time you make a code change.

## RUN Docker compose services
- ``` docker compose up ```
- ``` docker compose up --build --force-recreate --no-deps web ``` --> to rebuild the docker image
