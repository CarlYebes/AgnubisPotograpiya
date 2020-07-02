from django.shortcuts import render
from .models import picture
# Create your views here.

def home(request):
    pictures = picture.objects.all()
    context = {
        'pictures': pictures
    }
    return render(request, 'index.html', context)