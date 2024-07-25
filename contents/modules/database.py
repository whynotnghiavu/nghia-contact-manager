
def read(txt_file_path):
    with open(txt_file_path, "r") as file:
        contents = file.readlines()
    vcards = []

    for content in contents:
        phone, name = content.strip().split(',')

        vcard = {'name': name, 'phone': phone}
        vcards.append(vcard)

    return vcards


def write(txt_file_path):
    with open(txt_file_path, "r") as file:
        contents = file.readlines()
    vcards = []

    for content in contents:
        phone, name = content.strip().split(',')

        vcard = {'name': name, 'phone': phone}
        vcards.append(vcard)

    return vcards
