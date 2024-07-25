# pip install flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    with open("phone_numbers.txt", "r") as file:
        contents = file.read()

    return render_template('index.html', content=contents)


if __name__ == '__main__':
    app.run(debug=True)
