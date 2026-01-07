from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import lgpio
import os

app = Flask(__name__)
CORS(app)

# 🔐 TOKEN SECRET (à changer)
API_TOKEN = "2755"

h = lgpio.gpiochip_open(0)

LED = 27
BUTTON = 4

lgpio.gpio_claim_output(h, LED, 0)
lgpio.gpio_claim_input(h, BUTTON)

# 🔐 Vérification du token
def check_auth():
    auth = request.headers.get("Authorization", "")
    if auth != f"Bearer {API_TOKEN}":
        abort(401)

@app.route("/led", methods=["POST"])
def set_led():
    check_auth()
    lgpio.gpio_write(h, LED, int(request.json["value"]))
    return jsonify(ok=True)

@app.route("/button")
def get_button():
    check_auth()
    return jsonify(value=lgpio.gpio_read(h, BUTTON))

app.run(host="0.0.0.0", port=3000)