# pip install flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    with open("phone_numbers.txt", "r") as file:
        content = file.read()
    
    return f"<pre>{content}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
