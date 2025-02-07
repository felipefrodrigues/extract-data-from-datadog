from flask import Flask
from metric import get_metric
app = Flask(__name__)

@app.route("/")
def hello():
    return get_metric()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
