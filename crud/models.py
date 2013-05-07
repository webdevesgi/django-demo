#-*- coding: utf-8 -*-
from django.db import models
 
class Framework(models.Model):
	id = models.AutoField(primary_key=True)
	nom = models.CharField(max_length=100)
	language = models.CharField(max_length=100)
	commentaire = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):

		return u"%s" % self.nom