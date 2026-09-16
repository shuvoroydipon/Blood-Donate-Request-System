from django.contrib import admin
from .models import DonorProfile, BloodRequest


@admin.register(DonorProfile)
class DonorProfileAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'blood_group',
        'phone',
        'location',
        'availability',
        'last_donation_date',
        'created_at',
    )

    list_filter = (
        'blood_group',
        'availability',
        'location',
    )

    search_fields = (
        'full_name',
        'phone',
        'location',
        'user__username',
        'user__email',
    )

    ordering = (
        '-created_at',
    )


@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):

    list_display = (
        'patient_name',
        'blood_group',
        'hospital_name',
        'hospital_location',
        'required_date',
        'bags_required',
        'contact_number',
        'status',
        'created_at',
    )

    list_filter = (
        'blood_group',
        'status',
        'hospital_location',
    )

    search_fields = (
        'patient_name',
        'hospital_name',
        'hospital_location',
        'contact_number',
        'requester__username',
        'requester__email',
    )

    ordering = (
        '-created_at',
    )

    date_hierarchy = 'required_date'