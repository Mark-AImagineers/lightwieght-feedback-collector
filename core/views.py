from django.shortcuts import render
from core.utils import get_faq_data
from django.conf import settings

def test_page(request):
    """
    used only to test templates
    """
    template = "test.html"
    return render(request, template)

def landing_view(request):
    template = "pages/landing/landing.html"
    context = {
        "faq_list": get_faq_data(settings.BASE_DIR)
    }
    return render(request, template, context)