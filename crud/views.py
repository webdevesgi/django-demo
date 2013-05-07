#-*- coding: utf-8 -*-
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from models import Framework

def home(request):
  
  framework_list = Framework.objects.order_by('nom')
  language_list = Framework.objects.all().values('language').distinct()
  
  return render(request, 'allframework.html', {'framework_list': framework_list, 'language_list':language_list})
  
def language(request, language):

  framework_list = Framework.objects.filter(language=language)
  
  return render(request, 'framework_language.html', {'framework_list': framework_list, 'language':language})