from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "It is a wonderful day"

app.run(host='0.0.0.0')