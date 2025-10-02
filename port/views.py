from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactForm
from .models import ContactMessage
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')


def contact(request):
    if request.method=="POST":
        form=contactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Contact form submitted succesfullyy..")
        return render(request, 'contact.html') 
    form = contactForm()
    return render(request, 'contact.html',{'form':form})  




