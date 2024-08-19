import quopri


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
    name = quopri.decodestring(name)
    name = name.decode('utf-8')

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
