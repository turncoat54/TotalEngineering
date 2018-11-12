from django.shortcuts import render
import json
import requests
import base64
from django.http import HttpResponse
import logging

LOG_FORMAT = "%(asctime)s- %(levelname)s - %(message)s"
logging.basicConfig(filename="my.log",level=logging.DEBUG,format = LOG_FORMAT)

# Create your views here.

def login(request):
    if request.method == "POST":

        # person.save()




        print("step in here")
        body = request.body
        body = str(body, encoding = "utf-8")
        print("body is " + body)
        js_code = json.loads(body)['code']
        print("js_code is " + js_code)
        
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
        logging.info("the result is" + result)
        print("result is "+ result)
        session_key = json.loads(result)['session_key']
        logging.info("get session_key succeed!")
        openid = json.loads(result)['openid']
        logging.info("get openid succeed!")

        s1 = bytes(result,encoding="utf8")
        session = base64.b64encode(s1)
        session = str(session,encoding="utf-8")

        # redis.set(session,result)
        # print("set success!")


        return_data={
            'session' : session
        }

        from wechat.models import Person
        Person.objects.create(session = session, session_key=session_key, openid=openid)


        # sql = "INSERT IGNORE into lover (session,session_key,openid) values('%s','%s','%s')" % (session, session_key, openid)

        # # sql = "INSERT INTO lover (session, session_key, openid) VALUES ('%s','%s','%s')" % (session, session_key, openid)
        # # db.ping(reconnect=True)    
        # cursor.execute(sql)
        # db.commit()
        # db.close()
        # logging.info("finish INSERTING")

        content=json.dumps(return_data)

        response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='200',reason='success',charset='utf-8')

        return response
    else:
        return render(request,'mypage/Love.html',{})