import os
import requests

BIN_NAME = "shaheerlab"
FILE_TO_SEND = ""

url = f"https://filebin.net/{BIN_NAME}/{os.path.basename(FILE_TO_SEND)}"

with open(FILE_TO_SEND, "rb") as f:
    response = requests.post(url, data=f)

if response.status_code in (200, 201):
    print(f"Successfully uploaded {FILE_TO_SEND} to filebin.net/{BIN_NAME}")
else:
    print("Upload failed:", response.status_code)