from django.db import models

# Create your models here.


class Client(models.Model):
    client_lead_name = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=100)
    # Add other project fields as needed