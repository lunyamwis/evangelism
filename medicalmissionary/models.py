from django.db import models

class ClinicSchedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} {self.location}"

class Patient(models.Model):
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    sda_health_message_adherence = models.BooleanField(null=True)  # Yes/No

    def __str__(self):
        return self.full_name

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_histories')
    details = models.TextField()

class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='treatments')
    condition_diagnosed = models.CharField(max_length=255)
    prescription_details = models.TextField()

class InventoryItem(models.Model):
    medicine_name = models.CharField(max_length=255)
    quantity_in_stock = models.PositiveIntegerField()
    reorder_level = models.PositiveIntegerField()

    def __str__(self):
        return self.medicine_name

class HealthEducationMaterial(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    resource_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
