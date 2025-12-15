from django.shortcuts import render
from django.http import HttpResponse
from .forms import contactForm
from .models import ContactMessage, Project

from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    # return render(request, 'portfolio.html')
    # projects = Project.objects.all()    
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




def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"New Inquiry from {name}"
        body = f"""
        Name: {name}
        Email: {email}
        Message:
        {message}
        """

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,   # from email
            ['agghevariya1111@gmail.com'],  # to email
            fail_silently=False,
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')
