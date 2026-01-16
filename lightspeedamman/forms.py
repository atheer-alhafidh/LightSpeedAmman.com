from django import forms
from .models import TestDrive, CarConfiguration
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class TestDriveForm(forms.ModelForm):
    class Meta:
        model = TestDrive
        fields = '__all__'


# Define options per model (JS object converted to Python dict)
CAR_OPTIONS = {
    'LS6': {
        'packages': ["2WD - Premium", "4WD - Ultra Premium"],
        'exterior': ["Metallic Champagne", "Aurora", "Snow White", "Graphite Black"],
        'interior': ["Crimson", "Elegant Black", "Off-White"]
    },
    'LS8': {
        'packages': ["2WD - Premium", "4WD - Ultra Premium"],
        'exterior': ["Snow White", "Graphite Black"],
        'interior': ["Crimson", "Elegant Black", "Off-White"]
    }
}


class CarConfigurationForm(forms.ModelForm):
    class Meta:
        model = CarConfiguration
        fields = ['package', 'exterior', 'interior']

    def __init__(self, *args, **kwargs):
        selected_model = kwargs.pop('selected_model', None)
        super().__init__(*args, **kwargs)

        if selected_model and selected_model in CAR_OPTIONS:
            options = CAR_OPTIONS[selected_model]
            self.fields['package'].widget = forms.Select(
                choices=[(p, p) for p in options['packages']])
            self.fields['exterior'].widget = forms.Select(
                choices=[(e, e) for e in options['exterior']])
            self.fields['interior'].widget = forms.Select(
                choices=[(i, i) for i in options['interior']])
        else:
            self.fields['package'].widget = forms.Select(choices=[])
            self.fields['exterior'].widget = forms.Select(choices=[])
            self.fields['interior'].widget = forms.Select(choices=[])


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password'
        })
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-input'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-input'
        })
    )
