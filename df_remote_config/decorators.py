from django.utils.module_loading import import_string
from rest_framework.decorators import action
from rest_framework.response import Response

from df_remote_config.models import ConfigItem


def default_handler(self, request, schema_name, *args, **kwargs):  # type: ignore
    get_object_or_404 = kwargs.get("get_object_or_404")
    config_item = get_object_or_404(
        ConfigItem,
        schema_name=schema_name,
        name=request.GET.get("name", ConfigItem.DEFAULT_NAME),
    )
    return Response(config_item.json)


ACTIONS = {
    "test": {
        "path": "test",
        "handler": default_handler,
    },
}


def add_dynamic_actions(actions):  # type: ignore
    def decorator(cls):  # type: ignore
        for schema_name, action_data in actions.items():
            path = action_data.get("path")
            handler_name = action_data.get("handler")

            # Retrieve the actual method or use the provided callable directly
            if isinstance(handler_name, str):
                handler = import_string(handler_name)
            else:
                handler = handler_name

            handler.__name__ = schema_name

            @action(detail=False, methods=["GET"], url_path=path)
            def action_wrapper(  # type: ignore
                self,
                request,
                *args,
                _handler=handler,
                _handler_name=handler_name,
                **kwargs,
            ):
                return _handler(self, request, _handler_name, *args, **kwargs)

            # Attach the wrapped method to the class with a dynamic name
            setattr(cls, schema_name, action_wrapper)

        return cls

    return decorator
