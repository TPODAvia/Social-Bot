#IMPORTING LIBS
import vk_api
from PIL.ExifTags import TAGS
from PIL import Image
import os, os.path
import numpy as np
from random import randint

#TEST TASK MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
import datetime
file = open(r'D:\Coding API\VK API\task.txt', 'a')

file.write(f'{datetime.datetime.now()} - The script ran \n')
'''

#KATE MOBILE MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
session = vk_api.VkApi(token="vk1.a.O9TFQM6vudNuJ...GX6JBWPs")
vk = session.get_api()

#GET UNREAD MODULE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
unread = session.method("messages.getConversations",{"filter": "unread"})
ItemsUnread = unread['items']
for j in reversed(ItemsUnread):
    str(j)
#print("Done Reading")

FromId = 112856336

if (ItemsUnread == []):
    print("No new messages")
else:
    #print("From ID: " + str(unread['items'][0]['last_message']['from_id']))
    #print("Date Is: " + str(unread['items'][0]['last_message']['date']))
    #print("Text Is: " + str(unread['items'][0]['last_message']['text']))

    
    if (unread['items'][0]['last_message']['from_id'] == FromId):
        
        #GET TEXT MODULE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        with open('D:/Coding API/VK API/Text.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        count = 0
        # Strips the newline character
        proverbs = np.array([])
        for line in lines:
            count += 1
            #print("Line{}: {}".format(count, line.strip()))
            proverbs = np.append(proverbs, line.strip())
        use_proverbs = proverbs[0]

        def send_user_message(user_id, text):
            session.method("messages.send",{"random_id": 0 ,"peer_id": user_id, "message": text})

        if (proverbs[0]==str(j)):
            send_user_message(290618168, "Не надо писать одной тоже пожалуйста")
        else:
            send_user_message(290618168, "День добрый отвечает бот. Я добавил вас в список автоответчика. Хозяйн больше не хочет отвечать ни на какие сообщения")

        f = open('D:/Coding API/VK API/new.txt', "+w", encoding="utf-8")
        for j in reversed(ItemsUnread):
            f.write(str(j)+"\n")

        f.close()
        #print("Done Writing")
