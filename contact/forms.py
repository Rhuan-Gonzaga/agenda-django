from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError


#Formulario django
class ContactForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init'
            }
        ),
        help_text='Teste'
    )


    #def __init__(self, *args, **kwargs):
      #  super().__init__(*args, **kwargs)

    #   self.fields['first_name'].widget.attrs.update({
     #       'class': 'classe-a classe-b',
     #       'placeholder': 'Escreva aqui'
     #   })

    class Meta:
        model = Contact
        fields ='first_name','last_name', 'phone'

        #widgets = {'first_name': forms.TextInput(
        #    attrs={
        #        'class': 'classe-a classe-b',
        #        'placeholder': 'Escreva aqui'
        #        }
        #    )}

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error('first_name',ValidationError("Mansagem de error",code='invald'))
        return super().clean()
