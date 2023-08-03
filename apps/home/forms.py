from django import forms

from apps.catalogue.models import Enquiry


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ("name", "mail", "place", "state", "district", "phone", "requirement", "message")