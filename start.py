from flask import Flask
import api_functions.countries as cn_api
import api_functions.users as users
import init_db

init_db.create_table()

app = Flask(__name__)
#-----------------COUNTRY API 

@app.route("/api/v1/countryinfo/<country_name>")
def countryinfo(country_name):
    return cn_api.get_country(country_name)

#---------------------USER REGESTRER-----------------------------------#

@app.route("/api/v1/users/register", methods=["POST"])
def user_register():
    return users.user_register()

@app.route("/api/v1/users/list", methods=["GET"])
def user_list():
    return users.user_list()

@app.route("/api/v1/users/delete", methods=["DELETE"])
def user_delete():
    return users.delete_user()

if __name__=='_name__':
    app.run()
app.run(host="0.0.0.0", port=5000)