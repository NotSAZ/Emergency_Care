"""
URL configuration for EMCSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Location import views as l_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',l_views.Location,name = 'Home'),
    path('Users/',l_views.Users,name = 'Users'),
    path('Hospital/',l_views.Hospital,name = 'hospital'),
    path('Services/',l_views.Services,name = 'Services'),
    path('Ambulance/',l_views.Ambulance,name = 'Ambulance'),
    path('ICUVacancy/',l_views.ICUVac,name = 'ICUVac'),
    path('DoctorList/',l_views.DoctorList,name = 'DoctorList'),
]
