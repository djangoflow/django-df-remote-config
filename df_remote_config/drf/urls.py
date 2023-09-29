from django.urls import path
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema

from ..settings import api_settings
from .viewsets import RemoteConfigView

urlpatterns = []

for schema_name, data in api_settings.REMOTE_CONFIG.items():
    view = RemoteConfigView.as_view(
        handler=data["handler"],
        schema_name=schema_name,
    )
    view = extend_schema(
        responses={
            200: OpenApiTypes.OBJECT,
        }
    )(view)
    urlpatterns.append(path(data["path"], view))
