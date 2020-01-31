from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from library.views import ProvinceViewSet, ExamViewSet, MediaViewSet
from library.views import company_types, departments, school_roles



router = DefaultRouter()
router.register(r'province', ProvinceViewSet)
router.register(r'exam', ExamViewSet)
router.register(r'media', MediaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^companytypes/$', company_types),
    url(r'^departments/$', departments),
    url(r'^schoolroles/$', school_roles),

]

