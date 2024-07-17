# models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    POSITIONS = [
        ('CMD', 'Chief Medical Director'),
        ('MO', 'Medical Officer'),
        ('VD', 'Visiting Doctor'),
        ('PAT', 'Patient'),
        ('NUR', 'Nurse'),
        ('SNUR', 'Senior Nurse'),
        ('REC', 'Receptionist'),
        ('LS', 'Lab Scientist'),
        ('SLS', 'Senior Lab Scientist'),
        ('VIS', 'Visitor'),
    ]
    position = models.CharField(max_length=4, choices=POSITIONS)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Add related_name argument
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Add related_name argument
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.username} ({self.get_position_display()})"

class Patient(models.Model):
    MARITAL_STATUSES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUSES)
    next_of_kin = models.CharField(max_length=100)
    weight = models.FloatField()
    height = models.FloatField()
    additional_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_marital_status_display()})"
