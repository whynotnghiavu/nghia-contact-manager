 

import quopri

# Define the input string
input_string = "Mã hóa ngược lại từ chuỗi văn bản bình thường."
input_string = "Mẹ"

# Encode the string to quoted-printable format
encoded_bytes = quopri.encodestring(input_string.encode('utf-8'))
encoded_string = encoded_bytes.decode('utf-8')

print(encoded_string)

# INPUT:
# input_string = "Mẹ"

# OUTPUT:
# M=E1=BA=B9 khác với   "=4D=E1=BA=B9"???
