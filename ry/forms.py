from django import forms
from .models import Person

class AddPersonForm_S(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("Id_Number","Name","Gender","Birthday")