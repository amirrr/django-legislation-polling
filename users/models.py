from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator

from datetime import datetime

from .manager import UserManager
from .phone_api import generate_verification_code



class User(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(regex=r'^(09)\d{9}$', message="شماره تلفن خود را به صورت 11 رقمی مثل 09123334455 وارد کنید")
    phone_number = models.CharField(_('phone'), validators=[phone_regex], max_length=11, unique=True)
    full_name = models.CharField(_('full name'), max_length=130, blank=True)
    city = models.CharField(_('city name'), max_length=100)
    email = models.EmailField(max_length=70)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    phone_number_verified = models.BooleanField(default=False)
    change_pw = models.BooleanField(default=True)
    verification_code = models.CharField(max_length=6, verbose_name='verification code', default=generate_verification_code())
    last_sent_vcode_time = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_active = models.BooleanField(_('is_active'), default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['city', 'email']

    class Meta:
        ordering = ('phone_number',)
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return str(self.full_name)
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def generate_another(self):
        """
        generate another verification code for the user if other was not sent
        """
        self.verification_code = generate_verification_code()
        self.save(update_fields=["verification_code"])
        return self.verification_code

    def get_verification_code(self):
        """
        get the verification code for this user
        """
        return self.verification_code

    def update_vcode_send_timer(self):
        self.last_sent_vcode_time = timezone.now()
        self.save(update_fields=["last_sent_vcode_time"])
        return

    def can_send_code_again(self):
        delta = timezone.now() - self.last_sent_vcode_time
        print(delta.total_seconds())
        if delta.total_seconds() > 60:  # TODO: add setting.time_until_sms to settings.py
            return True, 0.0
        else:
            return False, delta

    def get_full_name(self):
        """
        Returns the display name.
        If full name is present then return full name as display name
        else return ananymous.
        """
        if self.full_name != '':
            return self.full_name
        else:
            return 'ananymous'    # change

    def is_verified(self):
        """
        check if user phone number is verified
        """
        return self.phone_number_verified


    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
