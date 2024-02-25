from flask import Flask

app = Flask(__name__)

number = 0


@app.route("/", methods=["GET"])
def current_number():
    return str(number)


@app.route("/plus", methods=["POST"])
def number_plus():
    global number
    number += 1
    return str(number)


@app.route("/minus", methods=["POST"])
def number_minus():
    global number
    number -= 1
    return str(number)


if __name__ == "__main__":
    app.run()
