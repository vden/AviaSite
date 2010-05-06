from django import template
import settings, re

register = template.Library()

@register.simple_tag
def bg(request):
	print request.path
	
	img = u"%si/header_img_index.jpg"
	bgs = {r'^/company': u"%si/header_img_index.jpg", 
		r'^/toir': u"%si/m1.jpg",
		r'^/repair': u"%si/m4.jpg",
		r'^/ati': u"%si/p3.jpg" }

	for i in bgs.keys():
		if re.match(i, request.path):
			img = bgs[i]

	return img%settings.MEDIA_URL
