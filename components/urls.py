from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from components.views.component import ComponentViewSet

"""
ComponentViewSet
-------------------------------------------------------------
GET - getInfo               | retrieve      | /components/component/{component_id}
POST - searchQuestionType   | search        | /components/component/search
GET - getDetail             | user_detail   | /components/component/{component_id}/user_detail
GET - getParents            | parents       | /components/component/{component_id}/parents
POST - addQuestionType      | create        | /components/component/
PUT - updateQuestionType    | update        | /components/component/{component_id}
DEL - deleteQuestionType    | destroy       | /components/component/{component_id}
-------------------------------------------------------------
Yapılacaklar
-------------------------------------------------------------
GET - getCourses            | courses       |
"""

router = DefaultRouter()
router.register(r'component', ComponentViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]