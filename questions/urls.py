from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from questions.views import QuestionAnswerStatViewSet, CategoryView, QuestionViewSet
"""
QuestionViewSet
-------------------------------------------------------------
GET - getQuestion       | view          | /questions/question/{question_id}/view        
PUT - updateQuestion    | update        | /questions/question/{question_id}/            
DEL - deleteQuestion    | destroy       | /questions/question/{question_id}/            
GET - getParents        | parents       | /questions/question/{question_id}/parents     
GET - getDetail         | user_detail   | /questions/question/{question_id}/user_detail 
GET -                   | retrieve      | /questions/question/{question_id}/   
POST - addQuestion      | create        | /questions/question/              
GET - getCategories     | categories    | /questions/categories/{category_id}/
-------------------------------------------------------------
Yapılacaklar
-------------------------------------------------------------
GET - setAnswers    | 
POST - addAnswer    |

"""
# TODO setAnswers, addAnswer için route ayarlaması yapılmadı

router = DefaultRouter()
router.register(r'question', QuestionViewSet)


question_answer_stat = QuestionAnswerStatViewSet.as_view({
    'post': 'create'
})

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^categories/(?P<pk>[0-9]+)/$', CategoryView.as_view()),
    url(r'^question/answer/stat/$', question_answer_stat, name='question-answer-stat'),

]