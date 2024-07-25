from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
# def home():
#     with open("data/database.txt", "r") as file:
#         vcards = [line.strip() for line in file.readlines()]

#     return render_template('index.html', vcards=vcards)
    vcards = [
        {'name': 'John Doe', 'email': 'john@example.com'},
        {'name': 'Jane Smith', 'email': 'jane@example.com'},
        {'name': 'Emily Johnson', 'email': 'emily@example.com'}
    ]
    
    return render_template('index.html', vcards=vcards)

if __name__ == '__main__':
    app.run(debug=True)
