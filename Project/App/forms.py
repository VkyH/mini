from dataclasses import fields
from django.forms import ModelForm
from . models import CVmodel
class CVform(ModelForm):
    class Meta:
        model=CVmodel
        fields='__all__'
        
   