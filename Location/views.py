from django.shortcuts import render,redirect
from .models import Location,Hospital,User,Ambulance,ICUVacancy,DoctorList,Services
from .forms import *
# Create your views here.
def location(request):
    return render(request,template_name='hospital/Home.html')
def hospital(request):
    hospital = Hospital.objects.all()
    context={
       'hospital':hospital,
    }
    return render(request,template_name='hospital/hospital.html',context=context)
def details(request, id):
    hospital = Hospital.objects.get(pk=id)
    context = {
       'hospital': hospital,
    }
    return render(request, template_name='hospital/Details.html', context = context)
def add_hospital(request):
    form = HospitalForm()
    if request.method == 'POST':
        form = HospitalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hospital')

    context = {
        'form':form
    }
    return render(request, template_name='hospital/add_hospital.html',context=context)
def users(request):
    return render(request,template_name='hospital/Users.html')
def services(request):
    service = Services.objects.all()
    context = {
        'service': service,
    }
    return render(request, template_name='hospital/Services.html',context=context)
def servicedetails(request, id):
    service = Services.objects.get(pk=id)
    context = {
       'service': service,
    }
    return render(request, template_name='hospital/ServiceDetails.html', context=context)

def add_service(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Services')

    context = {
        'form':form
    }
    return render(request, template_name='hospital/add_service.html',context=context)
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

def doctordetails(request, id):
    doctorlist = DoctorList.objects.get(pk=id)
    context = {
       'doctorlist': doctorlist,
    }
    return render(request, template_name='hospital/DoctorDetails.html', context=context)

def add_doctor(request):
    form = DoctorListForm()
    if request.method == 'POST':
        form = DoctorListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('DoctorList')

    context = {
        'form':form
    }
    return render(request, template_name='hospital/add_doctor.html',context=context)