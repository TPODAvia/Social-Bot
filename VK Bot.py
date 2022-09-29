#IMPORTING LIBS
import vk_api
from PIL.ExifTags import TAGS
from PIL import Image
import os, os.path
import numpy as np
import glob
from random import randint


#KATE MOBILE MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
session = vk_api.VkApi(token="vk1.a.O9TFQM6vudNuJx71PbfsspzlUV2OUPLdXcBVmpImkj4tYbXAVyv8c_aceNAfMJ4UlX_x29g5wUJ99utM76-H0p23nuP0SOl1pno5DGisVs_qkuhpr0P3JH2dE3nMNuyWH23SWOe2IvrCGav1LAlyaeXA5j9EI681Qm1sYsIYBOf7x2OYfn-SaP8BGX6JBWPs")
vk = session.get_api()

def get_user_status(user_id):
    status = session.method("status.get",{"user_id": user_id})
    print(status["text"])

def send_user_message(user_id, text):
    session.method("messages.send",{"random_id": 0 ,"peer_id": user_id, "message": text})
    
#Done____________________________________________________________________________
#get_user_status()
send_user_message(487724496, "Hello World!")



#Experiment____________________________________________________________________________
from vk_api.longpoll import VkLongPoll, VkEventType

def get_user_message(user_id):
    message = session.method("messages.get",{"user_id": user_id, "filters": 8})
    print(message)

chat_id=9
user_id = 290618168

#f = open('new.txt', "x", encoding="utf-8")
f = open('new.txt', "+w", encoding="utf-8")

lastMessage = vk.messages.getHistory(count =1, peer_id=2000000000+chat_id, user_id=user_id)
pages=int(lastMessage['items'][0]['id']/200+1)
print("Pages (page -200 messages): " + str(pages))

history = vk.messages.getHistory(count=2, peer_id=487724496, user_id=user_id)
history = history['items']
for j in reversed(history):
    f.write(str(j)+"\n")

print(str(pages)+" out of " + str(pages))
f.close()
print("Done Reading")


#GET TEXT MODULE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
with open('D:/Coding API/new.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
count = 0

# Strips the newline character
proverbs = np.array([])
for line in lines:
    count += 1
    #print("Line{}: {}".format(count, line.strip()))
    proverbs = np.append(proverbs, line.strip())

use_proverbs = proverbs[0]

print(proverbs[0]==str(j))