#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse(u'Hello,富兰克林.')



# Create your views here.
