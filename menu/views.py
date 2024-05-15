from django.shortcuts import render
from contacts.views import contact_view, news_letter_view
from contacts.forms import ContactForm
from formations.models import Formations

# Create your views here.

def home(request):
    formations = Formations.objects.filter(active=True)
    form_contact = ContactForm()
    if request.method == 'POST':
        form_type = request.POST.get('form_type')  

        if form_type == 'contact':
            contact_view(request) 
        elif form_type == 'news-letter':
            news_letter_view(request)

    
    context = {"form_contact": form_contact, "formations": formations}
    return render(request, 'home/index.html', context)
