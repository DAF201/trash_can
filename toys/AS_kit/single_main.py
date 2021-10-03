import json
import time
import datetime
from datetime import datetime
import os
from multiprocessing import Process
import multiprocessing
import hashlib
import requests
import re
from os import path
import pickle
from cotrace import auto_call_trace

auto_call_trace([__file__])

def who():
    current_path = os.getcwd()
    print('who do you want to see today?')
    print('please enter the number corresponds, no need to separate with a comma')
    print('1.AWA 2.Bella 3.Carol 4.Diana 5.Elieen')
    uid = []
    person = input()
    if '1' in person:
        uid.append('672346917')

    if '2' in person:
        uid.append('672353429')

    if '3' in person:
        uid.append('351609538')

    if '4' in person:
        uid.append('672328094')

    if '5' in person:
        uid.append('672342685')

    if len(uid) == 0:
        print('invaild input,exiting')
        time.sleep(3)
        exit()
    with open(current_path+'who.json', 'w') as file:
        json.dump(uid, file)


def setup():
    current_path = os.getcwd()
    setting = {}
    print('want to enable language filter?')
    print('yes or no')
    demand_language_filter = input()
    if demand_language_filter == 'yes':
        setting['demand_language_filter'] = True
    else:
        setting['demand_language_filter'] = False

    if demand_language_filter:
        login_data = sess_and_csrf()
        setting['comment_data'] = auth(login_data)

    print('wanna leave a like before you go?')
    print('yes or no')
    demand_like = input()
    if demand_like == 'yes':
        setting['demand_like'] = True
    else:
        setting['demand_like'] = False

    print('download the video?')
    print('yes or no')
    demand_download = input()
    if demand_download == 'yes':
        setting['demand_download'] = True
    else:
        setting['demand_download'] = False

    with open(current_path+'setting.json', 'w') as file:
        json.dump(setting, file)


def sess_and_csrf():
    current_path = os.getcwd()
    login_data = {}

    if path.isfile(current_path + 'data.txt'):
        inputFile = current_path + 'data.txt'
        fd = open(inputFile, 'rb')
        dataset = pickle.load(fd)
        sessdata = dataset[0]
        csrf = dataset[1]
    else:
        print('please enter sessdata')
        sessdata = input()
        print('please enter csrf')
        csrf = input()
        dataset = [sessdata, csrf]
        outputFile = current_path + 'data.txt'
        fw = open(outputFile, 'wb')
        pickle.dump(dataset, fw)
        fw.close()

    login_data['sessdata'] = sessdata
    login_data['csrf'] = csrf
    return login_data


def new_video_check(uid):
    current_path = os.getcwd()
    video_data = {}
    fetch_data_url = 'http://api.bilibili.com/x/space/arc/search'
    param = {
        'mid': uid,
        'order': 'pubdate',
        'pn': '1',
        'ps': '1'
    }
    reply = requests.get(fetch_data_url, params=param).text
    title = json.loads(reply)['data']['list']['vlist'][0]['title']
    av = json.loads(reply)['data']['list']['vlist'][0]['aid']
    reply = {}
    reply['title'] = title
    reply['av'] = av

    if path.isfile(current_path + '\last_video_fetched%s.json' % uid):
        with open(current_path + '\last_video_fetched%s.json' % uid, 'r') as saved_data:
            video_data = json.load(saved_data)
            if video_data['av'] != av or video_data['title'] != title:
                video_data['title'] = title
                video_data['av'] = av
                video_data['updated'] = True
                print('updating data for %s' % uid)
            else:
                video_data['updated'] = False
                print('no new video found under %s' % uid)
        with open(current_path + '\last_video_fetched%s.json' % uid, 'w') as saved_data:
            json.dump(video_data, saved_data)
    else:
        with open(current_path + '\last_video_fetched%s.json' % uid, 'w') as saved_data:
            video_data['title'] = title
            video_data['av'] = av
            video_data['updated'] = True
            json.dump(video_data, saved_data)
            print('creating new record for %s' % uid)
    return video_data


def like_and_coins(video_data, login_data):
    check_like_url = 'http://api.bilibili.com/x/web-interface/archive/coins'
    like_url = 'http://api.bilibili.com/x/web-interface/coin/add'
    params_check = {
        'aid': video_data['av']
    }
    params_like_and_coins = {
        'aid': video_data['av'],
        'multiply': '2',
        'select_like': '1',
        'csrf': login_data['csrf']
    }
    cookie = {
        'SESSDATA': login_data['sessdata']
    }
    reply = requests.get(
        check_like_url, params=params_check, cookies=cookie).text
    reply = json.loads(reply)
    if reply['data']['multiply'] == 0:
        reply = requests.post(
            like_url, params=params_like_and_coins, cookies=cookie).text
        reply = json.loads(reply)
        if reply['data']['like'] == True:
            print('you give %s two coins and a like' % video_data['av'])
        else:
            print('fail to like the video')
            print(reply)
    else:
        print('you have give this video coins')


