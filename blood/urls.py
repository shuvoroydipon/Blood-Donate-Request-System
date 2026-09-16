


from django.urls import path
from . import views


urlpatterns = [

    # =====================================================
    # HOME
    # =====================================================

    path(
        '',
        views.home,
        name='home'
    ),


    # =====================================================
    # AUTHENTICATION
    # =====================================================

    path(
        'register/',
        views.register,
        name='register'
    ),


    # =====================================================
    # DASHBOARD
    # =====================================================

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),


    # =====================================================
    # DONOR PROFILE
    # =====================================================

    path(
        'profile/',
        views.donor_profile,
        name='donor_profile'
    ),

    path(
        'donors/',
        views.donor_list,
        name='donor_list'
    ),

    path(
        'donors/create/',
        views.donor_create,
        name='donor_create'
    ),

    path(
        'donors/edit/',
        views.donor_edit,
        name='donor_edit'
    ),

    path(
        'donors/delete/',
        views.donor_delete,
        name='donor_delete'
    ),


    # =====================================================
    # BLOOD REQUESTS
    # =====================================================

    path(
        'requests/',
        views.blood_request_list,
        name='blood_request_list'
    ),

    path(
        'requests/create/',
        views.blood_request_create,
        name='blood_request_create'
    ),

    path(
        'requests/<int:pk>/',
        views.blood_request_detail,
        name='blood_request_detail'
    ),

    path(
        'requests/<int:pk>/edit/',
        views.blood_request_edit,
        name='blood_request_edit'
    ),

    path(
        'requests/<int:pk>/delete/',
        views.blood_request_delete,
        name='blood_request_delete'
    ),

]

