from flask import Flask, request, jsonify
from flask_cors import CORS
import lgpio

app = Flask(__name__)
CORS(app)  # ← IMPORTANT

h = lgpio.gpiochip_open(0)

LED = 27
BUTTON = 4

lgpio.gpio_claim_output(h, LED, 0)
lgpio.gpio_claim_input(h, BUTTON)

@app.route("/led", methods=["POST"])
def set_led():
    lgpio.gpio_write(h, LED, int(request.json["value"]))
    return jsonify(ok=True)

@app.route("/button")
def get_button():
    return jsonify(value=lgpio.gpio_read(h, BUTTON))

app.run(host="0.0.0.0", port=3000)