import requests
import nltk
import pandas as pd
from collections import defaultdict

def fetch_and_preprocess_titles():
    century_category_counts = defaultdict(lambda: defaultdict(int))

    centuries = {
        "15th": ("1400", "1499"),
        "16th": ("1500", "1599"),
        "17th": ("1600", "1699"),
        "18th": ("1700", "1799"),
        "19th": ("1800", "1899"),
        "20th": ("1900", "1999")
    }

    for century, (begin_date, end_date) in centuries.items():
        endpoint_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
        parameters = {"q": "painting", "dateBegin": begin_date, "dateEnd": end_date}
        response = requests.get(endpoint_url, params=parameters)
        data = response.json()

        if 'objectIDs' in data and isinstance(data['objectIDs'], list):
            for object_id in data['objectIDs']:
                object_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
                object_response = requests.get(object_url)
                object_data = object_response.json()
                if 'title' in object_data:
                    title = object_data['title']
                    words = nltk.word_tokenize(title)
                    tagged_words = nltk.pos_tag(words)
                    named_entities = nltk.ne_chunk(tagged_words)

                    for entity in named_entities:
                        if isinstance(entity, nltk.Tree):
                            category = entity.label()
                            century_category_counts[century][category] += 1

    rows = []
    for century, category_counts in century_category_counts.items():
        for category, count in category_counts.items():
            rows.append({'Century': century, 'Category': category, 'Count': count})
    df = pd.DataFrame(rows)

    df.to_csv('artwork_title_categories.csv', index=False)

fetch_and_preprocess_titles()
