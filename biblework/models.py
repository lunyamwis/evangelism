from django.db import models

class StudySchedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} {self.topic}"

class LessonMaterial(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    resource_link = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title

class OutreachTeamMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class VisitLog(models.Model):
    date = models.DateField()
    address = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} {self.contact_person}"
