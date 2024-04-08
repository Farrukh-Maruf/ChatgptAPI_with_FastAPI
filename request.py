import requests
import json

url = 'http://127.0.0.1:8000/product_description'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
data = {
    "name": "Laptop",
    "notes": "4GB RAM . 256 GB Disk"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())
