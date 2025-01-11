from flask import Flask
import api_functions.countries as cn_api


app = Flask(__name__)

print("Flask app running")

@app.route("/api/v1/countryinfo/<country_name>", methods=["GET"])

def countryinfo(country_name):

    print("countryinfo running")

    return cn_api.get_country(country_name)

if __name__ == "__name__":
    app.run(host="0.0.0.0", port=5000)