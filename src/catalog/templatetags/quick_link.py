# -*- coding: utf-8 -*-
from django import template
import settings, re

register = template.Library()

@register.simple_tag
def quick_link(name):
	l = name[0].upper()
	
	rx = {ur'^[А-Е]$': "a",
		ur'^[Ж-Л]$': "zh",
		ur'^[М-Т]$': "m",
		ur'^[У-Я]$': "u"}
	
	print l
	for k in rx.keys():
		if re.match(k, l):
			
			return u"""<a name="%s"></a>"""%rx[k]

	return u""
