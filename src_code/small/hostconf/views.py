from django.conf import settings
from django.http import HttpResponseRedirect

DEF = getattr(settings, "DEF", "www.vishshort.com:8000")

def wildreq(request, path=None):
	new_url = DEF
	if path is not None:
		new_url = DEF + "/" + path
	return HttpResponseRedirect(new_url)
