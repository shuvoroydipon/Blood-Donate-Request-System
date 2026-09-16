from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from .models import DonorProfile, BloodRequest


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }
        )
    )

    first_name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name'
            }
        )
    )

    last_name = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name'
            }
        )
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Choose a username'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Create a password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'An account with this email already exists.'
            )

        return email


class DonorProfileForm(forms.ModelForm):

    class Meta:
        model = DonorProfile
        fields = [
            'full_name',
            'blood_group',
            'phone',
            'location',
            'last_donation_date',
            'availability',
            'description',
            'profile_picture',
        ]

        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your full name'
                }
            ),

            'blood_group': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '01XXXXXXXXX'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your location'
                }
            ),

            'last_donation_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'availability': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Write something about yourself'
                }
            ),

            'profile_picture': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone.isdigit():
            raise forms.ValidationError(
                'Phone number must contain only digits.'
            )

        if len(phone) < 10 or len(phone) > 15:
            raise forms.ValidationError(
                'Please enter a valid phone number.'
            )

        return phone

    def clean_last_donation_date(self):
        donation_date = self.cleaned_data.get(
            'last_donation_date'
        )

        if donation_date and donation_date > timezone.localdate():
            raise forms.ValidationError(
                'Last donation date cannot be in the future.'
            )

        return donation_date


class BloodRequestForm(forms.ModelForm):

    class Meta:
        model = BloodRequest

        fields = [
            'patient_name',
            'blood_group',
            'hospital_name',
            'hospital_location',
            'required_date',
            'bags_required',
            'contact_number',
            'description',
            'status',
        ]

        widgets = {
            'patient_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter patient name'
                }
            ),

            'blood_group': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'hospital_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter hospital name'
                }
            ),

            'hospital_location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter hospital location'
                }
            ),

            'required_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'bags_required': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 1,
                    'placeholder': 'Number of bags'
                }
            ),

            'contact_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '01XXXXXXXXX'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Reason or additional information'
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

    def clean_contact_number(self):
        phone = self.cleaned_data.get('contact_number')

        if not phone.isdigit():
            raise forms.ValidationError(
                'Contact number must contain only digits.'
            )

        if len(phone) < 10 or len(phone) > 15:
            raise forms.ValidationError(
                'Please enter a valid contact number.'
            )

        return phone

    def clean_bags_required(self):
        bags = self.cleaned_data.get('bags_required')

        if bags is None or bags < 1:
            raise forms.ValidationError(
                'At least 1 blood bag is required.'
            )

        return bags

    def clean_required_date(self):
        required_date = self.cleaned_data.get('required_date')

        if required_date < timezone.localdate():
            raise forms.ValidationError(
                'Required date cannot be in the past.'
            )

        return required_date