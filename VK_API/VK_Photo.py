#This programs need to change some lines of code to make it work
# 1) 'D:/Coding API/VK API/Text.txt'
# 2) vk_api.VkApi(token="vk1.a.........")
# 3) my_id = 1234567890
# 4) 'D:/Photo masterpieces/Photos/For Uploads'
# 5) 'D:\Photo masterpieces\Photos\For Reserve'
# 6) Run "Task Scheduler". To run Task Scheduler? You can open "Task Scheduler Samples" to see the example

#IMPORTING LIBS
from cmath import nan
from pyscreeze import screenshot
import vk_api
from PIL.ExifTags import TAGS
from PIL import Image
import sys
import os, os.path
from os import path
import numpy as np
import glob
import time
from random import randint

print("Python3 run. Do not move your mouse!!!!")
print("Keyboard and mouse is not disabled!!!!")
print("Don't move anything!!!!")
#TEST TASK MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
import datetime
file = open(os.path.dirname(__file__) + '\task.txt', 'a')

file.write(f'{datetime.datetime.now()} - The script ran \n')
'''

#GET TEXT MODULE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
text_dir = os.path.dirname(__file__) + '/Text.txt'

#Check if the directory is exist
if (path.exists(text_dir)==False):
    print("Check the path. The path or a file does not exist: <<" + text_dir + ">>")
    time.sleep(3)
    sys.exit()

#Read the informations
with open(text_dir, 'r', encoding='utf-8') as f:
    lines = f.readlines()
count = 0

# Strips the newline character
proverbs = np.array([])
for line in lines:
    count += 1
    #print("Line{}: {}".format(count, line.strip()))
    proverbs = np.append(proverbs, line.strip())

#choose a random sentenses
use_proverbs = proverbs[randint(0, count-1)]

#KATE MOBILE MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
session = vk_api.VkApi(token="vk1.a.gU7O8....KN4CU7k")
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
#Get PICTURE MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

img_path = np.array([])
count2 = 0

# get the path/directory
photo_dir = 'D:/Photo_masterpieces/Photos/For_Uploads'

#Check if the directory is exist
if (path.exists(photo_dir)==False):
    print("Check the path. The path or a file does not exist: <<" + photo_dir + ">>")
    time.sleep(3)
    sys.exit()

# iterate over files in that directory
for images in glob.iglob(f'{photo_dir}/*'):

    # check if the image ends with png/jpg/jpeg/JPG
    if (images.endswith(".png") or images.endswith(".jpg")\
        or images.endswith(".jpeg") or images.endswith(".JPG")):
        count2 += 1
        img_path = np.append(img_path, images)

#Check if Images is exist
if (str(img_path)=="[]"):
    print("No Image in folder: " + photo_dir)
    time.sleep(3)
    sys.exit()

use_img_path = img_path[randint(0, count2-1)]

#UPLOAD PICTURE MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

imagename=str(use_img_path)
image=Image.open(imagename)
exifdata=image._getexif()
if exifdata != None:
    exifdata[42035] = nan #Lens company
    exifdata[42036] = nan #Lens NAME
    exifdata[37386] = nan #Focal Lenght
    exifdata[41989] = nan #Focal Equivalent
    exifdata[33434] = nan #Ss
    exifdata[33437] = nan #f-stop
    exifdata[34855] = nan #ISO
    exifdata2=image._getexif()
    for x in exifdata2:
        exifdata[x] = exifdata2[x]

#Open this bracket to test
'''
print("Shutter speed: ", exifdata[33434]) #Ss
print("F-stop: ", exifdata[33437]) #f-stop
print("ISO: ", exifdata[34855]) #ISO

print("Focal Lenght: ", exifdata[37386]) #Focal Lenght
print("Focal Equivalent: ", exifdata[41989]) #Focal Equivalent

print("Body company: ", exifdata[271]) #Body company
print("Body NAME: ", exifdata[272]) #Body NAME
print("Lens company: ", exifdata[42035]) #Lens company
print("Lens NAME: ", exifdata[42036]) #Lens NAME
'''

#Set customs data
if str(exifdata[272]) == "FinePix S2950":
    exifdata[41989] = 5.6*exifdata[37386]
    exifdata[42035] = exifdata[271]
    exifdata[42036] = "5-90mm F/ 3.1-5.6"
#Check the exif-data
if exifdata==None or (str(exifdata[42035]) or str(exifdata[42036]) or str(exifdata[37386]) or \
    str(exifdata[41989]) or str(exifdata[33434]) or str(exifdata[33437]) or str(exifdata[34855])) == "nan":
    print("No exifdata")
    text = str(use_proverbs)
else:
    # Print "use_proverbs" + Focal lenght + Shutter speed + Aperature + ISO
    text = str(use_proverbs) + "\n\n"+ \
        str(exifdata[42035]) + " " + str(exifdata[42036]) + "\n" + \
        str(exifdata[37386]) + " mm (" + str(exifdata[41989]) + "mm equivalent)\n" + \
        "1/"+ str(float('{:.3f}'.format(10/exifdata[33434]*0.1))) + " sec\n" + \
        "ƒ/"+ str(exifdata[33437]) + "\n" + \
        "ISO "+ str(exifdata[34855])

#We need to close image else we can't mov this image to Reserve
image.close()

#Upload to VK
import requests
# Your id
my_id = 12345678
upload_url = vk.photos.getWallUploadServer(group_id=my_id, v=5.95)['upload_url']
request = requests.post(upload_url, files={'file': open(imagename, "rb")})
save_wall_photo= vk.photos.saveWallPhoto(group_id= my_id, v=5.95, photo=request.json()['photo'], server = request.json()['server'], hash = request.json()['hash'])
saved_photo = "photo" + str(save_wall_photo[0]['owner_id'])+"_"+ str(save_wall_photo[0]['id'])
#vk.wall.post(owner_id=my_id, v=5.95,  message=text, attachments = saved_photo, publish_date=1668669698)
vk.wall.post(owner_id=my_id, v=5.95,  message=text, attachments = saved_photo)

#DELETE PICTURE MODULE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import shutil

file_path = str(use_img_path)
trash_path = "D:\Photo_masterpieces\Photos\For_Reserve"

#Check if the directory is exist
if (path.exists(trash_path)==False):
    print("Check the path. The path or a file does not exist: <<" + trash_path + ">>")
    time.sleep(3)
    sys.exit()

#Move to another directory
if os.path.isfile(file_path):
    shutil.move(use_img_path, trash_path)
    print("File has been moved to <<Reserve>>")
else:
    print("File does not exist")
