from django.db import models

# Create your models here.

class users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=11)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name