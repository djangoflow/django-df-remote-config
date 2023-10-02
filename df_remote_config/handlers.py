from typing import Optional

from django.http import HttpRequest
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from df_remote_config.models import ConfigPart


class AbstractHandler:
    def handle_request(
        self, request: HttpRequest, part_name: str, tag_name: Optional[str]
    ) -> Response:
        raise NotImplementedError


class DefaultHandler(AbstractHandler):
    def handle_request(
        self, request: HttpRequest, part_name: str, tag_name: Optional[str]
    ) -> Response:
        queryset = ConfigPart.objects.filter(name=part_name).order_by("sequence")

        if tag_name:
            queryset = queryset.filter(tags__name=tag_name)

        if config_part := queryset.first():
            return Response(config_part.json)
        else:
            raise NotFound()
