#from fts import 

from django.http import HttpResponse
from django.shortcuts import render_to_response

from cms.models.pagemodel import Page
from core.models import Advantage
from news.models import News

from django.template import RequestContext

def search(request, search_string):
    res = [x for x in Page.objects.search(search_string)]
    res += [x.body for x in Advantage.objects.search(search_string)]
    res += [x.title for x in News.objects.search(search_string)]
    
    return render_to_response("core/search.html", {"result": res, "search_string": search_string}, context_instance=RequestContext(request))

def index(request):
    advantages = Advantage.objects.all().order_by('?')[:3]
    return render_to_response("core/index.html", {"advantages": advantages}, context_instance=RequestContext(request))
