from django.db import models # type: ignore

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    initials = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ('PLANNING', 'Planning'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('ON_HOLD', 'On Hold'),
    ]

    FACING_CHOICES = [
        ('N', 'North'),
        ('S', 'South'),
        ('E', 'East'),
        ('W', 'West'),
    ]

    lead_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLANNING')
    progress = models.IntegerField(default=0)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    spent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    land_facing = models.CharField(max_length=1, choices=FACING_CHOICES)
    land_width = models.DecimalField(max_digits=8, decimal_places=2)
    land_breadth = models.DecimalField(max_digits=8, decimal_places=2)
    num_floors = models.IntegerField()
    build_area = models.DecimalField(max_digits=10, decimal_places=2)
    team = models.ManyToManyField(TeamMember)

    def __str__(self):
        return f"{self.lead_name}'s Project - {self.location}"

    def get_status_display(self):
        return dict(self.STATUS_CHOICES)[self.status]