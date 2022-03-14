# Generated by Django 3.0.8 on 2020-07-18 05:54

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import users.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='شماره تلفن خود را به صورت 11 رقمی مثل 09123334455 وارد کنید', regex='^(09)\\d{9}$')], verbose_name='phone')),
                ('full_name', models.CharField(blank=True, max_length=130, verbose_name='full name')),
                ('city', models.CharField(max_length=100, verbose_name='city name')),
                ('email', models.EmailField(max_length=70)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('phone_number_verified', models.BooleanField(default=False)),
                ('change_pw', models.BooleanField(default=True)),
                ('verification_code', models.CharField(default='535485', max_length=6, verbose_name='verification code')),
                ('last_sent_vcode_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('phone_number',),
            },
            managers=[
                ('objects', users.manager.UserManager()),
            ],
        ),
    ]