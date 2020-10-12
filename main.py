from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/first')
def rome():
    return render_template("index_first.html")


@app.route('/second')
def rom():
    return render_template("index_second.html")


if __name__ == '__main__':
    app.run(debug=True)
