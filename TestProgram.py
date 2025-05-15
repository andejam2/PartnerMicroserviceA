import requests

# URL of your running microservice
url = "http://127.0.0.1:5000/getPackingList"

# Change this to test different trip types
data = {
    "trip_type": "moon"
}

# Send POST request
response = requests.post(url, json=data)

# Print status and JSON response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
