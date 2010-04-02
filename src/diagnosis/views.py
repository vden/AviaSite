from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from diagnosis.models import *

def index(request):
    devices = System.objects.all().filter(published=True)
    return render_to_response("diagnosis/index.html", {'all': devices}, context_instance=RequestContext(request))

def device_info(request, device_id):
    devices = System.objects.all().filter(published=True)
    device = get_object_or_404(System, id=device_id, published=True)

    blocks = SystemBlock.objects.filter(system=device, published=True)
    return render_to_response("diagnosis/device.html", {"device": device, "blocks": blocks, "all": devices}, context_instance=RequestContext(request))
