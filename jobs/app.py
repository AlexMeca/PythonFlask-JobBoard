from flask import Flask
from flask import render_template

app = Flask(__name__)


def render_template():
    pass


@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template('index.html')
