from django.db import models

# Create your models here.
from smaller.models import smallurl

class clickmanager(models.Manager):
	def createevent(self, instance):
		if isinstance(instance,smallurl):
			print("instance is",instance)
			obj,created = self.get_or_create(small_url=instance)
			print("obj is" ,obj)
			print("created is ",created)
			obj.count += 1
			obj.save()
			print("count is ",obj.count)

			return obj.count
		return None

class clicks(models.Model):
	small_url=models.OneToOneField(smallurl)
	count=models.IntegerField(default=0)

	objects=clickmanager()

	def __str__(self):
		return "{i}".format(i=self.count)

