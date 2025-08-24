from django.shortcuts import render, redirect, get_object_or_404
from .models import ClinicSchedule, Patient, Volunteer, Treatment, InventoryItem, HealthEducationMaterial
from .forms import ClinicScheduleForm, PatientForm, VolunteerForm, TreatmentForm, InventoryItemForm, HealthEducationMaterialForm

def dashboard_home(request):
    # A dashboard overview - customize as needed
    return render(request, 'medical_missionary/dashboard_home.html')

def clinic_schedule_list(request):
    schedules = ClinicSchedule.objects.all().order_by('date', 'time')
    if request.method == 'POST':
        form = ClinicScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clinic_schedule_list')
    else:
        form = ClinicScheduleForm()
    return render(request, 'medical_missionary/clinic_schedule.html', {'schedules': schedules, 'form': form})

def patient_list(request):
    patients = Patient.objects.all()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'medical_missionary/patient_list.html', {'patients': patients, 'form': form})

def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteer_list')
    else:
        form = VolunteerForm()
    return render(request, 'medical_missionary/volunteer_list.html', {'volunteers': volunteers, 'form': form})

def treatment_list(request):
    treatments = Treatment.objects.all()
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('treatment_list')
    else:
        form = TreatmentForm()
    return render(request, 'medical_missionary/treatment_list.html', {'treatments': treatments, 'form': form})

def inventory_list(request):
    items = InventoryItem.objects.all()
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm()
    return render(request, 'medical_missionary/inventory_list.html', {'items': items, 'form': form})

def health_education_list(request):
    materials = HealthEducationMaterial.objects.all()
    if request.method == 'POST':
        form = HealthEducationMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('health_education_list')
    else:
        form = HealthEducationMaterialForm()
    return render(request, 'medical_missionary/health_education_list.html', {'materials': materials, 'form': form})
