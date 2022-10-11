#This programs need to change some lines of code to make it work
# 1) 'D:/Coding API/Facebook API/Text.txt'
# 2) https://www.facebook.com/.....
# 3) 'D:/Photo masterpieces/Photos/For Uploads'
# 4) 'D:\Photo masterpieces\Photos\For Reserve'

#IMPORTING LIBS
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import webbrowser
import time
from random import randint
import glob
from PIL import Image
from os import path
import sys

#GET TEXT MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
text_dir='D:/Coding API/Facebook API/Text.txt'

#Check if the directory is exist
if (path.exists(text_dir)==False):
    print("Check the path. The path does not exist: <<" + text_dir + ">>")
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

#Get a trasnslator
translation = {}

translation[ord('ё')] = 't'
translation[ord('й')] = 'q'
translation[ord('ц')] = 'w'
translation[ord('у')] = 'e'
translation[ord('к')] = 'r'
translation[ord('е')] = 't'
translation[ord('н')] = 'y'
translation[ord('г')] = 'u'
translation[ord('ш')] = 'i'
translation[ord('щ')] = 'o'
translation[ord('з')] = 'p'
translation[ord('х')] = '['
translation[ord('ъ')] = ']'
translation[ord('ф')] = 'a'
translation[ord('ы')] = 's'
translation[ord('в')] = 'd'
translation[ord('а')] = 'f'
translation[ord('п')] = 'g'
translation[ord('р')] = 'h'
translation[ord('о')] = 'j'
translation[ord('л')] = 'k'
translation[ord('д')] = 'l'
translation[ord('ж')] = ';'
translation[ord('э')] = "'"
translation[ord('я')] = 'z'
translation[ord('ч')] = 'x'
translation[ord('с')] = 'c'
translation[ord('м')] = 'v'
translation[ord('и')] = 'b'
translation[ord('т')] = 'n'
translation[ord('ь')] = 'm'
translation[ord('б')] = ','
translation[ord('ю')] = '.'
translation[ord('.')] = '/'

translation[ord('Ё')] = 'T'
translation[ord('Й')] = 'Q'
translation[ord('Ц')] = 'W'
translation[ord('У')] = 'E'
translation[ord('К')] = 'R'
translation[ord('Е')] = 'T'
translation[ord('Н')] = 'Y'
translation[ord('Г')] = 'U'
translation[ord('Ш')] = 'I'
translation[ord('Щ')] = 'O'
translation[ord('З')] = 'P'
translation[ord('Х')] = '{'
translation[ord('Ъ')] = '}'
translation[ord('Ф')] = 'A'
translation[ord('Ы')] = 'S'
translation[ord('В')] = 'D'
translation[ord('А')] = 'F'
translation[ord('П')] = 'G'
translation[ord('Р')] = 'H'
translation[ord('О')] = 'J'
translation[ord('Л')] = 'K'
translation[ord('Д')] = 'L'
translation[ord('Ж')] = ':'
translation[ord('Э')] = '"'
translation[ord('Я')] = 'Z'
translation[ord('Ч')] = 'X'
translation[ord('С')] = 'C'
translation[ord('М')] = 'V'
translation[ord('И')] = 'B'
translation[ord('Т')] = 'N'
translation[ord('Ь')] = 'M'
translation[ord('Б')] = '<'
translation[ord('Ю')] = '>'
translation[ord(',')] = '?'

translation[ord(':')] = '^'
translation[ord('?')] = '&'
translation[ord(';')] = '$'

s1 = str(use_proverbs)
s2 = s1.translate(translation)

#Get PICTURE MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
img_path = np.array([])
count2 = 0

#Get the path/directory
photo_dir = 'D:/Photo masterpieces/Photos/For Uploads'
#Check if the directory is exist
if (path.exists(photo_dir)==False):
    print("Check the path. The path does not exist: <<" + photo_dir + ">>")
    sys.exit()

