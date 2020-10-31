from es_sin.es_compute import get_location
from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)
results = []


@app.route('/', methods=['GET'])
@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', results=results)


@app.route('/add_message', methods=['POST'])
def add_message():
    product = request.form['product']
    global results
    results = []
    results.append(get_location(product))
    return redirect(url_for('main'))


def main():
    app.run()
    pass


if __name__ == "__main__":
    main()