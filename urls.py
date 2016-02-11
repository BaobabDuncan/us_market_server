'''
Created on Apr 26, 2011

@author: woosanguk
'''
from django.conf.urls.defaults import patterns,include

urlpatterns = patterns('',  
)

# index page
urlpatterns += patterns('viewIndex.handler_Index',
    (r'^$','handler_Index'),
    (r'iphone','handler_Iphone'),
    (r'redirect/','handler_Redirect'),
)
