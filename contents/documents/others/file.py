import glob
import requests

url = 'http://127.0.0.1:5000/upload'
folder_path = r'C:\Users\vvn20206205\Desktop\danh_ba'

vcf_files = glob.glob(f"{folder_path}/*.vcf")
for file_path in vcf_files:
    with open(file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(url, files=files)
        print(f"Uploaded {file_path} with response {response.status_code}")
