from django.shortcuts import render
from wx_search.models import Student
from wx_search.models import User
from django.http import HttpResponse
import json
from django.core import serializers

from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate

import wx_search.log_in as login
"""
状态码 418 代表密码错误
	  419 用户名不存在
	  420 token过期
"""

# Create your views here.

#搜索功能
def search_by_id(request):
	if request.method == "POST":
		body = request.body
		body = str(body, encoding = "utf-8")
		# print("body is " , body)
		json_result = json.loads(body)

		token = json_result['token']

		if not login.check_token(token):
			return_data={
				'message' : 'token失效'
			}
			content=json.dumps(return_data)
			response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='420',reason='token expired',charset='utf-8')

			return response

		nju_id = str(json_result['userID'])
		result = serializers.serialize('json',Student.objects.filter(nju_id = nju_id))
		# print("类型")
		# print(type(result))
		# print(result)


		return_data={
		    'result' : result
		}


		content=json.dumps(return_data)
		response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='200',reason='success',charset='utf-8')

		return response


def search_by_name(request):
	if request.method == "POST":
		body = request.body
		body = str(body, encoding = "utf-8")
		# print("body is " , body)
		json_result = json.loads(body)

		token = json_result['token']

		if not login.check_token(token):
			return_data={
				'message' : 'token失效'
			}
			content=json.dumps(return_data)
			response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='420',reason='token expired',charset='utf-8')

			return response

		choose = json_result['choose']
		search_page = json_result['search_page']
		name = json_result['name']

		result = []
		if choose == 2:
			result = json.loads(serializers.serialize('json',Student.objects.filter(pinyin__contains = name)))
		elif choose == 3:
			result = json.loads(serializers.serialize('json',Student.objects.filter(name__contains = name)))
		# result = serializers.serialize('json',Student.objects.filter(name__contains = name))

		result_length = len(result)
		return_result = []
		if((search_page+1)*10 <= result_length):
			# print(result[0])
			return_result = result[search_page*10 : (search_page+1)*10]
		else:
			return_result = result[search_page*10 : result_length]

		# print(return_result)



		return_data={
		    'result' : str(return_result)
		}


		content=json.dumps(return_data)
		response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='200',reason='success',charset='utf-8')

		return response


#动态返回学生信息
def dynamic_search(request):
	if request.method == "POST":
		body = request.body
		body = str(body, encoding = "utf-8")
		# print("body is " , body)
		json_result = json.loads(body)

		choose = json_result['choose']
		name = json_result['name']

		result = []
		if choose == 2:
			result = json.loads(serializers.serialize('json',Student.objects.filter(pinyin__contains = name)))
			# print(result)
		elif choose == 3:
			result = json.loads(serializers.serialize('json',Student.objects.filter(name__contains = name)))

		# result = json.loads(serializers.serialize('json',Student.objects.filter(name__contains = name)))
		# if(len(result)>0): print(len(result))
		name_list = []
		for item in result:
			dict_item = {
				'name': item['fields']['name'],
				'major': item['fields']['major']
			}
			name_list.append(dict_item)


		return_data={
			'result' : name_list
		}

		# print(result)
		# print(type(result))

		return HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='200',reason='success',charset='utf-8')

#修改学生信息
def modify(request):
	if request.method == "POST":
		body = request.body
		body = str(body, encoding = "utf-8")
		# print("body is " , body)



		
		json_result = json.loads(body)
		nju_id = str(json_result['nju_id'])
		attribute_name = json_result['attributeName']
		detail = json_result['detail']

		token = json_result['token']

		if not login.check_token(token):
			return_data={
				'message' : 'token失效'
			}
			content=json.dumps(return_data)
			response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='420',reason='token expired',charset='utf-8')

			return response

		attribute = {
			"major" : lambda detail : Student.objects.filter(nju_id=nju_id).update(major=detail),
			"phone_number" : lambda detail : Student.objects.filter(nju_id=nju_id).update(phone_number=detail),
			"phone_number2" : lambda detail : Student.objects.filter(nju_id=nju_id).update(phone_number2=detail),
			"dorm_number" : lambda detail : Student.objects.filter(nju_id=nju_id).update(dorm_number=detail),
			"email_address" : lambda detail : Student.objects.filter(nju_id=nju_id).update(email_address=detail),
			"email_address2" : lambda detail : Student.objects.filter(nju_id=nju_id).update(email_address2=detail),
		}

		attribute[attribute_name](detail)


		# Student.objects.filter(nju_id = nju_id).update(major=major,dorm_number=dorm_number,phone_number=phone_number,email_address=email_address)

		return_data={
			'message' : 'succeed'
		}
		content=json.dumps(return_data)
		response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='200',reason='success',charset='utf-8')

		return response


#登陆
def log_in(request):

	if request.method == "POST":

		# for i in range(0,12000):
		# 	nju_id = '1712'+(str)(i).zfill(5)
		# 	name = str((int)(i/5)) + "温宗儒"
		# 	phone_number = '13182962578'
		# 	dorm_number = '1B427'
		# 	major = '计算机科学与技术系'
		# 	email_address = '392207009@qq.com'
		# 	grade = 2
		# 	Student.objects.create(nju_id=nju_id, name=name, phone_number=phone_number,dorm_number=dorm_number,major=major,email_address=email_address,grade=grade)



		# return_data={
		# 	'message' : 'success'
		# }
		# content=json.dumps(return_data)
		# response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='200',reason='success',charset='utf-8')

		# return response



		body = request.body
		body = str(body, encoding = "utf-8")
		json_result = json.loads(body)
		username = json_result['username']
		password = json_result['password']

		# user = User()
		# user.username = "test"
		# user.password = make_password("test")
		# user.save()


		search_result = serializers.serialize('json',User.objects.filter(username = username))
		search_result_to_json = json.loads(search_result)



		if search_result_to_json:
			search_password = search_result_to_json[0]['fields']['password']

			if check_password(password,search_password):
			# if password == search_password:
				token = login.create_token(username)

				return_data={
					'message' : token
				}
				content=json.dumps(return_data)
				response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='200',reason='success',charset='utf-8')

				return response
			else:
				return_data={
					'message' : "密码错误!"
				}
				content=json.dumps(return_data)
				response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='418',reason='Wrong password',charset='utf-8')

				return response

		else:
			return_data={
				'message' : '账号不存在!'
			}
			content=json.dumps(return_data)
			response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='419',reason='Account does not exist',charset='utf-8')

			return response	
	else:
		return render("chengg !!!!!!")


#下次登陆时判断token是否在有效期内
def check_token(request):
	if request.method == "POST":
		body = request.body
		body = str(body, encoding = "utf-8")
	
		json_result = json.loads(body)
		token = json_result['token']

		# print("token is "+ token)
		if login.check_token(token):
			username = login.get_username(token)
			token = login.create_token(username)
			return_data={
				'message' : token
			}
			content=json.dumps(return_data)
			response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='200',reason='success',charset='utf-8')

			return response
		else:
			return_data={
				'message' : 'token过期'
			}
			content=json.dumps(return_data)
			response = HttpResponse(content=json.dumps(return_data), content_type='application/json;charset = utf-8',status='420',reason='token expired',charset='utf-8')

			return response