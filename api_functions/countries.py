import requests
from flask import json
import env_vars1

def get_country(country_name):
    try:
        response = requests.get(f"{env_vars1.COUNTRY_API}/v3.1/name/{country_name}?fullText=true")
        data=response.json()
        results = {
            "name": data[0]["name"]["common"],
            "capital": data[0]["capital"][0],
            "lat": data[0]["capitalInfo"]["latlng"][0],
            "long": data[0]["capitalInfo"]["latlng"][1],
            "flag": data[0]["flag"],
            "languages": data[0]["languages"],
            "population": data[0]["population"],
            "timezones": data[0]["timezones"]
        }
    except Exception as e:
        error_data = {
            "errorjon": str(e)
        }
        return json.jsonify(error_data), 500
    return json.jsonify(results)
