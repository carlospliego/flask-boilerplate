from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "hello world no way"

app.run(host='0.0.0.0')