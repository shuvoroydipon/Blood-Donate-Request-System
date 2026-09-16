from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class DonorProfile(models.Model):

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='donor_profile'
    )

    full_name = models.CharField(
        max_length=100
    )

    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUP_CHOICES
    )

    phone = models.CharField(
        max_length=15
    )

    location = models.CharField(
        max_length=100
    )

    last_donation_date = models.DateField(
        null=True,
        blank=True
    )

    availability = models.CharField(
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default='Available'
    )

    description = models.TextField(
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to='donor_profiles/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.full_name} - {self.blood_group}"

    class Meta:
        ordering = ['-created_at']


class BloodRequest(models.Model):

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Fulfilled', 'Fulfilled'),
        ('Cancelled', 'Cancelled'),
    ]

    requester = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blood_requests'
    )

    patient_name = models.CharField(
        max_length=100
    )

    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUP_CHOICES
    )

    hospital_name = models.CharField(
        max_length=150
    )

    hospital_location = models.CharField(
        max_length=150
    )

    required_date = models.DateField()

    bags_required = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1)
        ]
    )

    contact_number = models.CharField(
        max_length=15
    )

    description = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.patient_name} - {self.blood_group}"

    class Meta:
        ordering = ['-created_at']
