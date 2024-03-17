import requests
from PIL import Image
import colorgram
import csv
import pandas as pd

#custmoize the time range here
endpoint_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
parameters = {"q": "painting", "dateBegin": "1700", "dateEnd": "1799"}

response = requests.get(endpoint_url, params=parameters)

object_ids = response.json()["objectIDs"]

image_urls = []
dominant_colors = []

for object_id in object_ids:
    object_response = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}")
    object_data = object_response.json()
    
    if "primaryImageSmall" in object_data:
        image_url = object_data["primaryImageSmall"]
        image_urls.append(image_url)
        image = Image.open(requests.get(image_url, stream=True).raw)
        colors = colorgram.extract(image, 1) 
        dominant_color = colors[0].rgb

        dominant_colors.append(f"#{dominant_color[0]:02x}{dominant_color[1]:02x}{dominant_color[2]:02x}")
    else:
        print(f"Object ID {object_id} does not have a valid image URL.")

# Create a DataFrame to hold image URLs and dominant colors
data = {
    "Image URL": image_urls,
    "Dominant Color": dominant_colors
}
df = pd.DataFrame(data)
df.to_csv("18th_color2.csv", index=False)
