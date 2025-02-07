from django.shortcuts import render,get_object_or_404,redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms

#Formulario django
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields ='first_name','last_name', 'phone'


def create(request):
    if request.method == 'POST':
     
        return render(
            request,
            'contact/create.html',
            {'context': 'teste','form':ContactForm(request.POST)}
        )
    
    return render(
            request,
            'contact/create.html',
            {'context': 'teste','form':ContactForm()}
        )
        
        
