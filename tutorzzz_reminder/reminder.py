import json
import requests
import config

def __getList():
    HEADERS = {
        'Cookie': config.tutorzzzCookie,
        'Content-Type': 'application/json' 
    }
    res = requests.post(config.tutorzzzURL, headers = HEADERS, json = config.tutorzzzReqBody)
    if res.status_code == 200:
        try:
            body = res.json()
        except:
            print("[ERROR]: tutorzzz cookie expired")
            return
        if body['msg'] == '操作成功':
            return body['data']['data']

def __filter():
    wanted = []
    assignList = __getList()
    if assignList == None:
        return
    for al in assignList:
        if al['orderStatus'] == '招募中':
            d = {}
            d['id'] = al['id']
            d['title'] = al['title']
            d['devPrice'] = al['devPrice']
            wanted.append(d)
    return wanted

def remind():
    wanted = __filter()
    if wanted == None:
        return
    if len(wanted) == 0:
        return '尚无招募任务'
    content = '招募中任务\n'
    for a in wanted:
        content += a['id'] + '\t' + a['title'] + '\t' + a['devPrice'] + '\n'
    return content
