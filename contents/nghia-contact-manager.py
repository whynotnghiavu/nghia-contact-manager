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
def parse_vcard(temp):
    vcard = {}

    for line in temp:
        if line.startswith('N;'):
            # field, name = decode_vcard_line(line)
            # vcard['Name'] = name
            vcard['name'] = line
        elif line.startswith('FN;'):
            # field, full_name = decode_vcard_line(line)
            # vcard['Full Name'] = full_name
            vcard['full_name'] = line




        elif line.startswith('TEL;'):
            phone = line.split(':')[-1]
            vcard['phone'] = phone.strip()
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
    vcf_file_path = "data/Danh bạ.vcf"
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
