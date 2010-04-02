from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
import settings
from orders.models import *
from django.core.urlresolvers import reverse

def _form(request, klass, view):
    err = False
    message = ""
    if request.method == "POST":
        f = klass(request.POST)
        try:
            f.save()
        except ValueError:
            err = True
        
        if not err:
            message = _("Thank you, your request sent! We will contact you shortly.")
            from django.core.mail import send_mail
            f = f.cleaned_data

            if not settings.DEBUG:
                send_mail(f['subject'], "%(name)s (%(company)s), %(phone)s, %(sender)s\n\n%(message)s"%f, f['sender'], settings.REQUEST_MAIL)
            else:
                print "MAIL: %(name)s (%(company)s), %(phone)s, %(sender)s\n\n%(message)s"%f

    else:
        f = klass()
            
    return render_to_response("orders/repair.html", {'form': f, 'err': err, "message": message, 'url': reverse(view)}, context_instance=RequestContext(request))

def repair(request):
    return _form(request, RepairForm, "repair_order")

def ati(request):
    return _form(request, PurchaseForm, "ati_order")
