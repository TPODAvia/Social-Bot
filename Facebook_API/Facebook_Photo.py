#This programs need to change some lines of code to make it work
# 1) 'D:/Coding API/Facebook API/Text.txt'
# 2) https://www.facebook.com/.....
# 3) 'D:/Photo masterpieces/Photos/For Uploads'
# 4) 'D:\Photo masterpieces\Photos\For Reserve'
# 5) Run "Task Scheduler". To run Task Scheduler? You can open "Task Scheduler Samples" to see the example

photo_dir = 'D:\Photo_masterpieces\Photos\For_Reserve'
trash_path = 'D:\Photo_masterpieces\Photos\For_Trash'
web_link = 'https://www.facebook.com/.../'
Template_Matching_LookUp = ['/1WriteSMTH.png', '/2WriteSMTH2.png', '/3Post.png']

#IMPORTING LIBS
from cmath import nan
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import webbrowser
import pyperclip, keyboard, time
from random import randint
import glob
from PIL import Image
import os, os.path
from os import path
import sys

print("Python3 run. Do not move your mouse!!!!")
print("Keyboard and mouse is not disabled!!!!")
print("Don't move anything!!!!")
time.sleep(3)
#TEST TASK MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
import datetime
file = open(os.path.dirname(__file__) + '\task.txt', 'a')

file.write(f'{datetime.datetime.now()} - The script ran 1 \n')
'''

#GET TEXT MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
text_dir= os.path.dirname(__file__) + '/Text.txt'

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

#Get PICTURE MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
img_path = np.array([])
count2 = 0

#Get the path/directory
# photo_dir = 'D:\Photo_masterpieces\Photos\For_Reserve'
#Check if the directory is exist
if (path.exists(photo_dir)==False):
    print("Check the path. The path or a file does not exist: <<" + photo_dir + ">>")
    time.sleep(3)
    sys.exit()

# trash_path = "D:\Photo_masterpieces\Photos\For Trash"
#Check if the directory is exist
if (path.exists(trash_path)==False):
    print("Check the path. The path or a file does not exist: <<" + trash_path + ">>")
    time.sleep(3)
    sys.exit()

# iterate over files in that directory
for images in glob.iglob(f'{photo_dir}/*'):

    # check if the image ends with png/jpg/jpeg/JPG
    if (images.endswith(".png") or images.endswith(".jpg")\
        or images.endswith(".jpeg") or images.endswith(".JPG") or images.endswith(".mp4")):
        count2 += 1
        img_path = np.append(img_path, images)

#Check if images is exist
if (str(img_path)=="[]"):
    print("No Image in folder: " + photo_dir)
    time.sleep(3)
    sys.exit()

use_img_path = img_path[randint(0, count2-1)]


#UPLOAD PICTURE MODULE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

text = " "
if (use_img_path.endswith(".png") or use_img_path.endswith(".jpg")\
        or use_img_path.endswith(".jpeg") or use_img_path.endswith(".JPG")):
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
        text = " "
    else:
        text = "\n\n"+ \
            str(exifdata[42035]) + " " + str(exifdata[42036]) + "\n" + \
            str(exifdata[37386]) + " mm (" + str(exifdata[41989]) + "mm equivalent)\n" + \
            "1/"+ str(float('{:.3f}'.format(10/exifdata[33434]*0.1))) + " sec\n" + \
            "f/"+ str(exifdata[33437]) + "\n" + \
            "ISO "+ str(exifdata[34855])
    image.close()

#Facebook OPEN CV +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def move_to_template(FromScreenshot):
    myScreenshot = pyautogui.screenshot()

    pathname = os.path.dirname(__file__)     
    myScreenshot.save(os.path.dirname(__file__) + '/Screenshot.png')
    img = cv.imread(os.path.dirname(__file__) + '/Screenshot.png',0)
    img2 = img.copy()
    template = cv.imread(os.path.dirname(__file__) + FromScreenshot,0)

    if (path.exists(os.path.dirname(__file__) + FromScreenshot)==False):
        print("Check the path. The path or a file does not exist: <<" + os.path.dirname(__file__) + FromScreenshot + ">>")
        time.sleep(3)
        sys.exit()

    w, h = template.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
                'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

    for meth in methods:
        print("Use method1: " + meth)

    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    #Move mouse
    pyautogui.moveTo(top_left[0] + w/2, top_left[1]+ h/2)
    pyautogui.click()

#Facebook OPEN CV +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#web_link = 'https://www.facebook.com/.../'
webbrowser.open(web_link)
time.sleep(25)
move_to_template(Template_Matching_LookUp[0])
time.sleep(5)
move_to_template(Template_Matching_LookUp[1])

#WRITE KEYBOARD MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def paste(text: str):    
    buffer = pyperclip.paste()
    pyperclip.copy(text)
    keyboard.press_and_release('ctrl + v')
    pyperclip.copy(buffer)


def type(text: str, interval=0.0):
    if interval == 0.0:
        paste(text)
        return

    buffer = pyperclip.paste()
    for char in text:
        pyperclip.copy(char)
        keyboard.press_and_release('ctrl + v')
        time.sleep(interval)
    pyperclip.copy(buffer)

time.sleep(4)
pyautogui.click()
time.sleep(1)
type(str(use_proverbs), 0.05)
time.sleep(1)
# Uncomment the "UPLOAD PICTURE MODULE" first 
type(text, 0.05)
time.sleep(1)

#COPY IMAGE MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import subprocess, sys

def send_to_clipboard(path):
    # path = str("Facebook_API//Grass.mp4")
    p = subprocess.Popen("powershell.exe -command \"Set-Clipboard -Path {0}\"".format(path), stdout=sys.stdout)
    p.communicate()

send_to_clipboard(use_img_path)
pyautogui.hotkey('ctrl', 'v')

time.sleep(30)

#UPLOAD CONTENT ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

move_to_template(Template_Matching_LookUp[2])

#DELETE PICTURE MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

screenshot1 = os.path.dirname(__file__) + '/Screenshot.png'
if os.path.isfile(screenshot1):
  os.remove(screenshot1)
  print("File has been deleted")
else:
  print("File does not exist")

if (photo_dir==trash_path):
    sys.exit()

import shutil
file_path = str(use_img_path)
#Move to another directory
if os.path.isfile(file_path):
    shutil.move(use_img_path, trash_path)
    print("File has been moved to <<Trash>>")
else:
    print("File does not exist")
