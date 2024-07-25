from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    with open("data/database.txt", "r") as file:
        contents = file.readlines()
    vcards = []

    for content in contents:
        phone, name = content.split(',')

        vcard = {}
        vcard['name'] = name
        vcard['phone'] = phone
        vcards.append(vcard)

    return render_template('index.html', vcards=vcards)


if __name__ == '__main__':
    app.run(debug=True)
