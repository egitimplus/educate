from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from universities.views.department import *

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'conditions', ConditionViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]