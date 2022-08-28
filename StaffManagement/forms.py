from django import forms
from .models import Staff

class StaffInsertForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('First_Name','Last_Name','Phone_num','Email')