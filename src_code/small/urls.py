from django.conf.urls import url
from django.contrib import admin

from smaller.views import urlclasses,Homepage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^a/(?P<newurl>[\w-]+)/$',urls),
    url(r'^(?P<newurl>[\w-]+)/$',urlclasses.as_view(),name="newurls"),
    url(r'^shorten1.html',Homepage.as_view())


]
 
