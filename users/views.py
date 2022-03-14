from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone

from users.forms import RegistrationForm, PhoneVerificationForm, LoginForm
from .phone_api import send_verfication_code
from .models import User

def register_view(request):
    context = {}
    form = RegistrationForm(request.POST)
    if request.POST:
        if form.is_valid():
            form.save()
            phone = form.cleaned_data.get('phone_number')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(phone_number=phone, password=raw_password)
            login(request, user)
            print(send_verfication_code(user))
            return redirect('phone_verification')
        else:
            context['registration_form'] = form
            return render(request, 'users/register.html', context)
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'users/register.html', context)

@login_required(login_url='/register/')
def phone_verification_view(request):
    context = {}
    user = request.user
    if request.method == "POST":
        form = PhoneVerificationForm(request.POST)
        if form.is_valid():
            verification_code = form.cleaned_data.get('verification_code')
            if user.phone_number_verified is False:
                if user.verification_code == verification_code:
                    user.phone_number_verified = True
                    user.save()
                    return redirect('home')
                else:
                    messages.add_message(request, messages.ERROR,  'wrong verification number.')
                    return render(request, 'phone_verify', {'user':user})
            else:
                messages.add_message(request, messages.ERROR,  'already verified.')
                return render(request, 'phone_verified', {'user':user})
        else:
            context = {
                'user': user,
                'form': form,
            }
            return render(request, 'phone_verify', context)
    else:
        if user.phone_number_verified is False:
            form = PhoneVerificationForm()
            context['verification_form'] = form
            context['phone'] = user.phone_number
            return render(request, 'users/phone_verify.html', context)
        else:
            return render(request, 'users/phone_verified.html', context)

@login_required
def phone_resend_code(request):
    
    user = request.user
    can_he, time_remain = user.can_send_code_again()
    if can_he:
        user.generate_another()     # tell user to generate another verification code
        print(send_verfication_code(user))
        data = {
            'is_sent': True,
            'time': 0
        }
        return JsonResponse(data)
    else:
        data = {
            'is_sent': False,
            'time': str(60 - time_remain.seconds)
        }
        return JsonResponse(data)



def phone_verified_view(request):
    context = {
    }
    return render(request, 'users/phone_verified.html', context)

def login_view(request):
    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect('home')
    
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'users/login.html', {'login_form': form })
