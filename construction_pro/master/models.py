from django.db import models

# Create your models here.


class EmployeeRole(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class EmployeeType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class VendorType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name