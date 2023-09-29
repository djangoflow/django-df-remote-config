from django.conf import settings
from rest_framework.settings import APISettings

DEFAULTS: dict[str, dict] = {
    "PARTS": {
        # "theme": {
        #     "path": "theme/",
        #     "handler": "df_remote_config.handlers.default_handler",
        # },
        "legal": {
            "SCHEMA": "df_remote_config.schemas.legal_schema",
            "HANDLER_CLASS": "df_remote_config.handlers.default_handler",
        },
        "auth": {
            "HANDLER_CLASS": "df_remote_config.handlers.AuthHandler",
        },
    }
}

api_settings = APISettings(getattr(settings, "DF_REMOTE_CONFIG", None), DEFAULTS)