trash_path = "D:\Photo masterpieces\Photos\For Reserve"
#Check if the directory is exist
if (path.exists(trash_path)==False):
    print("Check the path. The path does not exist: <<" + trash_path + ">>")
    sys.exit()

# iterate over files in that directory
for images in glob.iglob(f'{photo_dir}/*'):

    # check if the image ends with png/jpg/jpeg/JPG
    if (images.endswith(".png") or images.endswith(".jpg")\
        or images.endswith(".jpeg") or images.endswith(".JPG")):
        count2 += 1
        img_path = np.append(img_path, images)

#Check if images is exist
if (str(img_path)=="[]"):
    print("No Image in folder: " + photo_dir)
    sys.exit()

use_img_path = img_path[randint(0, count2-1)]

#UPLOAD PICTURE MODULE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
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
#Check the exif-data
if exifdata==None:
    print("No exifdata")
    text = str(use_proverbs)
    # IDK How to solve "'NoneType' object is not subscriptable"
    # If someone know? Please text me
else:
    text = "\n\n"+ \
        str(exifdata[42035]) + " " + str(exifdata[42036]) + "\n" + \
        str(exifdata[37386]) + " mm (" + str(exifdata[41989]) + "mm equivalent)\n" + \
        "1/"+ str(1/exifdata[33434]) + " sec\n" + \
        "f/"+ str(exifdata[33437]) + "\n" + \
        "ISO "+ str(exifdata[34855])
image.close()

#Facebook OPEN CV +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
webbrowser.open('https://www.facebook.com/.....')
time.sleep(6)
myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'D:\Coding API\Facebook API\Screenshot.png')
img = cv.imread('D:\Coding API\Facebook API\Screenshot.png',0)
img2 = img.copy()

#Check if the directory is exist
if (path.exists("D:\Coding API\Facebook API")==False):
    print("Check the path. The path does not exist: <<D:\Coding API\Facebook API>>")
    sys.exit()

template = cv.imread('D:\Coding API\Facebook API\WriteSMTH.png',0)
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:
    print(meth)

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
time.sleep(5)
pyautogui.moveTo(top_left[0] + w/2, top_left[1]-200)

#COPY IMAGE MODULE+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from io import BytesIO
import win32clipboard

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

filepath = use_img_path
image = Image.open(filepath)

output = BytesIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()

send_to_clipboard(win32clipboard.CF_DIB, data)


#CHECK KEYBOARD MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import ctypes
user32 = ctypes.WinDLL('user32', use_last_error=True)
curr_window = user32.GetForegroundWindow()
thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
klid = user32.GetKeyboardLayout(thread_id)
lid = klid & (2**16 - 1)
lid_hex = hex(lid)
if (lid_hex=="0x409"):
    pyautogui.hotkey("shift", "alt")

#WRITE KEYBOARD MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
time.sleep(5)
pyautogui.click()
pyautogui.write(str(s2), interval=0.02)
pyautogui.hotkey("shift", "alt")
pyautogui.click()
pyautogui.write(text, interval=0.02)
pyautogui.hotkey('ctrl', 'v')

time.sleep(30)

#Facebook OPEN CV +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'D:\Coding API\Facebook API\Screenshot2.png')
img = cv.imread('D:\Coding API\Facebook API\Screenshot2.png',0)
img2 = img.copy()


template = cv.imread('D:\Coding API\Facebook API\Post.png',0)
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:
    print("Lol")

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


#UPLOAD CONTENT ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

pyautogui.moveTo(top_left[0] + w/2, top_left[1]+ h/2)
#pyautogui.click()

#DELETE PICTURE MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os, os.path
import shutil

file_path = str(use_img_path)

#Move to another directory
if os.path.isfile(file_path):
    shutil.move(use_img_path, trash_path)
    print("File has been moved to <<Reserve>>")
else:
    print("File does not exist")

