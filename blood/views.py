

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, DonorProfileForm, BloodRequestForm
from .models import DonorProfile, BloodRequest


# =========================================================
# HOME
# =========================================================

def home(request):
    return render(request, 'home.html')


# =========================================================
# USER REGISTRATION
# =========================================================

def register(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                'Registration successful! Welcome to Blood Donate & Request System.'
            )

            return redirect('dashboard')

    else:
        form = RegisterForm()

    return render(
        request,
        'registration/register.html',
        {
            'form': form
        }
    )


# =========================================================
# DASHBOARD
# =========================================================

@login_required
def dashboard(request):

    total_donors = DonorProfile.objects.count()

    total_requests = BloodRequest.objects.count()

    my_requests = BloodRequest.objects.filter(
        requester=request.user
    ).count()

    available_donors = DonorProfile.objects.filter(
        availability='Available'
    ).count()

    pending_requests = BloodRequest.objects.filter(
        status='Pending'
    ).count()

    fulfilled_requests = BloodRequest.objects.filter(
        status='Fulfilled'
    ).count()

    recent_requests = BloodRequest.objects.all()[:5]

    context = {
        'total_donors': total_donors,
        'total_requests': total_requests,
        'my_requests': my_requests,
        'available_donors': available_donors,
        'pending_requests': pending_requests,
        'fulfilled_requests': fulfilled_requests,
        'recent_requests': recent_requests,
    }

    return render(
        request,
        'dashboard.html',
        context
    )


# =========================================================
# DONOR SEARCH & FILTER
# =========================================================

@login_required
def donor_list(request):

    donors = DonorProfile.objects.all()

    blood_group = request.GET.get(
        'blood_group',
        ''
    )

    location = request.GET.get(
        'location',
        ''
    )

    availability = request.GET.get(
        'availability',
        ''
    )

    # Filter by blood group
    if blood_group:

        donors = donors.filter(
            blood_group=blood_group
        )

    # Filter by location
    if location:

        donors = donors.filter(
            location__icontains=location
        )

    # Filter by availability
    if availability:

        donors = donors.filter(
            availability=availability
        )

    context = {
        'donors': donors,
        'blood_group': blood_group,
        'location': location,
        'availability': availability,
        'blood_groups': DonorProfile.BLOOD_GROUP_CHOICES,
        'availability_choices': DonorProfile.AVAILABILITY_CHOICES,
    }

    return render(
        request,
        'donors/donor_list.html',
        context
    )


# =========================================================
# DONOR PROFILE VIEW
# =========================================================

@login_required
def donor_profile(request):

    donor = get_object_or_404(
        DonorProfile,
        user=request.user
    )

    return render(
        request,
        'donors/donor_profile.html',
        {
            'donor': donor
        }
    )


# =========================================================
# DONOR CREATE
# =========================================================

@login_required
def donor_create(request):

    # Check whether user already has a donor profile
    if hasattr(request.user, 'donor_profile'):

        messages.info(
            request,
            'You already have a donor profile.'
        )

        return redirect('donor_profile')

    if request.method == 'POST':

        form = DonorProfileForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            donor = form.save(
                commit=False
            )

            donor.user = request.user

            donor.save()

            messages.success(
                request,
                'Donor profile created successfully!'
            )

            return redirect('donor_profile')

    else:

        form = DonorProfileForm()

    return render(
        request,
        'donors/donor_form.html',
        {
            'form': form,
            'page_title': 'Create Donor Profile',
            'button_text': 'Create Profile',
        }
    )


# =========================================================
# DONOR EDIT
# =========================================================

@login_required
def donor_edit(request):

    donor = get_object_or_404(
        DonorProfile,
        user=request.user
    )

    if request.method == 'POST':

        form = DonorProfileForm(
            request.POST,
            request.FILES,
            instance=donor
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Donor profile updated successfully!'
            )

            return redirect('donor_profile')

    else:

        form = DonorProfileForm(
            instance=donor
        )

    return render(
        request,
        'donors/donor_form.html',
        {
            'form': form,
            'page_title': 'Edit Donor Profile',
            'button_text': 'Update Profile',
        }
    )


