from django.db import models

# Create your models here.

class Staff(models.Model):
    First_Name = models.CharField(max_length=200, default="First Name")
    Last_Name = models.CharField(max_length=200, default="Last Name")
    Phone_num = models.IntegerField(blank=True,null=True)
    Email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.First_Name