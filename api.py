from flask import Flask, request, json
import requests
import urllib.parse

app = Flask(__name__)

API_TOKEN = "pk.eyJ1Ijoibm9hbW4iLCJhIjoiY2thYjY3ampjMHo0YzJ4czlqcTc2b3VnNSJ9.vvXvQ9paTOkTSlxH0kLoyQ"
MAPBOX_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places/"


@app.route("/geoloc")
def get_geo_loc():
    loc = request.args.get("loc")
    q = urllib.parse.quote(loc)
    url = MAPBOX_URL + q + ".json?access_token=" + API_TOKEN
    resp = requests.get(url)
    resp_obj = resp.json()
    return app.response_class(response=json.dumps(resp_obj['features']),
                              status=200,
                              content_type="application/json")


if __name__ == "__main__":
    app.run()

