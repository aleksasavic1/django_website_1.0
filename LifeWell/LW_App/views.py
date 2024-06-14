from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def fruits(request):
    return render(request, 'fruits.html', {})

def training(request):
    return render(request, 'training.html', {})

def about_me(request):
    return render(request, 'about_me.html', {})
