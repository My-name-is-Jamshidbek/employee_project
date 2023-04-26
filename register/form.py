from django import forms
from .models import Employee, Position

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
