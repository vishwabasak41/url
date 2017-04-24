from django.conf.urls import url

from .views import wildreq
urlpatterns = [
    url(r'^(?P<path>.*)', wildreq),
 

]