from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _

class RepairRequest(models.Model):
    name = models.CharField(_("Name"), max_length=1000, blank=False, null=False)
    sender = models.EmailField(_("E-mail"),  blank=False, null=False)
    company =  models.CharField(_("Company"), max_length=1000, blank=False, null=False)
    phone =  models.CharField(_("Phone"), max_length=100, blank=False, null=False)
    subject = models.CharField(_("Subject"), max_length=100, blank=True)
    number = models.CharField(_("Drawing number"), max_length=100, blank=True)
    decimal =  models.CharField(_("Decimal number"), max_length=100, blank=True)
    pmo =  models.CharField(_("PMO version"), max_length=100, blank=True)
    message = models.TextField(_("Message"), blank=True)

    
class RepairForm(forms.ModelForm):
    class Meta:
        model = RepairRequest

class PurchaseRequest(models.Model):
    name = models.CharField(_("Name"), max_length=1000, blank=False, null=False)
    sender = models.EmailField(_("E-mail"),  blank=False, null=False)
    company =  models.CharField(_("Company"), max_length=1000, blank=False, null=False)
    phone =  models.CharField(_("Phone"), max_length=100, blank=False, null=False)
    subject = models.CharField(_("Subject"), max_length=100, blank=True)
    message = models.TextField(_("Message"), blank=True)

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PurchaseRequest
