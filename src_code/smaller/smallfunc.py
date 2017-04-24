import random
import string
from django.conf import settings

maxi=getattr(settings,"MAX", 20)
mini=getattr(settings,"MIN",7)



def code_generator(size=mini,chars=string.ascii_lowercase+string.digits):
		'''new_code=''
		for _ in range(size):
			new_code+=random.choice(chars)
		return new_code'''
		return ''.join(random.choice(chars) for _ in range(size))

def code_create(instance,size=mini):
	finalcode=code_generator(size=size)
	
	clas=instance.__class__
	
	queryset=clas.objects.filter(newurl=finalcode).exists()
	
	if queryset:
		return code_create(size=size)
	return finalcode
 


