from django.shortcuts import render

# Create your views here.
def Location(request):
    return render(request,template_name='hospital/hospital.html')
def Users(request):
    return render(request,template_name='hospital/Users.html')