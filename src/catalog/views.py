# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from django.template import RequestContext
from catalog.models import Equipment

from django.core.paginator import Paginator
import re, settings

def __search_catalog(name, cipher):
	res = Equipment.objects.order_by('name')
	if name and len(name): 
		name = re.sub(r'[\\\|/,\.\-]', '', name)
		res = res.filter(name__icontains=name)
	if cipher and len(cipher): 
		cipher = re.sub(r'[\\\|/,\.\-\ ]', '', cipher)
		res = res.filter(cipher__icontains=cipher)

	return res

def index(request):
    	name = cipher = u""
	page = request.GET.get("page", 0)
	try: page = int(page)
	except: page = 0

	if request.method == "POST":
		name = request.POST.get("name", None)
		cipher = request.POST.get("cipher", None)

		res = __search_catalog(name, cipher)
		request.session["catalog_POST"] = (name, cipher)
	else:	
		post = request.session.get("catalog_POST", [])
		if page > 0:
			if post:
				res = __search_catalog(*post)
				name, cipher = post
			else:
				res = Equipment.objects.order_by('name') 
		else:        
			if post: del request.session["catalog_POST"]
			res = Equipment.objects.order_by('name') 
	rx = {	
		ur'^[А-Е]$': "a",
		ur'^[Ж-Л]$': "zh",
		ur'^[М-Т]$': "m",
		ur'^[У-Я]$': "u"
	     }

	rx_page = {'a': 1, 'zh': 1, 'm': 1, 'u': 1}
	rx_page_set = []

	current_num = 0
	for r in res:
		l = r.name[0].upper()
	
		for k in rx.keys():
			if re.match(k, l):	
				r.menu_anchor = rx[k]
				if not rx[k] in rx_page_set:
					rx_page[rx[k]] = current_num // settings.CATALOG_OBJECTS_PER_PAGE + 1
					rx_page_set.append(rx[k])
				break
		current_num += 1

	page = page == 0 and 1 or page
	paginator = Paginator(res, settings.CATALOG_OBJECTS_PER_PAGE)
	res = paginator.page(page)	

	

	return render_to_response("catalog/index.html", {'lst': res, 'name': name, 'cipher': cipher, 'pages': rx_page}, context_instance=RequestContext(request))
