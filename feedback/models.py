from django.db import models
from users.models import EmailUser

class Business(models.Model):
    owner = models.ForeignKey(EmailUser, on_delete=models.CASCADE, related_name="businesses")
    business_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="logos/", null=True, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name

class Event(models.Model):
    owner = models.ForeignKey(EmailUser, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    date = models.DateField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title