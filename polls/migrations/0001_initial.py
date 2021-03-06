# Generated by Django 3.0.8 on 2020-07-18 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='picture/', verbose_name='عکس بنر')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان لایحه')),
                ('description', models.TextField(verbose_name='متن لایحه')),
                ('option_one_count', models.IntegerField(default=0, verbose_name='تعداد رای آری')),
                ('option_two_count', models.IntegerField(default=0, verbose_name='تعداد رای خیر')),
                ('option_three_count', models.IntegerField(default=0, verbose_name='تعداد رای ممتنع')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
