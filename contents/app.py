from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def get_all_vcards_from_database(txt_file_path):
    with open(txt_file_path, "r") as file:
        contents = file.readlines()
    vcards = []

    for content in contents:
        phone, name = content.strip().split(',')

        vcard = {'name': name, 'phone': phone}
        vcards.append(vcard)

    return vcards


@app.route('/')
def index():
    vcards = get_all_vcards_from_database("data/database.txt")

    return render_template('index.html', vcards=vcards)


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/api/add', methods=['POST'])
def api_add():
    phone = request.form.get('phone')
    name = request.form.get('name')
#     #     vcards.append({'phone': phone, 'name': name})
    return redirect(url_for('index'))


# # Các route khác như chỉnh sửa, xóa có thể được thêm vào đây
if __name__ == '__main__':
    app.run(debug=True)
