#-*- coding: utf-8 -*-
# Create your views here.

from django.shortcuts import render
from models import Framework

def home(request):
  
  framework_list = Framework.objects.order_by('nom')
  language_list = Framework.objects.all().values('language').distinct()
  
  return render(request, 'allframework.html', {'framework_list': framework_list, 'language_list':language_list})
  
def language(request):
  
  return render(request, 'language.html', locals())