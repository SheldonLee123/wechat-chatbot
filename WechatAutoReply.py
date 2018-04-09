# -*- coding=utf-8 -*-
import requests
import itchat
import random

KEY = 'a2bd87304ad4415baaaee4d249ea7eee'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    print(msg["Text"])
    defaultReply = 'I received: ' + msg['Text']
    robots=['——By爱笑的流星雨','——By翔书记','——By反正不是本人']
    reply = get_response(msg['Text'])+random.choice(robots)
    print(reply)
    return reply or defaultReply

itchat.auto_login(hotReload=True)
itchat.run()
