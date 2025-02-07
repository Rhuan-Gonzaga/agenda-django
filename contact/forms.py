from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError


#Formulario django
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields ='first_name','last_name', 'phone'

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error('first_name',ValidationError("Mansagem de error",code='invald'))
        return super().clean()
