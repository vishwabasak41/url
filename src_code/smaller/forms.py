from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
	url_validator = URLValidator()
	val1=False
	val2=False
	try:
		url_validator(value)
	except:
		val1=True
		val2="http://"+value
		value=val2
		print("value",value)
	try:
		url_validator = URLValidator()
	except:
		val2=True

	if val1==True and val2==True:
		raise ValidationError("INVALID")
	return value



def validate_www(value):
	if not '.' in value:
		raise ValidationError("invalid")
	return value
		


class submiturl(forms.Form):
	#url2=forms.CharField(label='Submit url', validators=[validate_url,validate_www])
	url=forms.CharField(label='Submit url', validators=[validate_url,validate_www])

	''''def clean(self):
		cleaned_data=super(submiturl,self).clean()
		print(cleaned_data)
		url= cleaned_data.get('url')
		url_validator = URLValidator()
		try:
			url_validator(url)
		except:
			raise forms.ValidationError("INVALID")
		return url'''
		

	
		
 