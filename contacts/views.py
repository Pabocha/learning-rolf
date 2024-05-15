from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import NewsLetters

# Create your views here.

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

def news_letter_view(request):
    email = request.POST.get('email')
    if email:
        if '@' in email and '.' in email:
            NewsLetters.objects.create(email=email)
        else:
            pass
    else:
        pass
