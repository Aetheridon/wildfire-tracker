import dataset

import folium
from folium.plugins import HeatMap

from flask import Flask, render_template

app = Flask(__name__)
map = folium.Map(tiles="cartodb positron")

def plot_dataset():
    data = dataset.get_dataset()
    coords = []

    if data == "Error":
        pass #TODO: implement "Offline" message.

    else:
        for fire in data:
            coords.append([fire[1], fire[0]])
            HeatMap(coords).add_to(map)

plot_dataset()

INDEX = "templates/index.html"
map.save(INDEX)

@app.route("/")
def main_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)