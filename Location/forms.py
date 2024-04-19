from django.forms import ModelForm
from .models import *

class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

class ServiceForm(ModelForm):
    class Meta:
        model = Services
        fields = '__all__'

class DoctorListForm(ModelForm):
    class Meta:
        model = DoctorList
        fields = '__all__'