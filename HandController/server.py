from .data import Data
from flask import *
import json

app = Flask(__name__)
__data = Data()
USER = "admin"
PWD = "admin"


@app.route("/get_data", methods=["GET"])
def send_data():
    params = request.args.to_dict()
    if "user" in params and "pwd" in params:
        if params == {"user": USER, "pwd": PWD}:
            data = __data.get_origion_data(True)
            print(data)
            return json.dumps({"data": data})
    return json.dumps({"data": None})


def run_server(host="0.0.0.0", port=10086, debug=True, user="admin", pwd="admin"):
    global USER, PWD
    USER, PWD = user, pwd
    app.run(
        host=host,
        port=port,
        debug=debug
    )





