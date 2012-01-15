'''
Created on Jan 15, 2012

@author: arif
'''
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'demo.demoapp.views.index', name='index'),
)
