#-*- coding: utf-8 -*-
# Create your views here.

from django.shortcuts import render

def home(request):
  nombre = int(12)
  
  return render(request, 'lol.html', locals())