# =========================================================
# DONOR DELETE
# =========================================================

@login_required
def donor_delete(request):

    donor = get_object_or_404(
        DonorProfile,
        user=request.user
    )

    if request.method == 'POST':

        donor.delete()

        messages.success(
            request,
            'Donor profile deleted successfully.'
        )

        return redirect('donor_list')

    return render(
        request,
        'donors/donor_confirm_delete.html',
        {
            'donor': donor
        }
    )


# =========================================================
# BLOOD REQUEST LIST + SEARCH + FILTER
# =========================================================

@login_required
def blood_request_list(request):

    blood_requests = BloodRequest.objects.all()

    blood_group = request.GET.get(
        'blood_group',
        ''
    )

    hospital_location = request.GET.get(
        'hospital_location',
        ''
    )

    status = request.GET.get(
        'status',
        ''
    )

    # Filter by blood group
    if blood_group:

        blood_requests = blood_requests.filter(
            blood_group=blood_group
        )

    # Filter by hospital location
    if hospital_location:

        blood_requests = blood_requests.filter(
            hospital_location__icontains=hospital_location
        )

    # Filter by status
    if status:

        blood_requests = blood_requests.filter(
            status=status
        )

    context = {
        'blood_requests': blood_requests,
        'blood_group': blood_group,
        'hospital_location': hospital_location,
        'status': status,
        'blood_groups': BloodRequest.BLOOD_GROUP_CHOICES,
        'status_choices': BloodRequest.STATUS_CHOICES,
    }

    return render(
        request,
        'requests/request_list.html',
        context
    )


# =========================================================
# BLOOD REQUEST CREATE
# =========================================================

@login_required
def blood_request_create(request):

    if request.method == 'POST':

        form = BloodRequestForm(
            request.POST
        )

        if form.is_valid():

            blood_request = form.save(
                commit=False
            )

            # Set current logged-in user
            blood_request.requester = request.user

            blood_request.save()

            messages.success(
                request,
                'Blood request created successfully!'
            )

            return redirect(
                'blood_request_list'
            )

    else:

        form = BloodRequestForm()

    return render(
        request,
        'requests/request_form.html',
        {
            'form': form,
            'page_title': 'Create Blood Request',
            'button_text': 'Create Request',
        }
    )


# =========================================================
# BLOOD REQUEST DETAIL
# =========================================================

@login_required
def blood_request_detail(request, pk):

    blood_request = get_object_or_404(
        BloodRequest,
        pk=pk
    )

    return render(
        request,
        'requests/request_detail.html',
        {
            'blood_request': blood_request
        }
    )


# =========================================================
# BLOOD REQUEST EDIT
# =========================================================

@login_required
def blood_request_edit(request, pk):

    # User can edit only their own request
    blood_request = get_object_or_404(
        BloodRequest,
        pk=pk,
        requester=request.user
    )

    if request.method == 'POST':

        form = BloodRequestForm(
            request.POST,
            instance=blood_request
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Blood request updated successfully!'
            )

            return redirect(
                'blood_request_list'
            )

    else:

        form = BloodRequestForm(
            instance=blood_request
        )

    return render(
        request,
        'requests/request_form.html',
        {
            'form': form,
            'page_title': 'Edit Blood Request',
            'button_text': 'Update Request',
        }
    )


# =========================================================
# BLOOD REQUEST DELETE
# =========================================================

@login_required
def blood_request_delete(request, pk):

    # User can delete only their own request
    blood_request = get_object_or_404(
        BloodRequest,
        pk=pk,
        requester=request.user
    )

    if request.method == 'POST':

        blood_request.delete()

        messages.success(
            request,
            'Blood request deleted successfully.'
        )

        return redirect(
            'blood_request_list'
        )

    return render(
        request,
        'requests/request_confirm_delete.html',
        {
            'blood_request': blood_request
        }
    )




