from django.contrib import admin
from django.urls import path
from .views import test_page, landing_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_page, name='test'),
    path('', landing_view, name='landing')
]
