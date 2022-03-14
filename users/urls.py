from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('verify/', views.phone_verification_view, name='phone_verification'),
    path('verify/', views.phone_verified_view, name='phone_verified'),
    path('resend_otp/', views.phone_resend_code, name='resend_code'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]