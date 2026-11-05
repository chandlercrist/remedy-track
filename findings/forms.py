
from django import forms
from .models import Finding


class FindingForm(forms.ModelForm):
    class Meta:
        model = Finding
        fields = [
            "title",
            "description",
            "severity",
            "status",
            "assigned_to",
        ]


class FindingStatusForm(forms.ModelForm):
    class Meta:
        model = Finding
        fields = ["status"]

