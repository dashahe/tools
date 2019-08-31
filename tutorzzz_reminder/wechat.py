import config
import requests
from reminder import remind

def getAccessToken():
    parameters = {
        'grant_type':'client_credential',
        'appid':config.appID,
        'secret':config.appsecret
    }
    res = requests.get(url=config.getAccessTokenURL, params=parameters)
    if res.status_code == 200:
        json = res.json()
        if 'errcode' in json:
            print('reach max api daily quota limit')
            return
        return json['access_token']

def tempMsgSend(content, openID):
    accessToken = getAccessToken()
    if accessToken == None:
        return
    parameters = {
        'access_token':accessToken
    }
    body = {
        'touser':openID,
        'template_id':config.templateID,
        'url':'https://tutorzzz.com',
        'data':{
            'list':{
                'value':content
            }
        }
    }
    res = requests.post(url=config.templateSendURL, params=parameters, json=body)
