from django.urls import path
from feedback.views import businesses_view, events_view, qrcodes_view

urlpatterns = [
    path("businesses/", businesses_view, name="businesses"),
    path("events/", events_view, name="events"),
    path("qr-codes", qrcodes_view, name="qrcodes"),
]
