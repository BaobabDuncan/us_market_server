'''
Created on Apr 26, 2011

@author: woosanguk
'''
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect




def handler_Index(request): 
    sViewTitle = "index"
    t = loader.get_template('index.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c));
    

def handler_Redirect(request):    
    sViewTitle = "redirect"
    t = loader.get_template('redirect.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c));

def handler_Iphone(request):
    sViewTitle = "iphone"
    t = loader.get_template('iphone.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c));