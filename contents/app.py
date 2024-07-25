import os
import logging
from flask import Flask, render_template, request, redirect, url_for, jsonify
from modules.database import read, write, write_new
from modules.vcard import read_vcf


logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route('/')
def index():
    vcards = read("data/database.txt")

    return render_template('index.html', vcards=vcards)


def process_vcard(vcards, phone, name):
    phone_exists = False
    for vcard in vcards:
        if phone == vcard["phone"]:
            phone_exists = True
            if name == vcard["name"]:
                logging.info(f"Số điện thoại {phone} và tên {name} đã tồn tại. (Bỏ qua)")
            else:
                logging.info(f"Số điện thoại {phone} tồn tại nhưng với tên khác. (Ghi vào file error.txt)")
                write("data/error.txt", phone, name)
            break
    if not phone_exists:
        logging.info(f"Số điện thoại {phone} chưa có. (Thêm dữ liệu)")
        write("data/database.txt", phone, name)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    if request.method == 'POST':
        phone = request.form.get('phone')
        name = request.form.get('name')

        vcards = read("data/database.txt")
        process_vcard(vcards, phone, name)

        return redirect(url_for('index'))


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or request.files['file'].filename == '':
        return redirect(url_for('index'))

    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    new_vcards = read_vcf(filepath)
    vcards = read("data/database.txt")

    for new_vcard in new_vcards:
        process_vcard(vcards, new_vcard["phone"], new_vcard["name"])

    return redirect(url_for('index'))


@app.route('/error')
def error():
    vcards = read("data/error.txt")

    return render_template('error.html', vcards=vcards)


@app.route('/delete/<phone>/<name>/<file>', methods=['POST'])
def delete_vcard(phone, name, file):
    vcards = read(f"data/{file}.txt")

    new_vcards = [vcard for vcard in vcards if not (vcard.get('phone') == phone and vcard.get('name') == name)]

    write_new(f"data/{file}.txt", new_vcards)

    if file == "database":
        return redirect(url_for('index'))
    if file == "error":
        return redirect(url_for('error'))


if __name__ == '__main__':
    app.run(debug=True)
