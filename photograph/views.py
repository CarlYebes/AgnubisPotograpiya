from django.shortcuts import render
from .models import picture
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse

# Create your views here.

def home(request):
    pictures = picture.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if subject and message and email and name:
            try:
                send_mail(f'{subject} - {name}', message, email, ['yebes77@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    context = {
        'pictures': pictures
    }
    return render(request, 'index.html', context)


