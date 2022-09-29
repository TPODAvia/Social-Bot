#This programs need to change some lines of code to make it work
# 1) 'C:/proverb.txt'
# 2) 'C:/Users/thepo/Pictures/Screenshots'
# 3) vk_api.VkApi(token="vk1.a.........")

#IMPORTING LIBS
import vk_api
from PIL.ExifTags import TAGS
from PIL import Image
import os, os.path
import numpy as np
import glob
from random import randint

#GET TEXT MODULE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
with open('D:/Coding/proverb.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
count = 0

# Strips the newline character
proverbs = np.array([])
for line in lines:
    count += 1
    #print("Line{}: {}".format(count, line.strip()))
    proverbs = np.append(proverbs, line.strip())

use_proverbs = proverbs[randint(0, count-1)]

#KATE MOBILE MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
session = vk_api.VkApi(token="vk1.a.gU7O8Ha55oZ8isw5U5109KItRDNUFP-BOLjt91vx1_6WBf64tRf0vDesKRK9npFn1OoUvrmf0UpFgYEWDJ7bvOjz-2XQZxbnfjNNES69gyhkJD6uT9YXiA1q1vBl6lJo0MtE63NMtfo8QPz6IGFm62x-UyuCt8hudxxJ8bGfFxuHqXQ6RKUOFSyVbKN4CU7k")
vk = session.get_api()

'''
def get_user_status(user_id):
    status = session.method("status.get",{"user_id": user_id})
    print(status["text"])

def get_post_ms(message):
    post = session.method("wall.post",{"message": message})
    #vk.status.set(text="Hello World")

def get_post_ph(attachments):
    photos = session.method("wall.post",{"attachments":attachments})
    print(photos)
#get_user_status(290618168)
#get_post_ph(attachments="photo290618168_457248620")
'''
#Get PICTURE MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
img_path = np.array([])
count2 = 0

# get the path/directory
# ATTENTION! This folder is for copied images only! The image wil delete PERMANENTLY! Do not use a source folder!
folder_dir = 'D:/Photo masterpieces/Photos/For Uploads'
 
# iterate over files in
# that directory
for images in glob.iglob(f'{folder_dir}/*'):
   
    # check if the image ends with png
    if (images.endswith(".png") or images.endswith(".jpg")\
        or images.endswith(".jpeg")):
        count2 += 1
        img_path = np.append(img_path, images)

use_img_path = img_path[randint(0, count2-1)]

#UPLOAD PICTURE MODULE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#imagename="C:/12 (July 12, 2022)(135 mm)(ISO 200) 1-240 sec at f - 3.2.jpg"
imagename=str(use_img_path)
image=Image.open(imagename)
exifdata=image._getexif()

'''
print("Shutter speed: ", exifdata[33434]) #Ss
print("F-stop: ", exifdata[33437]) #f-stop
print("ISO: ", exifdata[34855]) #ISO

print("ISO: ", exifdata[37386]) #Focal Lenght
print("ISO: ", exifdata[41989]) #Focal Equivalent

print("Body company: ", exifdata[271]) #Body company
print("Body NAME: ", exifdata[272]) #Body NAME
print("Lens company: ", exifdata[42035]) #Lens company
print("Lens NAME: ", exifdata[42036]) #Lens NAME
'''

if exifdata==None:
    print("No exifdata")
    text = str(use_proverbs)
    # IDK How to solve "'NoneType' object is not subscriptable"
    # If someone know? Please text me
else:
    text = str(use_proverbs) + "\n\n"+ \
        str(exifdata[42035]) + " " + str(exifdata[42036]) + "\n" + \
        str(exifdata[37386]) + " mm (" + str(exifdata[41989]) + "mm equivalent)\n" + \
        "1/"+ str(1/exifdata[33434]) + " sec\n" + \
        "ƒ/"+ str(exifdata[33437]) + "\n" + \
        "ISO "+ str(exifdata[34855])


import requests
upload_url = vk.photos.getWallUploadServer(group_id=290618168, v=5.95)['upload_url']
request = requests.post(upload_url, files={'file': open(imagename, "rb")})
save_wall_photo= vk.photos.saveWallPhoto(group_id= 290618168, v=5.95, photo=request.json()['photo'], server = request.json()['server'], hash = request.json()['hash'])
saved_photo = "photo" + str(save_wall_photo[0]['owner_id'])+"_"+ str(save_wall_photo[0]['id'])
vk.wall.post(owner_id=290618168, v=5.95,  message=text, attachments = saved_photo, publish_date=1668669698)

#DELETE PICTURE MODULE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ATTENTION! This folder is for copied images only! The image wil delete PERMANENTLY! Do not use a source folder!

file_path = str(use_img_path)
if os.path.isfile(file_path):
  os.remove(file_path)
  print("File has been deleted")
else:
  print("File does not exist")

