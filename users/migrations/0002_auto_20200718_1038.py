# Generated by Django 3.0.8 on 2020-07-18 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verification_code',
            field=models.CharField(default='567219', max_length=6, verbose_name='verification code'),
        ),
    ]