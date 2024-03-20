import requests
from PIL import Image
from io import BytesIO

# Example image file and capture data
image_file = "example.jpg"
username = "example_user"
x = 10
y = 20

# Open and read the image file
with open(image_file, "rb") as f:
    image_data = f.read()

# Convert image data to PIL Image object
image = Image.open(BytesIO(image_data))

# Prepare capture data
capture_data = {
    "username": username,
    "capture": image,
    "x": x,
    "y": y
}

# Send POST request to the API
response = requests.post("http://localhost:/send_image", files={"photo": image_data}, data=capture_data)

# Check response
if response.status_code == 200:
    print("Image sent successfully!")
else:
    print("Error:", response.text)
