from flask import Flask, jsonify,Response
from api.users import apiUsers
from api.customers import apiCustomers
from api.improcess import apiImprocess
from application import createApp

app = createApp()
app.register_blueprint(apiImprocess)
app.register_blueprint(apiUsers)
app.register_blueprint(apiCustomers) 


@app.route("/")
def hello():
    return jsonify({"success":True,"message":"hello"})

if __name__ == "__main__":
    app.run(debug=True)

