from django.conf import settings
from core.utils import get_full_version_data

def version_data(request):
    """
    Injects the full version.json content into the template context
    Available in templates via {{version.name }}, etc.
    """
    try:
        data = get_full_version_data(settings.BASE_DIR)
    except Exception:
        data = {}

    return {'version': data}