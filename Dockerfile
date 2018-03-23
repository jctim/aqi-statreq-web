# our base image
FROM python:3-onbuild

# specify the port number the container should expose
EXPOSE 5000

COPY app/ /opt/aqi-app/
WORKDIR /opt/aqi-app

# run the application
CMD ["python", "./main.py"]
