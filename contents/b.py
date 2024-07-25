import quopri

# Define the input string
input_string = "=4D=E1=BA=B9"
input_string = "=42=E1=BB=91"
input_string = "=4E=67=68=C4=A9=61"
input_string = "=54=C3=AA=6E=20=4E=C3=A0=79=20=53=69=C3=AA=75=20=44=C3=A0=69=20=56=C5=A9=20=56=C4=83=6E=20=4E=67=68=C4=A9=61=20=20"



# FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:=54=C3=AA=6E=20=4E=C3=A0=79=20=53=69=C3=AA=75=20=44=C3=A0=69=20=56=C5=
# =A9=20=56=C4=83=6E=20=4E=67=68=C4=A9=61=20=20
# Decode the quoted-printable string
decoded_bytes = quopri.decodestring(input_string)
decoded_string = decoded_bytes.decode('utf-8')

print(decoded_string)
