import dataset

import folium
from flask import Flask, render_template

app = Flask(__name__)
map = folium.Map(location=(38.94, -105.64), zoom_start=7, min_zoom=7, max_bounds=True, dragging=False)

def plot_dataset():
    data = dataset.get_dataset()

    if data == "Error":
        pass #TODO: implement "Offline" message.

    else:
        for fire in data:
            folium.Marker(location=[fire[1], fire[0]], popup="Wildfire").add_to(map)
        
plot_dataset()

INDEX = "templates/index.html"
map.save(INDEX)

@app.route("/")
def main_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)