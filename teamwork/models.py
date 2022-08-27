from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=50)
    number = models.IntegerField(unique=True, blank=True, null=True)
    email = models.EmailField(max_length=154, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=50, unique=True, blank=True, null=True)

    GENDER =(
        ("1", "Female"),
        ("2", "Male"),
        ("3", "Other"),
        ("4", "Prefer Not Say"),
    )

    gender = models.CharField(max_length=50, choices=GENDER)
    
    PATH =(
        ("1", "Frontend"),
        ("2", "Backend"),
        ("3", "Data Science"),
        ("4", "Dev-Ops"),
    )
    
    path = models.CharField(max_length=50, choices=PATH)

    def __str__(self):
        return f"{self.number} {self.full_name}"