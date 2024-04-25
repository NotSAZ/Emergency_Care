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
from django.conf.urls.static import static
from django.conf import settings
from Location import views as l_views

urlpatterns = [
    path('register/',l_views.registerPage,name='register'),
    path('login/',l_views.loginPage,name='login'),
    path('logout/',l_views.logoutUser,name='logout'),
    path('admin/', admin.site.urls),
    path('',l_views.location,name='Home'),
    path('Users/',l_views.users,name='Users'),
    path('Hospital/',l_views.hospital,name='hospital'),
    path('Hospital/<str:id>',l_views.details, name='Details'),
    path('add_hospital/',l_views.add_hospital,name='add_hospital'),
    path('update_hospital/<str:id>',l_views.update_hospital,name='update_hospital'),
    path('delete_hospital/<str:id>',l_views.delete_hospital,name='delete_hospital'),
    path('Services/',l_views.services,name='Services'),
    path('Services/<str:id>', l_views.servicedetails, name='ServiceDetails'),
    path('add_service/',l_views.add_service,name='add_service'),
    path('update_service/<str:id>',l_views.update_service,name='update_service'),
    path('delete_service/<str:id>',l_views.delete_service,name='delete_service'),
    path('Ambulance/',l_views.ambulance,name='Ambulance'),
    path('add_ambulance/',l_views.add_ambulance,name='add_ambulance'),
    path('update_ambulance/<str:id>',l_views.update_ambulance,name='update_ambulance'),
    path('delete_ambulance/<str:id>',l_views.delete_ambulance,name='delete_ambulance'),
    path('ICUVacancy/',l_views.icuvac,name='ICUVac'),
    path('add_ICU/',l_views.add_ICU,name='add_ICU'),
    path('update_ICU/<str:id>',l_views.update_ICU,name='update_ICU'),
    path('delete_ICU/<str:id>',l_views.delete_ICU,name='delete_ICU'),
    path('DoctorList/',l_views.doctorlist,name='DoctorList'),
    path('DoctorList/<str:id>', l_views.doctordetails, name='DoctorDetails'),
    path('add_doctor/',l_views.add_doctor,name='add_doctor'),
    path('update_doctor/<str:id>',l_views.update_doctor,name='update_doctor'),
    path('delete_doctor/<str:id>',l_views.delete_doctor,name='delete_doctor'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
