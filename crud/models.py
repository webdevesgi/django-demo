#-*- coding: utf-8 -*-
from django.db import models
 
class Framework(models.Model):
	nom = models.CharField(max_length=100)
	language = models.CharField(max_length=100)
	commentaire = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")

	def __unicode__(self):

		return u"%s" % self.titre