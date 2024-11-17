from django import forms
from .models import EmployeeRole, EmployeeType, VendorType, Brand

class EmployeeRoleForm(forms.ModelForm):
    class Meta:
        model = EmployeeRole
        fields = ['name']

class EmployeeTypeForm(forms.ModelForm):
    class Meta:
        model = EmployeeType
        fields = ['name']

class VendorTypeForm(forms.ModelForm):
    class Meta:
        model = VendorType
        fields = ['name']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']