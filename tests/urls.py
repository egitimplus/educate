from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from tests.views.test import TestViewSet


router = DefaultRouter()
router.register(r'test', TestViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]