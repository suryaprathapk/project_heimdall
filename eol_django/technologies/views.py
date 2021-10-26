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
    return render(request, 'home.html', {'technologies': technologies})


def informatica(request):
    technologies = Technologies.objects
    return render(request, 'informatica.html', {'technologies': technologies})


def centos(request):
    technologies = Technologies.objects
    return render(request, 'centos.html', {'technologies': technologies})


def oracle(request):
    technologies = Technologies.objects
    return render(request, 'oracle.html', {'technologies': technologies})


def surya(request):
    technologies = Technologies.objects
    return render(request, 'surya.html', {'technologies': technologies})


def jboss(request):
    technologies = Technologies.objects
    return render(request, 'jboss.html', {'technologies': technologies})


def iis(request):
    technologies = Technologies.objects
    return render(request, 'iis.html', {'technologies': technologies})
