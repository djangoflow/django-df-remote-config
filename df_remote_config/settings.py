from django.conf import settings
from rest_framework.settings import APISettings

DEFAULTS: dict[str, dict] = {
    "REMOTE_CONFIG": {
        # "theme": {
        #     "path": "theme/",
        #     "handler": "df_remote_config.handlers.default_handler",
        # },
        "legal": {
            "path": "legal/",
            "handler": "df_remote_config.handlers.default_handler",
        },
    }
}

api_settings = APISettings(getattr(settings, "DF_REMOTE_CONFIG", None), DEFAULTS)
