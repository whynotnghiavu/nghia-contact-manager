# import re
# import quopri

# def decode_vcard_line(line):
#     match = re.match(r'(.+?)CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:(.+)', line)
#     if match:
#         field, encoded_value = match.groups()
#         decoded_value = quopri.decodestring(encoded_value).decode('utf-8')
#         return field.strip(), decoded_value.strip()
#     return line.split(':', 1)

# def parse_vcard(vcard_lines):
#     vcard = {}
#     for line in vcard_lines:
#         if line.startswith('N;'):
#             field, name = decode_vcard_line(line)
#             vcard['Name'] = name
#         elif line.startswith('FN;'):
#             field, full_name = decode_vcard_line(line)
#             vcard['Full Name'] = full_name
#         elif line.startswith('TEL;'):
#             field, phone = line.split(':', 1)
#             vcard['Phone'] = phone.strip()
#     return vcard

# def read_vcf(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         vcards = []
#         vcard_lines = []
#         for line in file:
#             line = line.strip()
#             if line == 'BEGIN:VCARD':
#                 vcard_lines = []
#             elif line == 'END:VCARD':
#                 vcard = parse_vcard(vcard_lines)
#                 vcards.append(vcard)
#             else:
#                 vcard_lines.append(line)
#         return vcards

# def main():
#     file_path = 'contacts.vcf'  # Replace with the path to your VCF file
#     file_path = 'data/Danh bạ.vcf'  # Replace with the path to your VCF file
#     file_path = 'data/Danh bạ_002.vcf'  # Replace with the path to your VCF file
#     vcards = read_vcf(file_path)

#     for i, vcard in enumerate(vcards, start=1):
#         print(f"**{i}.**")
#         for key, value in vcard.items():
#             print(f"  - **{key}:** {value}")
#         print()

# if __name__ == '__main__':
#     main()
