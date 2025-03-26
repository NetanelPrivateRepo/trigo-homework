import requests
import json
import time

inventory_url = "http://inventory-service:1337/inventory"

while True:
    try:
        response = requests.get(inventory_url)
        response.raise_for_status()
        sensors = response.json()

        targets = [{"targets": [sensor], "labels": {"job": "sensors"}} for sensor in sensors]

        with open('/etc/prometheus/targets.json', 'w') as f:
            json.dump(targets, f, indent=2)

        print("Updated targets.json with sensors:", targets)

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(10)
