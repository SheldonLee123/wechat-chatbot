#coding=utf8
import itchat, time
from itchat.content import *

@itchat.msg_register([PICTURE,TEXT])
def simple_reply(msg):
    if msg['Type'] == TEXT:
        print(msg['Text'])
        itchat.send_msg(msg['Text'],msg['FromUserName'])
    if msg['Type'] == PICTURE:
    	itchat.send_image("1.jpg",msg['FromUserName'])

itchat.auto_login(True)
itchat.run()
