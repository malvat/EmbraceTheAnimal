from django import forms
from .models import AccountUser

class AccountUserForm(forms.ModelForm):
    class Meta:
        model = AccountUser
        fields = ['first_name', 'last_name', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }