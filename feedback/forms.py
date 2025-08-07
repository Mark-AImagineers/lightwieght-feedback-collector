from django import forms
from .models import Business

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