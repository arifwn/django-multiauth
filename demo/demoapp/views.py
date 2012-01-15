'''
Created on Jan 15, 2012

@author: arif
'''
from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse

def index(request):
    t = get_template('demoapp/index.html')
    html = t.render(RequestContext(request, {}))
    return HttpResponse(html)