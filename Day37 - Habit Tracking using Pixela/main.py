import requests
from datetime import datetime

USERNAME = "xtremeandroid"
TOKEN = "abcd1234"
GRAPH_ID = 'graph1'

# Get Today Date in String
today = datetime.now()
today_str = today.strftime("%Y%m%d")

pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create Account
# response = requests.post(pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hr",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Create Graph
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# response.raise_for_status()
# print(response.text)

pixel_add_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today_str,
    "quantity": "5",
}

# ADD DATA TO GRAPH
# response = requests.post(pixel_add_endpoint, headers=headers, json=pixel_data)
# response.raise_for_status()
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_str}"
updated_pixel_data = {
    "quantity": "8",
}

# Update Pixel Data
# response = requests.put(pixel_update_endpoint, headers=headers, json=updated_pixel_data)
# response.raise_for_status()
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_str}"

# Delete Pixel Data
# response = requests.delete(pixel_delete_endpoint, headers=headers)
# response.raise_for_status()
# print(response.text)

