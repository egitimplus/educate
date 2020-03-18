from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from companies.views import CompanyGroupViewSet, SchoolViewSet, ClassroomViewSet, LessonViewSet

router = DefaultRouter()
router.register(r'group', CompanyGroupViewSet)

router_patterns = [
    url(r'^', include(router.urls))
]

school_list = SchoolViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
school_detail = SchoolViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
school_update = SchoolViewSet.as_view({
    'put': 'update_school'
})
school_manager = SchoolViewSet.as_view({
    'get': 'manager_list',
    'post': 'attach_manager',
    'put': 'detach_manager'
})
school_teacher = SchoolViewSet.as_view({
    'get': 'teacher_list',
    'post': 'attach_teacher',
    'put': 'detach_teacher'
})
school_student = SchoolViewSet.as_view({
    'get': 'student_list',
    'post': 'attach_student',
    'put': 'detach_student'
})
school_classroom = SchoolViewSet.as_view({
    'get': 'classroom_list',
})
school_lesson = SchoolViewSet.as_view({
    'get': 'lesson_list',
})
school_user = SchoolViewSet.as_view({
    'get': 'user_list',
    'post': 'attach_user',
    'put': 'detach_user'
})
school_lesson_teacher = SchoolViewSet.as_view({
    'get': 'lesson_teacher_list',
    'post': 'lesson_teacher_filter_list',
})
school_roles = SchoolViewSet.as_view({
    'post': 'update_roles',
})


lesson_list = LessonViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
lesson_detail = LessonViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
lesson_teacher = LessonViewSet.as_view({
    'get': 'list_lesson_teacher',
    'post': 'attach_lesson_teacher',
    'put': 'update_lesson_teacher',
    'delete': 'detach_lesson_teacher'
})

classroom_list = ClassroomViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
classroom_detail = ClassroomViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
classroom_student = ClassroomViewSet.as_view({
    'get': 'student_list',
    'post': 'attach_student',
    'put': 'detach_student'
})
classroom_teacher = ClassroomViewSet.as_view({
    'get': 'teacher_list',
    'post': 'attach_teacher',
    'put': 'detach_teacher'
})
classroom_lesson = ClassroomViewSet.as_view({
    'get': 'lesson_list',
    'post': 'attach_lesson',
    'put': 'detach_lesson'
})

course = ClassroomViewSet.as_view({
    'get': 'course',
})

url_patterns = format_suffix_patterns([
    url(r'^school/$', school_list, name='school-list'),
    url(r'^school/(?P<pk>[0-9]+)/$', school_detail, name='school-detail'),
    url(r'^school/(?P<pk>[0-9]+)/manager/$', school_manager, name='school-manager'),
    url(r'^school/(?P<pk>[0-9]+)/teacher/$', school_teacher, name='school-teacher'),
    url(r'^school/(?P<pk>[0-9]+)/student/$', school_student, name='school-student'),
    url(r'^school/(?P<pk>[0-9]+)/user/$', school_user, name='school-user'),
    url(r'^school/(?P<pk>[0-9]+)/classroom_list/$', school_classroom, name='school-classroom'),
    url(r'^school/(?P<pk>[0-9]+)/lesson_list/$', school_lesson, name='school-lesson'),
    url(r'^school/(?P<pk>[0-9]+)/lesson_teacher/$', school_lesson_teacher, name='school-lesson-teacher'),
    url(r'^school/(?P<pk>[0-9]+)/update_school/$', school_update, name='school-update'),
    url(r'^school/(?P<pk>[0-9]+)/update_roles/$', school_roles, name='school-update-roles'),

    url(r'^classroom/$', classroom_list, name='classroom-list'),
    url(r'^classroom/(?P<pk>[0-9]+)/$', classroom_detail, name='classroom-detail'),
    url(r'^classroom/(?P<pk>[0-9]+)/lesson/$', classroom_lesson, name='classroom-lesson'),
    url(r'^classroom/(?P<pk>[0-9]+)/teacher/$', classroom_teacher, name='classroom-teacher'),
    url(r'^classroom/(?P<pk>[0-9]+)/student/$', classroom_student, name='classroom-student'),

    url(r'^course/(?P<pk>[0-9]+)/$', course, name='course-list'),
    url(r'^course/$', classroom_list, name='classroom-list'),

    url(r'^lesson/$', lesson_list, name='lesson-list'),
    url(r'^lesson/(?P<pk>[0-9]+)/$', lesson_detail, name='lesson-detail'),
    url(r'^lesson/(?P<pk>[0-9]+)/lesson_teacher/$', lesson_teacher, name='lesson-teacher'),



])

urlpatterns = router_patterns + url_patterns


