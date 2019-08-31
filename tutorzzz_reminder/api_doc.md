* 获取access_token
```
https请求方式: GET
https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
```
参数|是否必须|说明
-|-|-
grant_type|是|获取access_token填写client_credential
appid|是|第三方用户唯一凭证
secret|是|第三方用户唯一凭证密钥，即appsecret