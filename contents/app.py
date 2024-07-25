# pip install flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    with open("phone_numbers.txt", "r") as file:
        # contents = file.read()
        phone_numbers = [line.strip() for line in file.readlines()]

    return render_template('index.html', phone_numbers=phone_numbers)


if __name__ == '__main__':
    app.run(debug=True)
