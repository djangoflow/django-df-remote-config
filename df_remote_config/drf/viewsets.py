from rest_framework import viewsets

from df_remote_config.decorators import ACTIONS, add_dynamic_actions


@add_dynamic_actions(ACTIONS)
class RemoteConfigViewSet(viewsets.GenericViewSet):
    pass
