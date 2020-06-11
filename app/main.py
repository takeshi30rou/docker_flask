from flask import Flask, render_template, request
app = Flask(__name__)
 
@app.route('/')
def index():
    html = render_template('index.html')
    return html

@app.route('/result/', methods = ["POST"])
def receive():
    result  = request.form
    text=str(result["text"])

    return render_template("result.html",a=text)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)