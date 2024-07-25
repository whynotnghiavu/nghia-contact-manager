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


# @app.route('/api/add', methods=['POST'])
# def api_add():
#     phone = request.form.get('phone')
#     name = request.form.get('name')

#     vcards = get_all_vcards_from_database("data/database.txt")

    
#     # for vcard in vcards:
#     #     print(vcard["phone"])
#     #     print(vcard["name"])

#     #     # if phone!= vcard["phone"]: thêm dữ liệu mới
#     #     # if phone= vcard["phone"]: xét name
#     #     #     if name = vcard["name"]: bỏ qua không làm gì cả
#     #     #     if name != vcard["name"]: ghi vào file error.txt
        
 


#     # return redirect(url_for('index'))

#     phone_exists = False

#     for vcard in vcards:
#         if phone == vcard["phone"]:
#             phone_exists = True
#             if name != vcard["name"]:
#                 write_error_to_file("data/error.txt", phone, name)
#             break

#     if not phone_exists:
#         write_vcard_to_database("data/database.txt", phone, name)

#     return redirect(url_for('index'))

# # Các route khác như chỉnh sửa, xóa có thể được thêm vào đây
if __name__ == '__main__':
    app.run(debug=True)



# take note
# readwrite
# read