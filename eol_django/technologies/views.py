from django.shortcuts import render

from .models import Technologies


# Create your views here.

def tech_list_view(request):
    tech_objects = Technologies.objects.all()
    context = {
        'tech_objects': tech_objects
    }
    return render(request, "index.html", context)


def home(request):
    technologies = Technologies.objects
    return render(request, 'technologies/home.html', {'technologies': technologies})
