from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Doctor(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    profession = models.CharField(max_length=200)
    experience = models.PositiveIntegerField(default=0)
    patients_number = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.last_name + ', ' + self.first_name
    
    def get_absolute_url(self):
        return reverse("doctor_detail", kwargs={"pk": self.pk})
    
    
    