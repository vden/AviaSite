#from fts import 

from django.http import HttpResponse
from django.shortcuts import render_to_response

from cms.models.pagemodel import Page
from core.models import Advantage
from news.models import News

from django.template import RequestContext

import settings

def search(request):
    
    search_string = request.GET.get('search', '')

    res = [ {'title': x.get_title(), 'url': x.get_absolute_url()} for x in Page.objects.search(search_string)]
    res += [{'title': x.title, 'url': '/news/%s/'%x.id} for x in News.objects.search(search_string)]
    request.search_string = search_string
    
    return render_to_response("core/search.html", {"result": res}, context_instance=RequestContext(request))

def index(request):
    advantages = Advantage.objects.all().order_by('id')

    news = News.objects.all().order_by('-date').filter(published=True)[:2]
    return render_to_response("core/index.html", {"advantages": advantages, "news": news}, context_instance=RequestContext(request))

def sitemap(request):
	soft_root = Page.objects.filter(soft_root = True)[0]

	level1st = Page.objects.filter(parent=soft_root, published=True, in_navigation=True)
	
	for p in level1st:
		p.mchildren = Page.objects.filter(parent=p, published=True, in_navigation=True)
		for pp in p.mchildren:
			pp.mchildren = Page.objects.filter(parent=pp, published=True, in_navigation=True)

	return render_to_response("core/sitemap.html", {"root": soft_root, "objects": level1st}, context_instance=RequestContext(request))
