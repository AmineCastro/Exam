
from .models import Exploi, Infrac
from django import forms

class ExploiForm(forms.ModelForm):
    class Meta:
        model = Exploi
        fields = '__all__'

class InfracForm(forms.ModelForm):
    class Meta:
        model = Infrac
        fields = '__all__'

