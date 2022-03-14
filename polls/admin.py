from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from polls.models import Poll
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PollAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

   

admin.site.register(Poll, PollAdmin)

