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
  
def framework(request, id):

  frm = Framework.objects.get(id=id)

  return render(request, 'framework.html', {'framework': frm})
  
def edit(request, id):
  
  frm = Framework.objects.get(id=id)
  
  return render(request, 'edit.html', {'framework': frm})
  
def delete(request, id):

  Framework.objects.filter(id=id).delete()
  
  return render(request, 'delete.html')

def new(request):
  
  return render(request, 'new.html')  
  
def added(request):
  if request.method == 'POST':
    p_commentaire = request.POST['commentaire']
    p_language = request.POST['language']
    p_nom = request.POST['nom']
    new_obj = Framework(nom=p_nom, commentaire=p_commentaire, language=p_language)
    new_obj.save()
  
    return render(request, 'added.html')  
  
def record(request, id):
  if request.method == 'POST':
	p_commentaire = request.POST['commentaire']
	p_language = request.POST['language']
	p_nom = request.POST['nom']
	Framework.objects.filter(id=id).update(commentaire=p_commentaire, nom=p_nom, language=p_language)
	return render(request, 'edited.html')