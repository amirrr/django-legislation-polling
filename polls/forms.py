from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['picture', 'title']
        widgets = {
            'description': SummernoteWidget(),
        }