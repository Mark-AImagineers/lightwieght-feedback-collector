from django import forms
from .models import Business, Event

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = [
            "business_name",
            "description",
            "logo",
            "contact_email",
            "contact_number",
        ]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "date",
            "location",
        ]