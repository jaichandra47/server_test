from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    year = models.IntegerField()
    college = models.CharField(max_length=50)
    branch = models.CharField(max_length=20)

