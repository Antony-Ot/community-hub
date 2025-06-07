# home/forms.py
from django import forms
from django.contrib.auth.models import User

class PaymentForm(forms.Form):
    card_number = forms.CharField(max_length=16, label='Card Number')
    expiration_date = forms.CharField(max_length=5, label='Expiration Date (MM/YY)')
    cvv = forms.CharField(max_length=3, label='CVV')
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label='Amount')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
