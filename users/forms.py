from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from users.models import User

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(required=False, help_text='در صورتی که می خواهید نام را وارد نکنید خالی بگذارید')
    city = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=11, required=True, help_text='شماره تلفن خود را به صورت 11 رقمی مثل 09123334455 وارد کنید')
    email = forms.EmailField(max_length=70, required=True, help_text='ایمیل خود را وارد کنید')

    class Meta:
        model = User
        fields = ['full_name', 'city', 'phone_number', 'email', 'password1', 'password2']

class PhoneVerificationForm(forms.Form):
    verification_code = forms.CharField(max_length=6, required=True)

    class Meta:
        fields = ['verification_code',]

class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=11, required=True, help_text='شماره تلفن خود را به صورت 11 رقمی مثل 09123334455 وارد کنید')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        fields = ['phone_number', 'password']

    def clean(self):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        user = authenticate(phone_number=phone_number, password=password)
        if not user:
            raise forms.ValidationError("شماره تلفن یا پاسورد اشتباه بود لطفاً مجدداً تلاش کنید")
        return self.cleaned_data

    def login(self, request):
        phone_number = self.cleaned_data.get('phone_number')
        password = self.cleaned_data.get('password')
        user = authenticate(phone_number=phone_number, password=password)
        return user

