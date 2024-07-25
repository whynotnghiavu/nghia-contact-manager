from flask import Flask, render_template, request, redirect, url_for
from modules.database import read, write

app = Flask(__name__)


@app.route('/')
def index():
    vcards = read("data/database.txt")

    return render_template('index.html', vcards=vcards)


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/api/add', methods=['POST'])
def api_add():
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


# # Các route khác như chỉnh sửa, xóa có thể được thêm vào đây
if __name__ == '__main__':
    app.run(debug=True)
