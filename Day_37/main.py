import requests
from datetime import datetime

USERNAME = "YOUR USERNAME"
TOKEN = "YOUR SELF GENERATED TOKEN"
GRAPH_ID = "YOUR GRAPH ID"

# Pixela endpoint for creating a new user (if needed)
pixela_endpoint = "https://pixe.la/v1/users"

# User configuration
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# POST request to create a new user (uncomment if you don't have a Pixela account yet)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Graph creation endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Graph configuration
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",  # You can change this color to any valid Pixela color
}

# Headers for authentication
headers = {
    "X-USER-TOKEN": TOKEN
}

# POST request to create the graph (uncomment if you haven't created a graph yet)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Pixel creation endpoint (adding a data point to the graph)
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Get today's date
today = datetime.now()

# Prepare the data for the pixel (data point to be added)
pixel_data = {
    "date": today.strftime("%Y%m%d"),  # Format date as YYYYMMDD
    "quantity": input("How many kilometers did you cycle today? "),  # Ask for user input
}

# POST request to create a new pixel (add the data point)
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# Update an existing pixel (data point) if needed
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# Prepare the new data for updating a pixel
new_pixel_data = {
    "quantity": "4.5"  # Example: updating to 4.5 km (you can change this value)
}

# PUT request to update the pixel (uncomment to test updating)
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Delete a pixel (data point)
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# DELETE request to remove a pixel (uncomment to test deleting)
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
