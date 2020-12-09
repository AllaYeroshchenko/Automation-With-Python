#!/usr/bin/env python3
import os
import requests

url = "http://localhost/upload/"
path = "supplier-data/images/"
files = os.listdir(path)
for file_name in files:
    if file_name.endswith(".jpeg"):
        with open(path+file_name, 'rb') as opened:
            r = requests.post(url, files={'file': opened})

