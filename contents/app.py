# pip install flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    with open("data/database.txt", "r") as file:
        vcards = [line.strip() for line in file.readlines()]

    return render_template('index.html', vcards=vcards)


if __name__ == '__main__':
    app.run(debug=True)

