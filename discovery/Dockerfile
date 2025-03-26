FROM python:3.11-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY discover_sensors.py discover_sensors.py

ENTRYPOINT [ "python3", "discover_sensors.py" ]