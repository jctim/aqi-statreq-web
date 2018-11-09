FROM python:3.7-alpine
LABEL Name=aqi-statreq-web Version=0.0.1

RUN python3 -m pip install --upgrade pip setuptools wheel

WORKDIR /opt/aqi-app

COPY requirements.txt .
RUN python3 -m pip --no-cache-dir install -r requirements.txt

COPY app/ .
CMD ["python", "./main.py"]
