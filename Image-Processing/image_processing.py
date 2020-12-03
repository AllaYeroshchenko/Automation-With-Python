
## for Windows
import os
from PIL import Image

path = "images/"
path_new = "images-new/"
new_size=(128, 128)
rot=90
files = os.listdir(path)
for file_name in files:
	im = Image.open(path+file_name)
	im_new = im.resize(new_size).rotate(rot)
	im_new = im_new.convert("RGB")
	if not os.path.exists(path_new):
		os.mkdir(path_new)
	im_new.save(path_new+file_name[:-3]+"jpg")


## For Linux
# import os
# from PIL import Image

# path = "images/"
# path_new = "/opt/icons/"
# new_size=(128, 128)
# rot=90
# files = os.listdir(path)
# for file_name in files:
#         print(path+file_name)
#         if not file_name.startswith('.'):
#                 im = Image.open(path+file_name)
#                 im_new = im.rotate(rot)
#                 im_new = im_new.resize(new_size)
#                 im_new = im_new.convert("RGB")
#                 if not os.path.exists(path_new):
#                         os.makedirs(path_new)
#                 im_new.save(path_new+file_name, format="JPEG")
