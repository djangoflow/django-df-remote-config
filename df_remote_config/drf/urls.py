from rest_framework.routers import DefaultRouter

from .viewsets import RemoteConfigViewSet

router = DefaultRouter()

router.register("", RemoteConfigViewSet, basename="remote-config")
urlpatterns = router.urls
