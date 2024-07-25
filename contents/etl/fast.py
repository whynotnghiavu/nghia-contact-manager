import glob
import requests

# URL của máy chủ bạn muốn tải tệp lên
url = 'http://127.0.0.1:5000/upload'

# Đường dẫn tới thư mục chứa các tệp .vcf
folder_path = r'C:\Users\vvn20206205\Desktop\_temp\data'

# Sử dụng glob để lấy danh sách tất cả các tệp .vcf trong thư mục
vcf_files = glob.glob(f"{folder_path}/*.vcf")

# Lặp qua từng tệp .vcf và gửi yêu cầu POST để tải lên
for file_path in vcf_files:
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
        print(f"Uploaded {file_path} with response {response.status_code}")
