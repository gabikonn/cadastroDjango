from django.shortcuts import render

def home(request):
    return render(request, 'cadastroapp/home.html')
# Create your views here.
