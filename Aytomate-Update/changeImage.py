#!/usr/bin/env python3
import os
from PIL import Image

path = "supplier-data/images/"
new_size=(600, 400)
files = os.listdir(path)
for file_name in files:
#    print(path+file_name)
    if file_name.endswith('.tiff'):
        print(path+file_name)
        im = Image.open(path+file_name)
        im_new = im.resize(new_size)
        im_new = im_new.convert("RGB")
        print(path+file_name[:-5]+".jpeg")
        im_new.save(path+file_name[:-5]+".jpeg", format="JPEG")

