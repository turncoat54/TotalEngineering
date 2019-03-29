from django.db import models

# Create your models here.


class Student(models.Model):
    nju_id = models.CharField(max_length = 255, null = False, primary_key = True)
    name = models.CharField(max_length = 255, null = False)
    pinyin = models.CharField(max_length = 255, null = False, default="test")
    phone_number = models.CharField(max_length = 20)
    phone_number2 = models.CharField(max_length = 20, null=True, default="15234721874")
    dorm_number = models.CharField(max_length = 10)
    major = models.CharField(max_length = 255)
    email_address = models.CharField(max_length = 255)
    email_address2 = models.CharField(max_length = 255, null = True)
    grade = models.IntegerField()
    avator = models.CharField(max_length=255,default="pig.jpg")

    """docstring for Person"""
    # def __init__(self,arg):
    #     super(Person, self).__init__()
    #     self.arg = arg


class User(models.Model):
	username = models.CharField(max_length=30,null=False,primary_key=True)
	password = models.CharField(max_length=255,null=False)
		