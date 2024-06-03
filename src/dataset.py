import sys
import json

import requests

def get_dataset():
    dataset = []
        
    try:
        r = requests.get("https://eonet.gsfc.nasa.gov/api/v3/events")

        if r.status_code == 200:
            data = r.json()
            for entry in data["events"]:
                for titles in entry["categories"]:
                    if titles["title"] == "Wildfires":
                        for coords in entry["geometry"]:
                            dataset.append(coords["coordinates"])
            
            return dataset

        else: 
            print(f"Recieved status code: {r.status_code} querying the API for wildfire data")
            sys.exit()

    except Exception as e:
        print(f"Recieved the following error: {e}\nExiting...")


