import config
import redis
import uuid
import time
import json
from flask import Flask, jsonify, request
from flask import abort, make_response

app = Flask(__name__)
db = redis.StrictRedis(host=config.DB_HOST, port=config.DB_PORT, db=config.DB_NAME)
PREDICT_PATH = f"/api/v{config.API_VERSION}/predict"


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.route("/")
def index():
    return jsonify({"status": "It's working!"})


@app.route(PREDICT_PATH, methods=["POST"])
def predict():
    """
    Puts input data in the queue and waits for result
    """
    response = {"success": False}
    if not request.json:
        # or any of the required fields in the request
        abort(400)

    ####################################################
    #
    # If required, preprocess data here
    # then pack everything into input_x
    #
    ####################################################

    k = str(uuid.uuid4())
    d = {"id": k, "input": input_x}
    db.rpush(config.DB_QUEUE, json.dumps(d))

    while True:
        output = db.get(k)
        if output is not None:
            output = output.decode("utf-8")
            response["payload"] = json.loads(output)
            db.delete(k)
            break
        time.sleep(config.CLIENT_SLEEP)
    response["success"] = True

    return make_response(response)


if __name__ == "__main__":
    app.run(bind="0.0.0.0", debug=True)
