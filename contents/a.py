import quopri

def read_txt(txt_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        contents = txt_file.readlines()

    vcards = []
    
    for content in contents:
        content = content.strip()
        if content:  # Ensure the line is not empty
            phone, name = content.split(',')
            vcard = {
                'name': name,
                'phone': phone
            }
            vcards.append(vcard)

    return vcards

def write_vcf(vcards, vcf_file_path):
    with open(vcf_file_path, 'w', encoding='utf-8') as vcf_file:
        for vcard in vcards:
            vcf_file.write('BEGIN:VCARD\n')
            vcf_file.write('VERSION:2.1\n')
            vcf_file.write(f'FN:{quopri.encodestring(vcard["name"].encode("utf-8")).decode("utf-8")}\n')
# FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:=4D=E1=BA=B9
            vcf_file.write(f'TEL;CELL;PREF:{vcard["phone"]}\n')
            vcf_file.write('END:VCARD\n')
            vcf_file.write('\n')  # Add a blank line between vCards for readability

def export():
    txt_file_path = "data/database.txt"
    vcf_file_path = "data/nghia-contact-manager.vcf"

    vcards = read_txt(txt_file_path)
    write_vcf(vcards, vcf_file_path)

if __name__ == '__main__':
    export()
