from django import forms
from . import models


class MeetingForm(forms.ModelForm):
    class Meta:
        model = models.Meeting
        fields = "__all__"
        # fields = "title description image"
