from django.db import models


# Create your models here.
class Doctor(models.Model):
    doc_id = models.AutoField()
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    speciality = models.CharField()
    fees = models.IntegerField()


class Patient(models.Model):
    pat_id = models.AutoField()
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True)
    disease = models.CharField()
    assigned_doctor = models.CharField()
    admit_date = models.DateField()
    status = models.BooleanField()


class Appointment(models.Model):
    pat_id = models.IntegerField()
    doc_id = models.IntegerField()
    appoint_date = models.DateField()
    description = models.CharField()

    #abhay