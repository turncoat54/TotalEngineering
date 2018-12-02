from django.db import models

# Create your models here.
		
class Person(models.Model):
    session = models.CharField(max_length = 255, null = False)
    session_key = models.CharField(max_length = 255, null = False)
    openid = models.CharField(max_length = 255, null = False, primary_key = True)
    nickname = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    gender = models.IntegerField(null = True)
    age = models.IntegerField()
    city = models.CharField(max_length = 255)
    latitude = models.FloatField(max_length = 11)
    longitude = models.FloatField(max_length = 11)
    """docstring for Person"""
    # def __init__(self,arg):
    #     super(Person, self).__init__()
    #     self.arg = arg