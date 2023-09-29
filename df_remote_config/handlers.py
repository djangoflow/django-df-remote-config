from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from df_remote_config.models import ConfigItem


def default_handler(request, schema_name, *args, **kwargs):  # type: ignore
    config_item = get_object_or_404(
        ConfigItem,
        schema_name=schema_name,
        name=request.GET.get("name", ConfigItem.DEFAULT_NAME),
    )
    return Response(config_item.json)


def auth_handler(request, schema_name, *args, **kwargs):  # type: ignore
    data = {"providers": []}
    return Response(data)