def sensative_comments(video_data):
    final = []
    user_uid = []
    content = []
    url = 'http://api.bilibili.com/x/v2/reply'
    params = {
        'type': '1',
        'oid': video_data['av'],
        'pn': '1',
        'ps': '49'
    }
    reply = requests.get(url, params=params).text
    reply = json.loads(reply)
    reply = reply['data']['replies']
    for x in reply:
        for y in ['隐私', '中之人', '负面', '发散', '[大哭]', '魔怔', '路人', '珈乐是谁', '不熟', '恶心', '离谱', '塔塔开', 'ttk', '乐华', '嘻嘻嘻', '懂不懂', '资本', '厉害', '[吃瓜]', '[偷笑]', '[鼓掌]', '[星星眼]', '机器人', '战场']:
            if y in x['content']['message'].encode('utf-8').decode('utf-8'):
                user_uid.append(x['member']['mid'])
                content.append(x['content']['message'])
    final = dict(zip(user_uid, content))
    for key in final:
        print(key+'\n'+final[key]+'\n')
    with open('user_and_comments@%s.json' % video_data['av'], 'w') as file:
        json.dump(final, file)


def download(login_data, video_data):
    def download_single_video(url, name, headers):

        res = requests.get(url, headers=headers)
        video_pattern = '__playinfo__=(.*?)</script><script>'
        playlist_info = json.loads(re.findall(video_pattern, res.text)[0])
        video_url = playlist_info['data']['dash']['video'][0]['baseUrl']
        audio_url = playlist_info['data']['dash']['audio'][0]['baseUrl']

        save_file(video_url, "%s.video" % name, headers)
        save_file(audio_url, "%s.audio" % name, headers)
        print('{} finished downloading:'.format(name))

    def save_file(url, type, headers):

        download_content = requests.get(url, headers=headers).content

        with open('{}.mp4'.format(type), 'wb') as output:
            output.write(download_content)

    def get_list_info(url, headers):

        aid_pattern = 'window.__INITIAL_STATE__={"aid":(\d*?),'
        res = requests.get(url, headers=headers)
        aid = re.findall(aid_pattern, res.text)[0]
        playlist_json_url = 'https://api.bilibili.com/x/player/pagelist?aid={}'.format(
            aid)
        json_info = json.loads(requests.get(
            playlist_json_url, headers=headers).content.decode('utf-8'))['data']
        return json_info

    def download_video():

        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
                   'cookie': "SESSDATA:%s" % login_data['sessdata']
                   }
        base_url = 'https://www.bilibili.com/video/av%s' % video_data['av']
        json_info = get_list_info(base_url, headers)

        for i in json_info:
            p = i['page']
            name = 'P{} - {}'.format(p, i['part'])
            url = base_url + '?p={}'.format(p)
            download_single_video(url, name, headers)

    download_video()


def comment(video_data, auth, login_data):
    if auth['auth'] == True:
        comment_url = 'http://api.bilibili.com/x/v2/reply/add'
        params = {
            'type': '1',
            'oid': video_data['av'],
            'message': auth['comment']+'\nAS_kit1.5测试版@%s' % datetime.now(),
            'csrf': login_data['csrf'],
            'SESSDATA': login_data['sessdata']
        }
        cookie = {
            'SESSDATA': login_data['sessdata']
        }
        text = requests.post(comment_url, params=params, cookies=cookie).text
        text = json.loads(text)
        if text['data']['success_toast'] == '发送成功':
            print('you said %s' % auth['comment'])
        else:
            print('comment failed')
            print(text)
    else:
        print('you have no access to it')


def auth(login_data):
    comment_data = {}
    print('wanna say something today?')
    print('yes or no')
    demand = input()

    if demand == 'yes':
        print('what do you want to say today')
        content = input()
        print('enter signature to continue \n signature = MD5 value of your comment + your csrf \n your csrf is %s' %
              login_data['csrf'])

        signautre = input()
        sign = login_data['csrf'] + content
        sign = hashlib.md5(sign.encode('UTF-8')).hexdigest()

        if signautre == sign:
            print('success')
            comment_data['comment'] = content
            comment_data['auth'] = True
            return comment_data
        else:
            print('failed')
            comment_data['auth'] = False
            return comment_data
    else:
        print('keep quiet is also not bad')
        comment_data['auth'] = False
        return comment_data


def run(uid, login_data, demand_language_filter, comment_data, demand_like, demand_download):
    while(True):
        video_data = new_video_check(uid)
        if video_data['updated'] == True:
            if demand_language_filter:
                sensative_comments(video_data)
            if comment_data['auth']:
                comment(video_data, comment_data, login_data)
            if demand_like:
                like_and_coins(video_data, login_data)
            if demand_download:
                download(login_data, video_data)
            print('finished at @%s for %s' % (datetime.now(), uid))
        time.sleep(900)


process_list = []
if __name__ == '__main__':
    multiprocessing.freeze_support()
    who()
    current_path = os.getcwd()
    login_data = sess_and_csrf()
    with open(current_path+'who.json', 'r') as file:
        person = json.load(file)

    setup()
    with open(current_path+'setting.json', 'r') as file:
        file = json.load(file)
        demand_language_filter = file['demand_language_filter']
        comment_data = file['comment_data']
        demand_like = file['demand_like']
        demand_download = file['demand_download']

    for i in range(0, len(person)):
        p = Process(target=run, args=(
            person[i], login_data, demand_language_filter, comment_data, demand_like, demand_download))
        p.start()
        process_list.append(p)

    for i in process_list:
        p.join()
