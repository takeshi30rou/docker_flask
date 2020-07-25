from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


@app.route('/')
def index():
    html = render_template('index.html')
    return html


@app.route('/result/', methods=["POST"])
def receive():
    result = request.form
    text = str(result["text"])

    return render_template("result.html", text=text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
