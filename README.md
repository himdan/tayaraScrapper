## Tayara scrapper environment

Docker environment for **Tayara scrapper** application.
## Prerequisites

Make sure you have installed all of the following prerequisites on your development machine: <br>
Check the official Docker documentation for information how to install Docker on your operating system. And then install Docker and supporting tools.

* Docker - [Official Website] - <a href="https://docs.docker.com/engine/install/">docker</a> <br>
* Docker Compose - [Official Website] - <a href="https://docs.docker.com/compose/install/">docker-compose</a> <br>
## Installation
 * build docker image
 ```bash
docker build ./scrapper -t python-cli
docker build ./webApp -t python-web
```
 * start the application
 ```bash
 docker-compose up -d