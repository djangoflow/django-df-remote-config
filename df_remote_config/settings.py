from django.conf import settings
from rest_framework.settings import APISettings

DEFAULTS: dict[str, dict] = {}

api_settings = APISettings(getattr(settings, "DF_REMOTE_CONFIG", None), DEFAULTS)
