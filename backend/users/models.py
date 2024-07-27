# models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
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
        return f"{self.username} ({self.get_full_name()})"

class Patient(models.Model):
    MARITAL_STATUSES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]

    RELATIONSHIP_CHOICES = [
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Sister', 'Sister'),
        ('Brother', 'Brother'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="patients")
    occupation = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUSES)
    age = models.IntegerField(blank=True, null=True)
    height = models.FloatField(help_text="Height in meters")
    weight = models.FloatField()
    house_number = models.CharField(max_length=10, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    landmark = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    next_of_kin_first_name = models.CharField(max_length=100)
    next_of_kin_last_name = models.CharField(max_length=100)
    next_of_kin_relationship = models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES)
    next_of_kin_phone_number = models.CharField(max_length=15)
    next_of_kin_address1 = models.TextField(blank=True, null=True)
    next_of_kin_address2 = models.TextField(blank=True, null=True)
    additional_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - ({self.get_marital_status_display()})"

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        ordering = ['user__last_name', 'user__first_name']


class Employee(models.Model):
    POSITIONS = [
        ('CMD', 'Chief Medical Director'),
        ('MO', 'Medical Officer'),
        ('VD', 'Visiting Doctor'),
        ('NUR', 'Nurse'),
        ('SNUR', 'Senior Nurse'),
        ('REC', 'Receptionist'),
        ('LS', 'Lab Scientist'),
        ('SLS', 'Senior Lab Scientist'), 
    ]
    
    DEPARTMENTS = [
        ('GEN', 'General'),
        ('CARD', 'Cardiology'),
        ('DERM', 'Dermatology'),
        ('NEUR', 'Neurology'),
        ('ORTH', 'Orthopedics'),
        ('PED', 'Pediatrics'),
        ('PSY', 'Psychiatry'),
        ('SURG', 'Surgery'),
        # Add more departments as needed
    ]

    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name="employees")
    position = models.CharField(max_length=4, choices=POSITIONS)
    department = models.CharField(max_length=5, choices=DEPARTMENTS)
    date_joined = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    emergency_contact = models.CharField(max_length=100, blank=True, null=True)
    emergency_phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.get_position_display()}"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ['user__last_name', 'user__first_name']