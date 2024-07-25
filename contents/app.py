import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from modules.database import read, write
from modules.vcard import read_vcf


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route('/')
def index():
    vcards = read("data/database.txt")

    return render_template('index.html', vcards=vcards)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    if request.method == 'POST':
        phone = request.form.get('phone')
        name = request.form.get('name')

        vcards = read("data/database.txt")

        phone_exists = False

        for vcard in vcards:
            if phone == vcard["phone"]:
                phone_exists = True
                if name != vcard["name"]:
                    write("data/error.txt", phone, name)
                break

        if not phone_exists:
            write("data/database.txt", phone, name)

        return redirect(url_for('index'))


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        vcards = read_vcf(filepath)

        return jsonify(vcards)


@app.route('/error')
def error():
    vcards = read("data/error.txt")

    return render_template('error.html', vcards=vcards)


# # Các route khác như chỉnh sửa, xóa có thể được thêm vào đây
if __name__ == '__main__':
    app.run(debug=True)
