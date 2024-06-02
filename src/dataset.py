import json
import requests

def get_dataset():
    dataset = []

    try:
        r = requests.get("https://eonet.gsfc.nasa.gov/api/v2.1/events")
        
        data = r.json()
        for entry in data["events"]:
            for titles in entry["categories"]:
                if titles["title"] == "Wildfires":
                    for coords in entry["geometries"]:
                        dataset.append(coords["coordinates"])
        return dataset

    except:
        return "Error"
