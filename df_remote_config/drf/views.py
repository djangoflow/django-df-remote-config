from typing import Any

from django.http import HttpRequest, HttpResponse
from django.utils.module_loading import import_string
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import permissions, views
from rest_framework.exceptions import NotFound

# Additional imports as per your project structure, e.g., `api_settings`
from df_remote_config.settings import api_settings


class RemoteConfigView(views.APIView):
    http_method_names = ["get"]
    permission_classes = [permissions.AllowAny]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="part",
                description="Name of the configuration part.",
                required=True,
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                enum=api_settings.PARTS.keys(),
            ),
            OpenApiParameter(
                name="tag",
                required=False,
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
            ),
        ],
        responses={
            200: OpenApiTypes.OBJECT,
        },
    )
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        part = request.GET.get("part")
        tag = request.GET.get("tag")
        if part not in api_settings.PARTS:
            raise NotFound()

        part_config = api_settings.PARTS[part]
        handler = import_string(part_config["HANDLER_CLASS"])()
        return handler.handle_request(request, part, tag)
