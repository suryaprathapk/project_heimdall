"""eol_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from technologies.views import tech_list_view, home, informatica, centos, oracle, surya

urlpatterns = [
    path('admin/', admin.site.urls),
    path('technologies/', tech_list_view),
    path('home/', home),
    path('informatica/', informatica),
    path('centos/', centos),
    path('oracle/', oracle),
    path('surya/', surya)
]
