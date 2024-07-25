def read_txt(txt_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        contents = txt_file.readlines()

    vcards = []

    for content in contents:
        content = content.strip()

        phone, name = content.split(',')

        vcards.append({'name': name, 'phone': phone})

    return vcards


def to_quoted_printable_hex(s):
    return ''.join(f'={b:02X}' for b in s.encode('utf-8'))


def write_vcf(vcards, vcf_file_path):
    with open(vcf_file_path, 'w', encoding='utf-8') as vcf_file:
        for vcard in vcards:
            name = vcard.get("name", "")
            phone = vcard.get("phone", "")

            # Encode name in quoted-printable
            encoded_name = to_quoted_printable_hex(name)

            vcf_file.write('BEGIN:VCARD\n')
            vcf_file.write('VERSION:2.1\n')
            vcf_file.write(f'FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:{encoded_name}\n')
            vcf_file.write(f'TEL;CELL;PREF:{phone}\n')
            vcf_file.write('END:VCARD\n')
            vcf_file.write('\n')


def export():
    txt_file_path = "data/database.txt"
    vcf_file_path = "data/nghia-contact-manager.vcf"

    vcards = read_txt(txt_file_path)
    write_vcf(vcards, vcf_file_path)


if __name__ == '__main__':
    export()
