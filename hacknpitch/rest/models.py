from django.db import models
from enum import Enum

# Blood groups
class BloodGroup(Enum):
  A_P = "A+"
  A_N = "A-"
  B_P = "B+"
  B_N = "B-"
  AB_P = "AB+"
  AB_N = "AB-"
  O_P = "O+"
  O_N = "O-"

# Create your models here.
class Hospital(models.Model):
  name = models.CharField(max_length=100)
  long = models.FloatField()
  lat = models.FloatField()
  address = models.CharField(max_length=250)
  created_at = models.DateTimeField(auto_now_add=True)

class User(models.Model):
  email = models.EmailField(primary_key=True)
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=250)
  blood_group = models.CharField(
    max_length=2,
    choices=[(tag, tag.value) for tag in BloodGroup]
  )
  created_at = models.DateTimeField(auto_now_add=True)
  admitted_at = models.ForeignKey(Hospital, on_delete=models.CASCADE)

class BloodBank(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=250)
  lat = models.FloatField()
  long = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)

class A_P(models.Model):
  blood_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE)
  stock = models.IntegerField()
  last_updated = models.DateTimeField(auto_now=True)

class A_N(models.Model):
  blood_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE)
  stock = models.IntegerField()
  last_updated = models.DateTimeField(auto_now=True)

class B_P(models.Model):
  blood_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE)
  stock = models.IntegerField()
  last_updated = models.DateTimeField(auto_now=True)

class B_N(models.Model):
  blood_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE)
  stock = models.IntegerField()
  last_updated = models.DateTimeField(auto_now=True)

class AB_P(models.Model):
  blood_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE)
  stock = models.IntegerField()
  last_updated = models.DateTimeField(auto_now=True)

class AB_N(models.Model):
  blood_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE)
  stock = models.IntegerField()
  last_updated = models.DateTimeField(auto_now=True)

class O_P(models.Model):
  blood_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE)
  stock = models.IntegerField()
  last_updated = models.DateTimeField(auto_now=True)

class O_N(models.Model):
  blood_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE)
  stock = models.IntegerField()
  last_updated = models.DateTimeField(auto_now=True)
