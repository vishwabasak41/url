from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views import View
from smaller.models import smallurl
from smaller.forms import submiturl
from analytics.models import clicks
# Create your views here.

def hbv(request,*args,**kwargs):
	if request.method=="POST":
		print("request.POST is",request.POST)
	return render(request,"shorten1.html",{})





class Homepage(View):
	def get(self,request, *args, **kwargs):
		urlform= submiturl()
		
		context = {
		"title":"VISH.CO",
		"forme":urlform
		}
		#print(context)
		return render(request, "shorten1.html", context)

	def post(self,request,*args,**kwargs):
		uform = submiturl(request.POST or None)
		context={
		"title":"VISH.CO",
		"form":uform
		}
		template="shorten1.html"

		if uform.is_valid():
			print(uform.cleaned_data.get("url"))
			url=uform.cleaned_data.get("url")
			print ("url in is valid is",url)
			obj,created =smallurl.objects.get_or_create(url=url)
			context={
			"objects":obj,
			"created":created
			}
			if created:
				template="success.html"
			else:
				template="exists.html" 

		return render(request, template ,context)








#	obj=get_object_or_404(smallurl, newurl=newurl)	
#	return HttpResponseRedirect(obj.url)

class urlclasses(View):
	def get(self,request,newurl=None,*args,**kwargs):
		print ("newurl in view",newurl)
		qs=smallurl.objects.filter(newurl__iexact=newurl)
		print("qs",qs)
		obj=qs.first()
		print("qs.first is",obj)
		print(clicks.objects.createevent(obj))
		print ("obj.url is",obj.url)
		return HttpResponseRedirect(obj.url)
	
	






