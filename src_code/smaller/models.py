import random
import string
from django.db import models
from django.conf import settings
from smaller.smallfunc import code_generator,code_create
from .forms import validate_url,validate_www
from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse

maxi=getattr(settings,"MAX", 20)
mini=getattr(settings,"MIN",7)
class smallmanager(models.Manager):
	#def all(self, *args ,**kwargs):
	#	qsfinal=super(smallmanager ,self).all(*args,**kwargs)
	#	qs=qsfinal.filter(active=True)
	#	return qs
	def refresh(self,items=10):
		print (items)
		qs2=smallurl.objects.filter(id__gte=1)
		print ('qs2',qs2)
		num=0
		if items is not None and isinstance(items,int):
			qs2=qs2.order_by('-id')[:items]
		for q in qs2:
			print ('present url is:',q)
			q.newurl = code_create(q)
			print ('original url:',q.url)
			print('id',q.id)
			print ('num',num)
			num+= 1
			q.save()
			print ('newurl is',q.newurl)
			if num==items:
				break
		return "number of new codes{i}".format(i=num)
	def all_set(self):
		qs3=smallurl.objects.count()
		return qs3




# Create your models here.
class smallurl(models.Model):
	url = models.CharField(max_length=220,default=None,validators=[validate_url,validate_www])
	newurl = models.CharField(max_length=maxi,null=True,blank=True,unique=True)
	active=models.BooleanField(default=True)
	
	objects=smallmanager()
	
	def save(self,*args,**kwargs):
		#if self.newurl is None or self.newurl=='':
		self.newurl = code_generator()

		super(smallurl,self).save(*args,**kwargs)

	def __str__(self):
		return (self.newurl)

	def newshorturl(self):
	
		print("newshort",self.newurl)
		urlpath = reverse("newurls",kwargs={'newurl':self.newurl},host='www' , scheme= 'http',port='8000')
		print ("urlpath is",urlpath)
		return urlpath



