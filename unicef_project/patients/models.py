from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    vk_bot = models.CharField(max_length=100, blank=True, null=True)
    telegram_bot = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return ' '.join([str(self.first_name.title()), str(self.last_name.title())])
    
    def get_absolute_url(self):
        return reverse("patients_list", kwargs={"pk": self.pk})