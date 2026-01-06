from flask import Flask, request, jsonify
import lgpio

app = Flask(__name__)

# Ouvre le contrôleur GPIO
h = lgpio.gpiochip_open(0)

LED = 27
BUTTON = 4

# Configuration GPIO
lgpio.gpio_claim_output(h, LED, 0)
lgpio.gpio_claim_input(h, BUTTON)

# État LED
led_state = 0

@app.route("/led", methods=["POST"])
def set_led():
    global led_state
    led_state = 1 if request.json.get("value") else 0
    lgpio.gpio_write(h, LED, led_state)
    return jsonify(ok=True, led=led_state)

@app.route("/button")
def get_button():
    value = lgpio.gpio_read(h, BUTTON)
    return jsonify(value=value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)