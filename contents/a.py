Hãy tạo quá trình ngược lại



def read_txt(txt_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as vcf_file:
        contents = vcf_file.readlines()

    vcards = []
    temp = []

    for content in contents:

        content = content.strip()
        print(content)
        phone, name = content.split(',')
 
    return vcards




def export():
    txt_file_path = "data/database.txt"
    vcf_file_path = "data/nghia-contact-manager.vcf"
    # print(txt_file_path)
    # print(vcf_file_path)


    vcards = read_txt(txt_file_path)

    print(vcards)


if __name__ == '__main__':
    export()
