from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'ypJourney/home.html')

def index(request):
    return render(request, 'ypJourney/index.html')

def aboutMe(request):
    return render(request, 'ypJourney/aboutMe.html')

