import requests
import json

inventory_url = "http://inventory-service:1337/inventory"
response = requests.get(inventory_url)
sensors = response.json()

if sensors:
    targets = []
    for sensor in sensors:
        targets.append({
            "targets": [sensor],
            "labels": {"job": "sensors"}
        })

    with open('/etc/prometheus/targets.json', 'w') as f:
        if targets:
            json.dump(targets, f, indent=2)
        else:
            print("No valid targets found, nothing written to the file.")
else:
    print("No sensors data available.")
