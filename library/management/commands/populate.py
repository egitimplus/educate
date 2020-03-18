from django.core.management.base import BaseCommand
from companies.models import *
from curricula.models import *
from publishers.models import *
from educategories.models import *
from questions.models import *
from components.models import *
from tests.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from users.models import *
from django.contrib.contenttypes.models import ContentType

User = get_user_model()


class Command(BaseCommand):

    def _data_crate(self):

        User.objects.bulk_create([
            User(id=1, password='123456', is_superuser=0, username='yonetici', first_name='Ymnetici', last_name='Çevik', email='a1@b.com', is_staff=0, is_active=1, identity_number=12345678901),
            User(id=2, password='123456', is_superuser=0, username='ogretmen', first_name='Öğretmen', last_name='Çevik', email='a2@b.com', is_staff=0, is_active=1, identity_number=12345678902),
            User(id=3, password='123456', is_superuser=0, username='ogrenci', first_name='Öğrenci', last_name='Çevik', email='a3@b.com', is_staff=0, is_active=1, identity_number=12345678903),
        ])

        Group.objects.bulk_create([
            Group(id=1, name="Ziyaretçi"),
            Group(id=2, name="Engellenmiş Kullanıcı"),
            Group(id=3, name="Öğrenci"),
            Group(id=4, name="Veli"),
            Group(id=5, name="Eğitim Koçu"),
            Group(id=6, name="Ders Öğretmeni"),
            Group(id=7, name="Sınıf Öğretmeni"),
            Group(id=8, name="Okul Personeli"),
            Group(id=9, name="Okul Yöneticisi"),
            Group(id=10, name="Yayınevi Editörü"),
            Group(id=11, name="Yayınevi Personeli"),
            Group(id=12, name="Yayınevi Yöneticisi"),
            Group(id=13, name="Grup Yöneticisi"),
            Group(id=14, name="Sistem Yöneticisi"),
        ])

        CompanyGroup.objects.bulk_create([
            CompanyGroup.objects.create(id=101, name='Educate', slug='educate', active=1, user_id=1),
            CompanyGroup.objects.create(id=102, name='Doğa', slug='doga', active=1, user_id=1),
        ])

        SchoolType.objects.bulk_create([
            SchoolType(id=1, name='Okul'),
            SchoolType(id=2, name='Dershane')
        ])

        School.objects.bulk_create([
            School(id=101, name='Educate Plus', slug='educate-plus', group_id=101, active=1, code='XXXX', type_id=1, address='adres 1'),
            School(id=102, name='Khan Academy', slug='khan-academy', group_id=101, active=1, code='XXXX', type_id=1, address='adres 1'),
            School(id=103, name='Doğa Ataşehir', slug='doga-atasehir', group_id=102, active=1, code='XXXX', type_id=1, address='adres 1'),
        ])

        Publisher.objects.bulk_create([
            Publisher(id=101, name='Khan Academy', slug='khan-academy', group_id=101, active=1),
            Publisher(id=102, name='Educate Yayınevi', slug='educate-yayinevi', group_id=101, active=1),
            Publisher(id=103, name='Doğa Yayınevi', slug='doga-yayinevi', group_id=102, active=1)

        ])

        Classroom.objects.bulk_create([
            Classroom(id=101, name='Khan Academy - Mat', slug='khan-academy-mat', year=2019, grade=12, department_id=1, active=1, school_id=102),
            Classroom(id=102, name='Khan Academy - Fen', slug='khan-academy-fen', year=2019, grade=12, department_id=1,active=1, school_id=102),
            Classroom(id=103, name='Educate - Mat', slug='educate-mat', year=2019, grade=12, department_id=1, active=1, school_id=101),
        ])

        LearningDomain.objects.bulk_create([
            LearningDomain(id=10,name='Cebir',content='Cebir Açıklaması',position=1,)
        ])

        SchoolUser.objects.bulk_create([
            SchoolUser(id=1, school_id=102, user_id=1),
            SchoolUser(id=2, school_id=102, user_id=2),
            SchoolUser(id=4, school_id=101, user_id=1),
            SchoolUser(id=5, school_id=103, user_id=1),
            SchoolUser(id=6, school_id=101, user_id=2),
            SchoolUser(id=7, school_id=103, user_id=2),
        ])

        SchoolManager.objects.bulk_create([
            SchoolManager(id=1, school_id=101, manager_id=1),
            SchoolManager(id=2, school_id=102, manager_id=1),
            SchoolManager(id=3, school_id=103, manager_id=1),
        ])

        SchoolTeacher.objects.bulk_create([
            SchoolTeacher(id=1, school_id=101, teacher_id=2),
            SchoolTeacher(id=2, school_id=102, teacher_id=2),
            SchoolTeacher(id=3, school_id=103, teacher_id=2),
        ])

        SchoolStudent.objects.bulk_create([
            SchoolStudent(id=1, school_id=102, student_id=3),
        ])

        SchoolLessonTeacher.objects.bulk_create([
            SchoolLessonTeacher(id=1, name='MAT-1', duration=4, teacher_id=2, lesson_id=101),
            SchoolLessonTeacher(id=2, name='MAT-2', duration=6, teacher_id=2, lesson_id=102),
            SchoolLessonTeacher(id=3, name='MAT-3', duration=2, teacher_id=2, lesson_id=103),
            SchoolLessonTeacher(id=4, name='MAT-1-1', duration=8, teacher_id=2, lesson_id=101),
            SchoolLessonTeacher(id=5, name='MAT-1', duration=4, teacher_id=1, lesson_id=101),
        ])

        ClassroomStudent.objects.bulk_create([
            ClassroomStudent(id=1, classroom_id=101, student_id=3),
        ])

        ClassroomTeacher.objects.bulk_create([
            ClassroomTeacher(id=1, classroom_id=101, teacher_id=2),
        ])

        ClassroomLesson.objects.bulk_create([
            ClassroomLesson(id=1, classroom_id=101, lesson_id=1),
            ClassroomLesson(id=2, classroom_id=101, lesson_id=2),
            ClassroomLesson(id=3, classroom_id=101, lesson_id=3),
            ClassroomLesson(id=4, classroom_id=101, lesson_id=4),
            ClassroomLesson(id=5, classroom_id=102, lesson_id=5),
            ClassroomLesson(id=6, classroom_id=102, lesson_id=1),
        ])

        Role.objects.bulk_create([
            Role(id=1, page='-', group_id=9, user_id=1),
            Role(id=2, page='-', group_id=12, user_id=1),
            Role(id=3, page='-', group_id=13, user_id=1),
            Role(id=4, page='-', group_id=14, user_id=1),
            Role(id=5, page='-', group_id=6, user_id=2),
            Role(id=6, page='-', group_id=7, user_id=2),
            Role(id=7, page='-', group_id=3, user_id=3),
        ])

        school_model = ContentType.objects.get_for_model(School)
        school_model_id = school_model.id

        group_model = ContentType.objects.get_for_model(CompanyGroup)
        group_model_id = group_model.id

        class_model = ContentType.objects.get_for_model(Classroom)
        class_model_id = class_model.id

        publisher_model = ContentType.objects.get_for_model(Publisher)
        publisher_model_id = publisher_model.id

        user_model = ContentType.objects.get_for_model(User)
        user_model_id = user_model.id

        lessonteacher_model = ContentType.objects.get_for_model(SchoolLessonTeacher)
        lessonteacher_model_id = lessonteacher_model.id

        Pattern.objects.bulk_create([
            Pattern(id=1, object_id=1, content_type_id=user_model_id, role_id=4),

            Pattern(id=2, object_id=101, content_type_id=school_model_id, role_id=1),
            Pattern(id=3, object_id=102, content_type_id=school_model_id, role_id=1),
            Pattern(id=4, object_id=103, content_type_id=school_model_id, role_id=1),

            Pattern(id=5, object_id=101, content_type_id=group_model_id, role_id=3),
            Pattern(id=6, object_id=102, content_type_id=group_model_id, role_id=3),

            Pattern(id=7, object_id=101, content_type_id=publisher_model_id, role_id=2),
            Pattern(id=8, object_id=102, content_type_id=publisher_model_id, role_id=2),

            Pattern(id=9, object_id=1, content_type_id=lessonteacher_model_id, role_id=5),
            Pattern(id=10, object_id=2, content_type_id=lessonteacher_model_id, role_id=5),
            Pattern(id=11, object_id=3, content_type_id=lessonteacher_model_id, role_id=5),
            Pattern(id=12, object_id=4, content_type_id=lessonteacher_model_id, role_id=5),
            Pattern(id=13, object_id=5, content_type_id=lessonteacher_model_id, role_id=5),

            Pattern(id=14, object_id=101, content_type_id=class_model_id, role_id=6),
            Pattern(id=15, object_id=101, content_type_id=class_model_id, role_id=7),
        ])

    def handle(self, *args, **options):
        self._data_crate()
