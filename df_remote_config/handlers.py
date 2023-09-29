from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from df_remote_config.models import ConfigItem


class BaseHandler:
    def prepare_request(self, request):
        pass

    def get_config_part(self, request):
        return ConfigPart.objects.filter(schema=request.data.schema, tags=request.data.tags)

    def default_handler(request, schema_name, *args, **kwargs):  # type: ignore
        config_item = get_object_or_404(
            ConfigItem,
            schema_name=schema_name,
            name=request.GET.get("name", ConfigItem.DEFAULT_NAME),
        )
        return Response(config_item.json)


class AuthHandler(BaseHandler):

    def handle_request(request, schema_name, *args, **kwargs):  # type: ignore
        data = {"providers": []}
        return Response(data)

    # A/B condition, check cache etc
