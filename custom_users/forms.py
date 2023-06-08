from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER = (("М", "M"), ("Ж", "Ж"))


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    work = forms.CharField(max_length=200, min_length=10)

    class Meta:
        model = models.CustomUsers
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "phone_number",
            "first_name",
            "last_name",
            "age",
            "gender",
            "work",
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
