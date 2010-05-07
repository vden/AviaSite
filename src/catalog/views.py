from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from django.template import RequestContext
from catalog.models import Equipment

import re

def index(request):
	if request.method == "POST":
		name = request.POST.get("name", None)
		cipher = request.POST.get("cipher", None)
	
		res = Equipment.objects.order_by('name')
                if name and len(name): 
			name = re.sub(r'[\\\|/,\.\-]', '', name)
			print name
			res = res.filter(name__icontains=name)
		if cipher and len(cipher): 
			cipher = re.sub(r'[\\\|/,\.\-\ ]', '', cipher)
			print cipher
			res = res.filter(cipher__icontains=cipher)
	else:	
            	name = cipher = u""
		res = Equipment.objects.order_by('name')

	return render_to_response("catalog/index.html", {'lst': res, 'name': name, 'cipher': cipher}, context_instance=RequestContext(request))
