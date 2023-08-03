from django import forms
from .models import Address, User
import re


class MobileField(forms.CharField):
    def validate(self, value):
        # Call the parent's form validation first
        super().validate(value)
        # Use regex to match the pattern of a phone number
        if not re.match(r'^[6789]\d{9}$', value):
            raise forms.ValidationError('Invalid phone number.')
        
class EmailField(forms.CharField):
    def validate(self, value):
        # Call the parent's form validation first
        super().validate(value)
        # Use regex to match the pattern of an email address
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value):
            raise forms.ValidationError('Invalid email address.')
        
class PincodeField(forms.CharField):
    def validate(self, value):
       
        super().validate(value)
       
        if not re.match(r'^\d{6}$', value):
            raise forms.ValidationError('Invalid pincode.')

class AdressForm(forms.ModelForm):
    mobile_number = MobileField()
    pincode = PincodeField()

    class Meta:
        model = Address
        fields = ('full_name', 'mobile_number', 'address1', 'address2', 'landmark', 'city', 'state', 'pincode', 'type')

    def __init__(self, *args, **kwargs):
        super(AdressForm, self).__init__(*args, **kwargs)
        self.fields['state'].required = True


class UserForm(forms.ModelForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['email'].disabled = True




