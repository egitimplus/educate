from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import TestUniqueViewSet, TestViewSet


router = DefaultRouter()
router.register(r'test', TestViewSet)
router.register(r'unique', TestUniqueViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]