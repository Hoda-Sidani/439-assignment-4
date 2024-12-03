# myapp3/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name', 
            'speciality', 
            'fees', 
            'contact_info', 
            'address', 
            'recommendation',
            'gender',  # Added gender field
            'hospital',  # Added hospital field
            'email',  # Added email field
            'experience'  # Added experience field
        ]

