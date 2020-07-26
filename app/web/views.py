from flask import render_template, request
from web import app


@app.route('/')
def index():
    html = render_template('index.html')
    return html


@app.route('/result/', methods=["POST"])
def receive():
    result = request.form
    text = str(result["text"])

    return render_template("result.html", text=text)
