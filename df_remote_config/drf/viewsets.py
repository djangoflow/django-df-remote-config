from typing import Callable, Union

from django.utils.module_loading import import_string
from rest_framework import permissions, views


class RemoteConfigView(views.APIView):
    handler: Union[str, Callable] = ""
    schema_name: str = ""
    http_method_names = ["get"]
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):  # type: ignore
        if isinstance(self.handler, str):
            handler = import_string(self.handler)
        else:
            handler = self.handler
        return handler(request, self.schema_name, *args, **kwargs)
