from django.shortcuts import render


# from .models import Technologies

# Create your views here.
def homepage(request):
    return render(request, 'homepage/home.html')
