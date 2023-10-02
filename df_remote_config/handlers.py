from typing import Optional

from django.http import HttpRequest
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from df_remote_config.models import ConfigPart


class AbstractHandler:
    def handle_request(self, request: HttpRequest, part_name: str) -> Response:
        raise NotImplementedError


class DefaultHandler(AbstractHandler):
    def get_config_part(
        self, request: HttpRequest, part_name: str
    ) -> Optional[ConfigPart]:
        attributes = request.GET.dict()
        attributes.pop("part", None)

        return (
            ConfigPart.objects.filter(name=part_name)
            .filter_attributes(attributes)
            .first()
        )

    def get_part_data(self, part: ConfigPart) -> dict:
        return part.json

    def handle_request(self, request: HttpRequest, part_name: str) -> Response:
        if config_part := self.get_config_part(request, part_name):
            return Response(self.get_part_data(config_part))
        else:
            raise NotFound()
