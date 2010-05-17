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
	letter = int(request.GET.get("letter", 0))
	try: page = int(page)
	except: page = 0

	rx = (	ur'^(А|Б|В|Г|Д|Е|а|б|в|г|д|е)',
		ur'^(Ж|З|И|К|Л|ж|з|и|к|л)', 
		ur'^(М|Н|О|П|Р|С|Т|м|н|о|п|р|с|т)',
		ur'^(У|Ф|Х|Ц|Ч|Ш|Щ|Э|Ю|Я|у|ф|х|ц|ч|ш|щ|э|ю|я)'  )

	if request.method == "POST":
		name = request.POST.get("name", None)
		cipher = request.POST.get("cipher", None)

		res = __search_catalog(name, cipher).order_by('name')
		request.session["catalog_POST"] = (name, cipher)
	elif letter > 0:
		letter = rx[letter-1]
		post = request.session.get("catalog_POST", [])
		if post:
			res = __search_catalog(*post).filter(name__regex = letter).order_by('name')
			name, cipher = post
		else:
			res = Equipment.objects.filter(name__regex = letter).order_by('name')
	else:	
		post = request.session.get("catalog_POST", [])
		if page > 0:
			if post:
				res = __search_catalog(*post).order_by('name')
				name, cipher = post
			else:
				res = Equipment.objects.order_by('name') 
		else:        
			if post: del request.session["catalog_POST"]
			res = Equipment.objects.order_by('name') 

	page = page == 0 and 1 or page
	paginator = Paginator(res, settings.CATALOG_OBJECTS_PER_PAGE)
	res = paginator.page(page)	

	return render_to_response("catalog/index.html", {'lst': res, 'name': name, 'cipher': cipher}, context_instance=RequestContext(request))
