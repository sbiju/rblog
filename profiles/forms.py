from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'photo',
            'gender',
            ]


class ContactusForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField()
    message = forms.CharField()
