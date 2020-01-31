from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from publishers.views import PublisherViewSet, SourceViewSet, BookViewSet
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'publisher', PublisherViewSet)
router.register(r'source', SourceViewSet)

router_patterns = [
    url(r'^', include(router.urls))
]

publisher_list = PublisherViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
publisher_detail = PublisherViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
publisher_update = PublisherViewSet.as_view({
    'put': 'update_publisher'
})
publisher_book = PublisherViewSet.as_view({
    'get': 'book_list'
})
publisher_manager = PublisherViewSet.as_view({
    'get': 'manager_list'
})

book_list = BookViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
book_detail = BookViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
book_lesson = BookViewSet.as_view({
    'get': 'lesson_list',
    'post': 'attach_lesson',
    'put': 'detach_lesson'
})
book_exam = BookViewSet.as_view({
    'get': 'exam_list',
    'post': 'attach_exam',
    'put': 'detach_exam'
})
book_source = BookViewSet.as_view({
    'get': 'source_list',
})

book_question = BookViewSet.as_view({
    'get': 'question_list',
})


url_patterns = format_suffix_patterns([
    url(r'^book/$', book_list, name='book-list'),
    url(r'^book/(?P<pk>[0-9]+)/$', book_detail, name='book-detail'),
    url(r'^book/(?P<pk>[0-9]+)/lesson/$', book_lesson, name='book-lesson'),
    url(r'^book/(?P<pk>[0-9]+)/exam/$', book_exam, name='book-exam'),
    url(r'^book/(?P<pk>[0-9]+)/source/$', book_source, name='book-source'),
    url(r'^book/(?P<pk>[0-9]+)/question/$', book_source, name='book-question'),

    url(r'^publisher/$', publisher_list, name='publisher-list'),
    url(r'^publisher/(?P<pk>[0-9]+)/$', publisher_detail, name='publisher-detail'),
    url(r'^publisher/(?P<pk>[0-9]+)/update/$', publisher_update, name='publisher-update'),
    url(r'^publisher/(?P<pk>[0-9]+)/book/$', publisher_book, name='publisher-book'),
    url(r'^publisher/(?P<pk>[0-9]+)/manager/$', publisher_manager, name='publisher-manager'),

])

urlpatterns = router_patterns + url_patterns
