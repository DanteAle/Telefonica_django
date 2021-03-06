"""telefonica_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include, re_path
from t_test import views as vi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vi.index,name='index'),
    path('here/',include('t_test.urls'),name='usuarios'),
    path('form/',vi.addTarea, name='formulario'),
    path('tareasnoc/',vi.tareasnoc, name='tareasnoc'),
]
