# AQI Station Requestor

A simple service aimed to search AQI stations by city name via interacting with AQI API service https://aqicn.org/api/

## Table of contents

* [Why this code appeared](#why-this-code-appeared)
* [Set up configuration](#set-up-configuration)
* [Run on local env](#run-on-local-env)
* [Run as docker container](#run-as-docker-container)
    * [Build](#build)
    * [Run](#run)
* [Observe in browser](#observe-in-browser)

## Why this code appeared

* Write a simple backed service for the settings page of Garmin Watch
  widget ["Air Quality Index"](https://apps.garmin.com/en-US/apps/7bb1bc3d-0f5d-4a38-98ac-cf55d35a6e2b)
* Playing with python and learning docker

## Set up configuration

1. Create your own config file `token.ini` based on example `token.ini.template` and set your API token generated on this
   page http://aqicn.org/data-platform/token/#/

## Run on local env

```bash
(bash) $ PORT=8080 && python3 app/main.py
```

or

```bash
(fish) > set PORT 8080; and python3 app/main.py
```

## Run as docker container

### Build

1. Install `docker` :

```
$ brew install docker
```

Then you may build the image locally or pull it from the Docker Hub

- Build image locally

```
$ docker build --rm -t jctim/aqi-statreq:latest .
```

- Pull image from the Docker Hub

```
$ docker pull jctim/aqi-statreq:latest .
```

### Run

```
$ docker run \
  -v $(pwd)/token.ini:/opt/aqi-app/token.ini \ 
  -v $(pwd)/info.log:/opt/aqi-app/info.log \ 
  --env PORT=5001 -p 8080:5001 \ 
  --name my-aqi-statreq \ 
  jctim/aqi-statreq
```

## Observe in browser

http://localhost:8080/station