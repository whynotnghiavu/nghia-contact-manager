def read(txt_file_path):
    vcards = []

    with open(txt_file_path, "r", encoding="utf-8") as file:
        for line in file:
            phone, name = line.strip().split(',')
            vcards.append({"phone": phone, "name": name})
    return vcards


def write(txt_file_path, phone, name):
    with open(txt_file_path, "a", encoding="utf-8") as file:
        file.write(f"{phone},{name}\n")


def write_new(txt_file_path, vcards):
    with open(txt_file_path, "w", encoding="utf-8") as file:
        for vcard in vcards:
            file.write(f"{vcard["phone"]},{vcard["name"]}\n")
