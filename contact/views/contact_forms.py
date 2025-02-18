from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.core.paginator import Paginator
from contact.forms import ContactForm


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            'form': form
        }

        if form.is_valid:
            form.save()
            return redirect('contact:create')
     
        return render(
            request,
            'contact/create.html',
            context
        )
    
    return render(
            request,
            'contact/create.html',
            {'context': 'teste','form':ContactForm()}
        )
        
        
