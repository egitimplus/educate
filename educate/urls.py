from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from companies.views import CourseViewSet

course = CourseViewSet.as_view({'get': 'course'})
course_lesson = CourseViewSet.as_view({'get': 'course_lesson',})
course_lecture_stat = CourseViewSet.as_view({'get': 'course_lecture_stat'})
course_user = CourseViewSet.as_view({'get': 'course_user'})
course_unit = CourseViewSet.as_view({'get': 'course_unit'})
course_list = CourseViewSet.as_view({'get': 'list'})
course_component_stats = CourseViewSet.as_view({'get': 'course_component_stats'})
course_lecture_stats = CourseViewSet.as_view({'get': 'course_lecture_stats'})

urlpatterns = format_suffix_patterns([
    url(r'^course/$', course_list, name='classroom-list'),
    url(r'^course/user/$', course_user, name='course-user'),
    url(r'^course/(?P<pk>[0-9]+)/$', course, name='course-list'),
    url(r'^course/(?P<pk>[0-9]+)/unit/$', course_unit, name='course-unit'),
    url(r'^course/(?P<pk>[0-9]+)/lecture/stat/$', course_lecture_stat, name='course-lecture-stat'),
    url(r'^course/(?P<pk>[0-9]+)/lesson/$', course_lesson, name='course-lesson'),
    url(r'^course/(?P<pk>[0-9]+)/component_stats/$', course_component_stats, name='course-component-stats'),
    url(r'^course/(?P<pk>[0-9]+)/lecture_stats/$', course_lecture_stats, name='course-lecture-stats'),
])

urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^components/', include('components.urls')),
    url(r'^companies/', include('companies.urls')),
    url(r'^library/', include('library.urls')),
    url(r'^curricula/', include('curricula.urls')),
    url(r'^publishers/', include('publishers.urls')),
    url(r'^auth/', include('users.urls')),
    url(r'^categories/', include('educategories.urls')),
    url(r'^questions/', include('questions.urls')),
    url(r'^tests/', include('tests.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
