from django import forms
from .models import Warranty
from apps.user.models import Address
import re


# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = ('address1', 'address2', 'landmark', 'pincode', 'state', 'city')


class PhoneField(forms.CharField):
    def validate(self, value):
        # Call the parent's form validation first
        super().validate(value)
        # Use regex to match the pattern of a phone number
        if not re.match(r'^\+?91?[6789]\d{9}$', value):
            raise forms.ValidationError('Invalid phone number.')
        
class EmailField(forms.CharField):
    def validate(self, value):
        # Call the parent's form validation first
        super().validate(value)
        # Use regex to match the pattern of an email address
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise forms.ValidationError('Invalid email address.')
        
    
class WarrantyForm(forms.ModelForm):
    phone = PhoneField()
    mail = EmailField()
    
    class Meta:
        model = Warranty
        fields = ('name', 'phone', 'mail', 'product_type', 'model', 'serial_number', 'invoice_date', 'invoice_number',
                  'image', 'billing_address1', 'billing_address2', 'billing_landmark', 'billing_pincode',
                  'billing_state', 'billing_district',  'installation_address1', 'installation_address2',
                  'installation_landmark', 'installation_pincode', 'installation_state', 'installation_district')
        
        

    def __init__(self, *args, **kwargs):
        super(WarrantyForm, self).__init__(*args, **kwargs)
        self.fields["billing_address1"].label = "Building/Apartment Name"
        self.fields["billing_address2"].label = "Block/Flat No"
        self.fields["billing_landmark"].label = "Street/Road Name"
        self.fields["billing_state"].label = "State"
        self.fields["billing_district"].label = "District"
        self.fields["billing_pincode"].label = "Pincode"
        self.fields["installation_address1"].label = "Building/Apartment Name"
        self.fields["installation_address2"].label = "Block/Flat No"
        self.fields["installation_landmark"].label = "Street/Road Name"
        self.fields["installation_state"].label = "State"
        self.fields["installation_district"].label = "District"
        self.fields["installation_pincode"].label = "Pincode"
        self.fields['billing_state'].widget.attrs['disabled'] = True
        self.fields['billing_district'].widget.attrs['disabled'] = True
        self.fields['installation_state'].widget.attrs['disabled'] = True
        self.fields['installation_district'].widget.attrs['disabled'] = True
        self.fields['product_type'].required = True
        self.fields['model'].required = True
        self.fields['invoice_number'].required = True
        self.fields['billing_address1'].required = True
        self.fields['billing_address2'].required = True
        self.fields['billing_pincode'].required = True
        self.fields['installation_pincode'].required = True

# class EnquiryForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=100)
#     email = forms.EmailField(label='Email', max_length=100)
#     place = forms.CharField(label='Place', max_length=100)
#     state = forms.CharField(label='State', max_length=100)
#     district = forms.CharField(label='District', max_length=100)
#     phone_number = forms.CharField(label='Phone Number', max_length=20)
#     message = forms.CharField(label='Message', widget=forms.Textarea)
