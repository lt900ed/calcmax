from django import forms
from .models import UnitSet


class UnitSetForm(forms.ModelForm):
    class Meta:
        model = UnitSet
        fields = ('unit_set_text',)
