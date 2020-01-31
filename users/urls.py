from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from users.views import PermissionViewSet, GroupViewSet, UserViewSet
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

router = DefaultRouter()
router.register(r'permission', PermissionViewSet)
router.register(r'group', GroupViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^verify/', verify_jwt_token),
    url(r'^refresh/', refresh_jwt_token),
    url(r'^', include(router.urls)),
]

