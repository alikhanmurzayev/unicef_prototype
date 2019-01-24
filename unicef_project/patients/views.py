from django.shortcuts import render

from django.views import generic
from . import models

# Create your views here.

class PatientListView(generic.ListView):
    model = models.Patient
    template_name = 'patient_list.html'

def patient_detail_view(request):
    return render(request, 'patient.html')
    