import requests
import csv

#Get titles of artwork for each century
def fetch_and_preprocess_titles(begin_date, end_date, century):
    endpoint_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
    parameters = {"q": "painting", "dateBegin": begin_date, "dateEnd": end_date}
    response = requests.get(endpoint_url, params=parameters)
    data = response.json()

    if 'objectIDs' in data and isinstance(data['objectIDs'], list):
        artwork_titles = []
        for object_id in data['objectIDs']:
            object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
            object_response = requests.get(object_url)
            object_data = object_response.json()
            if 'title' in object_data:
                artwork_titles.append(object_data['title'])

        with open(f"{century}_artwork_titles.csv", 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Artwork Title"])
            for title in artwork_titles:
                writer.writerow([title])

centuries = {
    "15th": ("1400", "1499"),
    "16th": ("1500", "1599"),
    "17th": ("1600", "1699"),
    "18th": ("1700", "1799"),
    "19th": ("1800", "1899"),
    "20th": ("1900", "1999")
}

for century, (begin_date, end_date) in centuries.items():
    fetch_and_preprocess_titles(begin_date, end_date, century)
