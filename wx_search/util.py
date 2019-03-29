# -*- coding:utf-8 -*-
from wx_search.models import User
from django.contrib.auth.hashers import make_password

def save_user():
	password = "password"
	new_password = make_password(password)
	print("new password is   "+new_password)


save_user()