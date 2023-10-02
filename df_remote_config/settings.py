from django.conf import settings
from rest_framework.settings import APISettings

DEFAULTS: dict[str, dict] = {
    "PARTS": {
        "legal": {
            "SCHEMA": "df_remote_config.schema.legal_schema",
            "HANDLER_CLASS": "df_remote_config.handlers.DefaultHandler",
        },
    }
}

api_settings = APISettings(getattr(settings, "DF_REMOTE_CONFIG", None), DEFAULTS)
