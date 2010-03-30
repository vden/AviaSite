#from fts import 

from django.http import HttpResponse
from django.shortcuts import render_to_response

from cms.models.pagemodel import Page

def search(request, search_string):
    res = Page.objects.search(search_string)
    
    return render_to_response("core/search.html", {"result": res, "search_string": search_string, "request": request})
