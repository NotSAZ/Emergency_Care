from django.shortcuts import render

# Create your views here.
def Location(request):
    return render(request,template_name='hospital/Home.html')
def Hospital(request):
    return render(request,template_name='hospital/hospital.html')
def Users(request):
    return render(request,template_name='hospital/Users.html')
def Services(request):
    return render(request, template_name='hospital/Services.html')
def Ambulance(request):
    return render(request, template_name='hospital/Ambulance.html')
def ICUVac(request):
    return render(request, template_name='hospital/ICUVac.html')
def DoctorList(request):
    return render(request, template_name='hospital/DoctorList.html')