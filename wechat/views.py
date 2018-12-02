from django.shortcuts import render
import json
import requests
import base64
from django.http import HttpResponse
import logging
from wechat.models import Person

LOG_FORMAT = "%(asctime)s- %(levelname)s - %(message)s"
logging.basicConfig(filename="my.log",level=logging.DEBUG,format = LOG_FORMAT)

# Create your views here.

def login(request):
    if request.method == "POST":
        #get code from post json
        body = request.body
        body = str(body, encoding = "utf-8")
        js_code = json.loads(body)['code']


        #post json to api so that we can get session_key and openid
        appid = "wxe43c3c66fd9b5591"
        secret = "8111e29229a5427e9196574f8c36c7dc"
        grant_type = "authorization_code"
        postData = {
            "appid" : appid,
            "secret" : secret,
            "js_code" : js_code,
            "grant_type" : grant_type
        }
        url = "https://api.weixin.qq.com/sns/jscode2session"
        result = requests.post(url,postData)
        result = result.text


        #get session_key and openid
        session_key = json.loads(result)['session_key']
        openid = json.loads(result)['openid']

        #转化为base64
        s1 = bytes(result,encoding="utf8")
        session = base64.b64encode(s1)
        session = str(session,encoding="utf-8")


        return_data={
            'session' : session
        }


        #判断是否存在，如果不存在则创建，如果存在则更新
        if Person.objects.filter(openid=openid).count():
            print("update")
            Person.objects.filter(openid=openid).update(session=session,session_key=session_key)   
        else:
            print("couldn't find the person")
            Person.objects.create(session = session, session_key=session_key, openid=openid)


        content=json.dumps(return_data)
        response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='200',reason='success',charset='utf-8')

        return response
    else:
        return render(request,'mypage/Love.html',{})


def setMsg(request):
    if request.method == "POST":
        print("step into setMsg")
        body = request.body
        body = str(body, encoding = "utf-8")
        print("body is " , body)


        session = json.loads(body)['session']
        nickname = json.loads(body)['nickname']
        name = json.loads(body)['name']
        gender = json.loads(body)['gender']
        age = json.loads(body)['age']
        city = json.loads(body)['city']
        latitude = json.loads(body)['latitude']
        longitude = json.loads(body)['longitude']



        result = base64.b64decode(session)
        session_key = json.loads(result)['session_key']
        openid = json.loads(result)['openid']

        print(openid)


        Person.objects.filter(openid=openid).update(nickname=nickname,name=name,gender=gender,age=age,city=city,latitude=latitude,longitude=longitude)

        print("setMsg succeed!")



        response = HttpResponse(content="succeed to set Msg!", content_type='application/json;charset = utf-8',status='200',reason='success',charset='utf-8')
        return response