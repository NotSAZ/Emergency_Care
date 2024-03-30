from django.shortcuts import render
from .models import Location,Hospital,User,Ambulance,ICUVacancy,DoctorList,Services

# Create your views here.
def location(request):
    return render(request,template_name='hospital/Home.html')

def hospital(request):
    hospital = Hospital.objects.all()
    context={
       'hospital':hospital,
    }
    return render(request,template_name='hospital/hospital.html',context=context)
def users(request):
    return render(request,template_name='hospital/Users.html')
def services(request):
    service = Services.objects.all()
    context = {
        'service': service,
    }
    return render(request, template_name='hospital/Services.html',context=context)
def ambulance(request):
    ambulance = Ambulance.objects.all()
    context = {
        'ambulance': ambulance,
    }
    return render(request, template_name='hospital/Ambulance.html',context=context)
def icuvac(request):
    icuvac = ICUVacancy.objects.all()
    context = {
        'icuvac': icuvac,
    }
    return render(request, template_name='hospital/ICUVac.html',context=context)
def doctorlist(request):
    doctorlist = DoctorList.objects.all()
    context = {
        'doctorlist': doctorlist,
    }
    return render(request, template_name='hospital/DoctorList.html',context=context)