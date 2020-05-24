from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from curricula.views import *

router = DefaultRouter()
router.register(r'lesson', LearningLessonViewSet)
router.register(r'unit', LearningUnitViewSet)
router.register(r'subject', LearningSubjectViewSet)
router.register(r'lecture', LearningLectureViewSet)
router.register(r'test', LearningTestViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]



