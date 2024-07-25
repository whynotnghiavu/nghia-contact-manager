# import re
# import quopri


# def decode_vcard_line(line):
#     match = re.match(r'(.+?)CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:(.+)', line)
#     if match:
#         field, encoded_value = match.groups()
#         decoded_value = quopri.decodestring(encoded_value).decode('utf-8')
#         return field.strip(), decoded_value.strip()
#     return line.split(':', 1)


# N;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:;=4D=E1=BA=B9;;;
# FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:=4D=E1=BA=B9
def parse_vcard(contents):
    for i, content in enumerate(contents):
        if content.startswith('FN;'):
            break
    contents = contents[i:]

    name = contents[:-1]
    name = "".join(name)
    name = name.split(':')[-1]
    while "==" in name:
        name = name.replace("==", "=")

    phone = contents[-1]
    phone = phone.split(':')[-1]

    vcard = {}
    vcard['name'] = name
    vcard['phone'] = phone
    return vcard


def read_vcf(vcf_file_path):
    with open(vcf_file_path, 'r', encoding='utf-8') as vcf_file:
        contents = vcf_file.readlines()

    vcards = []
    temp = []

    for content in contents:

        content = content.strip()

        if content == 'BEGIN:VCARD':
            temp = []
        elif content == 'END:VCARD':
            vcard = parse_vcard(temp)
            vcards.append(vcard)
        else:
            temp.append(content)

    return vcards


def main():
    vcf_file_path = "data/Danh bạ_002.vcf"

    vcards = read_vcf(vcf_file_path)

    for vcard in vcards:
        print(vcard)

#     for i, vcard in enumerate(vcards, start=1):
#         print(f"**{i}.**")
#         for key, value in vcard.items():
#             print(f"  - **{key}:** {value}")
#         print()


if __name__ == '__main__':
    main()
