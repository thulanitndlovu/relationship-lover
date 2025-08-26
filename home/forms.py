from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['surname', 'age', 'location', 'province', 'employment', 'show_profile']


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    location = forms.CharField(max_length=100)
    province = forms.CharField(max_length=100)
    employment = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'age', 'location', 'province', 'employment']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                age=self.cleaned_data['age'],
                location=self.cleaned_data['location'],
                province=self.cleaned_data['province'],
                employment=self.cleaned_data['employment']
            )
        return user