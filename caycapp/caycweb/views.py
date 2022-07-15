from django.shortcuts import render
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, 'home.html')


def missionandvision(request):
    return render(request, 'missionandvision.html')


def housefellow(request):
    return render(request, 'housefellow.html')


def mediaresources(request):
    return render(request, 'mediaresources.html')


def youthdiary(request):
    return render(request, 'youthdiary.html')


def testimony(request):
    return render(request, 'testimony.html')


def firsttimer(request):
    return render(request, 'firsttimer.html')


def altarcall(request):
    return render(request, 'altarcall.html')


def onlinegiving(request):
    return render(request, 'onlinegiving.html')


def contact(request):
    return render(request, 'contact.html')