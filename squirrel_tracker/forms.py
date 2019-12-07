#This file is for creating model forms.

from django.forms import ModelForm
from .models import Squirrel

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'
