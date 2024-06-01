import folium
from flask import Flask, render_template

app = Flask(__name__)
map = folium.Map(location=(38.94, -105.64), zoom_start=7, min_zoom=7, max_bounds=True, dragging=False)

INDEX = "templates/index.html"
map.save(INDEX)

@app.route("/")
def main_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)