from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    with open("data/database.txt", "r") as file:
        contents = file.readlines()
    vcards = []

    for content in contents:
        phone, name = content.strip().split(',')

        vcard = {'name': name, 'phone': phone}
        vcards.append(vcard)

    return render_template('index.html', vcards=vcards)


@app.route('/add', methods=['POST'])
def add():
    # phone = request.form.get('phone')
    # name = request.form.get('name')
    # if phone and name:
    #     vcards.append({'phone': phone, 'name': name})
    return redirect(url_for('index'))

# Các route khác như chỉnh sửa, xóa có thể được thêm vào đây


if __name__ == '__main__':
    app.run(debug=True)
