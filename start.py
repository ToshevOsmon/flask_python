from flask import Flask
import api_functions.countries as country


app = Flask(__name__)

@app.route("/api/v1/countryinfo/<country_name>", methods=["GET"])
def countryinfo(country_name):
    return country.get_country_info(country_name)

if __name__ == "__name__":
    app.run(host="0.0.0.0", port=5000)