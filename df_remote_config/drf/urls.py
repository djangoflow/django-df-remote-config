from django.urls import path

from ..settings import api_settings
from .viewsets import RemoteConfigView

urlpatterns = [
    path(
        data["path"],
        RemoteConfigView.as_view(
            handler=data["handler"],
            schema_name=schema_name,
        ),
    )
    for schema_name, data in api_settings.REMOTE_CONFIG.items()
]
