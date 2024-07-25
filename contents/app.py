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

 



import logging

logging.basicConfig(level=logging.INFO)

def process_vcard(vcards, phone, name):
    phone_exists = False
    for vcard in vcards:
        if phone == vcard["phone"]:
            phone_exists = True
            if name == vcard["name"]:
                logging.info(f"Phone {phone} already exists with the same name {name}. No action taken.")
            else:
                logging.info(f"Phone {phone} exists but with a different name. Adding to error log.")
                write("data/error.txt", phone, name)
            break
    if not phone_exists:
        logging.info(f"Phone {phone} does not exist. Adding new entry.")
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


# # Các route khác như chỉnh sửa, xóa có thể được thêm vào đây
if __name__ == '__main__':
    app.run(debug=True)
