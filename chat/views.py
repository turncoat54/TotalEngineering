#chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
import logging

LOG_FORMAT = "%(asctime)s- %(levelname)s - %(message)s"
logging.basicConfig(filename="my.log",level=logging.DEBUG,format = LOG_FORMAT)

def index(request):
	return render(request, 'chat/index.html', {})

def room(request, room_name):
	logging.info("room step in")
	return render(request, 'chat/room.html',{
		'room_name_json': mark_safe(json.dumps(room_name))
	})
