import requests
from const import *
import json
import time
import pathlib
from os import path
import random

PATH = str(pathlib.Path(__file__).parent.resolve())


def fetch():
    fetch_params = {
        'mid': UID,
        'order': 'pubdate',
        'pn': '1',
        'ps': '1'
    }
    reply = requests.get(fetch_url, params=fetch_params, cookies=cookie).text
    reply = json.loads(reply)
    if reply!={'code': 0, 'message': '0', 'ttl': 1, 'data': {'list': {'tlist': None, 'vlist': []}, 'page': {'pn': 1, 'ps': 1, 'count': 0}}}:
        aid = reply['data']['list']['vlist'][0]['aid']
        title = reply['data']['list']['vlist'][0]['title']
        video_info = {}
        video_info['aid'] = aid
        video_info['title'] = title
        with open(PATH+'last_fetch.json', 'w') as last_video:
            json.dump(video_info, last_video)
        return video_info['aid']
    else:
        print('no video found')
        pass


def comment(aid, comment, login_data):
    params = {
        'type': '1',
        'oid': aid,
        'message': comment,
        'csrf': login_data['csrf'],
        'SESSDATA': login_data['sessdata']
    }
    reply = requests.post(comment_url, headers=header,
                          params=params, cookies=cookie).text
    reply = json.loads(reply)
    if reply['code'] == 0:
        print('成功评论')
    elif reply['code'] == 12051:
        print('重复评论')
        print(reply)
    else:
        print('失败评论')
        print(reply)


def wishper(message, longin_data):
    params = {
        'msg[sender_uid]': longin_data['uid'],
        'msg[receiver_id]': UID,
        'msg[receiver_type]': '1',
        'msg[msg_type]': '1',
        'msg[dev_id]': DEV_ID,
        'msg[timestamp]': int(time.time()),
        'msg[content]': message,
        'csrf': longin_data['csrf']
    }
    reply = requests.post(wishper_url, params=params, cookies=cookie).text
    reply = json.loads(reply)
    if reply['code'] == 0:
        print('私信发送成功')
    else:
        print('私信发送失败')
        print(reply)


def login_data():
    login_data = {}
    if path.isfile(PATH + 'data.json'):
        inputFile = PATH + 'data.json'
        with open(inputFile, 'r') as inputFile:
            dataset = json.load(inputFile)
            sessdata = dataset['sessdata']
            csrf = dataset['csrf']
            uid = dataset['uid']
    else:
        print('please enter sessdata')
        sessdata = input()
        print('please enter csrf')
        csrf = input()
        print('please enter your UID')
        uid = input()
        login_data['sessdata'] = sessdata
        login_data['csrf'] = csrf
        login_data['uid'] = uid
        with open(PATH + 'data.json', 'w')as outputFile:
            json.dump(login_data, outputFile)
    login_data['sessdata'] = sessdata
    login_data['csrf'] = csrf
    login_data['uid'] = uid
    return login_data


def main():
    print('want to say today?')
    content = input()
    login = login_data()
    counter=0
    while True:
        fetched=fetch()
        dies=random.randrange(1,6)
        with open(PATH+'last_fetch.json','r') as file:
            save=json.load(file)
        if save['aid']!=fetched:
            print(dies)
            comment(fetched,content,login)
            for x in range(dies):
                wishper(content,login)
        else:
            print(save['aid'])
            print(fetched)
        print(counter)
        counter+=1
        time.sleep(dies*dies*dies)
main()
